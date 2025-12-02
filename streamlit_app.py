

import cv2
import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode

from src.hand_tracking import detect_hand
from src.virtual_boundary import (
    get_centered_rectangle,
    point_to_rect_distance,
    classify_state,
)


class HandBoundaryProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Convert to OpenCV BGR image
        img = frame.to_ndarray(format="bgr24")

        # Mirror for natural interaction
        img = cv2.flip(img, 1)

        h, w = img.shape[:2]

        # 1) Virtual rectangle
        x1, y1, x2, y2 = get_centered_rectangle(w, h)

        # 2) Detect hand/fingertip
        center, radius, fingertip, mask = detect_hand(
            img, target_rect=(x1, y1, x2, y2)
        )

        # 3) Use fingertip (preferred) or center as the point
        point = fingertip if fingertip is not None else center

        distance = None
        if point is not None:
            px, py = point
            distance = point_to_rect_distance(px, py, x1, y1, x2, y2)

        # 4) Classify state
        state, rect_color = classify_state(distance)

        # 5) Draw hand circle and fingertip
        if center is not None and radius > 0:
            cv2.circle(img, center, radius, (0, 0, 255), 2)

        if fingertip is not None:
            cv2.circle(img, fingertip, 6, (0, 255, 0), -1)
            cv2.putText(
                img, "Finger",
                (fingertip[0] + 5, fingertip[1] - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
            )

        # 6) Draw rectangle + state text
        cv2.rectangle(img, (x1, y1), (x2, y2), rect_color, 2)

        cv2.putText(
            img, f"STATE: {state}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, rect_color, 2
        )

        if state == "DANGER":
            cv2.putText(
                img, "DANGER DANGER", (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3
            )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():
    st.set_page_config(page_title="Hand Boundary POC", page_icon="🖐️")

    st.title("🖐️ Hand Boundary POC – Streamlit UI ⚠️")

    st.markdown(
        """
        **How to play**

        👉 Move your hand so that a single finger points into the box on the **right side** of the video.

        **States**
        - 🟢 **SAFE** – finger is comfortably far from the box  
        - 🟡 **WARNING** – finger is approaching the box  
        - 🔴 **DANGER** – finger is extremely close / inside the box  
          &nbsp;&nbsp;&nbsp;→ big **DANGER DANGER** warning appears on the video

        Press **STOP** under the video to end the demo.
        """
    )

    # Create three columns and put the video in the middle one
    col_left, col_center, col_right = st.columns([1, 9, 1])

    with col_center:
        webrtc_streamer(
            key="hand-boundary-demo",
            mode=WebRtcMode.SENDRECV,
            video_processor_factory=HandBoundaryProcessor,
            media_stream_constraints={"video": True, "audio": False},
        )


if __name__ == "__main__":
    main()
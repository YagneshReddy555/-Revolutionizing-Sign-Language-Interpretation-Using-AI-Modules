import cv2
from .ml_engine import detect_frame

class Camera:
    def __init__(self):
        self.camera = None

    def open(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)

    def close(self):
        if self.camera:
            self.camera.release()
            self.camera = None

    def get_frame(self):
        if self.camera and self.camera.isOpened():
            success, frame = self.camera.read()
            if success:
                return frame
        return None

    def generate_frames(self):
        self.open()
        if not self.camera.isOpened():
            return

        while self.camera.isOpened():
            success, frame = self.camera.read()
            if not success:
                break

            # Run detection
            frame = detect_frame(frame)

            # Encode
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

video_camera = Camera()

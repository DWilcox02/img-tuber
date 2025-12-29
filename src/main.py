import time
from camera_manager import CameraManager
from storage_manager import StorageManager
from deepface_manager import DeepfaceManager

class ScreenshotApp:
    def __init__(self):
        self.camera = CameraManager()
        self.storage = StorageManager(max_images=3)
        self.deepface_manager = DeepfaceManager()
        self.last_save_time = time.time()

    def run(self):
        print("Starting capture loop. Press ESC to exit.")
        try:
            while True:
                rval, frame = self.camera.get_frame()
                if not rval:
                    break

                self.camera.show_frame(frame)

                # Timing Logic
                current_time = time.time()
                if current_time - self.last_save_time >= 1.0:
                    self.storage.save_image(frame, current_time)
                    self.deepface_manager.check_emotion(frame)
                    self.last_save_time = current_time

                if self.camera.is_window_closed():
                    break
        finally:
            self.camera.release()


if __name__ == "__main__":
    app = ScreenshotApp()
    app.run()

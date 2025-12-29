import cv2


class CameraManager:
    def __init__(self, device_index=0):
        self.vc = cv2.VideoCapture(device_index)
        if not self.vc.isOpened():
            raise RuntimeError("Could not open video source.")

        cv2.namedWindow("preview")

    def get_frame(self):
        rval, frame = self.vc.read()
        return rval, frame

    def show_frame(self, frame):
        cv2.imshow("preview", frame)

    def is_window_closed(self):
        # Checks if 'X' was clicked or ESC was pressed
        if cv2.waitKey(20) == 27:
            return True
        return cv2.getWindowProperty("preview", cv2.WND_PROP_VISIBLE) < 1

    def release(self):
        self.vc.release()
        cv2.destroyAllWindows()

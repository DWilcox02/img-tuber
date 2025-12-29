import os
import shutil
import cv2


class StorageManager:
    def __init__(self, folder="screenshots", max_images=3):
        self.folder = folder
        self.max_images = max_images
        self.saved_files = []

        # Ensure folder exists and is empty
        self._prepare_directory()

    def _prepare_directory(self):
        """Creates the folder if it doesn't exist, or empties it if it does."""
        if os.path.exists(self.folder):
            # print(f"Emptying directory: {self.folder}")
            for filename in os.listdir(self.folder):
                file_path = os.path.join(self.folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Deletes file or symlink
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Deletes subdirectories
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            os.makedirs(self.folder)
            print(f"Created directory: {self.folder}")

    def save_image(self, frame, timestamp):
        filename = os.path.join(self.folder, f"shot_{int(timestamp)}.jpg")
        cv2.imwrite(filename, frame)
        self.saved_files.append(filename)
        # print(f"Saved: {filename}")

        self._rotate_files()
        return filename

    def _rotate_files(self):
        while len(self.saved_files) > self.max_images:
            oldest_file = self.saved_files.pop(0)
            if os.path.exists(oldest_file):
                os.remove(oldest_file)
                # print(f"Deleted oldest: {oldest_file}")

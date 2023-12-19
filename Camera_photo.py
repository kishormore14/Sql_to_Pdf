
# pip install opencv-python


import cv2
def capture_and_save_photo():
    # Open the default camera (usually the built-in webcam, camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        cap.release()
        return

    # Save the captured frame as a JPG image
    cv2.imwrite("captured_photo.jpg", frame)

    print("Photo captured and saved as 'captured_photo.jpg'")

    # Release the camera
    cap.release()

if __name__ == "__main__":
    capture_and_save_photo()

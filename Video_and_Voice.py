# pip install opencv-python sounddevice


import cv2
import sounddevice as sd
import numpy as np
import time

def record_video_with_audio(duration=10):
    # Open the default camera (usually the built-in webcam, camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set video width and height
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Set the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('recorded_video.avi', fourcc, 20.0, (640, 480))

    # Record audio
    audio_frames = []
    def callback(indata, frames, time, status):
        if status:
            print(status, flush=True)
        audio_frames.append(indata.copy())

    with sd.InputStream(callback=callback):
        print("Recording...")
        time.sleep(duration)

    print("Recording complete.")

    # Record video
    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        out.write(frame)

    # Save video
    out.release()

    # Save audio as WAV
    audio_data = np.concatenate(audio_frames, axis=0)
    sd.write('recorded_audio.wav', audio_data, samplerate=44100)

    # Release the camera
    cap.release()

    print("Video and audio recorded and saved.")

if __name__ == "__main__":
    record_video_with_audio(10)

from picamera2 import Picamera2
import cv2 as cv
import numpy as np

# Initialize Picamera2
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(camera_config)
picam2.start()

# Initialize Aruco detection
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_APRILTAG_36h11)
parameters = cv.aruco.DetectorParameters()
detector = cv.aruco.ArucoDetector(dictionary, parameters)

try:
    while True:
        # Capture a frame from the RPi camera
        frame = picam2.capture_array()

        # Detect AprilTags
        corners, ids, _ = detector.detectMarkers(frame)

        # Draw detected markers
        if ids is not None:
            cv.aruco.drawDetectedMarkers(frame, corners, ids)

        # Display the frame with detected tags
        cv.imshow("AprilTag Detection", frame)

        # Exit on 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    picam2.stop()
    cv.destroyAllWindows()

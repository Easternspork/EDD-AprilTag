import cv2 as cv

# Load the predefined dictionary
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_APRILTAG_36h11)

# Define detection parameters
parameters = cv.aruco.DetectorParameters()  # Default parameters

# Create the ArucoDetector object
detector = cv.aruco.ArucoDetector(dictionary, parameters)

# Open camera feed (update the index or address for your camera)
cap = cv.VideoCapture(0)  # 0 = default webcam, or provide your camera index

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Detect AprilTags
    corners, ids, _ = detector.detectMarkers(frame)

    # Draw detected markers on the frame
    if ids is not None:
        cv.aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the resulting frame
    cv.imshow("AprilTag Detection", frame)

    # Break the loop with 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

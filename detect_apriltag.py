import cv2
import numpy as np

# Initialize the AprilTag dictionary
tag_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)

# Create detector parameters
parameters = cv2.aruco.DetectorParameters_create()

# Initialize the camera (use camera index 0 for most setups)
cap = cv2.VideoCapture(0)  # Replace 0 with your camera index if different

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale (required for ArUco detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect AprilTags in the frame
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, tag_dict, parameters=parameters)

    # Draw detected markers and display IDs
    if ids is not None:
        # Draw the markers
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for i, tag_id in enumerate(ids):
            # Get the center of the detected AprilTag
            corner = corners[i][0]
            center_x = int(corner[:, 0].mean())
            center_y = int(corner[:, 1].mean())

            # Display the ID on the frame
            cv2.putText(
                frame,
                f"ID: {tag_id[0]}",
                (center_x - 20, center_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    # Display the frame
    cv2.imshow("AprilTag Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

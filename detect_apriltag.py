import cv2
import numpy as np

def detect_april_tags():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Use the correct camera index
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Define the AprilTag detector
    detector = cv2.apriltag.Detector(cv2.apriltag.DetectorOptions(families="tag36h11"))

    print("Press 'q' to quit.")

    while True:
        # Capture a frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture an image.")
            break

        # Convert the frame to grayscale (AprilTags require grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect AprilTags
        results = detector.detect(gray)

        # Loop through detected AprilTags
        for result in results:
            (ptA, ptB, ptC, ptD) = result.corners
            ptA = tuple(map(int, ptA))
            ptB = tuple(map(int, ptB))
            ptC = tuple(map(int, ptC))
            ptD = tuple(map(int, ptD))

            # Draw the bounding box of the tag
            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

            # Draw the center (optional)
            (cX, cY) = result.center
            cv2.circle(frame, (int(cX), int(cY)), 5, (0, 0, 255), -1)

            # Display the tag ID
            tag_id = result.tag_id
            cv2.putText(frame, f"ID: {tag_id}", (int(cX), int(cY) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the result
        cv2.imshow("AprilTag Detection", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_april_tags()

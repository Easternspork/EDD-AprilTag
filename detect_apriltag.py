import cv2
import apriltag

def detect_april_tags():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Use the correct camera index
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Initialize the AprilTag detector
    detector = apriltag.Detector()

    print("Press 'q' to quit.")

    while True:
        # Capture a frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture an image.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect AprilTags
        results = detector.detect(gray)

        # Loop through detected tags
        for r in results:
            # Extract the corners of the tag
            (ptA, ptB, ptC, ptD) = r.corners
            ptA = tuple(map(int, ptA))
            ptB = tuple(map(int, ptB))
            ptC = tuple(map(int, ptC))
            ptD = tuple(map(int, ptD))

            # Draw the bounding box
            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

            # Draw the center
            (cX, cY) = (int(r.center[0]), int(r.center[1]))
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

            # Display the tag ID
            tag_id = r.tag_id
            cv2.putText(frame, f"ID: {tag_id}", (cX - 10, cY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the result
        cv2.imshow("AprilTag Detection", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_april_tags()

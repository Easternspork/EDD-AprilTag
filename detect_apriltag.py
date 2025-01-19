import cv2

# Initialize the video capture object for the Raspberry Pi camera
cap = cv2.VideoCapture(0)  # 0 refers to the first camera device

# Set the resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'q' to exit the video stream.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nInterrupted by user.")

# Release resources
cap.release()
cv2.destroyAllWindows()

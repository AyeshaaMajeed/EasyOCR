import easyocr
import cv2
import numpy as np

# Load video file (Change to 0 for webcam)
VIDEO_PATH = 'video.mp4'  # Change to 0 for webcam
OUTPUT_VIDEO_PATH = 'output_video.avi'

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Open video
cap = cv2.VideoCapture(VIDEO_PATH)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (frame_width, frame_height))

# Check if video opened successfully
if not cap.isOpened():
    print(" Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit when the video ends

    # Perform OCR on frame
    result = reader.readtext(frame)

    # Draw bounding boxes and text
    for detection in result:
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]

        # Draw rectangle
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 3)

        # Put text on frame
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Show frame with detected text
    cv2.imshow("OCR Video", frame)

    # Write processed frame to output video
    out.write(frame)

    # Press 'q' to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"\n Processed video saved as: {OUTPUT_VIDEO_PATH}")

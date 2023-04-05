import cv2
import playsound

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read the video frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Play a sound if a face is detected
    if len(faces) > 0:
        playsound.playsound('alert.wav')

        # Save a snapshot of the frame
        cv2.imwrite('detected/user.jpg', frame)

    # Draw a rectangle around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the video frame
    cv2.imshow('Video', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

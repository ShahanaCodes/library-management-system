import cv2 #library import

# Haar Cascade classifier (OpenCV-ல் pre-trained)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")#face detect panna use panrathu

# Webcam open
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    # Image convert பண்ணு gray-scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Detected faces-ல் rectangle draw பண்ணு
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Window-ல் display பண்ணு
    cv2.imshow("Face Detection - Python 3.13", frame)

    # 'q' அழுத்தினாலே close ஆகும்
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam & close windows
cap.release()
cv2.destroyAllWindows()

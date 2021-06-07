import cv2
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')
nose_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')

fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 0.7
weared_mask = "Thank you for wearing MASK"
not_weared_mask = "Please wear MASK to defeat CORONA"
nose_problem = "Please wear MASK COMPLETELTY"
org = (30, 30)

cap= cv2.VideoCapture(1)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kameranizi kontrol ediniz!")
        os.system('cmd /k "python .\\__init__.py"')

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)

    if (len(faces) == 0):
        cv2.putText(frame, "Yuz Bulunamadi", org, fontFace,
                    fontScale, (255, 255, 255), 2)
    else:
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (255, 0, 0), 2)
            roi_gray = gray_image[y:y + h, x:x + w]

            mouth = mouth_cascade.detectMultiScale(roi_gray,
                                                   1.4, 1)
            nose = nose_cascade.detectMultiScale(roi_gray,
                                                 1.4, 1)
            i = 0
            if (len(mouth) == 0):

                if (len(nose) == 0):
                    cv2.putText(frame, weared_mask, (x + w, y + h), fontFace,
                                fontScale, (0, 255, 0),
                                2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, nose_problem, (x + w, y + h),
                                fontFace, fontScale, (0, 0, 255),
                                4, cv2.LINE_AA)
            else:
                cv2.putText(frame, not_weared_mask, (x + w, y + h),
                            fontFace, fontScale, (0, 0, 255),
                            4, cv2.LINE_AA)

    cv2.imshow("Mask Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
os.system('cmd /k "python .\\__init__.py"')
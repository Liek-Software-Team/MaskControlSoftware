import cv2
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +'haarcascade_frontalface_default.xml')  # Yüz tanıma işlemi için cascade tanımlandı.
mouth_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +'Mouth.xml')  # Yüz tanıma işlemi için cascade tanımlandı.
nose_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +'haarcascade_mcs_nose.xml')  # Burun tanıma işlemi için cascade tanımlandı.
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +'haarcascade_eye.xml')  # Göz tanıma işlemi için cascade tanımlandı.

fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Yazı fontu ayarlandı.
fontScale = 0.7  # Yazı büyüklüğü belirtildi.
weared_mask = "Thank you for wearing MASK"  # Yazılar sonrasında görüntüye yollanmak üzere hazırlandı.
not_weared_mask = "Please wear MASK to defeat CORONA"
nose_problem = "Please wear MASK COMPLETELTY"
cap = cv2.VideoCapture("corona_street_12.mp4")  # Video veya kamera görüntüsü ayarlandı.

while cap.isOpened():  # Yollanan görüntünün aktif olduğu zamanlar için döngü ayarlandı.
    ret, frame = cap.read()  # Okunan görüntü değişkenlere atandı.
    if not ret:  # Görüntünün okunamadığı zamanlar için kontrol koşulu sağlandı.
        print("Test Video Finished")
        cap.release()
        cv2.destroyAllWindows()
        os.system('cmd /k "python .\\__init__.py"')

    gray_image = cv2.cvtColor(frame,
                              cv2.COLOR_BGR2GRAY)  # Cascade classifier'ın çalışma şartlarından biri olarak görüntüler griye çevirildi

    faces = face_cascade.detectMultiScale(gray_image, 1.1,
                                          10)  # Görüntüdeki yüz algılamaları uygun koşullara göre ayarlandı.
    # parametreler:resim, multiscale oranı(çoğu zaman default), minimum komşu kare sayısı
    eyes = eye_cascade.detectMultiScale(gray_image, 1.1,
                                        5)  # Görüntüdeki göz algılamaları uygun koşullara göre ayarlandı.

    if (len(faces) == 0):
        cv2.putText(frame, "Yuz Bulunamadı...", (30, 30), fontFace,
                    fontScale, (255, 255, 255), 2)
    # Görüntüde yüz bulunmaması durumunda gönderilecek text koşul durumuyla belirtildi.

    else:
        for x, y, w, h in faces:
            # görüntüde yüz bulunması durumunda yüzleri belirten x,y,w,h değerlerine göre döngü oluşturuldu.
            if (len(eyes) == 0):
                cv2.putText(frame, "Yuz Bulunamadı...", (30, 30), fontFace,
                            fontScale, (255, 255, 255), 2)
            # göz bulunmaması durumunda hassasiyeti artırmak amacıyla kontrol texti yollandı.

            else:
                # göz bulunması durumunda yüz bir kare içerisine aldırıldı.
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              (255, 0, 0), 2)
                roi_gray = gray_image[y:y + h, x:x + w]
                # yüz içerisindeki ağız ve burun tespiti yapılabilmesi için roi(ilgilenilen bölge)(yüz) belirlendi.
                mouth = mouth_cascade.detectMultiScale(roi_gray,
                                                       1.4, 5)
                nose = nose_cascade.detectMultiScale(roi_gray,
                                                     1.4, 3)
                # ağız ve burun uygun parametreler sağlatılarak yüz içerisinde aratıldı.
                i = 0
                if (len(eyes) > 0):  # gözlerin bulunması durumunda;

                    if (len(mouth) == 0):  # ağzın bulunmaması durumunda;

                        if (len(nose) == 0):  # burnun bulunmaması durumunda;
                            cv2.putText(frame, weared_mask, (x + w, y + h), fontFace,
                                        fontScale, (0, 255, 0),
                                        2, cv2.LINE_AA)
                        # maskesini taktığı için görüntüdekine teşekkür texti görüntüye yollandı.
                        else:  # burnun bulunmaması durumunda;
                            cv2.putText(frame, nose_problem, (x + w, y + h),
                                        fontFace, fontScale, (0, 0, 255),
                                        4, cv2.LINE_AA)
                        # burnunu da kapatması için uyarı yapılan text görüntüye yollandı.
                    else:  # ağzın bulunmaması durumunda;
                        cv2.putText(frame, not_weared_mask, (x + w, y + h),
                                    fontFace, fontScale, (0, 0, 255),
                                    4, cv2.LINE_AA)
                    # maskenin olmadığına dair text görüntüye yollandı.

    cv2.imshow("Mask Detection", frame)  # Görüntüye yollanan tüm veriler ekrana yansıtıldı.

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q tuşuna basılması halinde program sonlandırıcı break komutu verildi.
        break

cap.release()  # görüntü serbest bırakıldı.
cv2.destroyAllWindows()  # açılan tüm pencereler temizlendi.
os.system('cmd /k "python .\\__init__.py"') #Backend çalışmayı sonlandırınca bu komut ile tekrardan GUI aktif hale getirilir

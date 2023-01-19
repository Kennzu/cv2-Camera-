# import numpy as np
import cv2
from PIL import Image, ImageChops
import time


    
def camera():
    cam = cv2.VideoCapture(0)
    while True: #Для постоянного считывания видеоряда
        succes, img = cam.read()  #succes - для возвращения результата о считывании картинки с видева а в img будет считыватсья инфа

        face_cas = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") # обращение к дериктории с указанием на каскады от open cv (Кскады здесь https://github.com/opencv/opencv/tree/master/data/haarcascades)
        # img = cv2.imread('scale_1200.jpg') # распознавание по фото
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Преобразование в оттенки серого
        faces = face_cas.detectMultiScale(img_g, 1.1, 19) #Если странно распознает, то поиграйтесь с цифрой 5. Поставьте больше/меньше
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)# 0 - синий цвет 255 - зеленый цвет и еще один 0 - красный цвет, а последняя цифра - толщина
        # cv2.imshow('crush, crush, crush', img_g)
        cv2.imshow('crush, crush, crush', img)
        if cv2.waitKey(1) & 0xff == ord("w"): # кнопка для выхода из просмотра
            break
        elif cv2.waitKey(2) & 0xff == ord("s"):
            # for i in range(30): # Типа прогрев камеры для более светлого снимка
                time.sleep(1)
                cam.read()
                rett, framee = cam.read() # Делается снимок
                cv2.imwrite('camcam11.png', framee) # Сохраняется снимок
                print("Скрин успешно сделан!")
                access = input("Нужен доступ к расширенному функционалу? Да / Нет: ")
                if access == 'Да':
                    access1()
                elif access == 'Нет':
                    print("Работа на этом окончена!")
                else:
                    print("Вы допустили ошибку в написании" + access)
                    cam.release()
    cam.release()# освобождает камеру
    cv2.destroyAllWindows()# Как чел объяснил - разрушает окошки, а какие я нихуя не понял, но для считывания видева обязательно в конце надо
camera()

def access1():
    cam = cv2.VideoCapture(0)
    while True: #Для постоянного считывания видеоряда
        succes, img = cam.read()  #succes - для возвращения результата о считывании картинки с видева а в img будет считыватсья инфа

        face_cas = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") # обращение к дериктории с указанием на каскады от open cv (Кскады здесь https://github.com/opencv/opencv/tree/master/data/haarcascades)
        # img = cv2.imread('scale_1200.jpg') # распознавание по фото
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Преобразование в оттенки серого
        faces = face_cas.detectMultiScale(img_g, 1.1, 19) #Если странно распознает, то поиграйтесь с цифрой 5. Поставьте больше/меньше
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)# 0 - синий цвет 255 - зеленый цвет и еще один 0 - красный цвет, а последняя цифра - толщина
        # cv2.imshow('crush, crush, crush', img_g)
        cv2.imshow('crush, crush, crush', img)
        if cv2.waitKey(1) & 0xff == ord('w'): # кнопка для выхода из просмотра
            break
        elif cv2.waitKey(2) & 0xff == ord("q"):
            for i in range(30): # Типа прогрев камеры для более светлого снимка
                cam.read()
            rett, framee = cam.read() # Делается снимок
            cv2.imwrite('camcam2.png', framee).photo[0].file_id # Сохраняется снимок
            def difference_images(img1, img2):
                image_1 = Image.open(img1)
                image_2 = Image.open(img2)
                result=ImageChops.difference(image_1, image_2).getbbox()
                if result==None:
                    print(img1,img2,'matches')
                return            
            difference_images()  



    



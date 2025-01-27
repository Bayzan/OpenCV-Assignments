import cv2

cam = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("drongri.avi", fourrc, 30.0 , (640,480))

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı")
        break

    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("videodan ayrıldınız")
        break

cam.release()
out.release()
cv2.destroyAllWindows()





















# cam = cv2.VideoCapture("futbol.mp4")

# while cam.isOpened():
    
#     ret, frame = cam.read()
    
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     if not ret:
#         print("kameradan görüntü alınamıyor")
#         break
    
#     cv2.imshow("görüntü",frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("video kapatıldı")
#         break

# cam.release()
# cv2.destroyAllWindows()








# sifir = np.zeros([300,300])

# bir = np.ones([300,300])

# cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
# cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

# cv2.imshow("sifir",sifir)
# cv2.imshow("bir",bir)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# cam = cv2.VideoCapture(0)

# print(cam.get(3))
# print(cam.get(3))

# cam.set(3, 320)
# cam.set(4,240) 

# print(cam.get(3))
# print(cam.get(3))


# if not cam.isOpened():
#     print("kamera tanınmadı")
#     exit()

# while True:
#     ret, frame = cam.read()
    
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
#     if not ret:
#         print("kameradan görüntü okunamıyor")
#         break
    
#     cv2.imshow("kamera",frame)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("görüntü sonlandırıldı")
#         break

# cam.release()
# cv2.destroyAllWindows()    










import os
import cv2
import time
import handTrackingModule as htm

cap = cv2.VideoCapture(0)
pTime = 0

FolderPath = "./Image_Fingers"
lst = os.listdir(FolderPath)
lst_2 = []
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    # print(f"{FolderPath}/{i}")
    lst_2.append(image)

detector = htm.handDetector(detectionCon=1)

fingerid = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False) #Hiển thị hand mark
    print (lmList)
    
    # Xử lý các ngón tay
    if len(lmList) != 0:
        
        fingers = []
        
        # Xử lý ngón cái 
        if lmList[fingerid[0]][1] < lmList[fingerid[0]-1][1]: #So sánh theo chiều rộng của ngón (xem hình hand_mark)
            fingers.append(1)
        else:
            fingers.append(0)
        
        
        # Xử lý các ngón dài
        for  id in range(1, 5):
            
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]: #So sánh theo chiều cao của ngón (xem hình hand_mark)
                fingers.append(1)
            else:
                fingers.append(0)
                
                
        countFinger = fingers.count(1) #Đếm số ngòn tay
        
    
        h, w, c = lst_2[countFinger-1].shape # lấy height, width, channel 
        # frame[0:h, 0:w] = lst_2[countFinger-1] # đưa ảnh ra ngoài webcam theo tỉ lệ của khung hình (400, 400, 3)
        
        
        # Vẽ hình hiện số ngòn tay
        cv2.rectangle(frame, (0, 200), (150, 400), (255, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, str(countFinger), (10, 300), font, 12, (255, 255, 255), 3)
    
    # Show FPS
    cTime = time.time() #Trả về số giấy, tính từ 0:0:00  1/1/1970 theo giờ utc, gọi là điểm bắt đầu thời gian
    fps = 1/(cTime - pTime)
    pTime = cTime #Để thực hiện vòng lặp mới
    
    # Show fps ra webcam
    cv2.putText(frame, f"FPS:{int(fps)}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    # (50, 50): toạ độ  x, y trên ảnh
    # cv2.FONT_HERSHEY_PLAIN : Loại chữ viết
    # 2 : Thông tin chữ có độ dài
    # (0, 0, 255) : Màu chữ , R-G-B
    # 2 : Kích thước chữ

    # Display the resulting frame on screen
    
    cv2.imshow("Nguyen Phong", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

    
    
    
    

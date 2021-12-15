import cv2

color = (255,0,0)

PlateCascade = cv2.CascadeClassifier("/Users/yc4ny/PycharmProjects/numberPlate_detector/haarcascade_russian_plate_number.xml")
img = cv2.imread("/Users/yc4ny/PycharmProjects/numberPlate_detector/images/image2.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plates = PlateCascade.detectMultiScale(imgGray, 1.1, 4)

for(x,y,w,h) in plates :
    cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,), 1)
    cv2.putText(img, "Number Plate", (x,y), cv2.FONT_HERSHEY_COMPLEX,0.5,color,2)
    plate = img[y:y+h, x:x+w]
    cv2.imshow("ROI", plate)
    cv2.imshow("Result", img)

    if cv2.waitKey(0) & 0XFF == ord('q'):
        break


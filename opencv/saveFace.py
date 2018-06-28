import cv2
from PIL import Image

casc_path = "C:\\Users\\KennyTseng\\Anaconda3\\pkgs\\opencv3-3.1.0-py35_0\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(casc_path)
image = cv2.imread("image\\us.jpg")
svImage = Image.open("image\\us.jpg")

faces = faceCascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
count = 1
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2)
    filename = "image\\faces" + str(count) + ".jpg"
    tmp = svImage.crop((x, y, x+w, y+h))
    faceImage = tmp.resize((200,200), Image.ANTIALIAS)
    faceImage.save(filename)
    count += 1

cv2.namedWindow("FaceDetect")
cv2.imshow("FaceDetect", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
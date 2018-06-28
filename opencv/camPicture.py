import cv2

cv2.namedWindow("CameraFrame")
# the number of camera
cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    ret, img = cam.read()
    if ret == True:
        cv2.imshow("CameraFrame", img)
        k = cv2.waitKey(0)
        if k == ord("s") or k == ord("S"):
            cv2.imwrite("image\\catch.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break

cam.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
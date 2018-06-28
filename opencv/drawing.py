import cv2, numpy

# window
cv2.namedWindow("Image")
# read image
image = cv2.imread("image\\landscape.jpg", cv2.IMREAD_UNCHANGED)

# drawing
cv2.line(image, (50,50), (500,300), (0,0,255), 2)
cv2.rectangle(image, (50,200), (200,350), (255,0,0), 3)
cv2.rectangle(image, (50,400), (200,550), (255,0,0), -1)
cv2.circle(image, (700,200), 100, (0,255,0), -1)
pts = numpy.array([[900,200], [1100,300], [1000,500]], numpy.int32)
cv2.polylines(image, [pts], True, (255,100,100), 20)
cv2.putText(image, "drawing by OpenCV", (400,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)

# saving image
# cv2.imwrite("image\\image.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100])

# show image 
cv2.imshow("Image", image)
# pause until input from keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
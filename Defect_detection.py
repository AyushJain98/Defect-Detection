import cv2
print(cv2.__version__)

import cv2
img = cv2.imread('surface.jpg')
print('Image Shape : ',img.shape)
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print('Grayscale Shape :',gray.shape)

edges = cv2.Canny(gray ,50,150)
print("Edges Shape ; ",edges.shape)

cv2.imwrite('grayscale.jpg', gray)
cv2.imwrite('edges.jpg', edges)
print("Images saved!")
result = img.copy()
result[edges !=0] = [0,0,255]
cv2.imwrite('defects_highlighted.jpg',result)
print("defect highlighted image saved!")
print("defective pixels found : ",edges[edges!=0].size)

result = img.copy()
for i,c in enumerate(filtered_contours):
    area = cv2.contourArea(c)

    if area<100:
       Size="Small"
    elif area <500:
        Size="medium"
    else :
        Size ="Large"
    x,y,w,h = cv2.boundingRect(c)
    result = cv2.rectangle(result, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(result,str(i+1),(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    cv2.putText(result,Size,(x,y+h+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)
cv2.imwrite("defects_boxed.jpg",result)
print(f"Total defects found: {len(filtered_contours)}")
small = 0
medium = 0
large = 0

for c in filtered_contours:
    area = cv2.contourArea(c)
    if area < 100:
        small += 1
    elif area < 500:
        medium += 1
    else:
        large += 1

print(f"Small defects: {small}")
print(f"Medium defects: {medium}")
print(f"Large defects: {large}")

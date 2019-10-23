import os
import cv2

mypath = 'tiles/'
imagefiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith('jpg')]
print(imagefiles)

for i in range(len(imagefiles)):
  img = cv2.imread(mypath + imagefiles[i])
  img = cv2.resize(img, (20,20))
  cv2.imwrite('tiles_20/'+str(i)+'.jpg', img)
  print('tiles_20/'+str(i)+'.jpg')

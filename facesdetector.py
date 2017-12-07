import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
#%matplotlib inline
class FaceDetector:
    def __init__(self):
        self.imagepath = 'file.jpg'
    def replacefaces(self, imagepath):
        self.imagepath = imagepath
        cascPath = "face_cascade_search.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        #faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagepath)
        image_PIL = Image.open(imagepath)
        #plt.imshow(image)
        #plt.show()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
           gray,
           scaleFactor=1.1,
           minNeighbors=5,
           minSize=(30, 30),
           flags = cv2.CASCADE_SCALE_IMAGE #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        #.resize()
        print("Found {0} faces!".format(len(faces)))

        pedo_img = Image.open("pedo.png")
        #pedo_img = Image.open('img.png')
        #pedo_img = pedo_img.convert("RGBA")
        '''datas = pedo_img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        '''
        #pedo_img.putdata(newData)
        #pedo_img.save("pedo2.png")
        #pedo1_img = Image.open("pedo2.png")
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            pedo_img = pedo_img.resize((int((w+x) / 1.5), int((w+x)/1.5)))
            image_PIL.paste(pedo_img, (int(x - w / 2), int(y - h / 2)), pedo_img)
            #cv2.circle(image, (int(x + w / 2), int(y + h / 2)), w if w > h else h, (255, 255, 0, 2))
            #cv2.circle()
        image_PIL.save('result.png')
        #plt.imshow(image)
        #plt.show()
        #image_PIL.show()
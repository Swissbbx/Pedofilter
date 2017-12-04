from PIL import Image, ImageFilter
from numpy import arange
import matplotlib.pyplot as plt

img = Image.open('image3.jpg')

#print("%s\n%s") % {img.size, img.format}
img = img.filter(ImageFilter.GaussianBlur(3))
#img = img.filter(ImageFilter.)
print(img.format)
#img.show()
#print(img.format)
area = (10, 10, 40, 40)
img_cropped = img.resize((40, 40))
#img_cropped = img
#img_cropped.show()
img_resized = img_cropped.resize((960, 640), Image.BICUBIC)
pixels = list(img_resized.getdata())
pixels = [pixels[i * img.size[0]:(i + 1) * img.size[0]] for i in range(img.size[1])]
print(img.format)
plt.plot(arange(len(pixels[50])), pixels[50], 'r')  # чистый сигнал
# #plt.plot(arange(pixels))
plt.xlabel(u'i, ')
plt.ylabel(u'm1(i), ')
plt.title(u'BICUBIC')
plt.grid(True)
plt.show()
img_resized1 = img_cropped.resize((960, 640), Image.BILINEAR)
pixels1 = list(img_resized1.getdata())
pixels1 = [pixels[i * img.size[0]:(i + 1) * img.size[0]] for i in range(img.size[1])]
print(img.format)
plt.plot(arange(len(pixels1[50])), pixels1[50],)  # чистый сигнал
# #plt.plot(arange(pixels))
plt.xlabel(u'i, ')
plt.ylabel(u'm1(i), ')
plt.title(u'BILINEAR')
plt.show()
img_resized1.show()
img_resized.show()
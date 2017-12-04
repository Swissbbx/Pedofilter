from PIL import Image, ImageFilter

def main():
    img = Image.open('image3.jpg')
    img2 = Image.open('image2.jpg')
    img2 = img2.resize(img.size)
    print(img.mode)
    r, g, b = img.split()
    r1, g1, b1 = img2.split()
    #img2.paste(0, (0, 0) + img.size)
    img3 = Image.merge('RGB', (r1, g, b1))
    img3 = img3.transpose(Image.FLIP_LEFT_RIGHT)
    for i in range(50):
        img3 = img3.filter(ImageFilter.SMOOTH)
    img3.show()
main()
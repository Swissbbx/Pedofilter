from PIL import Image, ImageFilter

def oldFoto(image):

    image = image.convert("RGB")
    R, G, B = image.split()

    R = R.filter(ImageFilter.SMOOTH)
    R = R.filter(ImageFilter.EMBOSS)
    G = G.filter(ImageFilter.BLUR)
    B = G.filter(ImageFilter.SHARPEN)
    return Image.merge("RGB", (R, G, B))

def frescoOnTheChromaKey(image):

    image = image.convert("RGB")
    image = image.filter(ImageFilter.FIND_EDGES)
    R, G, B = image.split()
    R = R.filter(ImageFilter.SHARPEN)
    G = G.filter(ImageFilter.EMBOSS)
    B = B.filter(ImageFilter.SHARPEN)
    return Image.merge("RGB", (R, G, B))

def demonInConsole(image):
    image = image.convert("RGB")

    R, G, B = image.split()
    R = R.filter(ImageFilter.CONTOUR)
    result = Image.merge("RGB", (R, G, B))
    result = result.filter(ImageFilter.FIND_EDGES)
    return result

def lemonParadise(image):
    image = image.convert("RGB")
    R, G, B = image.split()

    R = R.filter(ImageFilter.CONTOUR)
    G = G.filter(ImageFilter.CONTOUR)
    return Image.merge("RGB", (R, G, B))

def deepInPurple(image):
    image = image.convert("RGB")
    for i in range(0, 5):
        image = image.filter(ImageFilter.DETAIL)

    R, G, B = image.split()
    R = R.filter(ImageFilter.CONTOUR)
    B = B.filter(ImageFilter.CONTOUR)
    return Image.merge("RGB", (R, G, B))

def aquarium(image):
    image = image.convert("RGB")

    image = image.filter(ImageFilter.BLUR)
    R, G, B = image.split()
    R = R.filter(ImageFilter.FIND_EDGES)
    return Image.merge("RGB", (R, G, B))

def tonedCar(image):
    image = image.convert("CMYK")
    C, M, Y, K = image.split()
    for i in range(0, 3):
        K = K.filter(ImageFilter.EMBOSS)
    result = Image.merge("CMYK", (C, M, Y, K))
    return result.convert("RGB")

def roboPainter(image):
    image = image.convert("CMYK")
    C, M, Y, K = image.split()
    for i in range(0, 5):
        C = C.filter(ImageFilter.SHARPEN)
        M = M.filter(ImageFilter.SHARPEN)
        Y = Y.filter(ImageFilter.SHARPEN)
    result = Image.merge("CMYK", (C, M, Y, K))
    result = result.filter(ImageFilter.SMOOTH_MORE)
    return result.convert("RGB")

def indigo(image):
    image = image.convert("CMYK")
    C, M, Y, K = image.split()
    Y = Y.filter(ImageFilter.EMBOSS)
    result = Image.merge("CMYK", (C, M, Y, K))

    return result.convert("RGB")





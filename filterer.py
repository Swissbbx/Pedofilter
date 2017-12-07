from PIL import Image, ImageFilter, ImageMath, ImageOps, ImageChops
import math

class Filterer:
    def __init__(self):
        pass

    def oldPhoto(self, pathtoimage):
        image = Image.open(pathtoimage)
        image = image.convert("RGB")
        R, G, B = image.split()
        R = R.filter(ImageFilter.SMOOTH)
        R = R.filter(ImageFilter.EMBOSS)
        G = G.filter(ImageFilter.BLUR)
        B = G.filter(ImageFilter.SHARPEN)
        return Image.merge("RGB", (R, G, B))

    def frescoOnTheChromaKey(self, pathtoimage):
        image = Image.open(pathtoimage)
        image = image.convert("RGB")
        image = image.filter(ImageFilter.FIND_EDGES)
        R, G, B = image.split()
        R = R.filter(ImageFilter.SHARPEN)
        G = G.filter(ImageFilter.EMBOSS)
        B = B.filter(ImageFilter.SHARPEN)
        return Image.merge("RGB", (R, G, B))

    def demonInConsole(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("RGB")

        R, G, B = image.split()
        R = R.filter(ImageFilter.CONTOUR)
        result = Image.merge("RGB", (R, G, B))
        result = result.filter(ImageFilter.FIND_EDGES)
        return result

    def lemonParadise(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("RGB")
        R, G, B = image.split()

        R = R.filter(ImageFilter.CONTOUR)
        G = G.filter(ImageFilter.CONTOUR)
        return Image.merge("RGB", (R, G, B))

    def deepInPurple(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("RGB")
        for i in range(0, 5):
            image = image.filter(ImageFilter.DETAIL)

        R, G, B = image.split()
        R = R.filter(ImageFilter.CONTOUR)
        B = B.filter(ImageFilter.CONTOUR)
        return Image.merge("RGB", (R, G, B))

    def aquarium(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("RGB")

        image = image.filter(ImageFilter.BLUR)
        R, G, B = image.split()
        R = R.filter(ImageFilter.FIND_EDGES)
        return Image.merge("RGB", (R, G, B))

    def tonedCar(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("CMYK")
        C, M, Y, K = image.split()
        for i in range(0, 3):
            K = K.filter(ImageFilter.EMBOSS)
        result = Image.merge("CMYK", (C, M, Y, K))
        return result.convert("RGB")

    def roboPainter(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("CMYK")
        C, M, Y, K = image.split()
        for i in range(0, 5):
            C = C.filter(ImageFilter.SHARPEN)
            M = M.filter(ImageFilter.SHARPEN)
            Y = Y.filter(ImageFilter.SHARPEN)
        result = Image.merge("CMYK", (C, M, Y, K))
        result = result.filter(ImageFilter.SMOOTH_MORE)
        return result.convert("RGB")

    def indigo(self, pathtoimage):
        image = Image.open(pathtoimage)

        image = image.convert("CMYK")
        C, M, Y, K = image.split()
        Y = Y.filter(ImageFilter.EMBOSS)
        result = Image.merge("CMYK", (C, M, Y, K))
        return result.convert("RGB")




    def freq_colorize(self, img__, radius_lo=1, radius_hi=20, aa=4, iter_count=12):
        img_ = Image.open(img__)
        orig_size = img_.size

        img = img_.resize((aa * img_.size[0], aa * img_.size[1]), Image.BICUBIC)
        prev = img

        cur_mul = aa

        prev_r2 = 0
        now_r2 = 0

        ret = Image.new('RGB', img.size)

        for i in range(iter_count):
            prev_r2 = now_r2
            now_r2 = radius_lo * math.pow(radius_hi / radius_lo, 2 * i / iter_count)

            col = hsv2rgb(i, 1, iter_count)

            prev = img
            img = img.filter(ImageFilter.GaussianBlur(cur_mul * math.sqrt(now_r2 - prev_r2)))
            diff = ImageMath.eval("abs(a-b)", a=prev, b=img).convert('L')

            if (cur_mul * math.sqrt(now_r2) / aa) > 2:  # 2 is magic, please touch it
                img = img.resize((img.size[0] // 2, img.size[1] // 2), Image.BICUBIC)
                cur_mul /= 2

            ret = ImageChops.add(ret, ImageOps.colorize(diff.resize(orig_size, Image.BICUBIC), (0, 0, 0),
                                                        hsv2rgb(i / iter_count, 1, 2 * 255)))

        return ret

    #out = freq_colorize(img, 1, 20, 2, 12)
    #out.show()
    #out.save('out.png')

def hsv2rgb(h, s, v):
    K = (3 / 3, 2 / 3, 1 / 3, 3)
    p = (
        abs(((h + K[0]) % 1) * 6 - K[3]),
        abs(((h + K[1]) % 1) * 6 - K[3]),
        abs(((h + K[2]) % 1) * 6 - K[3]))
    return (
        v * mix(K[0], clamp(p[0] - K[0], 0, 1), s),
        v * mix(K[0], clamp(p[1] - K[0], 0, 1), s),
        v * mix(K[0], clamp(p[2] - K[0], 0, 1), s))

def clamp(x, lo, hi):
        return min(max(x, lo), hi)

def mix(x, y, a):
        return x * (1 - a) + y * a
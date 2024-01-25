try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


####################### 01

# captcha = Image.open("captcha1.png")
# result = pytesseract.image_to_string(captcha)
# print(result)


####################### 02
def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0

    data = img.getdata()
    w, h = img.size
    count = 0
    for x in range(1, h - 1):
        for y in range(1, h - 1):
            # 找出各个像素方向
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]

                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if down_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)

    return img


captcha = Image.open("captcha3.png")
result = captcha.convert('L')
result1 = convert_img(result, 150)
# result = captcha.convert()
result1.show()

# 识别一下
result2 = pytesseract.image_to_string(result1)
print(result2)

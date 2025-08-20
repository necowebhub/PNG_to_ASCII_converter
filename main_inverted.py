import cv2

string = " `.,-':<>;+!*/?%&98#"
coef = 255 / (len(string) - 1)
image = cv2.imread('img/maxresdefault.png')
height, width, channels = image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Инвертируем цвета изображения
inverted_gray_image = cv2.bitwise_not(gray_image)

with open("output/ASCII_Art.txt", "w") as file:
    for x in range(0, width - 1, 8):
        s = ""
        for y in range(0, height - 1, 4):
            try:
                s += string[len(string) - int(inverted_gray_image[x, y] / coef) - 1]
                continue
            except IndexError:
                pass
        if len(s) != 0:
            file.write(s + "\n")

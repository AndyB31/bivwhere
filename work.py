import os

from PIL import Image

#2682 / 17

#1772 / 11

NB_W = 20
NB_H = 12

GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
CLEAR = '\033[0m'

NO_TRAIL = 0
NEAR_TRAIL = 1
TRAIL = 2

def crop(im, path, height, width, k, page):
    imgwidth, imgheight = im.size
    x = 0
    for i in range(0,imgheight,height):
        y = 0
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            o = im.crop(box)
            try:
                # o = a.crop(area)
                o.save(os.path.join(path, f"{page}", f"IMG-{x}-{y}.png"))
            except Exception as e:
                print(e)
            k +=1
            y += 1
        x += 1

NB_PX_RANDO = 6

# rando rgba(191,160,49,255) +/-10
def rando_check(px):
    if px[0] < 180:
        return False
    if px[0] > 200:
        return False
    if px[1] < 150:
        return False
    if px[1] > 170:
        return False
    if px[2] < 40:
        return False
    if px[2] > 60:
        return False
    return True

def check_all_pix(img):
    width, height = img.size
    pixels = img.load()
    is_rando_box = False
    delta = 1 / NB_PX_RANDO
    tmp = 0

    for i in range(width):
        for j in range(height):
            px = pixels[i, j]
            if rando_check(px):
                tmp += delta

            if tmp >= 1:
                is_rando_box = True
                break

    return is_rando_box

def human_readable_display(img_arr):
    for line in img_arr:
        for box in line:
            color = RED
            if box == 1:
                color = BLUE
            if box == 2:
                color = GREEN
            print(f"{color}#{CLEAR} ", end="")
        print("\n")

def check_near_trail(img_arr):
    for i in range(NB_H):
        for j in range(NB_W):
            if img_arr[i][j] == TRAIL:
                continue
            tmp = []
            if i > 0:
                tmp.append(img_arr[i - 1][j])
                if j > 0:
                    tmp.append(img_arr[i - 1][j - 1])
                if j < NB_W - 1:
                    tmp.append(img_arr[i - 1][j + 1])
            if j > 0:
                tmp.append(img_arr[i][j - 1])
            if i < NB_H - 1:
                tmp.append(img_arr[i + 1][j])
                if j > 0:
                    tmp.append(img_arr[i + 1][j - 1])
                if j < NB_W - 1:
                    tmp.append(img_arr[i + 1][j + 1])
            if j < NB_W - 1:
                tmp.append(img_arr[i][j + 1])

            img_arr[i][j] = max(tmp) - 1
            img_arr[i][j] = 0 if img_arr[i][j] < 0 else img_arr[i][j]


def divide_image(input: str):
    name = input.split('/')[-1].split('.')[0]
    with Image.open(input) as im:
        imgwidth, imgheight = im.size
        lilw = int(imgwidth / NB_W)
        lilh = int(imgheight / NB_H)
        isExist = os.path.exists(f"./output/{name}")
        if not isExist:
            os.makedirs(f"./output/{name}")
        crop(im, "./output/", lilh, lilw, 0, name)

    lil_img = []
    for i in range(NB_H):
        lil_img.append([])
        for j in range(NB_W):
            with Image.open(f"./output/{name}/IMG-{i}-{j}.png") as img:
                lil_img[i].append(TRAIL if check_all_pix(img) else NO_TRAIL)

    human_readable_display(lil_img)
    print("------------------------------------------")
    check_near_trail(lil_img)
    human_readable_display(lil_img)


def main():
    divide_image("./map_test.png")


if __name__ == "__main__":
    main()
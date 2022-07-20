import os

from PIL import Image

NB_W = 40
NB_H = 22

GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
CLEAR = '\033[0m'

AUTHORIZED = 0
FORBIDDEN = 1

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

NB_PX_RANDO = 10

# protected rgba(190-250,190-250,1-50,255) +/-10
# border rgba(148,191,65,255)
def forbidden_check(px):
    if px[0] < 250:
        return False
    if px[1] < 250:
        return False
    if px[2] < 60:
        return False
    if px[2] > 70:
        return False
    return True

def check_all_pix(img):
    width, height = img.size
    pixels = img.load()
    is_forbidden_box = False
    delta = 1 / NB_PX_RANDO
    tmp = 0

    for i in range(width):
        for j in range(height):
            px = pixels[i, j]
            # print(px)
            if forbidden_check(px):
                tmp += delta

            if tmp >= 1:
                is_forbidden_box = True
                break

    return is_forbidden_box

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

def analyse_protected(path: str):
    lil_img = []
    for i in range(NB_H):
        lil_img.append([])
        for j in range(NB_W):
            with Image.open(os.path.join(path, f"IMG-{i}-{j}.png")) as img:
                lil_img[i].append(FORBIDDEN if check_all_pix(img) else AUTHORIZED)

    human_readable_display(lil_img)
    return lil_img
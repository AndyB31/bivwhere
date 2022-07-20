import os

from PIL import Image

#2682 / 17

#1772 / 11

NB_W = 40
NB_H = 22

GREEN = '\033[92m' # no pente
BLUE = '\033[94m' # pente1
PURPLE = '\033[95m' # pente2
ORANGE = '\033[93m' # pente3
RED = '\033[91m' # pente4
CLEAR = '\033[0m'

AUTHORIZED = 0
FORBIDDEN = 1

#totalpixel = 741 ligne
NB_PX_RANDO = 50

# pente4: rgba(233,209,229,255) / rgba(228,204,225,255) / rgba(221,194,215,255)
def pente4(px):
    if px[0] < 220:
        return False
    if px[0] > 240:
        return False
    if px[1] < 190:
        return False
    if px[1] > 210:
        return False
    if px[2] < 210:
        return False
    if px[2] > 230:
        return False
    return True

# pente3: rgba(242,154,188,255) / rgba(230,143,177,255) / rgba(239,153,187,255)
def pente3(px):
    if px[0] < 230:
        return False
    if px[0] > 245:
        return False
    if px[1] < 140:
        return False
    if px[1] > 160:
        return False
    if px[2] < 175:
        return False
    if px[2] > 190:
        return False
    return True

# pente2: rgba(250,197,166,255) / rgba(241,186,157,255) / rgba(243,189,159,255)
def pente2(px):
    if px[0] < 240:
        return False
    if px[1] < 185:
        return False
    if px[1] > 200:
        return False
    if px[2] < 155:
        return False
    if px[2] > 170:
        return False
    return True

# pente1: rgba(246,242,155,255) / rgba(234,230,143,255) / rgba(247,240,153,255)
def pente1(px):
    if px[0] < 230:
        return False
    if px[0] > 250:
        return False
    if px[1] < 225:
        return False
    if px[1] > 245:
        return False
    if px[2] < 140:
        return False
    if px[2] > 160:
        return False
    return True

def check_all_pix(img):
    width, height = img.size
    pixels = img.load()
    pente_classes = -1
    delta = 1 / NB_PX_RANDO
    tmp = [0, 0, 0, 0]

    for i in range(width):
        for j in range(height):
            px = pixels[i, j]
            # print(px)
            if pente4(px):
                tmp[3] += delta
            if pente3(px):
                tmp[2] += delta
            if pente2(px):
                tmp[1] += delta
            if pente1(px):
                tmp[0] += delta
    if max(tmp) > 1:
        pente_classes = tmp.index(max(tmp))
    return pente_classes + 1

def human_readable_display(img_arr):
    for line in img_arr:
        for box in line:
            color = GREEN
            if box == 1:
                color = BLUE
            if box == 2:
                color = PURPLE
            if box == 3:
                color = ORANGE
            if box == 4:
                color = RED 
            print(f"{color}#{CLEAR} ", end="")
        print("\n")

def analyse_slope(path: str):
    lil_img = []
    for i in range(NB_H):
        lil_img.append([])
        for j in range(NB_W):
            with Image.open(os.path.join(path, f"IMG-{i}-{j}.png")) as img:
                lil_img[i].append(check_all_pix(img))

    human_readable_display(lil_img)
    return lil_img
    # print("------------------------------------------")
    # check_near_trail(lil_img)
    # human_readable_display(lil_img)


import os
from re import A
from PIL import Image
from collections import defaultdict 

NB_W = 40
NB_H = 22

GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
CLEAR = '\033[0m'
ORANGE = '\033[93m'

AUTHORIZED = 0
FORBIDDEN = 1

NB_PX_RANDO = 550

# gris roche okay rgba(221,221,221,255) +/-10
# rouge habitation rgba(255,206,206, 255) +/-10
#vert buisson foret (219, 255, 219, 255) // 159,198,64
#bleu lac eau 204, 252, 255

def forbidden_check_primaire(px):
    if px[0] > px[1] and px[0] > px[2]:
        return True
    if px[1] > px[0] and px[1] > px[2]:
        return False
    if px[2] > px[1] and px[2] > px[0]:
        return True
    if px[0] > px[1] and px[0] > px[2] and px[1] > px[2]:
        return False
    if px[0] == px[1] == px[2]:
        return True
    
def per_image_proportion_primaire(px):
    if px[0] > px[1] and px[0] > px[2]:
        return "red"
    elif px[1] > px[0] and px[1] > px[2]:
        return "green"
    elif px[2] > px[1] and px[2] > px[0]:
        return "bleu"
    elif px[0] > px[1] and px[0] > px[2] and px[1] > px[2]:
        return "marron"
    elif px[0] == 0 == px[1] == px[2]:
        return "noir"
    elif px[0] == 255 == px[1] == px[2]:
        return "blanc"
    elif px[0] == px[1] == px[2]:
        return "gris"
    else:
        return "inconnu"
    
def check_all_pix_primaire(img):
    width, height = img.size
    pixels = img.load()
    is_forbidden_box = False
    delta = 1 / NB_PX_RANDO
    tmp = 0
    pixel_map = defaultdict(int)
    for i in range(width):
        for j in range(height):
            px = pixels[i, j]
            # print(px)
            if forbidden_check_primaire(px):
                tmp += delta
                
            pixel_map[per_image_proportion_primaire(px)]+=1
               
            if tmp >= 1:
                is_forbidden_box = True
                # break
        
    return is_forbidden_box, pixel_map

def human_readable_display(img_arr):
    for line in img_arr:
        for box in line:
            color = RED
            if box == 0:
                color = BLUE
            print(f"{color}#{CLEAR} ", end="")
        print("\n")

def analyse_primaire(path: str):
    lil_img = []
    pixel_proportion = defaultdict(int)
    for i in range(NB_H):
        lil_img.append([])
        for j in range(NB_W):
            with Image.open(os.path.join(path, f"IMG-{i}-{j}.png")) as img:
                data_img = check_all_pix_primaire(img)
                lil_img[i].append(FORBIDDEN if data_img[0] else AUTHORIZED)
                pixel_proportion[f"{i}{j} image"]=data_img[1]

    human_readable_display(lil_img)
    # print(pixel_proportion[f"{2}{10} image"])
    return lil_img
    

import os

from PIL import Image

NB_W = 40
NB_H = 22

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

def divide_image(input: str, path: str):
    name = input.split('/')[-1].split('.')[0]
    with Image.open(input) as im:
        imgwidth, imgheight = im.size
        lilw = int(imgwidth / NB_W)
        lilh = int(imgheight / NB_H)
        isExist = os.path.exists(os.path.join(path, name))
        if not isExist:
            os.makedirs(os.path.join(path, name))
        crop(im, path, lilh, lilw, 0, name)
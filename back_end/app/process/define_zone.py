NB_W = 40
NB_H = 22

GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
CLEAR = '\033[0m'
ORANGE = '\033[93m'

#inputs : 
# hikin (trail) : TRAIL 2 NEAR TRAIL 1 NO TRAIL 0 
#protected : Forbbiden 1 Authorized 0 
#primary : Forbbiden 1 Authorized 0
#slope : 0 no pente 1 ok 2 3 4 pas ok 
#outputs : 
#green OK bivouac 
#Orange ok but not perfect 
#Red not ok 
def analyze_bivouac_capacity(img_arr_hiking, img_arr_protected, img_arr_primary, img_arr_slope):
    print("Légende : GREEN bivouac ok, ORANGE bivouac ok but with some unworking area RED bivouac not ok")
    print("\n")
    bvz = []
    for line in range(NB_H):
        bvz.append([])
        for box in range(NB_W):
            tmp = 2
            color = GREEN
            if img_arr_protected[line][box] == 1:
                color = RED
                tmp = 0
            else:
                if  img_arr_hiking[line][box] == 0:
                    tmp = 1
                    color = ORANGE
                if img_arr_slope[line][box] == 2:
                    tmp = 1
                    color = ORANGE
                if img_arr_slope[line][box] == 3 or img_arr_slope[line][box] == 4:
                    tmp = 0
                    color = RED 
                if img_arr_primary[line][box] == 1:
                    tmp = 0
                    color = RED
            print(f"{color}#{CLEAR} ", end="")
            bvz[line].append(tmp)
        print("\n")
    return bvz
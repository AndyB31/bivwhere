import logging
# import config
import os

from app import process


# logging.basicConfig(level=config.LOGLEVEL)
# logger = logging.getLogger(__name__)

res_dir = "./app/ressources/maps/"

analysis = { #TODO: add couverture primaire
    "map_protected": process.analyse_protected,
    "map_slope_over_30": process.analyse_slope,
    "map_hiking_trail": process.analyse_hiking,
    "map_vector_25": process.analyse_primaire,
}

def analyze_location(long, lat):
    e, n = process.conversion_loc(long, lat)
    return analyse_coords(e, n)

def analyse_coords(e, n):
    if not os.path.isdir(res_dir):
        os.makedirs(res_dir)
    dirname = process.scrap_image(res_dir, e, n)
    path = os.path.join(res_dir, dirname)
    res = {}
    for map_type in analysis.keys():
        process.divide_image(f"{path}/{map_type}.png", f"{path}/")
        res[map_type] = analysis[map_type](os.path.join(path, map_type))

    print(res)
    bivouac_zone = process.analyze_bivouac_capacity(res["map_hiking_trail"], res["map_protected"], res["map_vector_25"], res["map_slope_over_30"])
    return bivouac_zone


def main():
    e = "2608084.69"
    n = "1173727.56"
    analyse_coords(e, n)

if __name__ == "__main__":
    main()
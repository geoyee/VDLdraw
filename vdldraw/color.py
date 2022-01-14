import random
import os.path as osp
from typing import List
from vdldraw import PATH


def get_xkcd_color(seed=1024) -> List:
    random.seed(seed)
    color_map = osp.join(PATH, "configs/rgb.txt")
    color_list = []
    with open(color_map, "r") as f:
        color_list = f.readlines()
    color_list.pop(0)  # del License
    color_list = [c.strip().split("\t")[-1] for c in color_list]
    random.shuffle(color_list)
    return color_list


if __name__ == "__main__":
    color_list = get_xkcd_color()
    print(color_list)
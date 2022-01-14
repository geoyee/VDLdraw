import os.path as osp
import matplotlib.pyplot as plt
from typing import List, Dict
from visualdl import LogReader
from convert import pb2dict
from folder import read_folder, mkdir_p
from color import get_xkcd_color
from canvas import init_canvas


def vdl_draw(log_dict: Dict, 
             save_folder: str="output", 
             tag_list: List=["mIoU", "Acc"]) -> None:
    sorted(log_dict)
    mkdir_p(save_folder)
    color_map = get_xkcd_color()
    for tag in tag_list:
        init_canvas(tag)
        for i, (name, path) in enumerate(log_dict.items()):
            reader = LogReader(file_path=path)        
            x = []
            y = []
            data = reader.get_data("scalar", "Evaluate/" + tag)
            for d in data:
                d = pb2dict(d)
                x.append(d["id"])
                y.append(d["value"])
            plt.plot(x, y, color=color_map[i], label=name)
        plt.legend()
        plt.savefig(osp.join(save_folder, (tag + ".png")))
        plt.close()
        print(f"Draw {tag} successfully!")


def vdl_draw_folder(log_folder: str, save_folder: str="output"):
    log_dict = read_folder(log_folder)
    vdl_draw(log_dict, save_folder)
    print("Finished!")
import os.path as osp
import matplotlib.pyplot as plt
from typing import List, Dict
from visualdl import LogReader
from .convert import pb2dict
from .folder import read_folder, mkdir_p


# TODO: 1.add title / 2.add color / 3.add mark / 4.support more tags
def vdl_draw(log_dict: Dict, 
             save_folder: str="output", 
             tag_list: List=["mIoU", "Acc"]) -> None:
    mkdir_p(save_folder)
    sorted(log_dict)
    for tag in tag_list:
        plt.figure(figsize=(10, 5))
        for name, path in log_dict.items():
            reader = LogReader(file_path=path)        
            x = []
            y = []
            data = reader.get_data("scalar", "Evaluate/" + tag)
            for d in data:
                d = pb2dict(d)
                x.append(d["id"])
                y.append(d["value"])
            plt.plot(x, y, label=name)
        plt.legend()
        plt.savefig(osp.join(save_folder, (tag + ".png")))
        print(f"Draw {tag} successfully!")


def vdl_draw_folder(log_folder: str, save_folder: str="output"):
    log_dict = read_folder(log_folder)
    vdl_draw(log_dict, save_folder)
    print("Finished!")
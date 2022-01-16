import os.path as osp
import matplotlib.pyplot as plt
from typing import List, Dict, Union
from visualdl import LogReader
from convert import pb2dict
from folder import read_folder, get_tags_from_dict,  mkdir_p
from color import get_xkcd_color
from canvas import init_canvas


def vdl_draw(log_dict: Dict,
             tag_list: List,
             save_folder: str="output",
             mplstyle: Union[str, None]=None) -> None:
    if len(tag_list) == 0:
        raise ValueError("No valid tags found!")
    sorted(log_dict)
    mkdir_p(save_folder)
    color_map = get_xkcd_color()
    for tag in tag_list:
        init_canvas(tag, mplstyle)
        for i, (name, path) in enumerate(log_dict.items()):
            reader = LogReader(file_path=path)
            data = reader.get_data("scalar", tag)
            if len(data) != 0:
                x = []
                y = []
                for d in data:
                    d = pb2dict(d)
                    x.append(d["id"])
                    y.append(d["value"])
                plt.plot(x, y, color=color_map[i], label=name)
        plt.legend()
        plt.savefig(osp.join(save_folder, (tag.replace("/", "@") + ".png")))
        plt.close()
        print("The {} saved successfully!".format(tag))


def vdl_draw_folder(log_folder: str, 
                    tag_list: List, 
                    save_folder: str="output",
                    mplstyle: Union[str, None]=None):
    log_dict = read_folder(log_folder)
    tags = check_tags(tag_list, get_tags_from_dict(log_dict))
    vdl_draw(log_dict, tags, save_folder, mplstyle)
    print("Finished!")


def check_tags(input_tags: List, usable_tags: List) -> List:
    output_tags = []
    for input_tag in input_tags:
        if input_tag in usable_tags:
            output_tags.append(input_tag)
        else:
            print("The {} is not in usable_tags, it will be ignored.".format(input_tag))
    return output_tags
import os.path as osp
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Union
from visualdl import LogReader
from .convert import pb2dict
from .folder import read_folder, get_tags_from_dict, mkdir_p
from .color import get_xkcd_color
from .canvas import init_canvas


def vdl_draw(log_dict: Dict,
             tag_list: List,
             save_folder: str="output",
             mplstyle: Union[str, None]=None,
             ranges: Union[List, Tuple, None]=None) -> None:
    marker=[".", ",", "o", "v", "^", "<", ">", 
            "1", "2", "3", "4", "s", "p", "*",
            "h", "H", "+", "x", "D", "d", "|",
            "_", ".", ","]
    if len(tag_list) == 0:
        raise ValueError("No valid tags found!")
    sorted(log_dict)
    mkdir_p(save_folder)
    color_map = get_xkcd_color()
    if len(log_dict) > len(color_map):
        raise AssertionError("Number of logs should not greater than {0}, but get {1}".format(
            len(color_map), len(log_dict)
        ))
    for tag in tag_list:
        init_canvas(tag, mplstyle)
        for i, (name, path) in enumerate(log_dict.items()):
            reader = LogReader(file_path=path)
            data = reader.get_data("scalar", tag)
            if len(data) != 0:
                x = []
                y = []
                if ranges is None:
                    for d in data:
                        d = pb2dict(d)
                        x.append(d["id"])
                        y.append(d["value"])
                else:
                    for d in data:
                        d = pb2dict(d)
                        if d["id"] > ranges[1]:
                            break
                        if d["id"] > ranges[0]:
                            x.append(d["id"])
                            y.append(d["value"])
                plt.plot(x, y, color=color_map[i], label=name, marker=marker[i])
        plt.legend()
        plt.savefig(osp.join(save_folder, (tag.replace("/", "@") + ".png")))
        plt.close()
        print("The {} saved successfully!".format(tag))


def vdl_draw_folder(log_folder: str, 
                    tag_list: List, 
                    save_folder: str="output",
                    mplstyle: Union[str, None]=None,
                    ranges: Union[List, Tuple, None]=None):
    log_dict = read_folder(log_folder)
    tags = check_tags(tag_list, get_tags_from_dict(log_dict))
    if isinstance(ranges, (list, tuple)):
        if len(ranges) != 2:
            raise ValueError("The ranges must have two int elements.")
        if not isinstance(ranges[0], int) and not isinstance(ranges[1], int):
            raise ValueError("The ranges elements must be int.")
        if ranges[1] <= ranges[0]:
            raise ValueError("The ranges[1] must greater than ranges[0].")
    vdl_draw(log_dict, tags, save_folder, mplstyle, ranges)
    print("Finished!")


def check_tags(input_tags: List, usable_tags: List) -> List:
    output_tags = []
    for input_tag in input_tags:
        if input_tag in usable_tags:
            output_tags.append(input_tag)
        else:
            print("The {} is not in usable_tags, it will be ignored.".format(input_tag))
    return output_tags
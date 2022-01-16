# import yaml
import os.path as osp
import matplotlib.pyplot as plt
from typing import Any, Union
from vdldraw import PATH


# def get_yaml_data(yaml_file: str) -> Any:
#     file_data = None
#     with open(yaml_file, "r", encoding="utf-8") as f:
#         file_data = f.read()
#     data = yaml.load(file_data, Loader=yaml.FullLoader)
#     return data


def init_canvas(tag: Any, mplstyle: Union[str, None]=None) -> None:
    plt_style = osp.join(PATH, "configs/plot.mplstyle") if mplstyle is None else mplstyle
    plt.style.use(plt_style)
    plt.figure()
    # TODO: How to better customize or use configuration files
    # yml_path = osp.join(PATH, osp.join("configs", (tag + ".yml")))
    # yml = get_yaml_data(yml_path)
    # plt.xlabel(yml["xlabel"])
    # plt.ylabel(yml["ylabel"])
    plt.xlabel("step")
    plt.ylabel(tag.split("/")[-1])
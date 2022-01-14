import yaml
import os.path as osp
import matplotlib.pyplot as plt
from typing import Any


def get_yaml_data(yaml_file: str) -> Any:
    file_data = None
    with open(yaml_file, "r", encoding="utf-8") as f:
        file_data = f.read()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def init_canvas(tag: Any) -> None:
    plt.style.use("configs/plot.mplstyle")
    plt.figure()
    yml_path = osp.join("configs", (tag + ".yml"))
    yml = get_yaml_data(yml_path)
    plt.xlabel(yml["xlabel"])
    plt.ylabel(yml["ylabel"])
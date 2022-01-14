import os
import os.path as osp
from typing import Dict


def read_folder(logs_folder: str) -> Dict:
    log_dict = dict()
    for root, dirs, files in os.walk(logs_folder):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == ".log":
                if name.split(".")[0] == "vdlrecords":
                    name = root.replace("/", "\\").split("\\")[-1]
                log_dict[name] = osp.join(root, file)
        for dir in dirs:
            log_dict.update(read_folder(dir))
    return log_dict


def mkdir_p(folder_path: str) -> None:
    if not osp.exists(folder_path):
        os.makedirs(folder_path)
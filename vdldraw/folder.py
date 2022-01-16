import os
import os.path as osp
from typing import Dict, List
from visualdl import LogReader


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


def get_tags_from_dict(log_dict: Dict) -> List:
    all_tags = []
    for _, path in log_dict.items():
        reader = LogReader(file_path=path)
        tags = reader.get_tags()["scalar"]
        all_tags.extend(tags)
    return list(set(all_tags))


def get_tags(logs_folder: str) -> List:
    log_dict = read_folder(logs_folder)
    all_tags = get_tags_from_dict(log_dict)
    print("You can use these tags: ", end="")
    print(all_tags)
    return all_tags


def mkdir_p(folder_path: str) -> None:
    if not osp.exists(folder_path):
        os.makedirs(folder_path)


if __name__ == "__main__":
    get_tags("vdl_logs")
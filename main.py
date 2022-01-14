import argparse
from vdldraw import vdl_draw_folder


parser = argparse.ArgumentParser(description="input parameters")
parser.add_argument("--log_folder", type=str, required=True)
parser.add_argument("--save_folder", type=str, default="output")


if __name__ == "__main__":
    args = parser.parse_args()
    vdl_draw_folder(args.log_folder, args.save_folder)
import sys
import os.path as osp


PATH = osp.dirname(osp.realpath(__file__))
sys.path.append(PATH)
# print(PATH)


from folder import get_tags
from draw import vdl_draw_folder
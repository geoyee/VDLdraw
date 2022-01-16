# VDLdraw

Batch plot the log files exported from VisualDL using Matplotlib.

|                           VisualDL                           |                           VDLdraw                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![Evaluate_mIoU](https://user-images.githubusercontent.com/71769312/149524214-4b673b9a-028f-4b62-a2ba-edcae44ebb01.png) | <img src="https://user-images.githubusercontent.com/71769312/149523531-30db9c22-44f8-4d41-8761-2c1554e2014e.png" alt="mIoU"  /> |



## How to install

It can be installed through `pip`:

```shell
pip install vdldraw
```

## How to use

```python
from vdldraw import get_tags, vdl_draw_folder


## 1.View available tags
get_tags(log_folder)
# Output like this:
# ['Evaluate/F1', 'Train/loss', 'Evaluate/mIoU', 'Evaluate/Acc']

## 2.Make up tags to be displayed
tag_list = ['Evaluate/mIoU', 'Evaluate/Acc']

## 3.Save image
vdl_draw_folder(log_folder, tag_list, save_folder="output", mplstyle=None)
# Args:
# 	 log_folder (str): Folder path where logs are saved.
# 	 tag_list (list): List of tags to be displayed.
# 	 save_folder (str, option): Folder path to save pictures. Default: "output".
# 	 mplstyle (str/path): Matplotlib style system. Default: None(Styles defined using VDLdraw).
```

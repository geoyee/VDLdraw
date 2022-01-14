# VDLdraw

Batch plot the log files exported from VisualDL using Matplotlib. At present, only mIoU and Acc of Evaluate in PaddleSeg can be exported.

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
from vdldraw import vdl_draw_folder

vdl_draw_folder(log_folder, save_folder)
# Args:
# 	 log_folder (str): Folder path where logs are saved.
#	 save_folder (str, option): Folder path to save pictures. Default: "output".
```

## TODO

- [ ] More tags: Train/Loss and etc.
- [ ] More params: figuresize, style, mark, etc.


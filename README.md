# VDLdraw

Batch plot the log files exported from VisualDL using Matplotlib. At present, only mIoU and Acc of Evaluate in PaddleSeg can be exported.

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


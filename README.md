# VDLdraw

Batch plot the log files exported from VisualDL using Matplotlib. At present, only mIoU and Acc of Evaluate in PaddleSeg can be exported.

## Install

```shell
pip install vdldraw
```

## Use

```python
from vdldraw import vdl_draw_folder

vdl_draw_folder(logs_folder)
```

## \*Test

```shell
# git clone https://github.com/geoyee/VDLdraw
# cd VDLdraw
# pip install -r requirements.txt
# python main.py --log_folder vdl_logs
```


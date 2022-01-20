# VDLdraw

Batch plot the log files exported from VisualDL using Matplotlib.

|                           VisualDL                           |                           VDLdraw                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![vdlmiou](https://user-images.githubusercontent.com/71769312/150273335-ef849dd6-a47f-4972-90b5-d917c24419dd.png) | ![Evaluate@mIoU](https://user-images.githubusercontent.com/71769312/150273323-4fbfb5c7-1353-4c05-b386-dc61db741eda.png) |

## How to install

It can be installed through `pip`:

```shell
pip install vdldraw
```

## How to use

Online experiences in [AI Studio](https://aistudio.baidu.com/aistudio/projectdetail/3414078) (Chinese).

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

## Colormap

Colormap reference [antv's contrasting orange](https://antv.vision/zh/docs/specification/language/palette#%E5%BC%BA%E5%AF%B9%E6%AF%94%E4%B8%BB%E9%A2%98), 20 colors in total.

![colors](https://user-images.githubusercontent.com/71769312/150271480-bea94bf9-140d-4f0d-839f-4b8022397e62.png)

## Style

If you need use some styles, you could use [SciencePlots](https://github.com/garrettj403/SciencePlots). This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses.

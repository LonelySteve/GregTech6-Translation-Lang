# GregTech6-Translation-Lang

格雷科技6 中文翻译 

因为 [GT changed its lang entry](https://github.com/TeamNED/GregTech6-Translation-Groupware/issues/9) 这个问题，[当前版本的语言文件](https://github.com/TeamNED/GregTech6-Translation-Groupware/releases/tag/6.15.10-alpha.2)实际上不能在最新版本的GT6（6.16.00^）中使用。

本项目临时修复了这个问题，直接使用 [gregtech.lang](./gregtech.lang) 文件即可。

## How to use

替换 `.minecraft` 文件夹下的 gregtech.lang 文件即可。

## Rebuild

1. 【可选】在 [GregTech6-Translation-Groupware Release 页面](https://github.com/TeamNED/GregTech6-Translation-Groupware/releases) 下载最新的 lang 文件，并替换本项目文件夹下的 [GregTech-TeamNED.lang](./GregTech-TeamNED.lang)
2. 安装 python 环境（3.8+）后在当前目录执行 `python ./converter.py`

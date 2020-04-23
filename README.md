# 前言简介
Termux 一键安装 Linux 脚本 

灵感来源于 AnLinux 和 AndroNix。

这两个软件提供的脚本下载资源都在国外，而且安装的系统里面更新源也是国外的，再没有 vim 编辑器的情况下，只能手动 echo 写入源 很是难受，于是一气之下就自己写了这个脚本了。

# 依赖安装

Termux 使用如下命令安装:

```bash
pkg install proot git python -y
```

# 基本使用

```bash
git clone https://github.com/sqlsec/termux-install-linux
cd termux-install-linux
python termux-linux-install.py
```


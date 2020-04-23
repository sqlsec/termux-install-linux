# 前言简介
Termux 一键安装 Linux 脚本 

灵感来源于 AnLinux 和 AndroNix。

这两个软件提供的脚本下载资源都在国外，而且安装的系统里面更新源也是国外的，再没有 vim 编辑器的情况下，只能手动 echo 写入源 很是难受，于是一气之下就自己写了这个脚本了，核心镜像文件的下载地址使用的是码云（心疼码云3秒钟）。

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

![](imgs/15876443823741.jpg) 

基本上可以直接上手，0 学习成本，用户输错了也没关系，因为国光我都考虑到了，用户想篡改我的网址我也想到了，除非你有点代码基础，否则不是白嫖党小白你想象的那样直接修改就可以了的！

## Ubuntu

安装成功后，可以直接这样启动：

```bash
cd ~/Termux-Linux/Ubuntu
./start-ubuntu.sh
```

# Kali

这个 Kali 是轻量级的，大家要安装完整的 Kali Nethunter 的话 ，可以参考我的 Termux 文章里面的操作细节: [Termux 高级终端安装使用配置教程: Kali NetHunter](https://www.sqlsec.com/2018/05/termux.html#toc-heading-112)

```bash
cd ~/Termux-Linux/Kali
./start-kali.sh
```

# Debian

```bash
cd ~/Termux-Linux/Debian
./start-debian.sh
```



# 总结

本脚本不会经常更新，除非有重大使用问题，暂时不考虑增加新的操作系统了，也不考虑增加图形化桌面安装功能，随缘佛系更新。
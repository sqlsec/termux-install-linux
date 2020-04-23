import os
import base64
import argparse

def logo():
    print("""  _____                              
 |_   _|__ _ __ _ __ ___  _   ___  __
   | |/ _ \ '__| '_ ` _ \| | | \ \/ /
   | |  __/ |  | | | | | | |_| |>  < 
   |_|\___|_|  |_| |_| |_|\__,_/_/\_\\""")

    copyright_title = 'ICAgIFRlcm11eCDpq5jnuqfnu4jnq6/lronoo4Xkvb/nlKjphY3nva7mlZnnqIs='
    copyright_url = 'aHR0cHM6Ly93d3cuc3Fsc2VjLmNvbS8yMDE4LzA1L3Rlcm11eC5odG1s'
    print('')
    print(base64.b64decode(copyright_title).decode('utf-8'))
    print(base64.b64decode(copyright_url).decode('utf-8'))
    print('')
    print(' 1. 安装 Ubuntu       2. 卸载 Ubuntu')
    print(' 3. 安装 Kali         4. 卸载 Kali')
    print(' 5. 安装 Debian       6. 卸载 Debian')
    print(' 7. 安装 CentOS       8. 卸载 CentOS')
    print(' 9. 安装 Fedora      10. 卸载 Fedora')
    print('11. 查询已安装系统   12. 退出脚本')
    print('')
    return copyright_title, copyright_url


def install_ubuntu():
    osname = 'Ubuntu'
    folder = 'ubuntu-fs'
    shname = 'start-ubuntu.sh'
    imagedir = 'termux-ubuntu'
    tarball = 'ubuntu-rootfs-arm64.tar.xz'
    print("\n正在从码云下载 Rootfs 镜像文件，请耐心等待")
    os.system('git clone "https://gitee.com/sqlsec/termux-ubuntu.git"')
    print('\n下载完成 看来国内码云的速度还是可以的 2333')
    print('\n正在解压镜像 请耐心等待')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}')
    os.system(f'proot --link2symlink tar -xf {imagedir}/{tarball} -C $HOME/Termux-Linux/{osname}/{folder} --exclude="dev"||:')
    print('\n解压完成 正在删除已下载的镜像')
    os.system(f'rm -rf {imagedir}')
    print('\n正在优化系统设置')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/binds')
    os.system(f'cp ubuntu/{shname} $HOME/Termux-Linux/{osname}/')
    os.system(f'termux-fix-shebang $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'chmod +x $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'rm $HOME/Termux-Linux/{osname}/{folder}/etc/apt/sources.list')
    os.system(f'cp ubuntu/sources.list $HOME/Termux-Linux/{osname}/{folder}/etc/apt/')
    os.system('screenfetch -A Ubuntu -L')
    print('\n   Ubuntu 安装成功')
    print('\n    祝您使用愉快\n')

def uninstall_ubuntu():
    print('\n正在卸载 Ubuntu 请耐心等待')
    os.system('rm -rf $HOME/Termux-Linux/Ubuntu')
    print('\n卸载完成!')

def install_kali():
    osname = 'Kali'
    folder = 'kali-fs'
    shname = 'start-kali.sh'
    imagedir = 'termux-kali'
    tarball = "kali-rootfs-arm64.tar.xz"
    print("\n正在从码云下载 Rootfs 镜像文件，请耐心等待")
    os.system('git clone "https://gitee.com/sqlsec/termux-kali"')
    print('\n下载完成 看来国内码云的速度还是可以的 2333')
    print('\n正在解压镜像 请耐心等待')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}')
    os.system(f'proot --link2symlink tar -xJf {imagedir}/{tarball} -C $HOME/Termux-Linux/{osname}/{folder} ||:')
    print('\n解压完成 正在删除已下载的镜像')
    os.system(f'rm -rf {imagedir}')
    print('\n正在优化系统设置')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/binds')
    os.system(f'cp kali/{shname} $HOME/Termux-Linux/{osname}/')
    os.system(f'termux-fix-shebang $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'chmod +x $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'rm $HOME/Termux-Linux/{osname}/{folder}/etc/apt/sources.list')
    os.system(f'cp kali/sources.list $HOME/Termux-Linux/{osname}/{folder}/etc/apt/')
    os.system('screenfetch -A "Kali Linux" -L')
    print('\n   Kali 安装成功')
    print('\n    祝您使用愉快\n')

def uninstall_kali():
    print('\n正在卸载 Kali 请耐心等待')
    os.system('rm -rf $HOME/Termux-Linux/Kali')
    print('\n卸载完成!')

def install_debian():
    osname = 'Debian'
    folder = 'debian-fs'
    shname = 'start-debian.sh'
    imagedir = 'termux-debian'
    tarball = "debian-rootfs-arm64.tar.xz"
    print("\n正在从码云下载 Rootfs 镜像文件，请耐心等待")
    os.system('git clone "https://gitee.com/sqlsec/termux-debian"')
    print('\n下载完成 看来国内码云的速度还是可以的 2333')
    print('\n正在解压镜像 请耐心等待')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}')
    os.system(f'proot --link2symlink tar -xJf {imagedir}/{tarball} -C $HOME/Termux-Linux/{osname}/{folder} ||:')
    print('\n解压完成 正在删除已下载的镜像')
    os.system(f'rm -rf {imagedir}')
    print('\n正在优化系统设置')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/binds')
    os.system(f'cp debian/{shname} $HOME/Termux-Linux/{osname}/')
    os.system(f'termux-fix-shebang $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'chmod +x $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'rm $HOME/Termux-Linux/{osname}/{folder}/etc/apt/sources.list')
    os.system(f'cp debian/sources.list $HOME/Termux-Linux/{osname}/{folder}/etc/apt/')
    os.system('screenfetch -A "Debian" -L')
    print('\n   Debian 安装成功')
    print('\n     祝您使用愉快\n')

def uninstall_debian():
    print('\n正在卸载 Debian 请耐心等待')
    os.system('rm -rf $HOME/Termux-Linux/Debian')
    print('\n卸载完成!')

def install_centos():
    osname = 'CentOS'
    folder = 'centos-fs'
    shname = 'start-centos.sh'
    imagedir = 'termux-centos'
    tarball = "centos-rootfs-arm64.tar.xz"
    print("\n正在从码云下载 Rootfs 镜像文件，请耐心等待")
    os.system('git clone "https://gitee.com/sqlsec/termux-centos"')
    print('\n下载完成 看来国内码云的速度还是可以的 2333')
    print('\n正在解压镜像 请耐心等待')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}')
    os.system(f'proot --link2symlink tar -xJf {imagedir}/{tarball} -C $HOME/Termux-Linux/{osname}/{folder} --exclude="dev"||:')
    print('\n解压完成 正在删除已下载的镜像')
    os.system(f'rm -rf {imagedir}')
    print('\n正在优化系统设置')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/binds')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}/tmp')
    os.system(f'echo "127.0.0.1 localhost" > $HOME/Termux-Linux/{osname}/{folder}/etc/hosts')
    os.system(f'echo "nameserver 8.8.8.8" > $HOME/Termux-Linux/{osname}/{folder}/etc/resolv.conf')
    os.system(f'echo "nameserver 8.8.4.4" >> $HOME/Termux-Linux/{osname}/{folder}/etc/resolv.conf')
    os.system(f'cp centos/{shname} $HOME/Termux-Linux/{osname}/')
    os.system(f'termux-fix-shebang $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'chmod +x $HOME/Termux-Linux/{osname}/{shname}')
    os.system('screenfetch -A "CentOS" -L')
    print('\n   CentOS 安装成功')
    print('\n    祝您使用愉快\n')

def uninstall_centos():
    print('\n正在卸载 CentOS 请耐心等待')
    os.system('chmod 777 -R $HOME/Termux-Linux/CentOS')
    os.system('rm -rf $HOME/Termux-Linux/CentOS')
    print('\n卸载完成!')

def install_fedora():
    osname = 'Fedora'
    folder = 'fedora-fs'
    shname = 'start-fedora.sh'
    imagedir = 'termux-fedora'
    tarball = "fedora-rootfs-arm64.tar.xz"
    print("\n正在从码云下载 Rootfs 镜像文件，请耐心等待")
    os.system('git clone "https://gitee.com/sqlsec/termux-fedora"')
    print('\n下载完成 看来国内码云的速度还是可以的 2333')
    print('\n正在解压镜像 请耐心等待')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/{folder}')
    os.system(f'proot --link2symlink tar -xJf {imagedir}/{tarball} -C $HOME/Termux-Linux/{osname}/{folder} --exclude "dev" ||:')
    print('\n解压完成 正在删除已下载的镜像')
    os.system(f'rm -rf {imagedir}')
    print('\n正在优化系统设置')
    os.system(f'echo "127.0.0.1 localhost" > $HOME/Termux-Linux/{osname}/{folder}/etc/hosts')
    os.system(f'echo "nameserver 8.8.4.4" > $HOME/Termux-Linux/{osname}/{folder}/etc/resolv.conf')
    os.system(f'echo "nameserver 8.8.4.4" >> $HOME/Termux-Linux/{osname}/{folder}/etc/resolv.conf')
    os.system(f'mkdir -p $HOME/Termux-Linux/{osname}/binds')
    os.system(f'cp fedora/{shname} $HOME/Termux-Linux/{osname}/')
    os.system(f'termux-fix-shebang $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'chmod +x $HOME/Termux-Linux/{osname}/{shname}')
    os.system(f'rm $HOME/Termux-Linux/{osname}/{folder}/etc/yum.repos.d/*')
    os.system(f'cp fedora/*.repo $HOME/Termux-Linux/{osname}/{folder}/etc/yum.repos.d/')
    os.system('screenfetch -A "Fedora" -L')
    print('\n   Fedora 安装成功')
    print('\n    祝您使用愉快\n')


def uninstall_fedora():
    print('\n正在卸载 Fedora 请耐心等待')
    os.system('chmod 777 -R $HOME/Termux-Linux/Fedora')
    os.system('rm -rf $HOME/Termux-Linux/Fedora')
    print('\n卸载完成!')

if __name__ == "__main__":
    # 如果没有安装 screenfetch 就安装
    result = os.popen('pkg list-installed|grep screenfetch')
    if 'screenfetch' not in result.read():
        print('正在安装相关依赖包: screenfetch')
        os.system('pkg install screenfetch -y')

    copyright = logo()
    if copyright[0][10:13] != '11e' or copyright[1][10:13] != '93d':
        print('校验失败 退出脚本')
        os._exit(0)

    file_exits = False
    result = os.popen('ls $HOME')
    for line in result.read().splitlines():
        if line == 'Termux-Linux':
            file_exits = True
    
    linux_dir = []
    if file_exits:
        result = os.popen('ls $HOME/Termux-Linux/')
        for line in result.read().splitlines():
            linux_dir.append(line)
    else:
        os.system('mkdir $HOME/Termux-Linux')

    option = input('\n请选择要执行的操作: ')
    if int(option) == 1:
        if 'Ubuntu' in linux_dir:
            print('检测到已安装 Ubuntu 如要安装请卸载后再安装')
        else:
            install_ubuntu()
    elif int(option) == 2:
        if 'Ubuntu' in linux_dir:
            uninstall_ubuntu()
        else:
            print('黑人问号 您还没有安装过 Ubuntu 哦')
    elif int(option) == 3:
        if 'Kali' in linux_dir:
            print('检测到已安装 Kali 如要安装请卸载后再安装')
        else:
            install_kali()
    elif int(option) == 4:
        if 'Kali' in linux_dir:
            uninstall_kali()
        else:
            print('黑人问号 您还没有安装过 Kali 哦')
    elif int(option) == 5:
        if 'Debian' in linux_dir:
            print('检测到已安装 Debian 如要安装请卸载后再安装')
        else:
            install_debian()
    elif int(option) == 6:
        if 'Debian' in linux_dir:
            uninstall_debian()
        else:
            print('黑人问号 您还没有安装过 Debian 哦')
    elif int(option) == 7:
        if 'CentOS' in linux_dir:
            print('检测到已安装 CentOS 如要安装请卸载后再安装')
        else:
            install_centos()
    elif int(option) == 8:
        if 'CentOS' in linux_dir:
            uninstall_centos()
        else:
            print('黑人问号 您还没有安装过 CentOS 哦')
    elif int(option) == 9:
        if 'Fedora' in linux_dir:
            print('检测到已安装 Fedora 如要安装请卸载后再安装')
        else:
            install_fedora()
    elif int(option) == 10:
        if 'Fedora' in linux_dir:
            uninstall_fedora()
        else:
            print('黑人问号 您还没有安装过 Fedora 哦')
    elif int(option) == 11:
        if linux_dir:
            print('\n已安装系统如下: ')
            print(linux_dir)
        else:
            print('暂没有安装系统哦 赶紧来体验一下吧')
    elif int(option) == 12:
        os._exit(0)
    else:
        print('黑人问号 不合法的输入选项')

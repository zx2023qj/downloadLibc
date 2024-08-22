# downloadLibc

因为在写pwn题的时候不知道去哪里下载libc库，后面发现了https://libc.rip/，但是懒得一个个点击下载，所以写了一个小脚本

使用方法：运行脚本然后输入已知函数的名字和地址

```
python downloadLibc.py
** symbols:   printf
** address(prefix:0x):   0x20202020
```

脚本就会自动在当前目前下载可能跟已知函数对应的libc库

在脚本中还预留了下载AllSymbols和deb文件的函数，需要的自行引用即可

Here's the translation of  content into English (by Chatgpt):


While working on pwn challenges, I didn't know where to download the libc library, but later I discovered https://libc.rip/. Since I was too lazy to click and download one by one, I wrote a small script.

**Usage**: Run the script and enter the known function name and address:

```
python downloadLibc.py
** symbols:   printf
** address(prefix:0x):   0x20202020
```

The script will automatically download the libc library that might correspond to the known function in the current directory.

The script also includes pre-defined functions to download AllSymbols and deb files, which you can use if needed.

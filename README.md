# 将Excel（xls、xlsx、csv）存进MySQL数据库
# excel save to MySQL 

电脑里存的表格文件比较多而且还有很多重复条目、希望用一种方法将这些文件内的信息存进数据库，这样方便管理和查找



- python 3.7
- 开发工具：PyCharm 2020.3


---
附一个快捷方法复制文件路径
右键复制文件路径：https://windows10.pro/added-to-the-right-click-menu-copy-path-option/

将下面的代码另存为`文件名.reg`然后运行
由于复制的文件路径两端带了双引号，我在程序中设置自动去掉了
```

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Allfilesystemobjects\shell\windows.copyaspath]

"CanonicalName"="{707C7BC6-685A-4A4D-A275-3966A5A3EFAA}"

"CommandStateHandler"="{3B1599F9-E00A-4BBF-AD3E-B3F99FA87779}"

"CommandStateSync"=""

"Description"="@shell32.dll,-30336"

"Icon"="imageres.dll,-5302"

"InvokeCommandOnSelection"=dword:00000001

"MUIVerb"="@shell32.dll,-30329"

"VerbHandler"="{f3d06e7c-1e45-4a26-847e-f9fcdee59be0}"

"VerbName"="copyaspath"
```
#cdnjspm
####cdnjspm 是用于下载  [cdnjs](https://cdnjs.com/) 资源的包管理器.

bower 和 npm 总是下载一些无关紧要的文件.

cdnjspm 能只下载必须的文件.

文件路径可以与 cdnjs 资源无缝切换.

#怎么用

cdnjspm 目前只能支持 python3

### 从源代码安装
```bash
pip install .
```
```bash
python setup.py install
```

## 搜索包名字

```bash
$ cdnjspm search jquery
jquery
jquery-compat
jquery.pjax
jquery-mobile
jqueryui
jquery-cookie
...
```

## 查看包版本
```bash
$ cdnjspm show jquery

3.1.0
3.0.0
2.2.4
2.2.3
2.2.2
2.2.1
...
```

## 安装包
```bash
$ cdnjspm install jquery 2.2.4

Installing jquery version 2.2.4...

Downloading ./jquery/2.2.4/jquery.js ... Done.
Downloading ./jquery/2.2.4/jquery.min.js ... Done.
Downloading ./jquery/2.2.4/jquery.min.map ... Done.

Successfully installed.
```

### 更多帮助
```bash
cdnjspm --help
```


##### 目前只是实现了基础功能后期会慢慢完善
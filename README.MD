#cdnjspm
####cdnjspm is a package manager for  [cdnjs](https://cdnjs.com/).

bower and npm always download many, annoying junk files.

cdnjspm can download only the necessary files.

file path seamless handover with cdnjs.cloudflare.com.
#How to use

### Installing from source
```bash
python setup.py install
```

## search package

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

## search package name

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
## show package versions
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

## install package
```bash
$ cdnjspm install jquery 2.2.4

Installing jquery version 2.2.4...

Downloading ./jquery/2.2.4/jquery.js ... Done.
Downloading ./jquery/2.2.4/jquery.min.js ... Done.
Downloading ./jquery/2.2.4/jquery.min.map ... Done.

Successfully installed.
```
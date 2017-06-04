# 生成markdown标题编号

## 原理

### 标题行识别

程序将以'#'开头的行识别为标题行

## 使用方法

### python命令行

需要使用python命令行传入两个参数，输入文件名与输出文件名

```
python mdChinese.py ./source.md ./result.md
```

这样将读入./source.md文件，给标题加上正确的编号之后，写入到./result.md
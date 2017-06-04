# 生成markdown标题编号

由[矿大翔工作室](https://github.com/cumtflyingstudio)后端组成员渣渣渣进，在其组长大人[八百](https://github.com/eightHundreds)的强势围观之下，开发而成，如有不满，欢迎来校门口堵我和我的组长大人

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

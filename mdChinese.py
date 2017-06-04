#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 使中文的markdown文档自动加上标题编号

# 全局变量，保存各级标题的序号
levelCounter = [0, 0, 0, 0, 0, 0]


# 判断是否为标题
def is_title(title):
    return title.startswith('#')


# 判断是几级标题，返回数字1,2,3,……,6
def get_title_level(title):
    count = len(title)
    number = 0
    for x in range(count):
        # 遇到' '，退出循环
        if title[x] == ' ':
            break
        # 遇到'#'，标题等级+1
        if title[x] == '#':
            number += 1
    # 返回时将字符串行首的空格去掉
    return number, title[x:].lstrip()


def get_title(title):
    '''
    获取标题等级以及标题内容（不含#号的部分）
    :param title: 原标题
    :return: 标题等级,标题内容（不含#号的部分）
    '''
    count = len(title)
    number = 0
    for x in range(count):
        # 遇到标题内容，退出循环
        if title[x] != '#':
            break
        # 遇到'#'，标题等级+1
        if title[x] == '#':
            number += 1

    return title[:x], number, title[x:]


def get_number_str(current_level):
    numberStr = ' '
    for x in range(current_level):
        numberStr = '%s%d%s' % (numberStr, levelCounter[x], '.')
    return numberStr


def new_title(title_prefix, number_str, title_content):
    return '%s%s%s' % (title_prefix, number_str, title_content)


def get_new_title(title_prefix, level, title_content):
    return new_title(title_prefix, get_number_str(level), title_content)


try:

    # 读入文件
    sourceMD = open(sys.argv[1], 'r')
    # sourceMD = open(sys.argv[0]'./source.md', 'r')
    # 写入文件
    resultMD = open(sys.argv[2], 'w')
    # resultMD = open(sys.argv[1]'./README.md', 'w')

    # 记录上一行的标题等级
    lastLevel = 1
    for line in sourceMD.readlines():

        # 判断是否为标题
        if not is_title(line):
            resultMD.write(line)
            continue

        # 获取标题前缀、等级以及内容
        titlePrefix, titleLevel, titleContent = get_title(line)
        # 相应的等级计数器自增
        levelCounter[titleLevel - 1] += 1

        # 当当前等级比上一次的等级小的时候，需要将等级计数器数组中大于当前等级的等级计数器重置
        if titleLevel < lastLevel:
            for x in range(titleLevel, len(levelCounter)):
                levelCounter[x] = 0
        lastLevel = titleLevel

        # 获取新标题
        newTitle = get_new_title(titlePrefix, titleLevel, titleContent)
        # 写入新标题
        resultMD.write(newTitle)

finally:
    if sourceMD:
        sourceMD.close()
    if resultMD:
        resultMD.close()

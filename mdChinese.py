#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 使中文的markdown文档自动加上标题编号

# 全局变量，保存各级标题的序号
levelCounter = [0, 0, 0, 0, 0, 0]


def is_title(title):
    '''
    以行是否以'#'开头，判断是否为标题行
    :param title: 一行文本
    :return: boolean值
    '''
    return title.startswith('#')


def get_title(title):
    '''
    获取标题前缀（由多个'#'组成的那个标题前缀）、等级以及标题内容（不含#号的部分）
    :param title: 原标题行
    :return: 标题前缀（由多个'#'组成的那个标题前缀），标题等级,标题内容（不含#号的部分）
    '''

    # 记录标题等级
    number = 0
    for x in range(len(title)):
        # 遇到标题内容，退出循环
        if title[x] != '#':
            break
        # 遇到'#'，标题等级+1
        if title[x] == '#':
            number += 1

    return title[:x], number, title[x:]


def get_number_str(current_level):
    '''
    获取标题编号字符串，如当前标题为2.2里面3级标题，那么相应的标题编号字符串为'2.2.3.'
    :param current_level: 当前标题的等级
    :return: 标题编号字符串
    '''

    # 编号前空一格
    numberStr = ' '
    for x in range(current_level):
        numberStr = '%s%d%s' % (numberStr, levelCounter[x], '.')
    return numberStr


def new_title(title_prefix, number_str, title_content):
    '''
    生成新标题
    :param title_prefix: 标题前缀，如'###'
    :param number_str: 标题编号字符串，如' 1.2.1.'
    :param title_content: 标题内容，如'我是三级标题'
    :return: 带有标题编号的标题字符串，如'### 1.2.1. 我是三级标题'
    '''
    return '%s%s%s' % (title_prefix, number_str, title_content)


def get_new_title(title_prefix, level, title_content):
    '''
    生成新标题
    :param title_prefix: 标题前缀，如'###'
    :param level: 标题等级，如3
    :param title_content: 标题内容，如'我是三级标题'
    :return: 带有标题编号的标题字符串，如'### 1.2.1. 我是三级标题'
    '''
    return new_title(title_prefix, get_number_str(level), title_content)


try:

    # 从传入参数指定的文件名读入文件
    # 传入参数的读取应该从下标1开始，以命令“python mdChinese.py ./source.md ./result.md”为例，下标0的参数是mdChinese.py
    sourceMD = open(sys.argv[1], 'r')
    # 从传入参数指定的文件名写入文件
    resultMD = open(sys.argv[2], 'w')

    # 记录上一行的标题等级
    lastLevel = 1
    for line in sourceMD.readlines():

        # 判断是否为标题，不是标题行，直接写入
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

        # 生成新标题
        newTitle = get_new_title(titlePrefix, titleLevel, titleContent)
        # 写入新标题
        resultMD.write(newTitle)

finally:
    if sourceMD:
        sourceMD.close()
    if resultMD:
        resultMD.close()

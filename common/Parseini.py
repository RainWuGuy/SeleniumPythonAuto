# coding=utf-8
'''
author: Jenny Ge
configuration of ini
'''

import configparser
import os

iniFileUrl=os.path.dirname(os.getcwd())+ '/config/config.ini'

conf = configparser.ConfigParser()
conf.read(iniFileUrl)  # 读取ini配置文件

def readConfigFile():
    """
    sections:配置文件中[]中的值
    options:每组中的键
    items:键-值的列表形式
    """

    # 获取每组类型中的section值
    sections = conf.sections()  # 获取所有sections
    print("---conf.ini文件中的section内容有：", sections)

    # 获取每行数据的键即指定section的所有option
    print("---group_a的所有键为：", conf.options("group_a"))
    print("---group_b的所有键为：", conf.options("group_b"))

    # 获取指定section的所有键值对
    print("---group_a的所有键-值为：", conf.items("group_a"))

    # 指定section，option读取具体值
    print("---group_a组的a_key1值为：", conf.get("group_a", "a_key1"))
    print("---group_b组的b_key1值为(取整数类型)：", conf.getint("group_b", "b_key1"))


def writeConfigFile():
    """
    根据分组名、键名修改为新键值
    @param sections: section分组名
    @param key: 分组中的key
    @param newvalue: 需要修改后的键值
    """
    conf.set("group_b", "b_key3", "new3")  # 指定section和option则更新value
    conf.set("group_b", "b_key5", "value5")  # 指定section，则增加option和value

    conf.add_section("group_d")  # 添加section组
    conf.set("group_d", "d_key1", "value1")  # 给添加的section组增加option-value
    # 写回配置文件
    conf.write(open(iniFileUrl, "wb"))


readConfigFile()
writeConfigFile()

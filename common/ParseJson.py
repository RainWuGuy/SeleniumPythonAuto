# encoding = utf-8

import json
import os

filepath = os.path.dirname(os.getcwd()) + '/pageobjects/uimapping'  # 获取目标json文件的路径
# filepath = "C:/JennyAutomationWeb/test_case/pageobjects/uimapping"
filenames = os.listdir(filepath)  # 获取文件夹中的文件名列表,aaa.json 或者bbb.json

class parseJson(object):
    def __init__(self,filepath, filenames):
        self.filepath = filepath
        self.filenames = filenames

    # 获取指定文件夹指定json文件名
    def getJsonfilename(self,name):

        L=[]
        for filename in filenames:
            if os.path.splitext(filename)[0]==name:
                filefullname = filepath + '/' + filename
                L.append(filefullname)
                jsonname = L[0]
        return jsonname

    # 获取具体json中key对应的value
    def getfilelocator(self,name,key):
        jsonname = self.getJsonfilename(name)

        with open(jsonname, 'r', encoding="utf-8") as openJson:
            dic = json.load(openJson)
            # keys = list(dic.keys)
            # values = list(dict.values())
            locator = dic.get(key)  #返回string型数据
            return locator


if __name__ == '__main__':

    testInstance = parseJson(filepath,filenames)
    value = testInstance.getfilelocator("aaa","Jianshu_LoginPage")
    print(value)

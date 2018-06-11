# coding=utf-8

'''
Created on 2018-06-04
@author: Jenny
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from common.ParseJson import parseJson
import os
import json

driver = webdriver.Firefox()
base_url = "https://www.jianshu.com/"
filepath = os.path.dirname(os.getcwd()) + '/pageobjects/uimapping'  # 获取目标json文件的路径
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
        # return jsonname

    # 获取具体json中key对应的value
    def getfilelocator(self,name,key):
        jsonname = self.getJsonfilename(name)
        with open(jsonname, 'r', encoding="utf-8") as openJson:
            dic = json.load(openJson)
            # keys = list(dic.keys)
            # values = list(dict.values())
            locator = dic.get(key)  #返回string型数据
            return locator

class basicPage(object):
    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url

    def openbrower(self):
        self.driver = driver
        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(8)

        # verificationErrors = []
        # self.accept_next_alert = True

    def quitbrower(self):
        self.driver = driver
        return driver.quit()

    # 重写元素定位方法 xpath
    def find_element(self,key):
        driver = self.driver
        driver.get(base_url)
        # jsonname = parseJson.getJsonfilename(name)
        locator = parseJson.getfilelocator(self,key)
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
            return driver.find_element_by_xpath(locator)
        except:
            print("Element can not be found in web!")

if __name__ == '__main__':
    testInstance = parseJson(filepath, filenames)
    name = "jianshuPage"
    key = "Jianshu_LoginPage"
    value = testInstance.getfilelocator(name,key)
    print(value)


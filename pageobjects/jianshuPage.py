# coding = utf-8

from selenium.webdriver.common.by import By
from common.BasicPage import *

name = "aaa"
driver = webdriver.Firefox()
base_url = "https://www.jianshu.com/"

class jianshuPage(basicPage):
    def __init__(self,driver,base_url):
        basicPage.__init__(self,driver,base_url)

    def getlocator(self,key):
        self.name = name
        locator = parseJson.getfilelocator(name,key)
        return locator

    def jianshu_loginPage(self):
        Jianshu_LoginPage = self.getlocator("Jianshu_LoginPage.")
        return basicPage.find_element(self,Jianshu_LoginPage)

    # def Jianshu_UserName(self):
    #     return basicPage.find_element(self,"aaa","Jianshu_UserName")

if __name__ == '__main__':
    testInstance = jianshuPage(driver, base_url)
    value = testInstance.jianshu_loginPage()
    print(value)

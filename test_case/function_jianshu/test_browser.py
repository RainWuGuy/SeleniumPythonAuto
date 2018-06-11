# coding = utf-8

import unittest
# from common.BasicPage import *
from pageobjects.jianshuPage import *

class TestBrowserEngine(unittest.TestCase):

    def setUp(self):
        basicPage.openbrower()

    def test_search(self):
        jianshuPage.jianshu_loginPage(self).click()
        # jianshuPage.Jianshu_UserName(self).send_keys("123")

    def tearDown(self):
        basicPage.quitbrower(self)

if __name__ == "__main__":
    unittest.main()



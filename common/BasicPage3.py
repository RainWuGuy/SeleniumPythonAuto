# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserDriver(object):
    def __init__(self, driver, browser='firefox'):  # 其实也可以创建一个局域变量 browser = 'FireFox'  # maybe Firefox, Chrome, IE

        if browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie":
            DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
            driver = webdriver.Ie("../resources/drivers/IEDriverServer.exe")
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'.")

        driver.maximize_window()
        driver.implicitly_wait(10)


    def getElement(self, by, value):
        '''

        :param by:     查找元素的方式
        :param value:  文本值
        :return:       查找到的元素
        '''
        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        elif by == "linktext":
            return self.driver.find_element_by_link_text(value)
        elif by == "partcialtext":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "tag":
            return self.driver.find_element_by_tag_name(value)
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif by == 'css_selector':
            return self.driver.find_element_by_css_selector(value)  #也可以直接命名　element = self.driver.find_element_by_css_selector(value), 最后return element， 已注释了。
        elif by == 'js' or by == "jquery":
            return self.ExcuteJs(value)
        else:
            print("请输入适合的查找元素方式。。。")
        # return element
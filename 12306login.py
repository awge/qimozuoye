import re
import time
import base64
import requests
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Login(object):
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.geturl = "http://littlebigluo.qicp.net:47720/"
        self.totalFlush = 0
        self.startTime = time.time()
        # self.driver = '' #驱动chrome浏览器进行操作
        driver = webdriver.Chrome()
        self.driver = driver #驱动chrome浏览器进行操作

    
    def login_input(self):
        self.driver.get(self.login_url)
        time.sleep(0.2)
        account = self.driver.find_element_by_class_name("login-hd-account")
        account.click()
        userName = self.driver.find_element_by_id("J-userName")
        userName.send_keys("15606879517")  # 12306账号
        password = self.driver.find_element_by_id("J-password")
        password.send_keys("64890110wjy")  # 12306密码
        time.sleep(5)


    def getImage(self):
        img_element =WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, "J-loginImg")))
        try:
            img_element
        except Exception as e:
            print("出错了，请稍后再试")    
        base64_str=img_element.get_attribute("src").split(",")[-1]
        imgdata=base64.b64decode(base64_str)
        with open('mylogin.jpg','wb') as file:
            file.write(imgdata)
        self.img_element=img_element
        time.sleep(2)


    def getResult(self):
        driver = webdriver.Chrome()
        driver.get(self.geturl)
        time.sleep(5)
        files ="C:\\Users\\Administrator\\Desktop\\爬虫期中作业\\mylogin.jpg"
        onput = driver.find_element_by_name("pic_xxfile")
        onput.send_keys(files)
        myclick = driver.find_element_by_xpath("/html/body/form/input[2]").click()
        result = driver.find_element_by_xpath("/html/body/p[1]/font/font")
        result=result.text.split(" ")
        print(result)
        self.result=result
        time.sleep(2)
        driver.quit()
    

    def Click(self):
        js=""
        for i in self.result:
            if i=='1':
                js=js+'<div randcode="42,50" class="lgcode-active" style="top: 66px; left: 29px;"></div>'
            elif i=='2':
                js=js+'<div randcode="109,43" class="lgcode-active" style="top: 59px; left: 96px;"></div>'
            elif i=='3':
                js=js+'<div randcode="186,36" class="lgcode-active" style="top: 52px; left: 178px;"></div>'
            elif i=='4':
                js=js+'<div randcode="256,50" class="lgcode-active" style="top: 62px; left: 241px;"></div>'
            elif i=='5':
                js=js+'<div randcode="31,124" class="lgcode-active" style="top: 140px; left: 18px"></div>'
            elif i=='6':
                js=js+'<div randcode="119,110" class="lgcode-active" style="top: 130px; left: 103px;"></div>'
            elif i=='7':
                js=js+'<div randcode="182,110" class="lgcode-active" style="top: 124px; left: 169px;"></div>'
            else :
                js=js+'<div randcode="258,110" class="lgcode-active" style="top: 128px; left: 245px;"></div>'
        resultjs='document.getElementById("J-passCodeCoin").innerHTML='+"'"+js+"'"
        print(resultjs)
        self.driver.execute_script(resultjs)
        time.sleep(5)
       
            

    def submit(self):
        self.driver.find_element_by_id("J-login").click()
        




if __name__ == '__main__':
    spider = Login()
    spider.login_input()
    spider.getImage()
    spider.getResult()
    spider.Click()
    spider.submit()

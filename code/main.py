# -*- coding: utf-8 -*-
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
import time

def init_chrome():
    '''初始化一个浏览器对象'''
    chromedriver = r"C:\Users\Machenike\AppData\Local\Google\Chrome\Application\chromedriver238.exe"  
    os.environ["webdriver.chrome.driver"] = chromedriver  
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(chrome_options = options ,executable_path = chromedriver)   
    return browser


def signin(email,password):
    chrome = init_chrome()
    GETurl = "http://adwords.google.com/"
    chrome.get(GETurl)
    signin = chrome.find_element_by_class_name('cta-signin')
    signin.send_keys(Keys.ENTER)
    canbelocate = True
    while canbelocate:
        try:
            EmailText = chrome.find_element_by_id('identifierId')
            canbelocate = False
        except NoSuchElementException:
            pass
    EmailText.send_keys(email)
    EmailText.send_keys(Keys.ENTER)
    canbelocate = True
    while canbelocate:
        try:
            PasswordText = chrome.find_element_by_name('password')
            PasswordText.send_keys(password)
            canbelocate = False
        except ElementNotVisibleException:
            pass
        except NoSuchElementException:
            pass
    
    
    EnterKey = chrome.find_element_by_id("passwordNext")
    EnterKey.send_keys(Keys.ENTER)
    print("sussess sign in ")
    return chrome



if __name__ == '__main__':
    
    Email = '.......@163.com'
    password = '...........'
    #chrome = signin(Email,password)
    chrome = init_chrome()
    GETurl = "http://adwords.google.com/"
    chrome.get(GETurl)
    signinbutton = chrome.find_element_by_class_name('cta-signin')
    signinbutton.send_keys(Keys.ENTER)
    canbelocate = True
    while canbelocate:
        try:
            EmailText = chrome.find_element_by_id('identifierId')
            canbelocate = False
        except NoSuchElementException:
            pass
    EmailText.send_keys(Email)
    EmailText.send_keys(Keys.ENTER)
    canbelocate = True
    while canbelocate:
        try:
            PasswordText = chrome.find_element_by_name('password')
            PasswordText.send_keys(password)
            canbelocate = False
        except ElementNotVisibleException:
            pass
        except NoSuchElementException:
            pass
    
    canbelocate = True
    while canbelocate:
        try:
            EnterKey = chrome.find_element_by_id("passwordNext")
            canbelocate = False
        except:
            pass
    try:
        EnterKey.send_keys(Keys.ENTER)
        print("sussess sign in ")
    except:
        print("strange error")
    
    '''从首页进入 `工具` 选项，进入关键词规划师'''
    print("5start")
    time.sleep(5)
    print("5end")
    canbelocate = True
    while canbelocate:
        try:
            testtag = chrome.find_element_by_id("gwt-uid-832")
            
            canbelocate = False
        except:
            print("can not find tool element")
            time.sleep(2)
    print("had get the tool element")
    
    
    ActionChains(chrome).click(testtag).move_to_element_with_offset(testtag,100,200).perform()
    ActionChains(chrome).click().perform()    
    
    
    '''从输入关键词，到点击加入计划书'''
    
    canbelocate = True
    while canbelocate:
        try:
            sectag = chrome.find_element_by_id("gwt-debug-splash-panel-stats-selection-input")
            canbelocate = False
        except:
            pass
    ActionChains(chrome).click(sectag).perform()
    
    canbelocate = True
    while canbelocate:
        try:
            textareatag = chrome.find_element_by_id("gwt-debug-upload-text-box")
            canbelocate = False
        except:
            pass
    textareatag.send_keys("Fintech")
    
    canbelocate = True
    while canbelocate:
        try:
            buttontag = chrome.find_element_by_id("gwt-debug-upload-ideas-button")
            canbelocate = False
        except:
            pass
    buttontag.send_keys(Keys.ENTER)
    time.sleep(2)
    canbelocate = True
    while canbelocate:
        try:
            addcontent = chrome.find_element_by_id("sel-kt-0")
            canbelocate = False
        except NoSuchElementException:
            print("NoSuchElementException")
            canbelocate_two = True
            while canbelocate_two:
                try:        
                    reflesh = chrome.find_element_by_id("gwt-debug-action-buttons")
                    canbelocate_two = False
                except:
                    print("fail to get reflesh button")
                    pass
            ActionChains(chrome).click(reflesh).perform() 
            time.sleep(2)
        except:
        	print("this case")
        	pass   
    addcontent.send_keys(Keys.ENTER)
    
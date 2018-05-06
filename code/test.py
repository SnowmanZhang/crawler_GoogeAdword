# -*- coding: utf-8 -*-
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
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

def func101(chrome,maxtime=10):
    canbelocate = True
    while canbelocate:
        
        keywordtag = chrome.find_element_by_xpath("//*[@id=\"gwt-debug-column-SAMPLE_KEYWORDS-row-0-2\"]/div/div")
        SEREflag = True
        while SEREflag:
            try:
                keywordtag = chrome.find_element_by_xpath("//*[@id=\"gwt-debug-column-SAMPLE_KEYWORDS-row-0-2\"]/div/div")
                ActionChains(chrome).click(keywordtag).perform()
                SEREflag = False
            except StaleElementReferenceException:
                print("SEREflag")
                time.sleep(1)
        starttime = time.time()
        while time.time() - starttime < maxtime:
            try:
                keyword2tag = chrome.find_element_by_xpath("/html/body/div[12]/div/div/div[1]/div[1]/textarea")
                canbelocate = False
                starttime = starttime - maxtime
            except NoSuchElementException:
                starttime = starttime - maxtime
                print("func101error1")

                time.sleep(1)

    maxtime = (maxtime + time.time() - starttime)/2
    return keyword2tag,maxtime


def func103(chrome,keyword,oldcitylist):
    flag1 = True
    number = 0
    while flag1:  
        try:
            for i in range(53):
                if flag1:
                    citynameid = 'gwt-debug-column-LOCATION_NAME-row-%d-0'%i
                    cityname = chrome.find_element_by_id(citynameid).get_attribute('textContent')                    
                    
                    if i == 0:
                        firstcity = cityname
                        firstvalue = chrome.find_elements_by_xpath("//*[@id=\"gwt-debug-column-IMPRESSIONS-row-0-3\"]/div")[1].get_attribute('textContent')
                    if oldcitylist[i] != cityname:
                        #print("oldcitylist is %s cityname is %s"%(oldcitylist[i],cityname))
                        flag1 = False
        except NoSuchElementException:
            print("func103 NoSuchElement "+str(i))
            flag1 = True
        except StaleElementReferenceException:
            print("func103 StaleElement "+str(i))
        print("func103 load new data fail "+str(i))
        number += 1
        if number > 15 and firstcity == '約翰內斯堡, 豪登省, 南非':
            print("this word %s is a nonword .firstvalue: %s"%(keyword[:-1],firstvalue))

            flag1 = False
        
        time.sleep(1)
                

    
    canbelocate = True
    citylist = list(range(53))
    while canbelocate:
        try:
            with open("englishandchinese.csv",'a',encoding="utf8") as f:
                for i in range(53):
                    citynameid = 'gwt-debug-column-LOCATION_NAME-row-%d-0'%i
                    countid = '//*[@id=\"gwt-debug-column-IMPRESSIONS-row-%d-3\"]/div'%i
                    cityname = chrome.find_element_by_id(citynameid).get_attribute('textContent')
                    count = chrome.find_elements_by_xpath(countid)[-1].get_attribute('textContent')
                #print(cityname+'\t'+count)
                    citylist[i] = cityname
                    f.write(keyword[:-1]+'\t'+cityname+'\t'+count+'\n')
                canbelocate = False
            print(keyword[:-1]+" is download")
        except NoSuchElementException:
            pass
            print("NoSuchElementException2 infomation not found ")
        except StaleElementReferenceException:
            print("func103 load new data2 fail"+str(i))
            time.sleep(1)

    return citylist

def func102(chrome,shorttime,maxtime = 20):
    canbelocate = True
    
    while canbelocate:
        biduileixing_tag = chrome.find_element_by_xpath("//*[@id=\"gwt-uid-4470\"]/div[4]/div[1]/span[1]/div[2]/div/div/div/div[2]/div")
        ActionChains(chrome).click(biduileixing_tag).perform()
        time.sleep(shorttime)
        ActionChains(chrome).move_to_element_with_offset(biduileixing_tag,20,80).perform()
        time.sleep(shorttime)
        ActionChains(chrome).move_to_element_with_offset(biduileixing_tag,80,100).perform()
        time.sleep(shorttime)
        ActionChains(chrome).click().perform()   
        time.sleep(shorttime)    
        starttime = time.time()
        while time.time() - starttime < maxtime:
            try:
                changebidui_tag = chrome.find_element_by_xpath("/html/body/div[12]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]")
                canbelocate = False
                starttime = starttime - maxtime
            except NoSuchElementException:
                starttime = starttime - maxtime

                print("func102error1")
                #time.sleep(0.5)
            except:
                refleshagain_tag = chrome.find_element_by_xpath("//*[@id=\"gwt-debug-ad-group-estimate-table\"]/div[1]/a")
                ActionChains(chrome).click(refleshagain_tag).perform()
                print("refleshagain")
                time.sleep(0.5)
                print("func102error2")
        maxtime = (maxtime + time.time() - starttime)/2
        if canbelocate:     
            print("changebiduitag not found ")
        
    return changebidui_tag,maxtime


if __name__ == '__main__': 
    with open("nonuse.csv",'r',encoding="utf8") as f:
        keywordlist = f.readlines()
    
    citylist = list(range(53))
    
    
    
    for keyword in keywordlist:
        
        '''更换关键词,将每一个关键词填入列表中
        code: 101
        '''
        print("101a")
        keyword2tag,maxtime = func101(chrome)
        print("func101end")
        keyword2tag.clear()
        keyword2tag.send_keys('['+keyword[:-1]+']')
        canbelocate = True
        while canbelocate:
            try:
                keyword3tag = chrome.find_element_by_xpath("/html/body/div[12]/div/div/div[1]/div[2]")
                canbelocate = False
            except NoSuchElementException:
                pass
                print("keyword3tag not found \n")
                time.sleep(2)
        
        keyword3tag.send_keys(Keys.ENTER)
        print("101b")
        

        print("103a")
        citylist = func103(chrome,keyword,citylist)
        print("103b")
    


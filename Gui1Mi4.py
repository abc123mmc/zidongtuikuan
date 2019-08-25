# -*- coding: utf-8 -*-
#已审核订单退款
import re
import time
import random #随机
import tong1yong4
import requests

class gui1Mi4(tong1yong4.qi3dong4web):
    def __init__(self):
        self.run_driver()
        self.stop001=False
        print('gui1Mi4')

    def Get_headers(self):#获取请求头         
        headers={'accept':'application/json, text/javascript, */*; q=0.01',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.8' ,
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8' ,
        'referer':'https://guimi.taobao.com/alert.htm?',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'x-requested-with':'XMLHttpRequest'}
        cookies=self.driver.get_cookies()
        cookieslist = []
        for i in cookies:
            name = i['name']
            value = i['value']
            if i['name'] == 'c_csrf':headers['hcsrf']=i['value']
            cookieslist.append(name + '=' + value + '; ')
            headers['Cookie']=''.join(cookieslist)
        return headers

    def guimichuli(self):
        '''规蜜处理'''
        self.driver.get('https://guimi.taobao.com/alert.htm?')
        qingxi=self.driver.find_elements_by_css_selector('div.tip.J_guide_wrap > button')
        if qingxi:qingxi[0].click()#点击清洗
        headers=self.Get_headers()
        s=requests.session()
        num=1
        while 1:
            if self.stop001:return
            print(num)
            url01='https://guimi.taobao.com/ajax/abnormalOrderHttpService/getNoDealData.do?page=%s&pageSize=10&_input_charset=UTF-8'% num
            num+=1
            date01=s.get(url01,headers=headers).json()
            panduan=0
            for i in date01['resultData']['pageData']:
                if i['statusDes']=='已失效':panduan=1  ;break
                dianhua=i['orderPhone']
                shuch=''
                if len(dianhua)!=11:shuch='%s电话不等于11位'% i['orderId']  ;print(shuch)
                elif dianhua[0]!='1':shuch='%s电话首位不是1'% i['orderId']  ;print(shuch)
                elif int(dianhua[1])<3:shuch='%s电话第二位小于3'% i['orderId'] ;print(shuch)
                if shuch:
                    time001=time.localtime()
                    with open('异常号码.txt','a') as ff:
                            ff=ff.write(shuch+'\n'+'*******************************%s-%s-%s %s:%s:%s**********************************\n'% time.localtime()[:6])#文件读取
            if panduan:break

if __name__=="__main__":
    pass
    a=gui1Mi4()
    #b=a.guimichuli()

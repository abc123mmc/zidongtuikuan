# -*- coding: utf-8 -*-
#退运费自动退款
import re
import time
import random #随机
import tong1yong4

class refundFreight(tong1yong4.qi3dong4web):
    def __init__(self):
        self.run_driver()
        self.stop001=False
        print('refundFreight')
    def tuiyunfei(self):
        '''仅退款，退运费处理'''
        self.driver.implicitly_wait(3)#等待网页元素加载20秒，针对此句后的所有网页元素
        self.driver.get(r'https://refund2.tmall.com/dispute/sellerDisputeList.htm')
        time.sleep(random.uniform(1,2))
        self.driver.find_element_by_xpath(r'//*[@id="sellerGridQueryContainer_1@3"]/div[2]/span').click()#退款页面退款原因
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/div/span[text()='退运费']").click()#退款页面退款原因里的退运费
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='仅退款(已发货)']").click()#退款页面仅退款（已发货）
        time.sleep(2)
        #退运费，筛选出退运费仅退款，等待操作
        li=[]
        while True:
            if self.stop001:return
            dingdbh=r'div> div.mod-dispute-body-col.brand>a'
            tuiktd=self.driver.find_elements_by_css_selector(dingdbh)#定位退款入口
            for td in tuiktd:li.append(td.get_attribute('href'))
            try:
                driver.find_element_by_css_selector('li[title="下一页"][class=" rc-pagination-next"][aria-disabled="false"]').click()
                time.sleep(random.uniform(2,3))
            except:break
        if li:
            for tk in li:
                if self.stop001:return
                self.driver.get(tk)
                time.sleep(random.uniform(1,2))
                ym1=self.driver.find_element_by_css_selector('body').text
                li001=[''.join(re.findall(r'\n买家：\n(.*?)\n',ym1)),#网名
                   ''.join(re.findall(r'\n订单编号：\n(.*?)\n',ym1)),#订单编号
                   ''.join(re.findall(r'\n原因：\n(.*?)\n',ym1)),#退款原因                       
                   ''.join(re.findall(r'\n退款金额：\n(.*?)\n',ym1)),#退款金额
                   ''.join(re.findall(r'\n成交时间：\n(.*?)\n',ym1)),#付款时间                       
                   ''.join(re.findall(r'\n修改备注\n(.*?)\n',ym1))#备注内容
                ]
                print(li001)
                if (li001[3][:-3] in li001[5]) and (li001[2]=='退运费') and ('已退款' not in li001[5]):
                    tytk="//div[contains(@class,'button')]/span[contains(text(),'同意退款')]"
                    self.driver.find_element_by_xpath(tytk).click()
                    time.sleep(random.uniform(2,3))
                    b1=self.driver.find_elements_by_xpath(tytk)
                    b1[1].click()
                    time.sleep(random.uniform(2,3))
                    self.driver.refresh()
                    if self.driver.find_elements_by_xpath("//span[contains(text(),'退款成功')]"):
                        filename=tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','excelname')#数据保存文件名
                        sheet_nanm='退运费'#表名
                        title=['旺旺ID','订单编号','退款原因','退款金额','付款时间','备注内容']#表头
                        tong1yong4.biao3ge2xie3ru4.excelwrite(filename,sheet_nanm,li001,title)
                        self.driver.find_element_by_xpath("//span[text()='修改备注']").click()#点击修改备注
                        time.sleep(random.uniform(2,3))
                        beizhu='***已退款[tuiyunfei]----伟'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))                        
                        self.driver.find_element_by_css_selector('textarea[placeholder="主订单备忘"]').send_keys(beizhu)#输入备注
                        time.sleep(1)
                        self.driver.find_element_by_css_selector('label[data-reactid$="@1.1.0:$4"]').click()#点击选择紫旗
                        time.sleep(1)
                        self.driver.find_element_by_xpath("//span[text()='确定']").click()#点击确认备注
                        time.sleep(random.uniform(1,2))

if __name__=="__main__":
    pass
    a=refundFreight()
    #b=a.tuiyunfei()

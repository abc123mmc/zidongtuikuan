# -*- coding: utf-8 -*-
#已审核订单退款
import re
import time
import random #随机
import tong1yong4

class examineRefund(tong1yong4.qi3dong4web):
    def __init__(self):
        self.run_driver()
        self.stop001=False
        print('examineRefund')

    def shenghedd(self):
        '''已审核订单退款处理'''        
        self.driver.implicitly_wait(3)#等待网页元素加载3秒，针对此句后的所有网页元素
        self.driver.get(r'https://refund2.tmall.com/dispute/sellerDisputeList.htm')
        time.sleep(1)
        yuanycdb1=self.driver.find_elements_by_xpath('//span[contains(text(),"已审核(")]')#退款页面已审核订单筛选
        yuanycdb1[0].click()
        time.sleep(random.uniform(0.5,1))
        yuanycdb1[1].click()
        time.sleep(random.uniform(2,3))
        #筛选出已审核订单退款，等待操作
        li=[]
        dingdbh=r'div> div.mod-dispute-body-col.brand>a'
        tuiktd=self.driver.find_elements_by_css_selector(dingdbh)#定位退款入口
        if tuiktd:
            for td in tuiktd:li.append(td.get_attribute('href'))
        if li:
            for tk in li:
                if self.stop001:return
                self.driver.get(tk)
                time.sleep(1)
                ym1=self.driver.find_element_by_css_selector('body').text
                li001=[''.join(re.findall(r'\n买家：\n(.*?)\n',ym1)),#网名
                   ''.join(re.findall(r'\n订单编号：\n(.*?)\n',ym1)),#订单编号
                   ''.join(re.findall(r'\n原因：\n(.*?)\n',ym1)),#退款原因                       
                   ''.join(re.findall(r'\n退款金额：\n(.*?)\n',ym1)),#退款金额
                   ''.join(re.findall(r'\n成交时间：\n(.*?)\n',ym1)),#付款时间                       
                   ''.join(re.findall(r'\n修改备注\n(.*?)\n',ym1))#备注内容
                ]
                print(li001)
                if re.findall(r'\n该笔订单已(.*?),审核员',ym1):
                    if re.findall(r'\n该笔订单已(.*?),审核员',ym1)[0]=='通过同意退款审核':
                        tytk="//div[contains(@class,'button')]/span[contains(text(),'同意退款')]"
                        self.driver.find_element_by_xpath(tytk).click()
                        time.sleep(random.uniform(2,3))
                        b1=self.driver.find_elements_by_xpath(tytk)
                        b1[1].click()
                        time.sleep(random.uniform(2,3))
                        self.driver.refresh()
                        if self.driver.find_elements_by_xpath("//span[contains(text(),'退款成功')]"):
                            filename=tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','excelname')#数据保存文件名
                            sheet_nanm='审核退款'#表名
                            title=['旺旺ID','订单编号','退款原因','退款金额','付款时间','备注内容','是否多笔']#表头
                            if '***已退款[' in li001[5]:
                                li001=li001+['此订单存在多个退款']
                                tong1yong4.biao3ge2xie3ru4.excelwrite(filename,sheet_nanm,li001,title)
                                continue
                            tong1yong4.biao3ge2xie3ru4.excelwrite(filename,sheet_nanm,li001,title) 
                            self.driver.find_element_by_xpath("//span[text()='修改备注']").click()#点击修改备注
                            time.sleep(random.uniform(2,3))
                            beizhu='***已退款[shenghedd]----伟'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                            self.driver.find_element_by_css_selector('textarea[placeholder="主订单备忘"]').send_keys(beizhu)#输入备注
                            time.sleep(1)
                            self.driver.find_element_by_css_selector('label[data-reactid$="@1.1.0:$4"]').click()#点击选择紫旗
                            time.sleep(1)
                            self.driver.find_element_by_xpath("//span[text()='确定']").click()#点击确认备注
                            time.sleep(random.uniform(1,2))

if __name__=="__main__":
    pass
    a=examineRefund()
    #b=a.shenghedd()

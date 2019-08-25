# -*- coding: utf-8 -*-
#退货提前自动退款
import re
import time
import random #随机
import tong1yong4

class earlyReturn(tong1yong4.qi3dong4web):
    def __init__(self):
        self.run_driver()
        self.stop001=False
        print('earlyReturn')
    def get_xujianchshuju(self):
        '''获取需检查数据，并返回可以提前退款的（退款）连接'''
        self.driver.get('https://refund2.tmall.com/dispute/sellerDisputeList.htm?spm=687.8433302.1309.1.PzKxnO&scm=1028.1.2.1309')
        self.driver.find_element_by_xpath("//div/span[contains(text(),'待商家收货：')]").click()
        time.sleep(2)
        ketuikuan=['已签收','物流走件中','派送中']
        ketuikuandingdan=[]
        while True:
            if self.stop001:return
            dingDan=self.driver.find_elements_by_css_selector('div[id*="sellerGridContainer"]')#退款订单
            for i in range(len(dingDan)):
                tuihuowuliu=dingDan[i].find_element_by_css_selector('div:nth-child(6)>p>span').text#退款物流
                tuihuojinge=dingDan[i].find_element_by_css_selector('div:nth-child(3)>p>span').text#退款金额
                tuihuojinge=re.findall('￥(.*).',tuihuojinge)[0]
                if [i for i in ketuikuan if tuihuowuliu in i] and float(tuihuojinge)<500:#退货物流状态为23行的三类且金额小于500判定为可以退款
                    tuiktd=dingDan[i].find_element_by_css_selector('div.mod-dispute-body-col.brand>a')#定位退款入口
                    ketuikuandingdan.append(tuiktd.get_attribute('href'))
            try:
                self.driver.find_element_by_css_selector('li[title="下一页"][aria-disabled="false"]').click()
                time.sleep(3)
            except:
                print('可提前退款的数据有：%s条'% ketuikuandingdan)
                return ketuikuandingdan

    def tuikuan001(self,ketuikuandingdan):
        '''执行退款，并把退款数据写入到表格'''
        for i in ketuikuandingdan:
            if self.stop001:return
            try:
                self.driver.get(i)
                time.sleep(random.uniform(2,3))
                ym1=self.driver.find_element_by_css_selector('body').text
                tytk="//div[contains(@class,'button')]/span[contains(text(),'同意退款')]"
                self.driver.find_element_by_xpath(tytk).click()
                time.sleep(random.uniform(2,3))
                b1=self.driver.find_elements_by_xpath(tytk)
                b1[1].click()
                time.sleep(random.uniform(2,3))
                self.driver.refresh()
                if self.driver.find_elements_by_xpath("//span[contains(text(),'退款成功')]") and '***已退款[tiqianchuli]' not in re.findall(r'\n修改备注\n(.*?)\n',ym1)[0]:#备注内容
                    self.driver.find_element_by_xpath("//span[text()='修改备注']").click()#点击修改备注
                    time.sleep(random.uniform(2,3))
                    tuikuanshijian=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                    beizhu='***已退款[tiqianchuli]----伟'+tuikuanshijian
                    self.driver.find_element_by_css_selector('textarea[placeholder="主订单备忘"]').send_keys(beizhu)#输入备注
                    time.sleep(1)
                    self.driver.find_element_by_css_selector('label[data-reactid$="@1.1.0:$4"]').click()#点击选择紫旗
                    time.sleep(1)
                    self.driver.find_element_by_xpath("//span[text()='确定']").click()#点击确认备注
                    time.sleep(random.uniform(1,2))
                    li001=[re.findall(r'\n订单编号：\n(.*?)\n',ym1)[0], #订单编号
                           tuikuanshijian,#退款时间
                           re.findall('买家已退货：(.*)（(.*)\)查看物流详情',ym1)[0][0],#物流单号
                           re.findall('买家已退货：(.*)（(.*)\)查看物流详情',ym1)[0][1],#物流公司
                           ]
                           #['订单编号','退货物流','退货单号','退款时间']
                    print('%s\n*******************退款成功'% li001)
                    filename=tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','excelname')#数据保存文件名
                    sheet_nanm='退货提前退款'#表名
                    title=['订单编号','退款时间','退货物流','退货单号']#表头
                    tong1yong4.biao3ge2xie3ru4.excelwrite(filename,sheet_nanm,li001,title)
            except:pass

if __name__=="__main__":
    pass
    a=earlyReturn()
    #b=a.get_xujianchshuju

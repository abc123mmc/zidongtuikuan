# _*_ coding:utf-8 _*_
#通用
import xlrd
import xlwt
from xlutils.copy import copy
import traceback#用于错误处理
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ctypes#弹出框
import configparser#配置文件
import re

class pei4zhi4:
    #pei4zhi4('peizhi1.ini').change('DEFAULT',{'钱志伟':'123'})
    def __init__(self,file_path_name):
        self.file_path_name=file_path_name
        content = open(file_path_name,'rb').read()
        content=content.decode(encoding='UTF-8')
        content=re.sub('\ufeff','',content)
        open(file_path_name,'wb').write(bytes(content, encoding='utf-8'))
        self.config=configparser.ConfigParser()
        self.config.read(self.file_path_name,encoding='UTF-8')#读文件
    def read(self,Section,Key):
        '''传入项(Section)和键(Key),查询值(value)'''
        return self.config[Section][Key]
    def change(self,Section,dict1):
        '''传入项(Section)和字典(dict1)，进行增和修改'''
        for i in dict1:
            try:self.config.add_section(Section)
            except:pass
            finally:self.config[Section][i]=dict1[i]
        with open(self.file_path_name,'w',encoding='UTF-8') as f:self.config.write(f)
    def del1(self,Section,Key):
        '''传入项(Section)和键(Key)，进行删除'''
        self.config.remove_option(Section,Key) #删除一个配置项
        with open(self.file_path_name,'w',encoding='UTF-8') as f:self.config.write(f)

class qi3dong4web:
    def run_driver(self):
        #option = webdriver.ChromeOptions()
        #option.add_argument('disable-infobars')
        #option.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")#设置成用户自己的数据目录
        #self.driver= webdriver.Chrome(chrome_options=option)
        self.driver= webdriver.Chrome()
        self.driver.get('https://login.taobao.com/member/login.jhtml')
        self.driver.maximize_window()
        ctypes.windll.user32.MessageBoxW(0, '初始化成功，请登陆账号进行后续操作','提示',0)
    def yan4zheng4beng3dian4():
        '''验证是否为本店'''
        li111=['七匹狼箱包旗舰店','septwolves美之瑞专卖店','七匹狼雅赋专卖店','SEPTWOLVES雅赋专卖店',
        '少年狼箱包','拼多多美之瑞专卖店','京东七匹狼雅赋专卖店','自然之名旗舰店','evm旗舰店',
        '自然之名雅赋专卖店','nacola旗舰店','汉苑良方海川专卖店','麂翔旗舰店','lucky旗舰店',
        'cosmecontact隐形眼镜旗舰','安娜苏隐形眼镜旗舰店','欧朗睛隐形眼镜旗舰店','洁云家居旗舰店',
        'mia米娅东冠专卖店','mia米娅旗舰店','vancl凡客诚品旗舰店']
        b=self.driver.find_element_by_css_selector('body').text
        b=[i for i in li111 if i in b]
        if not b:
            ctypes.windll.user32.MessageBoxW(0,'未授权或者帐号未登陆[非本公司店铺]，如有疑问联系老钱QQ：1043014552', u'提醒消息',0)
            return False
        else:return True

class ri4zhi4:#日志
    def cuo4wu4(self):
        '''记录错误日志到当前文件夹下的abnormal.txt上'''
        with open(r"abnormal.txt",'a') as f:
            traceback.print_exc(file=f)
            f.write('*******************************'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))+'************************************\n\n')
    def xie3ru4(self,wjm,nr):
        ''''''
        riqi=time.strftime("%Y%m%d", time.localtime(time.time()))
        with open(wjm+riqi+".txt",'a') as f:
            f.write(nr+'\n')
            
class biao3ge2xie3ru4():
    def excelwrite(self,filename,sheet_name,DataList,Header=None):
        '''
        #在excel的最后一行写入列表DataList，如果excel文件（或者表名）不存在的话会自动创建
        传入filename(Excel文件名)、sheet_name（表名）、DataList（数据，类型为列表）、Header（表头，即第一行）
        '''
        filename+='.xls'
        if DataList is None:DataList = []
        try:workbook = xlrd.open_workbook(filename, formatting_info=True)
        except:
            workbook=xlwt.Workbook()
            table=workbook.add_sheet(sheet_name)
            for i in range(len(Header)):table.write(0,i,Header[i])
            workbook.save(filename)
            workbook = xlrd.open_workbook(filename, formatting_info=True)
        sheet = workbook.sheet_by_name(sheet_name)
        rowNum = sheet.nrows
        colNum = sheet.ncols
        newbook = copy(workbook)
        newsheet = newbook.get_sheet(sheet_name)
        for i in range(len(DataList)):newsheet.write(rowNum,i,DataList[i])# 在末尾增加新行
        newbook.save(filename)# 覆盖保存

class biao3ge2ri4zhi4(biao3ge2xie3ru4,ri4zhi4):
    pass

if __name__=="__main__":
    #a=biao3ge2ri4zhi4()
    filename='退款数据'#导出数据名
    qi3dong4=qi3dong4web()
    qi3dong4.run_driver()
    #a.excelwrite(filename,'sheet_nanm',['a','b','c','d'],[1,2,3,4])


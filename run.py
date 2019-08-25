import win32api,win32con  #弹出框
import sys
import threading #线程

import AppMain#界面
import BuyWrong#错拍多拍
import EarlyReturn#提前退款
import ExamineRefund#已审核订单退款
import Gui1Mi4#规蜜处理
import RefundFreight#退运费
import tong1yong4#其他


class Ui_Form(BuyWrong.buyWrong,EarlyReturn.earlyReturn,Gui1Mi4.gui1Mi4,RefundFreight.refundFreight,AppMain.Ui_Form):
    def __init__(self):
        super(RefundFreight.refundFreight,self).__init__()
        super(Ui_Form,self).__init__()
        self.run0001=True
    def run123(self):
        if self.run0001:self.run0001=False
        else:
            win32api.MessageBox(0,u'应用已运行,请勿重复点开始按钮', u'提醒消息',win32con.MB_OK)
            return
            
        while 1:
            if self.stop001:
                self.stop001=False
                self.run0001=True
                win32api.MessageBox(0,u'应用已经停止运行', u'提醒消息',win32con.MB_OK)
                return
                        
            try:
                if self.checkBox.isChecked():self.cuodb()#错多不
            except:tong1yong4.ri4zhi4().cuo4wu4()
                        
            try:#提前退款
                if self.checkBox_5.isChecked():
                    ketuikuandingdan=self.get_xujianchshuju()
                    self.tuikuan001(ketuikuandingdan)
            except:tong1yong4.ri4zhi4().cuo4wu4()

            try:
                if self.checkBox_2.isChecked():self.shenghedd()#审核订单退款
            except:tong1yong4.ri4zhi4().cuo4wu4()

            try:
                if self.checkBox_4.isChecked():self.guimichuli()#规蜜处理
            except:tong1yong4.ri4zhi4().cuo4wu4()

            try:
                if self.checkBox_3.isChecked():self.tuiyunfei()#退运费
            except:tong1yong4.ri4zhi4().cuo4wu4()

    def stop002(self):
        if self.stop001:self.stop001=False
        else:self.stop001=True

    def start002(self):
        super().start002()
        t1 = threading.Thread(target=lambda:self.run123())
        t1.start()


if __name__=="__main__":
    app=AppMain.QtWidgets.QApplication(sys.argv)
    widget=AppMain.QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())



from PySide2 import QtCore, QtGui, QtWidgets
import sys
import tong1yong4


class Ui_Form(object):
    def setupUi(self, Form):
        #界面位置
        Form.setObjectName("Form")
        Form.resize(413, 181)
        label = QtWidgets.QLabel(Form)
        label.setGeometry(QtCore.QRect(140, 20, 201, 16))
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(Form)
        label_2.setGeometry(QtCore.QRect(140, 50, 81, 16))
        label_2.setObjectName("label_2")
        label_3 = QtWidgets.QLabel(Form)
        label_3.setGeometry(QtCore.QRect(140, 80, 81, 16))
        label_3.setObjectName("label_3")
        label_4 = QtWidgets.QLabel(Form)
        label_4.setGeometry(QtCore.QRect(140, 110, 111, 16))
        label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(341, 19, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(222, 49, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(222, 79, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(242, 109, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        pushButton = QtWidgets.QPushButton(Form)
        pushButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(Form)
        pushButton_2.setGeometry(QtCore.QRect(320, 140, 75, 23))
        pushButton_2.setObjectName("pushButton_2")
        checkb={'checkBox':self.checkBox,'checkBox_2':self.checkBox_2,'checkBox_3':self.checkBox_3,'checkBox_4':self.checkBox_4,'checkBox_5':self.checkBox_5}
        for i in checkb:
            checkb[i].setChecked(eval(tong1yong4.pei4zhi4('peizhi.ini').read('appMain',i)))
        #界面文字
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "自动退款规蜜", None, -1))
        label.setText(QtWidgets.QApplication.translate("Form", "错拍多拍付款到退款的时长（分钟）：", None, -1))
        label_2.setText(QtWidgets.QApplication.translate("Form", "导出表格名称：", None, -1))
        label_3.setText(QtWidgets.QApplication.translate("Form", "日志文件名称：", None, -1))
        label_4.setText(QtWidgets.QApplication.translate("Form", "退款使用的旺旺号：", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("Form", tong1yong4.pei4zhi4('peizhi.ini').read('cuoduobu','time'), None, -1))
        self.lineEdit_2.setText(QtWidgets.QApplication.translate("Form", tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','excelName'), None, -1))
        self.lineEdit_3.setText(QtWidgets.QApplication.translate("Form", tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','riZhiName'), None, -1))
        self.lineEdit_4.setText(QtWidgets.QApplication.translate("Form", tong1yong4.pei4zhi4('peizhi.ini').read('DEFAULT','user'), None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Form", "错拍多拍退款", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("Form", "审核订单退款", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("Form", "退运费", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("Form", "规蜜处理", None, -1))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("Form", "退货提前退", None, -1))
        pushButton.setText(QtWidgets.QApplication.translate("Form", "开始", None, -1))
        pushButton_2.setText(QtWidgets.QApplication.translate("Form", "暂停", None, -1))

        QtCore.QObject.connect(pushButton, QtCore.SIGNAL("clicked()"), self.start002)
        QtCore.QObject.connect(pushButton_2, QtCore.SIGNAL("clicked()"), self.stop002)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def start002(self):
        print('start001')
        checkb={'checkBox':self.checkBox,'checkBox_2':self.checkBox_2,'checkBox_3':self.checkBox_3,
                'checkBox_4':self.checkBox_4,'checkBox_5':self.checkBox_5}
        for i in checkb:
            tong1yong4.pei4zhi4('peizhi.ini').change('appMain',{i:str(checkb[i].isChecked())})
        tong1yong4.pei4zhi4('peizhi.ini').change('cuoduobu',{'time':self.lineEdit.text()})
        linee={'user':self.lineEdit_4,'excelName':self.lineEdit_2,'riZhiName':self.lineEdit_3}
        for i in linee:
            tong1yong4.pei4zhi4('peizhi.ini').change('DEFAULT',{i:linee[i].text()})
        
    def stop002(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        print(self.checkBox.isChecked())

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)  
    widget=QtWidgets.QWidget()
    ui=Ui_Form()  
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

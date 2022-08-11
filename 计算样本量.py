from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('计算样本量的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel('灵敏度',self)
        label1.move(50,50)
        self.line1=QLineEdit(self)
        self.line1.move(150,50)
        self.line1.setText('0.9')

        label2=QLabel('特异度',self)
        label2.move(50,100)
        self.line2=QLineEdit(self)
        self.line2.move(150,100)
        self.line2.setText('0.85')

        label3=QLabel('患病率',self)
        label3.move(50,150)
        label3.setToolTip('CE患病率为0~12%,AE患病率为0~14%')
        self.line3=QLineEdit(self)
        self.line3.move(150,150)
        self.line3.setText('0.12')
        
        label4=QLabel('容许误差',self)
        label4.move(50,200)
        label4.setToolTip('误差范围在0.03~0.1之间')
        self.line4=QLineEdit(self)
        self.line4.move(150,200)
        self.line4.setText('0.1')

        btn=QPushButton('计算',self)
        btn.move(50,250)
        btn.clicked.connect(self.on_click)

        label5=QLabel('样本量(按灵敏度计算)',self)
        label5.move(50,300)
        self.label5_1=QLabel('',self)
        self.label5_1.move(250,300)
        label6=QLabel('样本量(按特异度计算)',self)
        label6.move(50,350)
        self.label6_1=QLabel('',self)
        self.label6_1.move(250,350)
    def on_click(self, event):
        self.method_sen()
        self.method_spe()
    def method_sen(self):
        sen=float(self.line1.text())
        err=float(self.line4.text())
        pre=float(self.line3.text())
        n1=((1.96**2)*(sen)*(1-sen))/((err**2)*(pre))
        self.label5_1.setText(str(round(n1,2)))
        self.label5_1.adjustSize()
    def method_spe(self):
        spe=float(self.line2.text())
        err=float(self.line4.text())
        pre=float(self.line3.text())
        n1=((1.96**2)*(spe)*(1-spe))/((err**2)*(1-pre))
        self.label6_1.setText(str(round(n1,2)))
        self.label6_1.adjustSize()    

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())
# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

result = 0.0
operator = ''
isPOp = False
optimes = 0
pnum = None
newnum = None
error = False

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)
        self.Clear()
        nums = [self.btn0,self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9]
        ops = [self.btnDivide,self.btnMultiply,self.btnMinus,self.btnPlus]

        for item in nums:
            item.clicked.connect(self.Digit)
        for it in ops:
            it.clicked.connect(self.operation)

        self.btnEqual.clicked.connect(self.Equal)
        self.btnClear.clicked.connect(self.Clear)
        self.btnDot.clicked.connect(self.Dot)

    def operation(self):
        global isPOp
        global operator
        global optimes
        global pnum
        global newnum
        global error
        if not error:
            de = False
            optimes += 1
            newnum = None
            if optimes > 1 and pnum is not None and newnum is not None:
                self.Equal()
            pnum = float(self.txtDisplay.text())
            operator = self.sender().text()
            isPOp = True

    def Digit(self):
        global newnum
        global isPOp
        global optimes
        global error
        if not error:
            optimes = 0
            newnum = int(self.sender().text())
            setNum = str(newnum)
            if isPOp == False:
                if (pnum is None and newnum is None) or self.txtDisplay.text() == "0":
                    self.txtDisplay.setText(setNum)
                else:
                    self.txtDisplay.setText(self.txtDisplay.text() + setNum)
            else:
                self.txtDisplay.setText(setNum)
                isPOp = False
            if len(self.txtDisplay.text()) > 12:
                self.txtDisplay.setText("Exceed Max of 12 digits")
                error = True
            newnum = float(self.txtDisplay.text().replace(",",""))

    def Equal(self):
        global operator
        global pnum
        global newnum
        global result
        global error
        global isPOp
        isPOp = True
        if pnum is not None and newnum is not None:
            if operator == "/":
                result = pnum / newnum
            elif operator == "x":
                result = pnum * newnum
            elif operator == "-":
                result = pnum - newnum
            elif operator == "+":
                result = pnum + newnum
        self.txtDisplay.setText(str(round(result,int(self.cboDecimal.currentText()))))
        print(operator,pnum,newnum,result,self.chkSeparator.isChecked())
        pnum = None
        newnum = None
        if len(self.txtDisplay.text().replace(".","")) > 12:
            self.txtDisplay.setText("Exceed Max of 12 digits")
            error = True
        num = float(self.txtDisplay.text())
        if self.chkSeparator.isChecked() == True:
            num = '{0:,}'.format(int(num))
            self.txtDisplay.setText(num + "." + self.txtDisplay.text().split(".")[1])

    def Clear(self):
        global result
        global operator
        global isPOp
        global optimes
        global pnum
        global newnum
        global error
        error = False
        result = 0.0
        operator = ''
        isPOp = False
        optimes = 0
        pnum = None
        newnum = None
        self.txtDisplay.setText("0")
        self.cboDecimal.setCurrentIndex(0)
        self.chkSeparator.setChecked(False)

    def Dot(self):
        global error
        if not error:
            if "." in self.txtDisplay.text():
                return
            else:
                self.txtDisplay.setText(self.txtDisplay.text() + ".")


currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()

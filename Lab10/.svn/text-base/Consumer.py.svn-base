import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.boxes = [self.addressLineEdit,self.cityLineEdit,self.firstNameLineEdit,self.lastNameLineEdit,self.stateLineEdit,self.emailLineEdit,self.zipLineEdit]

        self.clearButton.clicked.connect(self.ClearForm)
        self.saveToTargetButton.clicked.connect(self.Save)
        self.loadButton.clicked.connect(self.loadData)
        self.saveToTargetButton.setEnabled(False)
        #self.errorInfoLabel.setText("")
        self.loadButton.setEnabled(True)
        self.states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        for item in self.boxes:
            item.textChanged.connect(self.EnableSave)

    def EnableSave(self):
        for box in self.boxes:
            if box.text() is not "":
                self.saveToTargetButton.setEnabled(True)
            else:
                self.saveToTargetButton.setEnabled(False)

    def Save(self):
        #print(self.zipLineEdit.text())
        #print(self.stateLineEdit.text())
        for box in self.boxes:
            if box.text() == "":
                self.errorInfoLabel.setText("All fields are required.")
                return
        if self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("State is not valid.")
            return
        m = re.match(r'\w+@\w+\.\w+',self.emailLineEdit.text())
        if not m:
            self.errorInfoLabel.setText("Email is not valid.")
            #print(self.errorInfoLabel.text() != "")
            return
        try:
            zip = int(self.zipLineEdit.text())
            if len(self.zipLineEdit.text()) != 5:
                raise ValueError
        except:
            self.errorInfoLabel.setText("zip code is not valid.")
            return


        with open("target.xml","w") as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<user>\n')
            file.write('\t<FirstName>'+self.firstNameLineEdit.text()+'</FirstName>\n')
            file.write('\t<LastName>'+self.lastNameLineEdit.text()+'</LastName>\n')
            file.write('\t<Address>'+self.addressLineEdit.text()+'</Address>\n')
            file.write('\t<City>'+self.cityLineEdit.text()+'</City>\n')
            file.write('\t<State>'+self.stateLineEdit.text()+'</State>\n')
            file.write('\t<ZIP>'+self.zipLineEdit.text()+'</ZIP>\n')
            file.write('\t<Email>'+self.emailLineEdit.text()+'</Email>\n')
            file.write('</user>\n')
        self.errorInfoLabel.setText("")
    def ClearForm(self):
        for box in self.boxes:
            box.setText("")
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)
        self.errorInfoLabel.setText("")
    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath,"r") as file:
            lines = file.readlines()
            lines = lines[2:]
            self.firstNameLineEdit.setText(lines[0][12:-13])
            self.lastNameLineEdit.setText(lines[1][11:-12])
            self.addressLineEdit.setText(lines[2][10:-11])
            self.cityLineEdit.setText(lines[3][7:-8])
            self.stateLineEdit.setText(lines[4][8:-9])
            self.zipLineEdit.setText(lines[5][6:-7])
            self.emailLineEdit.setText(lines[6][8:-9])
        self.loadButton.setEnabled(False)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()

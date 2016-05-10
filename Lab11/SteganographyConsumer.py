import sys
import os
from PySide.QtGui import *
from SteganographyGUI import *
from Steganography import *
import numpy
from scipy.misc import *

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.viewPayload1.deleteLater()
        self.viewPayload1 = Imageframe(self.grpPayload1)
        self.viewPayload1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewPayload1.setObjectName("viewPayload1")

        self.viewCarrier1.deleteLater()
        self.viewCarrier1 = Imageframe(self.grpCarrier1)
        self.viewCarrier1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier1.setObjectName("viewCarrier1")

        self.viewCarrier2.deleteLater()
        self.viewCarrier2 = Imageframe(self.grpCarrier2)
        self.viewCarrier2.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier2.setObjectName("viewCarrier2")

        self.slideCompression.valueChanged.connect(self.SlideValueChanged)
        self.chkApplyCompression.stateChanged.connect(self.chkApplyCompressionStateChanged)
        self.txtPayloadSize.textChanged.connect(self.chkEmbedSaveButton)
        self.txtCarrierSize.textChanged.connect(self.chkEmbedSaveButton)
        self.chkOverride.stateChanged.connect(self.chkEmbedSaveButton)
        self.btnSave.clicked.connect(self.SaveBtn)
        self.btnClean.clicked.connect(self.CleanBtn)
        self.btnExtract.clicked.connect(self.ExtractBtn)
        #self.slideCompression.installEventFilter(self)
    def eventFilter(self,source, e):
        print(e.type())
        return False
        '''self.scene = None
        self.viewPayload1.setAcceptDrops(True)
        self.viewCarrier1.setAcceptDrops(True)
        self.viewCarrier2.setAcceptDrops(True)
        self.viewPayload1.installEventFilter(self)
        self.viewCarrier1.installEventFilter(self)
        self.viewCarrier2.installEventFilter(self)

    def eventFilter(self,source, e):
        print(e.type())
        if e.type() == QtCore.QEvent.DragEnter:
            if e.mimeData().hasUrls:
                e.setDropAction(QtCore.Qt.CopyAction)
                e.accept()
                for url in e.mimeData().urls():
                    fname = str(url.toLocalFile())
                self.scene = QGraphicsScene()
                self.scene.addPixmap(QPixmap(fname))
            else:
                e.ignore()
        if e.type() == QtCore.QEvent.Enter and self.scene is not None:
            if source is self.viewPayload1:
                self.viewPayload1.setScene(self.scene)
            if source is self.viewCarrier1:
                self.viewCarrier1.setScene(self.scene)
            if source is self.viewCarrier2:
                self.viewCarrier2.setScene(self.scene)
            self.scene = None
        return False'''
    def SlideValueChanged(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.viewPayload1.imgclass = Payload(self.viewPayload1.imgclass.img,self.slideCompression.value())
        self.txtPayloadSize.setText(str(len(self.viewPayload1.imgclass.xml)))
        self.chkEmbedSaveButton()

    def chkApplyCompressionStateChanged(self):
        if self.chkApplyCompression.isChecked() == False:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.lblLevel.setEnabled(False)
            self.viewPayload1.imgclass = Payload(self.viewPayload1.imgclass.img,0)
            self.txtPayloadSize.setText(str(len(self.viewPayload1.imgclass.xml)))
        else:
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.lblLevel.setEnabled(True)
            self.viewPayload1.imgclass = Payload(self.viewPayload1.imgclass.img,self.slideCompression.value())
            self.txtPayloadSize.setText(str(len(self.viewPayload1.imgclass.xml)))
        self.chkEmbedSaveButton()

    def chkEmbedSaveButton(self):
        if int(self.txtCarrierSize.text()) >= int(self.txtPayloadSize.text()):
            if not self.viewCarrier1.imgclass.payloadExists():
                self.btnSave.setEnabled(True)
            else:
                if self.chkOverride.isChecked():
                    self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)

    def SaveBtn(self):
        filename = QtGui.QFileDialog.getSaveFileName(self,'Save As','',selectedFilter='*.png')
        if filename:
            img = self.viewCarrier1.imgclass.embedPayload(self.viewPayload1.imgclass,self.chkOverride.isChecked())
            imsave(filename[0]+'.png',img)
        else:
            raise ValueError

    def CleanBtn(self):
        img = self.viewCarrier2.imgclass.clean()
        imsave(self.viewCarrier2.filename,img)
        self.btnExtract.setEnabled(False)
        self.btnClean.setEnabled(False)
        self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
        scene = QGraphicsScene()
        self.viewPayload2.setScene(scene)

    def ExtractBtn(self):
        payload = self.viewCarrier2.imgclass.extractPayload()
        imsave('tmp.png',payload.img)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap('tmp.png'))
        self.viewPayload2.setScene(scene)
        self.viewPayload2.fitInView(scene.sceneRect(),QtCore.Qt.KeepAspectRatio)
        os.remove('tmp.png')

class Imageframe(QGraphicsView):
    def __init__(self,parent=None):
        super(Imageframe,self).__init__(parent)
        self.setAcceptDrops(True)
        self.imgclass = None
        self.par = parent
        self.filename = None
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                fname = str(url.toLocalFile())
            self.filename = fname
            img = imread(fname)
            if isinstance(img,numpy.ndarray):
                if 'Payload' in self.objectName():
                    self.imgclass = Payload(img,0)
                    self.par.findChild(QtGui.QCheckBox,"chkApplyCompression").setChecked(False)
                    self.par.findChild(QtGui.QLineEdit,"txtPayloadSize").setText(str(len(self.imgclass.xml)))
                    self.par.findChild(QtGui.QSlider,"slideCompression").setEnabled(False)
                    self.par.findChild(QtGui.QSlider,"slideCompression").setValue(0)
                    self.par.findChild(QtGui.QLineEdit,"txtCompression").setEnabled(False)
                    self.par.findChild(QtGui.QLineEdit,"txtCompression").setText("0")
                    self.par.findChild(QtGui.QLabel,"lblLevel").setEnabled(False)
                elif 'viewCarrier1' in self.objectName():
                    self.imgclass = Carrier(img)
                    if self.imgclass.payloadExists():
                        self.par.findChild(QtGui.QLabel,"lblPayloadFound").setText(">>>>Payload Found<<<<")
                        self.par.findChild(QtGui.QCheckBox,"chkOverride").setEnabled(True)
                    else:
                        self.par.findChild(QtGui.QLabel,"lblPayloadFound").setText("")
                        self.par.findChild(QtGui.QCheckBox,"chkOverride").setEnabled(False)
                    self.par.findChild(QtGui.QCheckBox,"chkOverride").setChecked(False)
                    self.par.findChild(QtGui.QLineEdit,"txtCarrierSize").setText(str(len(self.imgclass.img.flatten())))
                else:
                    self.imgclass = Carrier(img)
                    if self.imgclass.payloadExists():
                        [i.setEnabled(True) for i in self.par.findChildren(QtGui.QPushButton)]
                        self.par.findChild(QtGui.QLabel,"lblCarrierEmpty").setText("")
                    else:
                        [i.setEnabled(False) for i in self.par.findChildren(QtGui.QPushButton)]
                        self.par.findChild(QtGui.QLabel,"lblCarrierEmpty").setText(">>>>Carrier Empty<<<<")
                    p2 = self.par.parent().findChild(QtGui.QGraphicsView,"viewPayload2")
                    s = QGraphicsScene()
                    p2.setScene(s)

                scene = QGraphicsScene()
                scene.addPixmap(QPixmap(fname))
                self.setScene(scene)
                self.fitInView(scene.sceneRect(),QtCore.Qt.KeepAspectRatio)
        else:
            e.ignore()
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
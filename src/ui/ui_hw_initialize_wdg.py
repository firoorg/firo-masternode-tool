# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_hw_initialize_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgInitializeHw(object):
    def setupUi(self, WdgInitializeHw):
        WdgInitializeHw.setObjectName("WdgInitializeHw")
        WdgInitializeHw.resize(836, 447)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WdgInitializeHw)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages = QtWidgets.QStackedWidget(WdgInitializeHw)
        self.pages.setObjectName("pages")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gbNumberOfMnemonicWords = QtWidgets.QGroupBox(self.page1)
        self.gbNumberOfMnemonicWords.setObjectName("gbNumberOfMnemonicWords")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbNumberOfMnemonicWords)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rbWordsCount24 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount24.setChecked(True)
        self.rbWordsCount24.setObjectName("rbWordsCount24")
        self.verticalLayout_7.addWidget(self.rbWordsCount24)
        self.rbWordsCount18 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount18.setObjectName("rbWordsCount18")
        self.verticalLayout_7.addWidget(self.rbWordsCount18)
        self.rbWordsCount12 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount12.setObjectName("rbWordsCount12")
        self.verticalLayout_7.addWidget(self.rbWordsCount12)
        self.verticalLayout_3.addWidget(self.gbNumberOfMnemonicWords)
        self.chbUsePIN = QtWidgets.QCheckBox(self.page1)
        self.chbUsePIN.setChecked(True)
        self.chbUsePIN.setObjectName("chbUsePIN")
        self.verticalLayout_3.addWidget(self.chbUsePIN)
        self.chbUsePassphrase = QtWidgets.QCheckBox(self.page1)
        self.chbUsePassphrase.setObjectName("chbUsePassphrase")
        self.verticalLayout_3.addWidget(self.chbUsePassphrase)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtDeviceLabel = QtWidgets.QLineEdit(self.page1)
        self.edtDeviceLabel.setObjectName("edtDeviceLabel")
        self.horizontalLayout.addWidget(self.edtDeviceLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pages.addWidget(self.page1)
        self.verticalLayout_4.addWidget(self.pages)

        self.retranslateUi(WdgInitializeHw)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WdgInitializeHw)

    def retranslateUi(self, WdgInitializeHw):
        _translate = QtCore.QCoreApplication.translate
        WdgInitializeHw.setWindowTitle(_translate("WdgInitializeHw", "Form"))
        self.gbNumberOfMnemonicWords.setTitle(_translate("WdgInitializeHw", "Number of seed words"))
        self.rbWordsCount24.setText(_translate("WdgInitializeHw", "24"))
        self.rbWordsCount18.setText(_translate("WdgInitializeHw", "18"))
        self.rbWordsCount12.setText(_translate("WdgInitializeHw", "12"))
        self.chbUsePIN.setText(_translate("WdgInitializeHw", "Use PIN"))
        self.chbUsePassphrase.setText(_translate("WdgInitializeHw", "Use Passphrase"))
        self.edtDeviceLabel.setPlaceholderText(_translate("WdgInitializeHw", "Device label"))

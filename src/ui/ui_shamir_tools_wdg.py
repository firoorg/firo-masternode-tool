# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_shamir_tools_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgShamirToolsHw(object):
    def setupUi(self, WdgShamirToolsHw):
        WdgShamirToolsHw.setObjectName("WdgShamirToolsHw")
        WdgShamirToolsHw.resize(587, 352)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WdgShamirToolsHw)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages = QtWidgets.QStackedWidget(WdgShamirToolsHw)
        self.pages.setObjectName("pages")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPage0Title = QtWidgets.QLabel(self.page0)
        self.lblPage0Title.setObjectName("lblPage0Title")
        self.verticalLayout.addWidget(self.lblPage0Title)
        self.gbMainActionType = QtWidgets.QGroupBox(self.page0)
        self.gbMainActionType.setTitle("")
        self.gbMainActionType.setFlat(False)
        self.gbMainActionType.setObjectName("gbMainActionType")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gbMainActionType)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rbActionTypeSplit = QtWidgets.QRadioButton(self.gbMainActionType)
        self.rbActionTypeSplit.setChecked(False)
        self.rbActionTypeSplit.setObjectName("rbActionTypeSplit")
        self.verticalLayout_5.addWidget(self.rbActionTypeSplit)
        self.rbActionTypeCombine = QtWidgets.QRadioButton(self.gbMainActionType)
        self.rbActionTypeCombine.setChecked(False)
        self.rbActionTypeCombine.setObjectName("rbActionTypeCombine")
        self.verticalLayout_5.addWidget(self.rbActionTypeCombine)
        self.verticalLayout.addWidget(self.gbMainActionType)
        self.lblPage0Message = QtWidgets.QLabel(self.page0)
        self.lblPage0Message.setWordWrap(True)
        self.lblPage0Message.setOpenExternalLinks(True)
        self.lblPage0Message.setObjectName("lblPage0Message")
        self.verticalLayout.addWidget(self.lblPage0Message)
        spacerItem = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pages.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lblPage1Title = QtWidgets.QLabel(self.page1)
        self.lblPage1Title.setObjectName("lblPage1Title")
        self.verticalLayout_9.addWidget(self.lblPage1Title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.page1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.cboShares = QtWidgets.QComboBox(self.page1)
        self.cboShares.setMinimumSize(QtCore.QSize(100, 0))
        self.cboShares.setObjectName("cboShares")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.cboShares.addItem("")
        self.horizontalLayout.addWidget(self.cboShares)
        self.label_5 = QtWidgets.QLabel(self.page1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.cboThreashold = QtWidgets.QComboBox(self.page1)
        self.cboThreashold.setMinimumSize(QtCore.QSize(100, 0))
        self.cboThreashold.setObjectName("cboThreashold")
        self.horizontalLayout.addWidget(self.cboThreashold)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.lblPage1Message = QtWidgets.QLabel(self.page1)
        self.lblPage1Message.setText("")
        self.lblPage1Message.setWordWrap(True)
        self.lblPage1Message.setObjectName("lblPage1Message")
        self.verticalLayout_9.addWidget(self.lblPage1Message)
        spacerItem2 = QtWidgets.QSpacerItem(20, 249, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.pages.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblPage2Title = QtWidgets.QLabel(self.page2)
        self.lblPage2Title.setObjectName("lblPage2Title")
        self.verticalLayout_2.addWidget(self.lblPage2Title)
        self.groupBox = QtWidgets.QGroupBox(self.page2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rbInputBIP39Seed = QtWidgets.QRadioButton(self.groupBox)
        self.rbInputBIP39Seed.setObjectName("rbInputBIP39Seed")
        self.verticalLayout_8.addWidget(self.rbInputBIP39Seed)
        self.rbInputCharString = QtWidgets.QRadioButton(self.groupBox)
        self.rbInputCharString.setObjectName("rbInputCharString")
        self.verticalLayout_8.addWidget(self.rbInputCharString)
        self.rbInputHexString = QtWidgets.QRadioButton(self.groupBox)
        self.rbInputHexString.setObjectName("rbInputHexString")
        self.verticalLayout_8.addWidget(self.rbInputHexString)
        self.rbInputGPGPrivateKey = QtWidgets.QRadioButton(self.groupBox)
        self.rbInputGPGPrivateKey.setObjectName("rbInputGPGPrivateKey")
        self.verticalLayout_8.addWidget(self.rbInputGPGPrivateKey)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.lblPage2Message = QtWidgets.QLabel(self.page2)
        self.lblPage2Message.setText("")
        self.lblPage2Message.setWordWrap(True)
        self.lblPage2Message.setObjectName("lblPage2Message")
        self.verticalLayout_2.addWidget(self.lblPage2Message)
        spacerItem3 = QtWidgets.QSpacerItem(20, 310, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pages.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblPage3Title = QtWidgets.QLabel(self.page3)
        self.lblPage3Title.setObjectName("lblPage3Title")
        self.verticalLayout_6.addWidget(self.lblPage3Title)
        self.edtInputSecret = QtWidgets.QTextEdit(self.page3)
        self.edtInputSecret.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.edtInputSecret.setObjectName("edtInputSecret")
        self.verticalLayout_6.addWidget(self.edtInputSecret)
        self.pages.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblPage4Title = QtWidgets.QLabel(self.page4)
        self.lblPage4Title.setWordWrap(True)
        self.lblPage4Title.setOpenExternalLinks(True)
        self.lblPage4Title.setObjectName("lblPage4Title")
        self.verticalLayout_7.addWidget(self.lblPage4Title)
        self.pages.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblPage5Title = QtWidgets.QLabel(self.page5)
        self.lblPage5Title.setText("")
        self.lblPage5Title.setObjectName("lblPage5Title")
        self.verticalLayout_3.addWidget(self.lblPage5Title)
        spacerItem4 = QtWidgets.QSpacerItem(20, 293, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.pages.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lbPage6Title = QtWidgets.QLabel(self.page6)
        self.lbPage6Title.setText("")
        self.lbPage6Title.setObjectName("lbPage6Title")
        self.verticalLayout_10.addWidget(self.lbPage6Title)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.pages.addWidget(self.page6)
        self.verticalLayout_4.addWidget(self.pages)

        self.retranslateUi(WdgShamirToolsHw)
        self.pages.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(WdgShamirToolsHw)

    def retranslateUi(self, WdgShamirToolsHw):
        _translate = QtCore.QCoreApplication.translate
        WdgShamirToolsHw.setWindowTitle(_translate("WdgShamirToolsHw", "Form"))
        self.lblPage0Title.setText(_translate("WdgShamirToolsHw", "<b>Main action type</b>"))
        self.rbActionTypeSplit.setText(_translate("WdgShamirToolsHw", "Split secret"))
        self.rbActionTypeCombine.setText(_translate("WdgShamirToolsHw", "Combine (recover) secret"))
        self.lblPage0Message.setText(_translate("WdgShamirToolsHw", "..."))
        self.lblPage1Title.setText(_translate("WdgShamirToolsHw", "<b>Specify the number of shares and the threshold required to recover the secret</b>"))
        self.label_4.setText(_translate("WdgShamirToolsHw", "Number of shares:"))
        self.cboShares.setItemText(0, _translate("WdgShamirToolsHw", "2"))
        self.cboShares.setItemText(1, _translate("WdgShamirToolsHw", "3"))
        self.cboShares.setItemText(2, _translate("WdgShamirToolsHw", "4"))
        self.cboShares.setItemText(3, _translate("WdgShamirToolsHw", "5"))
        self.cboShares.setItemText(4, _translate("WdgShamirToolsHw", "6"))
        self.cboShares.setItemText(5, _translate("WdgShamirToolsHw", "7"))
        self.cboShares.setItemText(6, _translate("WdgShamirToolsHw", "8"))
        self.cboShares.setItemText(7, _translate("WdgShamirToolsHw", "9"))
        self.cboShares.setItemText(8, _translate("WdgShamirToolsHw", "10"))
        self.cboShares.setItemText(9, _translate("WdgShamirToolsHw", "11"))
        self.cboShares.setItemText(10, _translate("WdgShamirToolsHw", "12"))
        self.cboShares.setItemText(11, _translate("WdgShamirToolsHw", "13"))
        self.cboShares.setItemText(12, _translate("WdgShamirToolsHw", "14"))
        self.cboShares.setItemText(13, _translate("WdgShamirToolsHw", "15"))
        self.cboShares.setItemText(14, _translate("WdgShamirToolsHw", "16"))
        self.label_5.setText(_translate("WdgShamirToolsHw", "threashold:"))
        self.lblPage2Title.setText(_translate("WdgShamirToolsHw", "<b>Specify the input data type</b>"))
        self.rbInputBIP39Seed.setText(_translate("WdgShamirToolsHw", "BIP-39 seed words (aka recovery seed)"))
        self.rbInputCharString.setText(_translate("WdgShamirToolsHw", "Character string (e.g. password)"))
        self.rbInputHexString.setText(_translate("WdgShamirToolsHw", "Hexadecimal string"))
        self.rbInputGPGPrivateKey.setText(_translate("WdgShamirToolsHw", "GPG private key (ASCII)"))
        self.lblPage3Title.setText(_translate("WdgShamirToolsHw", "<b>Enter the input secret</b>"))
        self.lblPage4Title.setText(_translate("WdgShamirToolsHw", "<b>Enter the words of your recovery seed</b>"))

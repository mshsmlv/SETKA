# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editordialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorDialog(object):
    def setupUi(self, EditorDialog):
        EditorDialog.setObjectName("EditorDialog")
        EditorDialog.resize(482, 388)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditorDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(EditorDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.e1_edit = QtWidgets.QLineEdit(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e1_edit.sizePolicy().hasHeightForWidth())
        self.e1_edit.setSizePolicy(sizePolicy)
        self.e1_edit.setObjectName("e1_edit")
        self.horizontalLayout.addWidget(self.e1_edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(EditorDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.e2_edit = QtWidgets.QLineEdit(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e2_edit.sizePolicy().hasHeightForWidth())
        self.e2_edit.setSizePolicy(sizePolicy)
        self.e2_edit.setObjectName("e2_edit")
        self.horizontalLayout_2.addWidget(self.e2_edit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(EditorDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.e3_edit = QtWidgets.QLineEdit(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e3_edit.sizePolicy().hasHeightForWidth())
        self.e3_edit.setSizePolicy(sizePolicy)
        self.e3_edit.setObjectName("e3_edit")
        self.horizontalLayout_3.addWidget(self.e3_edit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(EditorDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.e4_edit = QtWidgets.QLineEdit(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e4_edit.sizePolicy().hasHeightForWidth())
        self.e4_edit.setSizePolicy(sizePolicy)
        self.e4_edit.setObjectName("e4_edit")
        self.horizontalLayout_4.addWidget(self.e4_edit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(EditorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.recipe_spin_box = QtWidgets.QSpinBox(EditorDialog)
        self.recipe_spin_box.setObjectName("recipe_spin_box")
        self.horizontalLayout_5.addWidget(self.recipe_spin_box)
        self.warning_label = QtWidgets.QLabel(EditorDialog)
        self.warning_label.setText("")
        self.warning_label.setObjectName("warning_label")
        self.horizontalLayout_5.addWidget(self.warning_label)
        self.save_button = QtWidgets.QPushButton(EditorDialog)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_5.addWidget(self.save_button)
        self.open_button = QtWidgets.QPushButton(EditorDialog)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_5.addWidget(self.open_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.recipes_list = QtWidgets.QListWidget(EditorDialog)
        self.recipes_list.setObjectName("recipes_list")
        self.verticalLayout.addWidget(self.recipes_list)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(EditorDialog)
        self.buttonBox.accepted.connect(EditorDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(EditorDialog)

    def retranslateUi(self, EditorDialog):
        _translate = QtCore.QCoreApplication.translate
        EditorDialog.setWindowTitle(_translate("EditorDialog", "Редактор рецептов"))
        self.label.setText(_translate("EditorDialog", "Создать новый / редактировать старый рецепт"))
        self.label_2.setText(_translate("EditorDialog", "Экструдер"))
        self.label_3.setText(_translate("EditorDialog", "Фильера1"))
        self.label_4.setText(_translate("EditorDialog", "Фильера2"))
        self.label_5.setText(_translate("EditorDialog", "Приемка  "))
        self.label_6.setText(_translate("EditorDialog", "Номер рецепта"))
        self.save_button.setText(_translate("EditorDialog", "Сохранить"))
        self.open_button.setText(_translate("EditorDialog", "Открыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorDialog = QtWidgets.QDialog()
    ui = Ui_EditorDialog()
    ui.setupUi(EditorDialog)
    EditorDialog.show()
    sys.exit(app.exec_())


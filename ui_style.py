from PyQt5 import QtCore,QtGui

def btn_style(screen, translator, name_btn):
    btn_font = QtGui.QFont()
    btn_font.setFamily("Poppins Medium")
    btn_font.setPointSize(11)
    screen.avancar.setFont(btn_font)
    screen.avancar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    screen.avancar.setStyleSheet(
        "QPushButton{\n"
        "    border-radius: 7px;\n"
        "    border-style:solid;\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-width:3px;\n"
        "    border-color: #411E8F;\n"
        "    background-color: #2A2438;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border:10px;\n"
        "    background-color:#411E8F;\n"
        "}")

    screen.avancar.setObjectName("avancar")
    screen.avancar.setText(translator("MainWindow", name_btn))
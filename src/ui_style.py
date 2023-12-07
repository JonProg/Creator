from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QFrame

font = QtGui.QFont()
font.setFamily("Poppins")
font.setPointSize(11)

btn_font = QtGui.QFont()
btn_font.setFamily("Poppins Medium")
btn_font.setPointSize(11)

color_text = 'rgb(255, 255, 255)'

def btn_style(screen, translator, name_btn):
    screen.avancar.setFont(btn_font)
    screen.avancar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    screen.avancar.setStyleSheet(
        "QPushButton{\n"
        "    border-radius: 7px;\n"
        "    border-style:solid;\n"
        f"    color: {color_text};\n"
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

def input_style(element):
    element.setFont(font)
    element.viewport().setProperty(
    "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
    
    element.setStyleSheet(
        "QPlainTextEdit{\n"
            "border-radius: 4px;\n"
            f"background-color: {color_text};\n"
        "}\n"
        "\n"
        "QPlainTextEdit:focus{\n"
            "border: 2px solid #6A1B9A\n"
        "}"
    )

    element.setFrameShape(QFrame.NoFrame)

def mista_style(button):
    button.setFont(font)
    button.setStyleSheet(
        "border-radius: 5px;\n"
        "border-style:solid;\n"
        f"color: {color_text};\n"
        "border-width:3px;\n"
        "border-color: #411E8F;\n"
        "background-color: #2A2438;"
    )
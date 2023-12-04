from PyQt5 import uic,QtCore,QtGui
from PyQt5.QtWidgets import (QLabel, QFrame, QPlainTextEdit,
                            QPushButton,QApplication,QMessageBox, QFileDialog)
from backend import order_data, criar_prova
from functools import partial
from ui_style import btn_style, input_style, mista_style

questions = [[]]
questoes = {}
elements = []

win_escrita = uic.loadUi("screens/win_escrita.ui")
win_download = uic.loadUi("screens/win_download.ui")
win_multi = uic.loadUi("screens/win_multi.ui")
win_mista = uic.loadUi("screens/win_mista.ui")
win_main = uic.loadUi("screens/win_main.ui")

windows = [win_multi, win_escrita, win_mista]

def return_window(screen):
    global questions,questoes

    for item in elements:
        item.close()

    elements.clear()
    questoes.clear()

    questions = [[]]
    win_download.quest_choice.setChecked(False)
    win_download.qtd_provas.setValue(1)
    
    screen.close()
    win_main.show()

win_download.home_btn.clicked.connect(partial(return_window,win_download))

#------------------------------------------------------------------------------------
#Tela para o download do pdf

def pdf_download(screen, quests:list, questoes:dict):
    screen.close()
    order_data(quests,questoes)
    def folder():    
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("QLabel{font-size: 15px;}")

        qtd_provas = 0
        fname = QFileDialog.getExistingDirectory(
            win_download, caption='Selecione uma Pasta',
            )
        qtd_provas+=win_download.qtd_provas.value()

        try:
            if win_download.quest_choice.isChecked():
                criar_prova(questoes, fname, qtd_provas, True)
            else:
                criar_prova(questoes, fname, qtd_provas)
        except:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Erro ao criar arquivo PDF \n\n(ಥ﹏ಥ)")
            msg.setWindowTitle("Error")
            return msg.exec_()

        msg.setText("PDF Criado com Sucesso \n\nd–(^ ‿ ^ )z")
        msg.setWindowTitle("Sucesso")
        quests.clear()
        return msg.exec_()

    def frame_choice():
        if win_download.quest_choice.isChecked():
            win_download.frame_provas.show()

        else:
            win_download.frame_provas.hide()
            win_download.qtd_provas.setValue(1)

    win_download.frame_provas.hide()
    win_download.quest_choice.clicked.connect(frame_choice)
    win_download.avancar.clicked.connect(folder)
    return win_download.show()

#----------------------------------------------------------------------
#Tela de questões escritas

def quests_escritas(quests:int):
    input_y = 0
    win_escrita.frame_quest = QFrame(win_escrita.frame)
    win_escrita.frame_quest.setGeometry(QtCore.QRect(9, 120, 381, 101))
    win_escrita.frame_quest.setObjectName(f"frame_quest")
    height_frame = win_escrita.frame_quest.frameGeometry().height()

    _translate = QtCore.QCoreApplication.translate
    win_escrita.avancar = QPushButton(win_escrita.frame)
    win_escrita.avancar.setGeometry(QtCore.QRect(150, 380, 101, 41))

    elements.extend([win_escrita.frame_quest,win_escrita.avancar])

    for quest in range(1,quests+1):

        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)

        win_escrita.text_quest = QLabel(win_escrita.frame_quest)
        win_escrita.text_quest.setGeometry(QtCore.QRect(10, 10+input_y, 91, 16))
        win_escrita.text_quest.setStyleSheet("color: rgb(255, 255, 255);")
        win_escrita.text_quest.setObjectName(f"quest_{quest}")
        win_escrita.text_quest.setFont(font)
        #------------------------------------------------------------
        win_escrita.input_quest = QPlainTextEdit(win_escrita.frame_quest)
        win_escrita.input_quest.setGeometry(QtCore.QRect(10, 40+input_y, 361, 61))
        
        questions.append(win_escrita.input_quest)
        questions[0].append(None)

        input_style(win_escrita.input_quest)
        win_escrita.input_quest.setObjectName(f"input_quest{quest}")
        #------------------------------------------------------------

        win_escrita.text_quest.setText(_translate("MainWindow", f"Questão {quest}:"))
        win_escrita.frame_quest.resize(381, height_frame+input_y)
        win_escrita.input_quest.show()
        input_y +=120

    btn_style(win_escrita, _translate, "Avançar")
    win_escrita.avancar.move(150, input_y+140)

    win_escrita.frame.setMinimumSize(QtCore.QSize(0, input_y+200))
    return win_escrita.show()
#----------------------------------------------------------------------
#Tela de questões de multipla escolha

def quests_multi(quests:int):
    position_quest = 0
    alternatives = ['A','B','C','D']

    win_multi.frame_quest = QFrame(win_multi.frame)
    win_multi.frame_quest.setGeometry(QtCore.QRect(10, 140, 361, 411))
    win_multi.frame_quest.setFrameShape(QFrame.NoFrame)
    win_multi.frame_quest.setObjectName(f"frame_quest")
    height_frame = win_multi.frame_quest.frameGeometry().height()

    _translate = QtCore.QCoreApplication.translate
    win_multi.avancar = QPushButton(win_multi.frame)
    win_multi.avancar.setGeometry(QtCore.QRect(150, 380, 101, 41))

    elements.extend([win_multi.frame_quest, win_multi.avancar])

    for quest in range(1,quests+1):
        alternatives_text = []
        position_alternative = position_quest +120
        
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)

        win_multi.quest_title = QLabel(win_multi.frame_quest)
        win_multi.quest_title.setGeometry(QtCore.QRect(0, position_quest, 101, 16))
        font.setPointSize(12)
        win_multi.quest_title.setFont(font)
        win_multi.quest_title.setStyleSheet("color: rgb(255, 255, 255);")
        win_multi.quest_title.setObjectName(f"quest_{quest}")
        #------------------------------------------------------------
        win_multi.input_quest = QPlainTextEdit(win_multi.frame_quest)
        win_multi.input_quest.setGeometry(QtCore.QRect(0, 30 + position_quest, 361, 61))
        input_style(win_multi.input_quest)
        win_multi.input_quest.setObjectName(f"input_quest{quest}")

        questions.append(win_multi.input_quest)
        #------------------------------------------------------------

        _translate = QtCore.QCoreApplication.translate
        win_multi.quest_title.setText(_translate("MainWindow", f"Questão {quest}:"))

        win_multi.input_quest.show()
        #------------------------------------------------------------
        
        for letra in alternatives:
            win_multi.label_alternative = QLabel(win_multi.frame_quest)
            win_multi.label_alternative.setGeometry(QtCore.QRect
            (30, 10 + position_alternative, 20, 31))
            
            font.setPointSize(15)
            win_multi.label_alternative.setFont(font)
            win_multi.label_alternative.setStyleSheet(
                "color: rgb(255, 255, 255);"
            )
            win_multi.label_alternative.setObjectName(f"label_{quest}")

            win_multi.alternative = QPlainTextEdit(win_multi.frame_quest)
            win_multi.alternative.setGeometry(QtCore.QRect
            (60, position_alternative, 301, 51))
            
            input_style(win_multi.alternative)
            win_multi.alternative.setObjectName(f"alternative_{quest}")
            
            position_alternative += 80

            win_multi.label_alternative.setText(_translate("MainWindow", f"{letra}"))

            win_multi.alternative.show()

            alternatives_text.append(win_multi.alternative)
    
        #------------------------------------------------------------
        questions[0].append(alternatives_text)
        win_multi.frame_quest.resize(361,height_frame + position_quest)
        position_quest +=460
        btn_style(win_multi, _translate, "Avançar")
        win_multi.avancar.move(150,position_quest+130)
        win_multi.frame.setMinimumSize(QtCore.QSize(0, position_quest+190))
    
    return win_multi.show()
#----------------------------------------------------------------------
#Tela de questões mistas

def quest_mistas(quests:int):
    frames = []
    mc_answers = []
    written_answers = []

    alternative_questions = [[]]
    seen_buttons = []
    buttons = []

    id_btn = 0
    position_label = 100
    word_letter = ['A','B','C','D']

    def criar_quest(valor, btn):
        button : QPushButton = buttons[btn]
        frame : QFrame = frames[valor]

        def modify_frames(value):

            for other_frames in frames[valor+1:]:
                frame_y = other_frames.frameGeometry().y()
                other_frames.move(0,(frame_y+value))

            last_frame = frames[-1].frameGeometry().y()

            if frame == frames[-1] and btn%2 == 0:
                win_mista.avancar.move(140, (last_frame+190))

            elif frame == frames[-1] and btn%2 != 0:
                win_mista.avancar.move(140, (last_frame+470))

            else:
                position_button = 0
                height_last_frame:int = frames[-1].frameGeometry().height()

                if height_last_frame == 441:
                    position_button+=350
                
                elif height_last_frame == 161:
                    position_button+=200
                
                else:
                    position_button += 120

                win_mista.avancar.move(140, (last_frame+position_button))
            
            win_mista.frame.setMinimumSize(QtCore.QSize
                (0, win_mista.avancar.frameGeometry().y()+50)
                )
            
        if button.isCheckable():
            height_frame = frame.frameGeometry().height()
            button.setCheckable(False)

            if btn%2 == 0:
                    value_height = 80
                    add_margin = 60
                    if valor in seen_buttons: #Verifica se o botão já foi clicado
                        questions.pop(valor+1)
                        questions[0].pop(valor)

                        mc_answers[valor].hide()
                        value_height -= value_height
                        value_height-=280

                        add_margin -= add_margin
                        add_margin -=300
                        
                    else:
                        seen_buttons.append(valor)
                    
                    frame.resize(381,height_frame+value_height)
                    written_answers[valor].show()       
                    buttons[btn+1].setCheckable(True)    
                    modify_frames(add_margin) #Modifica os outros frames

                    questions.append(written_answers[valor])
                    questions[0].append(None)

            else:
                margin_frames = 360
                add_height = 360
                if valor in seen_buttons:   
                    questions.pop(valor+1)
                    questions[0].pop(valor)

                    written_answers[valor].hide()
                    add_height -= add_height
                    add_height += 280

                    margin_frames -= margin_frames
                    margin_frames += 300

                else:
                    seen_buttons.append(valor)

                frame.resize(381,height_frame+add_height)
                mc_answers[valor].show()
                buttons[btn-1].setCheckable(True)
                modify_frames(margin_frames)

                questions.append(alternative_questions[valor+1])
                questions[0].append(alternative_questions[0][valor])

    #-----------------------------------------------------------------------------------
    _translate = QtCore.QCoreApplication.translate
    win_mista.avancar = QPushButton(win_mista.frame)
    win_mista.avancar.setGeometry(QtCore.QRect(150, 380, 101, 41))
    btn_style(win_mista, _translate, "Avançar")
    elements.append(win_mista.avancar)
    
    for quest in range(quests):
        
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)

        win_mista.frame_quest = QFrame(win_mista.frame)
        win_mista.frame_quest.setGeometry(QtCore.QRect(0, position_label, 381, 81))
        win_mista.frame_quest.setFrameShadow(QFrame.Raised)
        win_mista.frame_quest.setFrameShape(QFrame.NoFrame)
        win_mista.frame_quest.setObjectName(f"frame_{quest}")

        elements.append(win_mista.frame_quest)

        frames.append(win_mista.frame_quest)

        #-----------------------------------------------------------------------------
        position_quest = 80
        alternatives = []

        win_mista.frame_alternative = QFrame(win_mista.frame_quest)
        win_mista.frame_alternative.setGeometry(QtCore.QRect(0, 100, 381, 341))
        win_mista.frame_alternative.setFrameShadow(QFrame.Raised)
        win_mista.frame_alternative.setFrameShape(QFrame.NoFrame)
        win_mista.frame_alternative.setObjectName(f"frame_alternative{quest}")

        win_mista.question = QPlainTextEdit(win_mista.frame_alternative)
        win_mista.question.setGeometry(QtCore.QRect(10, 0, 361, 61))
        win_mista.question.setObjectName(f'question_alternative{quest}')
        input_style(win_mista.question)
        win_mista.question.show()
        alternative_questions.append(win_mista.question)
        
        for letter in word_letter:
            win_mista.label_alternative = QLabel(win_mista.frame_alternative)
            win_mista.label_alternative.setGeometry(
                QtCore.QRect(40, position_quest+10, 21, 31)
                )
            font.setPointSize(14)
            win_mista.label_alternative.setFont(font)
            win_mista.label_alternative.setStyleSheet("color: rgb(255, 255, 255);")
            win_mista.label_alternative.setText(_translate("MainWindow", f"{letter}"))

            win_mista.quest_alternative = QPlainTextEdit(win_mista.frame_alternative)
            win_mista.quest_alternative.setGeometry(
                QtCore.QRect(70, position_quest, 301, 50)
                )
            input_style(win_mista.quest_alternative)
            win_mista.quest_alternative.setObjectName(f'quest_{letter}')
            win_mista.quest_alternative.show()
            position_quest += 70
            alternatives.append(win_mista.quest_alternative)
        
        alternative_questions[0].append(alternatives)
        mc_answers.append(win_mista.frame_alternative)

        win_mista.quest_label = QLabel(win_mista.frame_quest)
        win_mista.quest_label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        win_mista.quest_label.setFont(font)
        win_mista.quest_label.setStyleSheet("color: rgb(255, 255, 255);")
        win_mista.quest_label.setObjectName(f"quest_label{quest}")

        win_mista.quest_label.setText(_translate("MainWindow", f"Questão {quest+1}:"))
        

        #------------------------------------------------------------------------------

        win_mista.multi_btn = QPushButton(win_mista.frame_quest)
        win_mista.multi_btn.setGeometry(QtCore.QRect(210, 50, 141, 31))
        win_mista.multi_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        win_mista.multi_btn.setObjectName(f"multi_btn{quest}")

        win_mista.escrita_btn = QPushButton(win_mista.frame_quest)
        win_mista.escrita_btn.setGeometry(QtCore.QRect(30, 50, 141, 31))
        win_mista.escrita_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        win_mista.escrita_btn.setObjectName(f"escrita_btn{quest}")

        for button in [win_mista.escrita_btn, win_mista.multi_btn]:
            mista_style(button)

        #---------------------------------------------------------------------------

        win_mista.multi_btn.setText(_translate("MainWindow", f"Multipla Escolha"))
        win_mista.escrita_btn.setText(_translate("MainWindow", f"Escrita"))

        win_mista.multi_btn.setCheckable(True)
        win_mista.escrita_btn.setCheckable(True)

        win_mista.multi_btn.clicked.connect(partial(criar_quest,quest, id_btn+1))
        win_mista.escrita_btn.clicked.connect(partial(criar_quest,quest, id_btn)) 

        #-----------------------------------------------------------------------------

        win_mista.quest = QPlainTextEdit(win_mista.frame_quest)
        win_mista.quest.setGeometry(QtCore.QRect(10, 100, 361, 61))
        win_mista.quest.setObjectName(f'quest_{quest}')
        input_style(win_mista.quest)
        win_mista.quest.hide()
        written_answers.append(win_mista.quest)

        #------------------------------------------------------------------------------
        buttons.extend((win_mista.escrita_btn,win_mista.multi_btn))

        id_btn+=2
        position_label+=120

    win_mista.avancar.move(140, position_label)
    btn_style(win_mista,_translate,'Avançar')
    win_mista.frame.setMinimumSize(QtCore.QSize
        (0, win_mista.avancar.frameGeometry().y()+50)
        )

    return win_mista.show()

#------------------------------------------------------------------------------------

#----------------------------------------------------------------------
#Função que ativa as outras telas

def activity_screen(qtd_questao: int, screen):
    win_download.avancar = QPushButton(win_download.centralwidget)
    win_download.avancar.setGeometry(QtCore.QRect(70, 370, 291, 41))
    _translate = QtCore.QCoreApplication.translate
    btn_style(win_download, _translate, "Guardar Prova...")

    screens = [quests_multi, quests_escritas, quest_mistas]

    screnn_current = windows[screen]
    screen_choice = screens[screen]

    screen_choice(qtd_questao)
    screnn_current.voltar_btn.clicked.connect(partial(return_window, screnn_current))
    screnn_current.avancar.clicked.connect(partial(pdf_download, screnn_current, questions, questoes))
#----------------------------------------------------------------------

#Primeira tela
#---------------------------------------------------------------------------
def home_screen():
    qtd_quest = win_main.qtd_questoes.value()
    radios = [win_main.rad_multi, win_main.rad_escritas, win_main.rad_mistas]
    
    for indice ,radio in enumerate(radios):
        if radio.isChecked():
            activity_screen(qtd_quest,indice)
            win_main.close()
            break
    else:
        msg = QMessageBox()
        msg.setText("Escolha o tipo de questão!\n\n(ノಠ益ಠ)ノ彡┻━┻")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setStyleSheet("QLabel{font-size: 15px;}")
        return msg.exec_()


app = QApplication([])
win_main.btn_avancar.clicked.connect(home_screen)
win_main.show()
app.exec_()

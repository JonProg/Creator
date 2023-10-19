from PyQt5 import uic
from PyQt5.QtWidgets import (QFileDialog,QMessageBox,QApplication)
from random import shuffle, choices
import string as s
from fpdf import FPDF

app = QApplication([])
win_download = uic.loadUi("telas/win_download.ui")

def criar_prova(questions:dict, path_folder, qtd_question:int, randoms=False):
    for index in range(qtd_question):
        key = ''.join(choices(s.ascii_letters, k=2))

        pdf = FPDF(format="A4")
        pdf.add_page()
        pdf.add_font('Arial','','fonts\ARIAL.ttf',uni=True)
        pdf.add_font('Arial','B','fonts\ARIALBD.ttf',uni=True)

        pdf.set_font('Arial', 'B', 12)

        count = 1
        label_alternative = ['A','B','C','D']
        header = u"""
Escola: ____________________________________________________\n\
Data: ____/____/______  Turma:___________\n\
Aluno: _____________________________________________________"""
        pdf.multi_cell(txt=header, w=0, h=10, align='l')
        pdf.ln(7)
        
        if randoms:
            quests_choice = list(questions.items())
            shuffle(quests_choice)
            questions = dict(quests_choice)

        for questao, alternativas in questions.items():
            pdf.ln(8)
            pdf.set_font(style='')
            quest = f'{count}) {questao}'
            pdf.multi_cell(txt=quest,w=0, h=7, align='l')
            

            if alternativas[0] == None:
                linha = '__'*37
                for i in range(5):
                    pdf.ln(10)
                    pdf.cell(txt=linha, align='l')
                pdf.ln(10)

            else:
                for i,alternativa in enumerate(alternativas):
                    alternative_text= f'    ({label_alternative[i]}) {alternativa}'
                    pdf.ln(10)
                    pdf.set_font(style='')
                    pdf.cell(txt=alternative_text)
            pdf.ln(8)
            count+=1
        
        pdf.output(name=f'{path_folder}/prova_creater{key}-{index}.pdf') #Modificar o index por um valor aleatorio


#----------------------------------------------------------------------
#Função para ordenar os dados de forma correta para o dict {quest}
def activity(questions:list, questoes:dict):
    for quest in questions[1:]:
        questoes.update({quest.toPlainText():[]})

    for i,list_ in enumerate(questoes.values()):
        list_:list

        if questions[0][i] == None:
            list_.append(None)
        else:
            for alternatives in questions[0][i]:
                alternativa = alternatives.toPlainText()
                list_.append(alternativa)

#----------------------------------------------------------------------
#Função que salva o pdf em uma pasta e chama a função de criar o pdf

def save_pdf(screen, quests:list, questoes:dict):
    screen.close()
    activity(quests,questoes)
    def folder():    
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("QLabel{font-size: 15px;}")

        qtd_provas = 0
        fname = QFileDialog.getExistingDirectory(
            win_download, caption='Seleciona um Pasta',
            )
        qtd_provas+=win_download.qtd_provas.value()

        try:
            if win_download.quest_choice.isChecked():
                criar_prova(questoes, fname, qtd_provas, True)
            else:
                criar_prova(questoes, fname, qtd_provas)
        except:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Erro ao criar arquivo PDF")
            msg.setWindowTitle("Error")
            return msg.exec_()

        msg.setText("PDF Criado com Sucesso")
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



        
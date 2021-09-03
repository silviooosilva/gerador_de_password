from PyQt5.Qt import *
import pyperclip as clipboard
import random
from sys import argv
from simpleSubCipher import encryptMessage


class PWD(QApplication):
    def __init__(self):
        super().__init__(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowIcon(QIcon("img/favicon/favicon-16x16.png"))
        self.ferramentas.setWindowTitle("Gerador de Passwords")
        self.ferramentas.setPalette(QPalette(QColor('blue')))
        self.ferramentas.setFixedSize(500, 300)

        menu = QMenuBar(self.ferramentas)
        instr = menu.addAction("Instruções")
        instr.triggered.connect(self.instrucao)
        sobre = menu.addAction("Sobre")
        sobre.triggered.connect(self.sobre)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 25, 500, 280)

        self.principal()

    def principal(self):
        def codificar():
            if pwd.text() == '' or len(pwd.text()) <= 5:
                QMessageBox.warning(self.ferramentas, 'Atenção', 'Digite antes uma palavra com mais de 6 caracteres\npara que a codificação seja bem sucedida..')
            else:
                password = encryptMessage(None, pwd.text())
                return labelPwd.setText(password)

        janela1 = QWidget()
        layout2 = QVBoxLayout()

        labelIntro = QLabel("<h2>Gerador de Passwords</h2>")
        labelIntro.setAlignment(Qt.AlignCenter)
        layout2.addWidget(labelIntro)

        # labelImagem = QLabel()
        # labelImagem.setPixmap(QPixmap("img/01.png"))
        # labelImagem.setAlignment(Qt.AlignCenter)
        # layout2.addWidget(labelImagem)

        labelPwd = QLabel("...")
        labelPwd.setAlignment(Qt.AlignCenter)
        labelPwd.setPalette(QPalette(QColor('white')))
        layout2.addWidget(labelPwd)

        layoutPwd = QFormLayout()
        pwd = QLineEdit()
        pwd.returnPressed.connect(codificar)
        layoutPwd.addRow('<b>Digite a palavra: *</b>', pwd)
        layout2.addLayout(layoutPwd)

        botaoFraca = QPushButton('Codificar')
        botaoFraca.setDefault(True)
        botaoFraca.clicked.connect(codificar)
        layout2.addWidget(botaoFraca)

        def copiar():
            clipboard.copy(labelPwd.text())
            QMessageBox.information(self.ferramentas, 'Copiado', 'Password copiada!\nAgora já pode colar ela onde for necessário..')

        botaoCopiar = QPushButton("Copiar Password")
        botaoCopiar.setDefault(True)
        botaoCopiar.clicked.connect(copiar)
        layout2.addWidget(botaoCopiar)

        janela1.setLayout(layout2)
        self.tab.addTab(janela1, 'Principal')
        self.tab.setCurrentWidget(janela1)

    def sobre(self):
        QMessageBox.information(self.ferramentas, "Sobre o Programa", """
Nome: Gerador de Passwords
Versão: 1.1
Programador: Silvio Silva
Designer: Nurul-GC
""")

    def instrucao(self):
        QMessageBox.information(self.ferramentas, 'Instruções', """
COMO CRIAR PASSWORDS SEGURAS: 

[1] - NÃO USE SEU NOME PRÓPRIO OU DE ALGUM FAMILIAR;
[2] - UTILIZE CARACTERES ESPECIAIS (SE PERMITIDO), COMO O @;
[3] - FAÇA A JUNÇÃO DE LETRAS MAIÚSCULAS E MINÚSCULAS NAS SUAS PASSWORDS;
[4] - UTILIZE NÚMEROS;
[5] - UTILIZE SENHAS MAIORES OU IGUAIS A SEIS(6) CARÁCTERES;

CRIE BOAS PASSWORDS E SALVE SUAS INFORMAÇÕES PESSOAIS!!!
""")


if __name__ == '__main__':
    app = PWD()
    app.ferramentas.show()
    app.exec_()

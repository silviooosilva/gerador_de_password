from PyQt5.Qt import *
import pyperclip as clipboard
import random
from sys import argv
from simpleSubCipher import encryptMessage


class PWD(QApplication):
    def __init__(self):
        super().__init__(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowIcon(QIcon("img/favicon/favicon-32x32.png"))
        self.ferramentas.setWindowTitle("Gerador de Passwords")
        self.ferramentas.setPalette(QPalette(QColor('blue')))
        self.ferramentas.setFixedSize(500, 500)

        menu = QMenuBar(self.ferramentas)
        sobre = menu.addAction("Sobre")
        sobre.triggered.connect(self.sobre)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 25, 500, 480)

        self.principal()

    def principal(self):
        def codificar():
            password = encryptMessage(None, pwd.text())
            return labelPwd.setText(password)

        janela1 = QWidget()
        layout2 = QVBoxLayout()

        labelIntro = QLabel("<h2>Gerador de Passwords</h2>")
        labelIntro.setAlignment(Qt.AlignCenter)
        layout2.addWidget(labelIntro)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/01.png"))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout2.addWidget(labelImagem)

        labelPwd = QLabel("...")
        labelPwd.setAlignment(Qt.AlignCenter)
        labelPwd.setPalette(QPalette(QColor('white')))
        layout2.addWidget(labelPwd)

        layoutPwd = QFormLayout()
        pwd = QLineEdit()
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


if __name__ == '__main__':
    app = PWD()
    app.ferramentas.show()
    app.exec_()

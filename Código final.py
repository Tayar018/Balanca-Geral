from tkinter import *
import tkinter

# Funções pra  abrir as janelas
from tkinter import Toplevel


def abrirCalcularIMC():
    janelaIMC = Toplevel()
    janelaIMC.title('Calculadora IMC')
    janelaIMC.geometry('450x250')
    janelaIMC.configure(background='darkgray')
    f2 = Frame(janelaIMC, height='200', width='400').place(x='25', y='25')
    tituloIMC = Label(janelaIMC, text='Calculadora de IMC', font='Arial 20 bold').place(relx=0.5, rely=0.2, anchor=CENTER)
    entradaPeso = Label(janelaIMC, text='Peso em Kg:').place(relx=0.19, rely=0.45, anchor=CENTER)
    Peso = Entry(janelaIMC, width=14)
    Peso.place(relx=0.41, rely=0.45, anchor=CENTER)
    entradaAltura = Label(janelaIMC, text='Altura em cm:').place(relx=0.2, rely=0.55, anchor=CENTER)
    Altura = Entry(janelaIMC, width=14)
    Altura.place(relx=0.41, rely=0.55, anchor=CENTER)
    def calcularIMC():
        global imc
        try:
            imc = round(float(Peso.get().replace(',', '.')) / ((float(Altura.get().replace(',', '.')) ** 2) / 10000), 2)
            resultadoIMC['text'] = f'Seu imc é: {imc}'
        except ValueError:
            resultadoIMC['text'] = 'Insira valores válidos!'
        if imc <= 18.5:
            Indice['text'] = ' Você está abaixo do peso'
        elif imc > 18.5 and imc <= 24.9:
            Indice['text'] = 'Você está no peso ideal'
        elif imc > 24.9:
            Indice['text'] = 'Você está acima do peso'

    # Botão janela
    imcCalculo = Button(janelaIMC, text='Calcular', command=calcularIMC)
    imcCalculo.place(relx=0.4, rely=0.78, anchor=CENTER)
    # Botão return
    voltarIMC = Button(janelaIMC, text="Voltar", command=janelaIMC.destroy)
    voltarIMC.place(relx=0.6, rely=0.78, anchor=CENTER)

    # saida do resultado
    resultadoIMC = Label(janelaIMC, text='')
    resultadoIMC.place(relx=0.74, rely=0.54, anchor=CENTER)
    Indice = Label(janelaIMC, text='')
    Indice.place(relx=0.74, rely=0.45, anchor=CENTER)

def abrirCalcularTMB():
    janelaTMB = tkinter.Toplevel()
    janelaTMB.title('Calculadora da TMB')
    janelaTMB.geometry('450x250')
    janelaTMB.configure(background='darkgray')

    f3 = Frame(janelaTMB, height=200, width=400).place(x=25, y=25)
    tituloTMB = Label(janelaTMB, text='Calculadora de Taxa Metabólica Basal', font='Arial 16 bold').place(relx=0.5, rely=0.19, anchor=CENTER)
    desc = Label(janelaTMB, text='A Taxa Metabólica Basal é utilizada para calcular aproximadamente\n'
                                 'quantas calorias seu corpo gasta por dia').place(relx=0.5, rely=0.3, anchor=CENTER)

    entradaSexo = Label(janelaTMB, text='Insira seu Sexo:')
    entradaSexo.place(relx=0.2, rely=0.44, anchor=CENTER)
    Sexo = Entry(janelaTMB, width=20)
    Sexo.place(relx=0.44, rely=0.44, anchor=CENTER)

    entradaPeso = Label(janelaTMB, text='Peso em Kg:')
    entradaPeso.place(relx=0.18, rely=0.52, anchor=CENTER)
    Peso = Entry(janelaTMB, width=20)
    Peso.place(relx=0.44, rely=0.52, anchor=CENTER)

    AlturaTmb = Label(janelaTMB, text='Altura em cm:')
    AlturaTmb.place(relx=0.19, rely=0.6, anchor=CENTER)
    Altura = Entry(janelaTMB, width=20)
    Altura.place(relx=0.44, rely=0.6, anchor=CENTER)

    entradaIdade = Label(janelaTMB, text='Insira sua Idade:')
    entradaIdade.place(relx=0.2, rely=0.68, anchor=CENTER)
    idade = Entry(janelaTMB, width=20)
    idade.place(relx=0.44, rely=0.68, anchor=CENTER)

    # função calcular TMB
    def calcularTMb():
        global tmb
        if Sexo.get() == 'F':
            tmb = round(655 + 9.6 * float(Peso.get().replace(',', '.'))) + 1.8 * float(Altura.get()) - 4.7 * int(
                idade.get())
            resultadoTMB['text'] = f'TMB: {tmb}'
            return tmb
        elif Sexo.get() == 'M':
            tmb = round(
                66 + 13.8 * float(Peso.get().replace(',', '.')) + 5 * float(Altura.get()) - 6.8 * int(idade.get()))
            resultadoTMB['text'] = f'TMB: {tmb}'
            return tmb


    # resultado tmb
    resultadoTMB = Label(janelaTMB, text='')
    resultadoTMB.place(relx=0.75, rely=0.5, anchor=CENTER)
    Taxa = Label(janelaTMB, text='')
    Taxa.place(relx=0.65, rely=0.57, anchor=CENTER)

    # botão calculo tmb
    tmbCalculo = Button(janelaTMB, text='Calcular', command=calcularTMb)
    tmbCalculo.place(relx=0.4, rely=0.81, anchor=CENTER)
    voltarTMB = Button(janelaTMB, text="Voltar", command=janelaTMB.destroy)
    voltarTMB.place(relx=0.6, rely=0.8, anchor=CENTER)

def abrirCalcualrCAlorias():
    janelaCalorias: Toplevel = Toplevel()
    janelaCalorias.title('Calculadora de Calorias')
    janelaCalorias.geometry('450x250')
    janelaCalorias.configure(background='darkgray')

    f4 = Frame(janelaCalorias, height='200', width='400').place(x='25', y='25')
    caloriasTitulo = Label(janelaCalorias, text='Calculadora de Calorias', font='Arial 20 bold').place(relx=0.5, rely=0.2, anchor=CENTER)
    l2 = Label(janelaCalorias, text='Insira Quantas Calorias Foram Consumidas\n'
                                    'em Cada Refeição', font='Arial 10').place(relx=0.5, rely=0.32, anchor=CENTER)

    CM = Label(janelaCalorias, text='Café da manhã:')
    CM.place(relx=0.16, rely=0.45, anchor=CENTER)
    CM = Entry(janelaCalorias, width=15)
    CM.place(relx=0.39, rely=0.46, anchor=CENTER)

    LM = Label(janelaCalorias, text='Lanche Matutino:')
    LM.place(relx=0.17, rely=0.53, anchor=CENTER)
    LM = Entry(janelaCalorias, width=15)
    LM.place(relx=0.39, rely=0.55, anchor=CENTER)

    A = Label(janelaCalorias, text='Almoço:')
    A.place(relx=0.12, rely=0.62, anchor=CENTER)
    A = Entry(janelaCalorias, width=15)
    A.place(relx=0.39, rely=0.63, anchor=CENTER)

    CT = Label(janelaCalorias, text='Café da Tarde:')
    CT.place(relx=0.6, rely=0.45, anchor=CENTER)
    CT = Entry(janelaCalorias, width=15)
    CT.place(relx=0.82, rely=0.46, anchor=CENTER)

    J = Label(janelaCalorias, text='Jantar:')
    J.place(relx=0.56, rely=0.53, anchor=CENTER)
    J = Entry(janelaCalorias, width=15)
    J.place(relx=0.82, rely=0.55, anchor=CENTER)

    C = Label(janelaCalorias, text='Ceia:')
    C.place(relx=0.54, rely=0.62, anchor=CENTER)
    C = Entry(janelaCalorias, width=15)
    C.place(relx=0.82, rely=0.63, anchor=CENTER)

    resultadoCalorias = Label(janelaCalorias, text='')
    resultadoCalorias.grid(row=7, column=1)

    def calcularCalorias():
        Calorias = round(
            float(CM.get()) + float(LM.get()) + float(A.get()) + float(CT.get()) + float(J.get()) + float(C.get()))
        try:
            resultadoCalorias['text'] = f'Você Consumiu {Calorias}'
        except ValueError:
            resultadoCalorias['text'] = f'Insira Valores Válidos'


    Comparacao=Label(janelaCalorias, text='')
    # Botão calculo de calorias
    Cal = Button(janelaCalorias, text='Calcular', command=calcularCalorias)
    Cal.place(relx=0.4, rely=0.78, anchor=CENTER)
    voltarCalorias = Button(janelaCalorias, text="Voltar", command=janelaCalorias.destroy)
    voltarCalorias.place(relx=0.6, rely=0.78, anchor=CENTER)

    resultadoCalorias = Label(janelaCalorias, text='')
    resultadoCalorias.place(relx=0.2, rely=0.78, anchor=CENTER)

def fecharPrograma():
    janela.destroy()


# menuWindow
janela = Tk()
janela.title('Balança Geral')
janela.geometry('450x250')
janela.configure(bg='darkgray')
# frameOne
f1 = Frame(height='200', width='400').place(x='25', y='25')
l0 = Label(f1, text='Balança Geral', font='Arial 20 bold').place(relx=0.5, rely=0.2, anchor=CENTER)
desc = Label(f1, text='Insira seu Nome para Continuar', font='Arial 11').place(relx=0.5, rely=0.4, anchor=CENTER)
nome = Entry(f1, width=20).place(relx=0.5, rely=0.6, anchor=CENTER)


def MENU():
    menu = Tk()
    menu.geometry('450x250')
    menu.configure(background='darkgray')
    menu.title('Balança Geral')
    f5 = Frame(menu, height='200', width='400').place(x='25', y='25')
    l7 = Label(menu, text='Balança Geral', font='Arial 20 bold').place(relx=0.5, rely=0.2, anchor=CENTER)
    l1 = Label(menu, text='Selecione o Ramal Desejado', font='Arial 13').place(relx=0.5, rely=0.35, anchor=CENTER)
    # buttonsMenuWindow
    IMC = Button(menu, text='Calculadora de IMC', command=abrirCalcularIMC).place(relx=0.2, rely=0.55, anchor=CENTER)
    TMB = Button(menu, text='Calculadora de TMB', command=abrirCalcularTMB).place(relx=0.5, rely=0.55, anchor=CENTER)
    Cal = Button(menu, text=' Calcular  Calorias ', command=abrirCalcualrCAlorias).place(relx=0.8, rely=0.55, anchor=CENTER)
    End = Button(menu, text=' Voltar ', command=menu.destroy).place(relx=0.5, rely=0.75, anchor=CENTER)

contButton = Button(f1, text='Continuar', command=MENU).place(relx=0.4, rely=0.8, anchor=CENTER)
END = Button(f1, text=' Encerrar ', command=janela.destroy).place(relx=0.6, rely=0.8, anchor=CENTER)

janela.mainloop()
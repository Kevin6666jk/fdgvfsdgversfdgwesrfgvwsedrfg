import tkinter as tk

def adicionar_ao_visor(valor):
    """Adiciona um valor (dígito ou operador) ao visor da calculadora."""
    visor.insert(tk.END, valor)

def limpar_visor():
    """Limpa o visor da calculadora."""
    visor.delete(0, tk.END)

def calcular():
    """Avalia a expressão no visor e exibe o resultado."""
    try:
        # A função eval() é usada para calcular o resultado da string no visor.
        resultado = eval(visor.get())
        limpar_visor()
        visor.insert(0, str(resultado))
    except (SyntaxError, NameError, ZeroDivisionError):
        # Captura erros comuns de cálculo e exibe uma mensagem.
        limpar_visor()
        visor.insert(0, "Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# O visor (Entry) onde os números e resultados serão exibidos
visor = tk.Entry(janela, width=25, borderwidth=5, font=('Arial', 14))
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definição dos botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

# Criação dos botões usando um loop
for (texto, linha, coluna) in botoes:
    # A função lambda é usada para passar o valor do botão para a função
    # adicionar_ao_visor sem executá-la imediatamente.
    botao = tk.Button(janela, text=texto, padx=20, pady=10,
                      command=lambda texto=texto: adicionar_ao_visor(texto))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de igual (=) para calcular o resultado
botao_igual = tk.Button(janela, text='=', padx=40, pady=10, command=calcular)
botao_igual.grid(row=4, column=2, padx=5, pady=5)

# Botão de limpar (C)
botao_limpar = tk.Button(janela, text='C', padx=20, pady=10, command=limpar_visor)
botao_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()
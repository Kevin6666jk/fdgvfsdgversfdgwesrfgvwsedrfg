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
        resultado = eval(visor.get())
        limpar_visor()
        visor.insert(0, str(resultado))
    except (SyntaxError, NameError, ZeroDivisionError):
        limpar_visor()
        visor.insert(0, "Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# --- Adicionando um rótulo de texto (Label) ---
# O widget Label é usado para exibir texto estático na janela.
rotulo = tk.Label(janela, text="Calculadora Simples", font=('Arial', 16, 'bold'))
# O 'sticky="ew"' faz com que o rótulo se expanda para preencher a largura da célula.
rotulo.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="ew")
# --- Fim da adição do rótulo ---

# O visor (Entry) agora está na linha 1
visor = tk.Entry(janela, width=25, borderwidth=5, font=('Arial', 14))
visor.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Definição dos botões da calculadora
botoes = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 3)
]

# Criação dos botões usando um loop
for (texto, linha, coluna) in botoes:
    botao = tk.Button(janela, text=texto, padx=20, pady=10,
                      command=lambda texto=texto: adicionar_ao_visor(texto))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de igual (=)
botao_igual = tk.Button(janela, text='=', padx=40, pady=10, command=calcular)
botao_igual.grid(row=5, column=2, padx=5, pady=5)

# Botão de limpar (C)
botao_limpar = tk.Button(janela, text='C', padx=20, pady=10, command=limpar_visor)
botao_limpar.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()

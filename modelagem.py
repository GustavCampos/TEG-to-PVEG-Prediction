import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa a classe messagebox para exibir mensagens de erro

# Funções de cálculo
def usina_termoeletrica(energia_kwh):
    # Calcula a quantidade de madeira necessária para uma usina termoelétrica com base na energia em kWh
    eficiencia_termica = 0.30
    poder_calorifico_madeira = 18
    energia_mj = energia_kwh * 3.6
    madeira_kg = energia_mj / (poder_calorifico_madeira * eficiencia_termica)
    return madeira_kg

def paineis_solares(energia_kwh):
    eficiencia_solar = 0.209
    radiacao_solar_media = 1000
    horas_sol = 11
    energia_diaria = energia_kwh / horas_sol
    energia_watts = energia_diaria * 1000
    area_m2 = energia_watts / (radiacao_solar_media * eficiencia_solar * horas_sol)
    return area_m2

def poluicao_termoeletrica(energia_kwh):
    # Calcula a emissão de CO2 associada à geração de energia em kWh
    emissao_co2_kg_por_kwh = 0.85
    emissao_co2_total = energia_kwh * emissao_co2_kg_por_kwh
    return emissao_co2_total

# Funções da interface gráfica
def calcular():
    # Função chamada ao clicar no botão "Calcular"
    try:
        energia_desejada = float(entrada_energia.get())  # Obtém o valor inserido pelo usuário

        # Imprimir dados da base utilizada
        imprimir_dados_base()

        # Calcula os resultados com base na energia desejada
        madeira_necessaria = usina_termoeletrica(energia_desejada)
        paineis_necessarios = paineis_solares(energia_desejada)
        emissao_co2 = poluicao_termoeletrica(energia_desejada)

        # Define o texto a ser exibido no resultado
        resultado_texto.set("Para gerar {} kWh de energia:\n"
                            "- Seria necessária a queima de aproximadamente {:.2f} kg de madeira.\n"
                            "- Seriam necessários aproximadamente {:.2f} metros quadrados de painéis solares.\n"
                            "- A emissão de CO2 seria de aproximadamente {:.2f} kg.".format(
            energia_desejada, madeira_necessaria, paineis_necessarios, emissao_co2))

    except ValueError:
        # Exibe uma mensagem de erro se o valor inserido não for um número
        messagebox.showerror("Erro", "Por favor, insira um valor válido para a energia desejada.")

def limpar():
    # Limpa a entrada de energia e os resultados
    entrada_energia.delete(0, tk.END)
    resultado_texto.set("")
    resultado_dados_base.set("")

def fechar_janela():
    # Fecha a janela principal
    root.destroy()

# Função para imprimir dados da base utilizada
def imprimir_dados_base():
    # Define e exibe os dados da base utilizada
    dados_base_texto = "Dados da base utilizada:\n" \
                       "- Eficiência térmica da usina termoelétrica: 30%\n" \
                       "- Poder calorífico da madeira: 18 MJ/kg\n" \
                       "- Eficiência solar dos painéis: 15%\n" \
                       "- Radiação solar média: 1000 W/m²\n" \
                       "- Horas de sol por dia: 5\n" \
                       "- Emissão de CO2 por kWh: 0.85 kg/kWh"

    resultado_dados_base.set(dados_base_texto)

# Configuração da interface gráfica
root = tk.Tk()  # Cria a janela principal
root.title("Calculadora de Energia")  # Define o título da janela

frame = tk.Frame(root, bg="lightgrey")  # Cria um frame dentro da janela principal
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  # Expande e preenche o frame na janela principal

# Cria e posiciona os elementos na interface
tk.Label(frame, text="Insira a quantidade de energia desejada (kWh):", font=("Arial", 12)).pack()  # Cria um rótulo

# Entrada de energia com texto centralizado
entrada_energia = tk.Entry(frame, font=("Arial", 12), justify="center")
entrada_energia.pack(fill=tk.X)

# Botão "Calcular"
botao_calcular = tk.Button(frame, text="Calcular", command=calcular, font=("Arial", 12))
botao_calcular.pack(pady=10)

# Labels para exibir os resultados e os dados da base utilizada
resultado_dados_base = tk.StringVar()
dados_base_label = tk.Label(frame, textvariable=resultado_dados_base, wraplength=380, justify="left", font=("Arial", 12))
dados_base_label.pack(fill=tk.BOTH, expand=True)

resultado_texto = tk.StringVar()
resultado_label = tk.Label(frame, textvariable=resultado_texto, wraplength=380, justify="left", font=("Arial", 12))
resultado_label.pack(fill=tk.BOTH, expand=True)

# Novo frame para agrupar os botões "Limpar" e "Fechar"
frame_botoes = tk.Frame(frame, bg="lightgrey")
frame_botoes.pack()

# Botão "Limpar"
botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar, font=("Arial", 12))
botao_limpar.pack(side=tk.LEFT, padx=5, pady=10)

# Botão "Fechar"
botao_fechar = tk.Button(frame_botoes, text="Fechar", command=fechar_janela, font=("Arial", 12))
botao_fechar.pack(side=tk.LEFT, padx=5, pady=10)

root.mainloop()  # Inicia o loop principal da interface gráfica

import tkinter as tk
from tkinter import messagebox

# Funções de cálculo

def usina_termoeletrica(energia_kwh):
    eficiencia_termica = 0.30
    poder_calorifico_madeira = 18
    energia_mj = energia_kwh * 3.6
    madeira_kg = energia_mj / (poder_calorifico_madeira * eficiencia_termica)
    return madeira_kg

def paineis_solares(energia_kwh):
    eficiencia_solar = 0.15
    radiacao_solar_media = 1000
    horas_sol = 5
    energia_diaria = energia_kwh / horas_sol
    energia_watts = energia_diaria * 1000
    area_m2 = energia_watts / (radiacao_solar_media * eficiencia_solar * horas_sol)
    return area_m2

def poluicao_termoeletrica(energia_kwh):
    emissao_co2_kg_por_kwh = 0.85
    emissao_co2_total = energia_kwh * emissao_co2_kg_por_kwh
    return emissao_co2_total

# Funções da interface gráfica

def calcular():
    try:
        energia_desejada = float(entrada_energia.get())

        # Imprimir dados da base utilizada
        imprimir_dados_base()

        madeira_necessaria = usina_termoeletrica(energia_desejada)
        paineis_necessarios = paineis_solares(energia_desejada)
        emissao_co2 = poluicao_termoeletrica(energia_desejada)

        resultado_texto.set("Para gerar {} kWh de energia:\n"
                            "- Seria necessária a queima de aproximadamente {:.2f} kg de madeira.\n"
                            "- Seriam necessários aproximadamente {:.2f} metros quadrados de painéis solares.\n"
                            "- A emissão de CO2 seria de aproximadamente {:.2f} kg.".format(
            energia_desejada, madeira_necessaria, paineis_necessarios, emissao_co2))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para a energia desejada.")

def limpar():
    entrada_energia.delete(0, tk.END)
    resultado_texto.set("")
    resultado_dados_base.set("")

def fechar_janela():
    root.destroy()  # Fecha a janela principal

# Função para imprimir dados da base utilizada
def imprimir_dados_base():
    dados_base_texto = "Dados da base utilizada:\n" \
                       "- Eficiência térmica da usina termoelétrica: 30%\n" \
                       "- Poder calorífico da madeira: 18 MJ/kg\n" \
                       "- Eficiência solar dos painéis: 15%\n" \
                       "- Radiação solar média: 1000 W/m²\n" \
                       "- Horas de sol por dia: 5\n" \
                       "- Emissão de CO2 por kWh: 0.85 kg/kWh"

    resultado_dados_base.set(dados_base_texto)

# Configuração da interface gráfica

root = tk.Tk()
root.title("Calculadora de Energia")

frame = tk.Frame(root, bg="lightgrey")
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

tk.Label(frame, text="Insira a quantidade de energia desejada (kWh):", font=("Arial", 12)).pack()

# Entrada de energia com texto centralizado
entrada_energia = tk.Entry(frame, font=("Arial", 12), justify="center")
entrada_energia.pack(fill=tk.X)

botao_calcular = tk.Button(frame, text="Calcular", command=calcular, font=("Arial", 12))
botao_calcular.pack(pady=10)

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

root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Função para calcular os resultados com base na quantidade de energia desejada
def calcular():
    try:
        # Obtendo a quantidade de energia desejada do campo de entrada e convertendo para float
        energia_desejada = float(entrada_energia.get())

        # Chamando as funções para calcular os resultados com base na energia desejada
        madeira_necessaria = usina_termoeletrica(energia_desejada)
        paineis_necessarios = paineis_solares(energia_desejada)
        emissao_co2 = poluicao_termoeletrica(energia_desejada)

        # Exibindo os resultados na interface gráfica
        resultado_texto.set("Para gerar {} kWh de energia:\n"
                            "- Seriam necessários aproximadamente {:.2f} kg de madeira na usina termoelétrica.\n"
                            "- Seriam necessários aproximadamente {:.2f} metros quadrados de painéis solares.\n"
                            "- A emissão de CO2 seria de aproximadamente {:.2f} kg.".format(
            energia_desejada, madeira_necessaria, paineis_necessarios, emissao_co2))
    except ValueError:
        # Exibindo uma mensagem de erro se o valor inserido não puder ser convertido para float
        messagebox.showerror("Erro", "Por favor, insira um valor válido para a energia desejada.")

# Função para calcular a quantidade de madeira necessária na usina termoelétrica
def usina_termoeletrica(energia_kwh):
    # Estimativas de eficiência e poder calorífico da madeira
    eficiencia_termica = 0.30  # Eficiência de conversão térmica da usina termoelétrica
    poder_calorifico_madeira = 18  # Poder calorífico da madeira em MJ/kg

    # Calculando a quantidade de madeira necessária
    energia_mj = energia_kwh * 3.6  # Convertendo kWh para MJ
    madeira_kg = energia_mj / (poder_calorifico_madeira * eficiencia_termica)

    return madeira_kg

# Função para calcular a quantidade de painéis solares necessários
def paineis_solares(energia_kwh):
    # Estimativas de eficiência e radiação solar média
    eficiencia_solar = 0.15  # Eficiência dos painéis solares
    radiacao_solar_media = 1000  # Radiação solar média em W/m²
    horas_sol = 5  # Horas de sol por dia

    # Calculando a área de painéis solares necessária
    energia_diaria = energia_kwh / horas_sol  # kWh por hora
    energia_watts = energia_diaria * 1000  # Convertendo kWh para watts
    area_m2 = energia_watts / (radiacao_solar_media * eficiencia_solar * horas_sol)

    return area_m2

# Função para calcular a emissão de CO2 na usina termoelétrica
def poluicao_termoeletrica(energia_kwh):
    # Emissão de CO2 por kWh de energia gerada em uma usina termoelétrica
    emissao_co2_kg_por_kwh = 0.85  # Estimativa de emissão de CO2 em kg/kWh

    # Calculando a emissão total de CO2
    emissao_co2_total = energia_kwh * emissao_co2_kg_por_kwh

    return emissao_co2_total

# Configurando a interface gráfica
root = tk.Tk()
root.title("Calculadora de Energia")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Label e campo de entrada para a quantidade de energia desejada
tk.Label(frame, text="Insira a quantidade de energia desejada (kWh):").pack()
entrada_energia = tk.Entry(frame)
entrada_energia.pack()

# Botão para calcular os resultados
botao_calcular = tk.Button(frame, text="Calcular", command=calcular)
botao_calcular.pack(pady=10)

# Variável para armazenar o texto do resultado e label para exibi-lo
resultado_texto = tk.StringVar()
resultado_label = tk.Label(frame, textvariable=resultado_texto, wraplength=400)
resultado_label.pack()

# Iniciando o loop principal da interface gráfica
root.mainloop()

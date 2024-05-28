# Suposicoes assumidas:
# Operação em estado estacionário.
# Distribuição uniforme de temperatura na câmara de combustão.
# Propriedades conhecidas do combustível de biomassa (por exemplo, valor calorífico, teor de umidade).

class CamaraCombustao():
    def __init__(self, 
                 fluxo_de_massa: float, 
                 valor_calorifico: float, 
                 eficiencia: float) -> None:
        # Taxa de fluxo de massa da biomassa (kg/s)
        self.fluxo_de_massa = fluxo_de_massa
        
        # Valor calorífico da biomassa (J/kg)
        self.valor_calorifico = valor_calorifico
        
        # Eficiência térmica da câmara de combustão
        # Quanto do calor é transferido para o modulo termoeletrico
        self.eficiencia = eficiencia
        
    def calcular_calor_gerado(self) -> float:
        # Calor gerado na câmara de combustão (W)
        calor_gerado = self.fluxo_de_massa * self.valor_calorifico
        return calor_gerado
    
    def calcular_calor_transferido(self) -> float:
        # Calor transferido para o modulo termoeletrico (W)
        calor_transferido = self.eficiencia * self.calcular_calor_gerado()
        return calor_transferido

class TrocadorDeCalor():
    pass

class ModuloTermoeletrico():
    def __init__(self, eficiencia: float) -> None:
        self.eficiencia = eficiencia
        
    def calcular_energia_gerada(self, calor_transferido: float, n_modulos: int) -> float:
        # Energia gerada pelo módulo termoelétrico (W)
        energia_gerada = self.eficiencia * calor_transferido * n_modulos
        return energia_gerada

class MecanismoDeRefrigeracao():
    pass
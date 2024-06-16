# Retorna a quantidade de madeira necessária para gerar a energia desejada
def calc_consume_amount(energy_kwh: float, 
                        thermal_efficiency: float, 
                        calorific_power: float) -> float:
    
    energy_megajoule = energy_kwh * 3.6
    return energy_megajoule / (calorific_power * thermal_efficiency)

# Retorna a área necessária de painéis solares necessários para gerar a energia desejada
def calc_solar_area(energy_kwh: float,
                    solar_efficiency: float,
                    mean_solar_radiation: float,
                    exposion_hours: float) -> float:
    
    daily_energy = energy_kwh / exposion_hours
    daily_energy_in_watts = daily_energy * 1000
    
    return daily_energy_in_watts / (mean_solar_radiation * solar_efficiency * exposion_hours)

# Retorna a quantidade de CO2 emitida para gerar a energia desejada
def calc_teg_polution(energy_kwh: float, emission_rate: float) -> float:
    return energy_kwh * emission_rate
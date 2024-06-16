THERMAL_EFFICIENCY = 0.30
CALORIFIC_POWER = 18

SOLAR_EFFICIENCY = 0.15
MEAN_SOLAR_RADIATION = 1000
EXPOSION_HOURS = 5

# Kg de CO2 emitidos por kWh
CO2_EMISSION_RATE = 0.85

# Moudule SAPM variables
SAPM_MODULES = [
    {
        "module": "vidro/vidro",
        "mounting": "rack aberto",
        "a": -3.47,
        "b": -0.0594,
        "delta_t": 3   
    },{
        "module": "vidro/vidro",
        "mounting": "telhado fechado",
        "a": -2.98,
        "b": -0.0471,
        "delta_t": 1
    },{
        "module": "vidro/polímero",
        "mounting": "rack aberto",
        "a": -3.56,
        "b": -0.075,
        "delta_t": 3
    },{
        "module": "vidro/polímero",
        "mounting": "traseira isolada",
        "a": -2.81,
        "b": -0.0455,
        "delta_t": 0
    }
]

# Base panel variables (BYD MGK-36 MONOFACIAL 455W)
REFERENCE_MODULE = {
    "TEMPERATURE_COEFFICIENT": -0.0038, # -0.38%/°C
    "REFERENCE_TEMPERATURE": 25,
    "SINGLE_PANEL_AREA": 1.6,
    "EFFICIENCY": 0.209,    
}

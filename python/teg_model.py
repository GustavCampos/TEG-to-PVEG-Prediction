from datetime import datetime


def predict_biomass_amount(
    required_kwh_energy: float,
    date_range: tuple,
    daily_work_hours: float,
    module_quantity: int,
    module_efficiency: float,
    heat_transfer_efficiency: float,
    biomass_calorific_power: float
    ) -> dict:

    date_model = "%Y-%m-%d"
    start_date = datetime.strptime(date_range[0], date_model)
    end_date = datetime.strptime(date_range[1], date_model)
    
    days_of_work = (end_date - start_date).days
    
    total_work_hours = daily_work_hours * days_of_work
    
    # Variable in watts
    power_ouput = (required_kwh_energy / total_work_hours) * 1e3
    
    module_heat = power_ouput / (module_efficiency * module_quantity)
    
    combustion_heat = module_heat / heat_transfer_efficiency
    
    hourly_biomass = combustion_heat / biomass_calorific_power
    
    return {
        "total_kg_biomass": hourly_biomass * total_work_hours,
        "total_work_hours": total_work_hours,
        "hourly_kwh_power_output": power_ouput / 1e3,
        "module_heat": module_heat,
        "combustion_heat": combustion_heat,
        "hourly_biomass": hourly_biomass
    }
from datetime import datetime


def predict_biomass_amount(
        required_kwh_energy: float,
        date_range: tuple,
        daily_work_hours: float,
        module_quantity: int,
        module_efficiency: float,
        heat_transfer_efficiency: float,
        mjkg_biomass_calorific_power: float
        ) -> dict:

    date_model = "%Y-%m-%d"
    start_date = datetime.strptime(date_range[0], date_model)
    end_date = datetime.strptime(date_range[1], date_model)
    
    days_of_work = (end_date - start_date).days
    
    total_work_hours = daily_work_hours * days_of_work
    
    # Power output in Mj
    power_ouput = (required_kwh_energy / total_work_hours) * 3.6
    
    module_heat = power_ouput / (module_efficiency * module_quantity)
    
    combustion_heat = module_heat / heat_transfer_efficiency
    
    # Convert biomass Mj to joules
    hourly_biomass = combustion_heat / (mjkg_biomass_calorific_power)
    
    return {
        "total_kg_biomass": hourly_biomass * total_work_hours,
        "total_work_hours": total_work_hours,
        "hourly_kwh_power_output": power_ouput / 3.6,
        "module_heat": module_heat,
        "combustion_heat": combustion_heat,
        "hourly_biomass": hourly_biomass
    }
    
def predict_co2_emission(
        biomass_kg_amount: float,
        carbon_content: float,
        ) -> float:
    
    conversion_rate = 44 / 12
    
    return biomass_kg_amount * carbon_content * conversion_rate

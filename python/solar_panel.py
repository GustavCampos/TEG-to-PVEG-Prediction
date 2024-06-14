import pvlib
import pandas as pd
from constants import REFERENCE_MODULE


def calc_power_output(irradiation, temperature) -> float | list[float]:
    return_value = []
    
    try:
        for irr, tp in zip(irradiation, temperature):
            return_value.append(calc_power_output(irr, tp))
        
        return return_value
    except TypeError:
        efficiency = REFERENCE_MODULE['EFFICIENCY']
        temp_coefficient = REFERENCE_MODULE['TEMPERATURE_COEFFICIENT']
        reference_temp = REFERENCE_MODULE['REFERENCE_TEMPERATURE']
        panel_area = REFERENCE_MODULE['SINGLE_PANEL_AREA']
        
        delta_temp = temperature - reference_temp
        
        real_efficiency = efficiency * (1 + (temp_coefficient * delta_temp))
        
        return irradiation * panel_area * real_efficiency

def predict_panel_area(
        required_kwh_energy: float,
        start_date: str,
        end_date: str,
        surface_tilt: float,
        surface_azimuth: float,
        latitude: float,
        longitude: float,
        altitude: float,
        timezone: str,
        sapm_values: dict,
    ) -> float:
    
    location = pvlib.location.Location(latitude, longitude, timezone, altitude)

    # Define the time range
    times = pd.date_range(start_date, end_date, freq='h', tz=location.tz)
    
    # Calculate the solar position and clear-sky props
    solar_position = location.get_solarposition(times)
    clear_sky_props = location.get_clearsky(times)

    # Calculate the irradiance
    poa_irradiance = pvlib.irradiance.get_total_irradiance(
        surface_tilt=surface_tilt,
        surface_azimuth=surface_azimuth,
        dni=clear_sky_props["dni"],
        ghi=clear_sky_props["ghi"],
        dhi=clear_sky_props["dhi"],
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth']
    )['poa_global']

    # Get cell temperature for every checkpoint
    cell_temperature = pvlib.temperature.sapm_cell(
        poa_irradiance, 25, 1, sapm_values['a'], sapm_values['b'], sapm_values['delta_t']
    )

    power_output = calc_power_output(poa_irradiance, cell_temperature)
    
    print(power_output)

    # Calculate total energy output (kWh)
    total_energy_output = sum(power_output) * 1e-3  # convert W to kW

    # Calculate the required panel area
    panel_area = (required_kwh_energy / total_energy_output) * REFERENCE_MODULE['SINGLE_PANEL_AREA']

    return panel_area

import json
from math import ceil
from dotenv import dotenv_values
from flask import Flask, render_template, request

# "Autoral" code
import python.constants as CONSTANTS
from python.teg_model import predict_biomass_amount, predict_co2_emission
from python.solar_panel import predict_panel_area, get_sapm_modules, get_sapm_module


CONFIG = dotenv_values(".env")
app = Flask(__name__)

@app.route('/')
def load_index():
    sapm_modules = get_sapm_modules()
    
    return render_template("index.html",
        th_eff=CONSTANTS.THERMAL_EFFICIENCY,
        cal_pow=CONSTANTS.CALORIFIC_POWER,
        co2_emm_rat=CONSTANTS.CO2_EMISSION_RATE,
        sapm_modules=sapm_modules,
    )
    
@app.route("/calculate_analysis/", methods=["POST"])
def calculate_analysis():    
    try:    
        # TEG prediction ______________________________________________________       
        biomass_dict =  predict_biomass_amount(
            required_kwh_energy=float(request.form["wanted-energy"]),
            date_range=(request.form["start-date"], request.form["end-date"]),
            daily_work_hours=float(request.form["daily-work-hours"]),
            cicle_efficiency=float(request.form["cicle-efficiency"]),
            heat_transfer_efficiency=float(request.form["heat-transfer-efficiency"]),
            mjkg_biomass_calorific_power=float(request.form["calorific-power"])
        )
        
        co2_emittted = predict_co2_emission(
            biomass_kg_amount=biomass_dict["total_kg_biomass"],
            carbon_content=float(request.form["carbon-content"])
        )
        
        total_total_kwh_power_output = biomass_dict["hourly_kwh_power_output"] * biomass_dict["total_work_hours"]
        
        # PVEG Prediction _____________________________________________________
        module = get_sapm_module(request.form["panel-module"])
                
        pvpanel_dict = predict_panel_area(
            required_kwh_energy=float(request.form["wanted-energy"]),
            date_range=(request.form["start-date"], request.form["end-date"]),
            surface_tilt=float(request.form["surface-tilt"]),
            surface_azimuth=float(request.form["surface-azimuth"]),
            sapm_values=module,
            latitude=float(request.form["latitude"]),
            longitude=float(request.form["longitude"]),
            altitude=float(request.form["altitude"]),
        )
        
        aprox_panel_number = ceil(pvpanel_dict['total_area'] / CONSTANTS.REFERENCE_MODULE['SINGLE_PANEL_AREA'])
        total_panel_output = (pvpanel_dict['total_kWh_output'] * aprox_panel_number)
        pvpanel_co2_emission = (CONSTANTS.REFERENCE_MODULE['CO2_EMISSION'] * total_panel_output)
        
        # Response ____________________________________________________________
        response_json = {
            "wanted_kWh_energy": float(request.form["wanted-energy"]),
            "date_range": {
                "start": request.form["start-date"],
                "end": request.form["end-date"]
            },
            "teg": {
                "emitted_kg_co2_amount": co2_emittted,
                "total_kg_biomass": biomass_dict['total_kg_biomass'],  
                "hourly_biomass": biomass_dict['hourly_biomass'],
                "hourly_kwh_power_output": biomass_dict['hourly_kwh_power_output'],
                "total_kwh_power_output": total_total_kwh_power_output,
                "total_work_hours": biomass_dict["total_work_hours"],
                "boiler_heat": biomass_dict["boiler_heat"],
                "combustion_heat": biomass_dict["combustion_heat"],
            },
            "pvpanel": {
                "module": CONSTANTS.REFERENCE_MODULE,
                "total_kWh_output_per_panel": pvpanel_dict['total_kWh_output'],
                "total_area": pvpanel_dict['total_area'],
                "single_panel_area": pvpanel_dict['panel_area'],
                "aprox_panel_number": aprox_panel_number,
                "total_kWh_output": total_panel_output,
                "emitted_kg_co2_amount": pvpanel_co2_emission,
                "hourly_data": {
                    "wh_output": pvpanel_dict["wh_output"],
                    "cell_temperature": pvpanel_dict["cell_temperature"],
                },
            },
        }
        
        request_dict = request.form.to_dict()
        
        return render_template("/analysis_result/index.html",
            result_dict=response_json,
            request_dict=request_dict,
            response_json=json.dumps(response_json, indent=4),
            request_json=json.dumps(request_dict, indent=4),
        )
        
    except Exception as e:
        print(e)
        print(e.args)
        
        return json.dumps({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
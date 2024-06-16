import json
from dotenv import dotenv_values
from flask import Flask, render_template, request

# "Autoral" code
import python.constants as CONSTANTS
import python.calc_functions as calc
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

@app.route("/api/calculate_analisis/", methods=["POST"])
def calculate_analisis():
    try:       
        biomass_dict =  predict_biomass_amount(
            required_kwh_energy=float(request.form["wanted-energy"]),
            date_range=(request.form["start-date"], request.form["end-date"]),
            daily_work_hours=float(request.form["daily-work-hours"]),
            module_quantity=int(request.form["module-quantity"]),
            module_efficiency=float(request.form["module-efficiency"]),
            heat_transfer_efficiency=float(request.form["heat-transfer-efficiency"]),
            mjkg_biomass_calorific_power=float(request.form["calorific-power"])
        )
        
        co2_emittted = predict_co2_emission(
            biomass_kg_amount=biomass_dict["total_kg_biomass"],
            carbon_content=float(request.form["carbon-content"])
        )
        
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
        
        
        return json.dumps({
            "wanted-kWh-energy": request.form["wanted-energy"],
            "date-range": {
                "start": request.form["start-date"],
                "end": request.form["end-date"]
            },
            "teg": {
                "emitted_kg_co2_amount": co2_emittted,
                "total-kg-biomass": biomass_dict['total_kg_biomass'],  
                "hourly_biomass": biomass_dict['hourly_biomass'],
                "hourly_kwh_power_output": biomass_dict['hourly_kwh_power_output'],
                "total_work_hours": biomass_dict["total_work_hours"],
                "module_heat": biomass_dict["module_heat"],
                "combustion_heat": biomass_dict["combustion_heat"],
            },
            "pvpanel": {
                "total-kWh-output": pvpanel_dict['total_kWh_output'],
                "single-panel-area": pvpanel_dict['panel_area'],
                "total-area": pvpanel_dict['total_area'],
            },
        })
    except Exception as e:
        print(e)
        print(e.args)
        
        return json.dumps({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
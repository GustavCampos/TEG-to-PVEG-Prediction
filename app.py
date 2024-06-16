import json
from dotenv import dotenv_values
from flask import Flask, render_template, request

# "Autoral" code
import python.constants as CONSTANTS
import python.calc_functions as calc
from python.solar_panel import predict_panel_area


CONFIG = dotenv_values(".env")
app = Flask(__name__)

@app.route('/')
def load_index():
    sapm_modules = map(lambda n: f"{n['module']} - {n['mounting']}", CONSTANTS.SAPM_MODULES)
    
    return render_template("index.html",
        th_eff=CONSTANTS.THERMAL_EFFICIENCY,
        cal_pow=CONSTANTS.CALORIFIC_POWER,
        co2_emm_rat=CONSTANTS.CO2_EMISSION_RATE,
        sapm_modules=sapm_modules,
    )

@app.route("/api/calculate_analisis/", methods=["POST"])
def calculate_analisis():
    try:
        kg_wood_needed = calc.calc_consume_amount(
            energy_kwh=float(request.form["wanted_energy"]),
            thermal_efficiency=float(request.form["thermal-efficiency"]),
            calorific_power=float(request.form["calorific-power"])
        )
        
        teg_polution = calc.calc_teg_polution(
            energy_kwh=float(request.form["wanted_energy"]),
            emission_rate=float(request.form["co2-emission-rate"])
        )
        
        sapm_module = CONSTANTS.SAPM_MODULES[0]
        
        pvpanel_dict = predict_panel_area(
            required_kwh_energy=float(request.form["wanted_energy"]),
            date_range=(request.form["start-date"], request.form["end-date"]),
            surface_tilt=float(request.form["surface-tilt"]),
            surface_azimuth=float(request.form["surface-azimuth"]),
            sapm_values=sapm_module,
            latitude=float(request.form["latitude"]),
            longitude=float(request.form["longitude"]),
            altitude=float(request.form["altitude"]),
        )
        
        
        return json.dumps({
            "date-range": {
                "start": request.form["start-date"],
                "end": request.form["end-date"]
            },
            "wanted-kWh-energy": request.form["wanted_energy"],
            "wood-kg-needed": f"{kg_wood_needed:.4f}",
            "teg-polution": f"{teg_polution:.4f}",
            "pvpanel": {
                "total-kWh-output": f"{pvpanel_dict['total_kWh_output']:.4f}",
                "single-panel-area": f"{pvpanel_dict['panel_area']:.4f}",
                "total-area": f"{pvpanel_dict['total_area']:.4f}",
            },
        })
    except Exception as e:
        return json.dumps({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
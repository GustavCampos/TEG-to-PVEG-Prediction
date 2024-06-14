from flask import Flask, render_template, request
import json

# "Autoral" code
import python.constants as CONSTANTS
import python.calc_functions as calc


app = Flask(__name__)

@app.route('/')
def load_index():
    return render_template("index.html",
                           th_eff=CONSTANTS.THERMAL_EFFICIENCY,
                           cal_pow=CONSTANTS.CALORIFIC_POWER,
                           sol_eff=CONSTANTS.SOLAR_EFFICIENCY,
                           me_sol_rad=CONSTANTS.MEAN_SOLAR_RADIATION,
                           exp_hour=CONSTANTS.EXPOSION_HOURS,
                           co2_emm_rat=CONSTANTS.CO2_EMISSION_RATE)

@app.route("/api/calculate_analisis/", methods=["POST"])
def calculate_analisis():
    kg_wood_needed = calc.calc_consume_amount(
        energy_kwh=float(request.form["wanted_energy"]),
        thermal_efficiency=float(request.form["thermal-efficiency"]),
        calorific_power=float(request.form["calorific-power"])
    )
    
    m2_solar_panel = calc.calc_solar_area(
        energy_kwh=float(request.form["wanted_energy"]),
        solar_efficiency=float(request.form["solar-efficiency"]),
        mean_solar_radiation=float(request.form["mean-solar-radiation"]),
        exposion_hours=float(request.form["exposion-hours"])
    )
    
    teg_polution = calc.calc_teg_polution(
        energy_kwh=float(request.form["wanted_energy"]),
        emission_rate=float(request.form["co2-emission-rate"])
    )
    
    return json.dumps({
        "wanted-energy": request.form["wanted_energy"],
        "wood-needed": f"{kg_wood_needed:.4f}",
        "solar-panel-area": f"{m2_solar_panel:.4f}",
        "teg-polution": f"{teg_polution:.4f}"
    })
    
@app.route('/api/users/<int:user_id>')
def return_user(user_id: int):
    return json.dumps({
        "user_id": user_id,
        "user_name": "John Doe"
    })

if __name__ == "__main__":
    app.run(debug=True)
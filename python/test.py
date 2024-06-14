import constants
from solar_panel import predict_panel_area


def main():
    sapm_values = next((
        i for i in constants.SAPM_MODULES if f"{i["module"]} - {i["mounting"]}" == "glass/glass - open_rack"
    ), None)
    
    print(predict_panel_area(
        required_kwh_energy=100,
        start_date="2024-06-06",
        end_date="2024-06-07",
        surface_tilt=20,
        surface_azimuth=180,
        latitude=-28.385370,
        longitude=-53.928020,
        altitude=354,
        timezone="America/Sao_Paulo",
        sapm_values=sapm_values
    ))

if __name__ == "__main__":
    main()
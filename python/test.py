from teg_model import predict_biomass_amount, predict_co2_emission

def main():
    teg = predict_biomass_amount(
        required_kwh_energy=54,
        date_range= ("2024-06-06", "2024-06-7"),
        daily_work_hours=1,
        module_quantity=10,
        module_efficiency=0.05,
        heat_transfer_efficiency=0.6,
        mjkg_biomass_calorific_power=18
    )
    
    print(teg)

    print("\n", predict_co2_emission(
        biomass_kg_amount=1000,
        carbon_content=0.65
    ))

if __name__ == "__main__":
    main()
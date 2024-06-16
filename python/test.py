from teg_model import predict_biomass_amount

def main():
    print(predict_biomass_amount(
        required_kwh_energy=54,
        date_range= ("2024-06-06", "2024-06-7"),
        daily_work_hours=1,
        module_quantity=10,
        module_efficiency=0.05,
        heat_transfer_efficiency=0.6,
        biomass_calorific_power=18e6
    ))

if __name__ == "__main__":
    main()
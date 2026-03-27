from premium_model import (
    calculate_weekly_premium,
    get_weather_disruption,
    get_pollution_disruption,
    get_curfew_disruption
)

if __name__ == "__main__":

    city = "Bhubaneswar"
    zone_risk = 10

    weather_factor = get_weather_disruption(city)
    pollution_factor = get_pollution_disruption(city)
    curfew_factor = get_curfew_disruption()

    total_disruption = weather_factor + pollution_factor + curfew_factor

    premium = calculate_weekly_premium(
        base=50,
        zone_risk=zone_risk,
        disruption_factor=total_disruption
    )

    print(f"City: {city}")
    print(f"Zone Risk: ₹{zone_risk}")
    print(f"Weather Factor: ₹{weather_factor}")
    print(f"Pollution Factor: ₹{pollution_factor}")
    print(f"Curfew Factor: ₹{curfew_factor}")
    print("Weekly Premium:", premium)



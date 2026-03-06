import logging
from premium_model import (
    calculate_weekly_premium,
    get_weather_disruption,
    get_pollution_disruption,
    get_curfew_disruption
)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    city = "Bhubaneswar"
    zone_risk = 10

    weather_factor = get_weather_disruption(city)
    pollution_factor = get_pollution_disruption(city)
    curfew_factor = get_curfew_disruption()

    total_disruption = weather_factor + pollution_factor + curfew_factor
    premium = calculate_weekly_premium(50, zone_risk, total_disruption)

    logging.info(f"City: {city}")
    logging.info(f"Zone Risk: ₹{zone_risk}")
    logging.info(f"Weather Factor: ₹{weather_factor}")
    logging.info(f"Pollution Factor: ₹{pollution_factor}")
    logging.info(f"Curfew Factor: ₹{curfew_factor}")
    logging.info(f"Weekly Premium: ₹{premium}")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--city", default="Bhubaneswar")
parser.add_argument("--zone-risk", type=int, default=10)
args = parser.parse_args()

import csv
with open("premium_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([city, zone_risk, weather_factor, pollution_factor, curfew_factor, premium])




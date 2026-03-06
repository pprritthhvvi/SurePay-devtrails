import csv
from premium_model import calculate_weekly_premium

def run_test_cases():
    scenarios = [
        {"city": "Bhubaneswar", "zone_risk": 10, "weather": 0, "pollution": 0, "curfew": 0},
        {"city": "Bhubaneswar", "zone_risk": 10, "weather": 5, "pollution": 0, "curfew": 0},
        {"city": "Bhubaneswar", "zone_risk": 10, "weather": 15, "pollution": 5, "curfew": 20},
    ]

    with open("premium_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["City", "Zone Risk", "Weather", "Pollution", "Curfew", "Premium"])

        for s in scenarios:
            disruption = s["weather"] + s["pollution"] + s["curfew"]
            premium = calculate_weekly_premium(50, s["zone_risk"], disruption)

            writer.writerow([s["city"], s["zone_risk"], s["weather"], s["pollution"], s["curfew"], premium])
            print(f"Case: {s} → Premium: ₹{premium}")

if __name__ == "__main__":
    run_test_cases()


from rules import run_rules
from semantic_network import build_semantic_network, show_network, analyze_indicator
from net import train_model, predict_rate
from frames import InflationFrame, GDPFrame, RiskFrame

print("=== Гібридна система: правила + графи + фрейми + нейронна мережа ===")

G = build_semantic_network()
show_network(G)

facts = {
    "trend": "up",
    "inflation": "high",
    "oil_price": "up",
    "gdp": "up",
    "unemployment": "high",
    "risk": "high",
    "stocks": "fall",
    "politics": "unstable",
    "exports": "growth",
    "rate_diff": "high"
}
run_rules(facts)

inflation = InflationFrame(name="Inflation", value=75.0, country="Ukraine", unit="PM2.5")
gdp = GDPFrame(name="GDP", value=3.2, country="Ukraine", unit="%")
risk = RiskFrame(name="PoliticalRisk", value=0.8)

print(f"\nФрейми: {inflation}, {gdp}, {risk}")

analyze_indicator(G, "Inflation", "high")
analyze_indicator(G, "GDP", "up")
analyze_indicator(G, "Oil Price", "down")

model = train_model()
input_data = [0.8, 0.7, 0.6]
predict_rate(model, input_data)
from rules import run_rules
from semantic_network import build_semantic_network, show_network, analyze_indicator
from net import train_model, predict_rate

print("\n=== 1) Семантична мережа ===")
G = build_semantic_network()
show_network(G)

print("\n=== 2) Правила ===")
facts = {
    "trend": "up",
    "inflation": "low",
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

print("\n=== Додаткові приклади семантичної мережі ===")
analyze_indicator(G, "Inflation", "high")
analyze_indicator(G, "GDP", "up")
analyze_indicator(G, "Oil Price", "down")

print("\n=== 3) Нейронна мережа ===")
model = train_model()
input_data = [0.2, 0.8, 0.6]
predict_rate(model, input_data)

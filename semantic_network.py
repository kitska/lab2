import networkx as nx

def build_semantic_network():
    G = nx.DiGraph()
    
    nodes = ["USD", "EUR", "GBP", "Inflation", "Interest Rate",
             "GDP", "Risk", "Oil Price", "Exports", "Market Trend",
             "Economic Indicator", "Political Stability", "Stocks", "Commodities"]
    G.add_nodes_from(nodes)

    edges = [
        ("Inflation", "USD", "affects"),
        ("Inflation", "Economic Indicator", "is_a"),
        ("Interest Rate", "USD", "drives"),
        ("Interest Rate", "Economic Indicator", "is_a"),
        ("GDP", "EUR", "supports"),
        ("Risk", "GBP", "reduces"),
        ("Oil Price", "Forex", "influences"),
        ("Exports", "GBP", "improves"),
        ("Market Trend", "USD", "predicts"),
        ("Political Stability", "Forex", "impacts"),
        ("Stocks", "Market Trend", "correlates"),
        ("Commodities", "Forex", "correlates")
    ]
    
    for src, tgt, label in edges:
        G.add_edge(src, tgt, relation=label)
    
    return G

def show_network(G):
    print("\nВузли:", list(G.nodes))
    print("\nЗв’язки:")
    for src, tgt, data in G.edges(data=True):
        print(f"{src} → {tgt} [{data['relation']}]")

# Додатковий метод для демонстрації впливу на валюту
def analyze_indicator(G, indicator, value):
    print(f"\nАналіз за індикатором: {indicator} = {value}")
    if indicator in ["Inflation", "Risk"]:
        print("Висновок: Валюта під тиском")
    elif indicator in ["GDP", "Exports"]:
        print("Висновок: Валюта зміцнюється")
    else:
        print("Висновок: Прогноз не визначений")

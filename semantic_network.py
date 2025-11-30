import networkx as nx

def build_semantic_network():
    G = nx.DiGraph()

    nodes = [
        "USD", "EUR", "GBP", "Inflation", "Interest Rate", "GDP",
        "Risk", "Oil Price", "Exports", "Market Trend", "Forex",
        "Economic Indicator", "Political Stability", "Stocks", "Commodities"
    ]
    G.add_nodes_from(nodes)

    relations = [
        ("Inflation", "USD", "affects"),
        ("Interest Rate", "USD", "drives"),
        ("GDP", "EUR", "supports"),
        ("Risk", "GBP", "reduces"),
        ("Oil Price", "Forex", "influences"),
        ("Exports", "GBP", "improves"),
        ("Political Stability", "Forex", "impacts"),
        ("Stocks", "Market Trend", "correlates"),
        ("Commodities", "Forex", "correlates"),
        ("Market Trend", "USD", "predicts"),
        ("Interest Rate", "Economic Indicator", "is_a"),
        ("Inflation", "Economic Indicator", "is_a"),
    ]

    for a, b, r in relations:
        G.add_edge(a, b, relation=r)

    return G


def show_network(G):
    print("Вузли:", G.nodes())
    print("\nЗв’язки:")
    for u, v, data in G.edges(data=True):
        print(f"{u} → {v} [{data['relation']}]")

from experta import *

class MarketFacts(Fact):
    pass


class FxRuleEngine(KnowledgeEngine):

    @Rule(MarketFacts(trend='up', inflation='low'))
    def rule_1(self):
        print("Правило 1: прогноз – зміцнення валюти")

    @Rule(MarketFacts(trend='down', inflation='high'))
    def rule_2(self):
        print("Правило 2: прогноз – послаблення валюти")

    @Rule(MarketFacts(rate_diff='high'))
    def rule_3(self):
        print("Правило 3: велика різниця ставок → валюта зміцниться")

    @Rule(MarketFacts(oil_price='up'))
    def rule_4(self):
        print("Правило 4: зростання нафти → зміцнення для нафтодобувних країн")

    @Rule(MarketFacts(gdp='up'))
    def rule_5(self):
        print("Правило 5: зростання ВВП → позитив для валюти")

    @Rule(MarketFacts(unemployment='high'))
    def rule_6(self):
        print("Правило 6: високе безробіття → валюта слабшає")

    @Rule(MarketFacts(risk='high'))
    def rule_7(self):
        print("Правило 7: високий ризик → відтік капіталу")

    @Rule(MarketFacts(stocks='fall'))
    def rule_8(self):
        print("Правило 8: падіння фондового ринку → тиск на валюту")

    @Rule(MarketFacts(politics='unstable'))
    def rule_9(self):
        print("Правило 9: політична нестабільність → девальвація")

    @Rule(MarketFacts(exports='growth'))
    def rule_10(self):
        print("Правило 10: ріст експорту → валюта зміцнюється")


def run_rules(example_facts: dict):
    engine = FxRuleEngine()
    engine.reset()
    engine.declare(MarketFacts(**example_facts))
    engine.run()

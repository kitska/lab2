from dataclasses import dataclass

@dataclass
class Indicator:
    name: str
    value: float


@dataclass
class MacroIndicator(Indicator):
    country: str
    unit: str


@dataclass
class InflationFrame(MacroIndicator):
    impact: str = "negative"


@dataclass
class InterestRateFrame(MacroIndicator):
    impact: str = "positive"


@dataclass
class GDPFrame(MacroIndicator):
    impact: str = "positive"


@dataclass
class RiskFrame(Indicator):
    impact: str = "negative"

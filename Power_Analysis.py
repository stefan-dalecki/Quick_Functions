import numpy as np
from statsmodels.stats.power import TTestIndPower

class Power:
    def __init__(self, effect_size, alpha, power):
        self.effect_size = effect_size
        self.alpha = alpha
        self.power = power

    def analysis(self):
        analysis_type = TTestIndPower()
        self.required_size = analysis_type.solve_power(effect_size = self.effect_size, alpha = self.alpha, power = self.power)
        return (f'Required Sample Size : {self.required_size}')

this_power = Power(0.5, 0.05, 0.8)
this_power_analysis = Power.analysis(this_power)
print(this_power_analysis)

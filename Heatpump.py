class Heatpump():
    def __init__(self, input_energy, efficiency):
        self.E_in_HP = input_energy          # Energy imported to HP in Wh
        self.efficiency = efficiency
        self.max_out_HP = 14  # max energy output of heat pump in Wh


    def HP_output(self):
        E_HP_out = self.E_in_HP * self.efficiency
        return E_HP_out()
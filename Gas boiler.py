class Gas_boiler():
    def __init__(self, input_energy, efficiency):
        self.E_in_boiler = input_energy          # Energy imported to boiler in Wh
        self.efficiency = efficiency
        self.max_out_Boiler = 35  # max energy output of boiler in Wh


    def Boiler_output(self):
        E_boiler_out = self.E_in_boiler * self.efficiency
        return E_boiler_out()
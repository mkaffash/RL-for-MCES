class PV():
    def __init__(self, solar, efficiency):
        self.solar = solar          # Energy imported to PV in Wh
        self.efficiency = efficiency

    def PV_generation(self):
        return E_PV_in()

    def E_PV_in(self):
        return self.solar * self.efficiency

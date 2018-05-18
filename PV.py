class PV():
    def __init__(self, solar, efficiency):
        self.solar = solar          # Energy imported to PV in Wh
        self.efficiency = efficiency

    def PV_generation(self):
        E_PV_in = self.solar * self.efficiency
        return E_PV_in()


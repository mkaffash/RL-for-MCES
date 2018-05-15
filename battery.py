'''
Created on 15 apr. 2018

@author: MBUWIRB
'''
class Battery():
    DISCHARGE = -1
    CHARGE    = 1
    IDLE      = 0

    def __init__(self, capacity, charging_rate):
        self.capacity           = capacity          # Energy capacity in Wh
        self.charging_rate      = charging_rate           # Power in W
        self.efficiency         = 0.95
        self.deltaT             = 60*60             # timestamp in seconds for hourly data

    def reset(self):
        self.state = {
            "charge": 0
        }

        return self._observe()

    def step(self, u):
        E      = self.execute_action(u)

        return self._observe(), u, E

    def execute_action(self, u):
        # If charging, the efficiency needs to be taken into account to calculate the battery charge
        if u == self.CHARGE or u == self.IDLE:
            efficiency = self.efficiency
        # When discharging, the full amount of energy will be discharged from the battery
        elif u == self.DISCHARGE:
            efficiency = 1

        # u should have either of the following values: 1 (charging), 0 (idle), -1 (discharging)
        delta_charge          = u * self.charging_rate * self.time_step_duration * self.deltaT
        self.state["charge"] += delta_charge * efficiency / 3600

        E = self.total_energy(delta_charge)

        return E

    def total_energy(self, delta_charge):
        # Compute excess energy and adjust battery state.
        if self.state["charge"] > self.capacity:
            # Calculate the energy that the battery took from the environment
            E                    = delta_charge - ((self.state["charge"] - self.capacity) / self.efficiency)
            self.state["charge"] = self.capacity
        elif self.state["charge"] < 0:
            # Calculate the energy that the battery delivers to the environment
            E                    = (delta_charge + self.state["charge"]) * self.efficiency
            self.state["charge"] = 0
        # If no excess energy, compute the amount of energy that has been delivered to or from the grid
        else:
            if delta_charge < 0:
                E = delta_charge * self.efficiency
            elif delta_charge > 0:
                E = delta_charge / self.efficiency
            else:
                E = 0

        return E

    def _observe(self):
        return self.state

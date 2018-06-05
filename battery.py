import pandas as pd
import numpy as np

class Battery():
    def __init__(self, charge_efficiency, bat_capacity, discharging_rate,charging_rate, horizon = 24):
        self.charge_efficiency = charge_efficiency
        self.discharge_efficiency = 1
        self.bat_capacity = bat_capacity #in kWh
        self.charge_rate = charging_rate #in kW
        self.discharge_rate = discharging_rate
        self.time_delta = 1 # simulation timestep of one hour
        self.horizon = horizon
        self.max_SoC = 1
        self.min_SoC = 0.2
        self.compute_energy_cost = False #calculates the cost of buying energy to charge battery or  money recieved for selling enrgy from discharging the battery

    def do_action (self, data, compute_energy_cost): #data = dataframe with information on the SoC of the battery
        # data['action'] = [action]
        self.compute_energy_cost = compute_energy_cost
        data['delta_energy'] = np.where(data['initial_action'] > 0 , (self.charge_efficiency*self.charge_rate * self.time_delta)/self.bat_capacity, (self.discharge_rate * self.time_delta)/self.bat_capacity)
        data['delta_energy'] = np.where(data['initial_action'] == 0 , 0, data['delta_energy'])

        self.battery_backup_controller(min_SoC_action = 1, max_SoC_action = -1,data = data)

        data['new_SoC'] = data['SoC']  + data['action'] * data['delta_energy']
        # data['delta_energy'] = self.delta_energy
        if self.compute_energy_cost:
            data['energy_cost'] =  data['delta_energy'] * data['price']
        return data

    def reset_state(self,data):
        data['SoC'] = [0 for _ in range(self.horizon)]

    def battery_backup_controller(self, min_SoC_action, max_SoC_action, data):
        data['action'] = np.where(data['SoC'] > self.max_SoC, max_SoC_action, data['initial_action'])
        data['action'] = np.where(data['SoC'] < self.min_SoC, min_SoC_action, data['initial_action'])

        return data



if __name__ == '__main__':
    optimization_horizon = 3
    action_space = [-1,0,1] #-1 = DISCHARGE, 0 = IDLE, 1 = CHARGE
    battery = Battery(charge_efficiency = 0.95, bat_capacity = 15, discharging_rate = 1.5, charging_rate = 2, horizon = optimization_horizon)
    data = pd.DataFrame({'SoC': np.linspace(0.1,0.5,optimization_horizon), 'price': np.linspace(1,4,optimization_horizon), 'initial_action': action_space, 'action': action_space})

    # battery.battery_backup_controller(min_SoC_action = 1, max_SoC_action = -1,data = data)
    battery.do_action(data,compute_energy_cost = False)
    print(data)

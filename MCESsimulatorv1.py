import pandas as pd
import numpy as np
import datetime as dt

from battery import Battery
from ElectricalDemand import ED
from heatPump import HP
from PVModel import PV
from ThermalDemand import TD




def system(data, horizon):
    pv_model = PV(area=4)
    HP_model = HP(efficiency=0.9)
    battery = Battery(charge_efficiency=0.95, bat_capacity=15, discharging_rate=1.5, charging_rate=2,horizon=optimization_horizon)
    ED_model = ED()
    TD_model = TD()
    pv = pv_model.get_PV_data('data-openideas.csv', 'solar', horizon, data)
    HP = HP_model.get_td_data('data-openideas.csv', 'out_QradD', 'out_QradN', 35, horizon, data)
    ed = ED_model.get_ED_data('linear data.csv', horizon, data)
    battery.do_action(data, compute_energy_cost=False)
    TD = TD_model.get_TD_data('data-openideas.csv', 'out_QradD', 'out_QradN', horizon, data)



    return data

if __name__ == '__main__':
    optimization_horizon = 9
    action_space = [-1,0,1]*3
    data = pd.DataFrame({'timestep': pd.date_range(dt.datetime(2014,1,1), periods = optimization_horizon, freq = '60min'),
                         'SoC': np.linspace(0,1,optimization_horizon), 'price': np.linspace(1,4,optimization_horizon), 'action': action_space, 'initial_action': action_space, 'TD':})
    system(data,optimization_horizon)
    print(data)


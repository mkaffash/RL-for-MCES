import pandas as pd
import numpy as np
class HP():
    def __init__(self, efficiency):
        self.efficiency = efficiency

    def get_td_data(self, file_name, day, night, bioler_output ,horizon, data):
        space_heating = pd.read_csv(file_name)
        day_zone = space_heating[[day]].values
        night_zone = space_heating[[night]].values
        thermal_demand = np.zeros(8400)
        alpha = np.zeros(8400) #define whether HP should be on or off based on max nominal of boiler
        for i in range(8400):
            thermal_demand[i] = (day_zone[i] + night_zone[i]) / 1000  # convert the data from W to kW
            if thermal_demand[i]>= bioler_output:
                alpha[i]=1 #means HP should be on
            else:
                alpha[i] = 0 #heat pump should be off
        data['HP'] = (thermal_demand - bioler_output)*alpha / self.efficiency
        return data['HP']

# if __name__ == '__main__':
#     horizon = 10
#     HP_model = HP(efficiency=0.9)
#     data = pd.DataFrame()
#     print('--------')
#     HP = HP_model.get_td_data('data-openideas.csv','out_QradD','out_QradN', 35,  horizon, data)
#     print(np.max(data))
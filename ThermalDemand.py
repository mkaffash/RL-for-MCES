import pandas as pd
import numpy as np

class TD():
    def __init__(self):
        pass

    def get_TD_data(self, file_name,day, night, horizon, data):
        space_heating = pd.read_csv(file_name)
        day_zone = space_heating[[day]].values
        night_zone = space_heating[[night]].values
        thermal_demand = np.zeros(8400)
        for i in range(8400):
            thermal_demand[i] = (day_zone[i] + night_zone[i]) / 1000 #convert the data from W to kW
        data['TD'] = thermal_demand
        return data

if __name__ == '__main__':
    horizon = 10
    TD_model = TD()
    data = pd.DataFrame()
    print('--------')
    TD = TD_model.get_TD_data('data-openideas.csv','out_QradD','out_QradN',  horizon, data)
    print((data/0.9)[:50])
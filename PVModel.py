import numpy as np
import pandas as pd


class PV():
    def __init__(self, area): # the openideas data is declare the PV production for 1m*1m in Wh in each hour
        self.area = area

    def get_PV_data(self, file_name,column, horizon, data):
        solar_in = pd.read_csv(file_name)
        solar_in = solar_in[[column]].values
        solar = np.zeros(8400)
        for i in range(8400):
            solar[i] = solar_in[i] * self.area/1000
        data['PV']= solar
        return data


if __name__ == '__main__':
    horizon = 4
    pv_model = PV(area = 4)
    data = pd.DataFrame()
    print('--------')
    pv = pv_model.get_PV_data('data-openideas.csv','solar', horizon,data)
    print(data)
import pandas as pd
import numpy as np

class ED():
    def __init__(self):
        pass

    def get_ED_data(self, file_name, horizon, data):
        linear_data = pd.read_csv(file_name)
        linear_data = linear_data.values
        linear_q = np.zeros([350, 96]) #data is available only for 350 days with 15 min frequency
        i = 0
        for j in range(len(linear_data)):
            if j % 200 == 0:  ###choose 1 customer amoung 200 customers
                linear_q[i] = linear_data[j]
                i = i + 1
        linear_series = np.zeros(33600) #change data to time series
        q = 0
        for i in range(350):
            for j in range(96):
                linear_series[q] = linear_q[i, j]
                q = q + 1
        linear_h = np.zeros(8400)  #convert from quarterly to hourly
        j = 0
        for i in range(8400):
            linear_h[i] = (linear_series[j] + linear_series[j+1] + linear_series[j+2] + linear_series[j+3])
            j = j + 4
        data['ED']= linear_h
        return data

if __name__ == '__main__':
    horizon = 10
    ED_model = ED()
    data = pd.DataFrame()
    print('--------')
    ed = ED_model.get_ED_data('linear data.csv', horizon,data)
    print(data)
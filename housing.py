# Linear Reggression for Housing Prices
# Author: David Basilio Rodriguez Cortez
# Dreamplan                 22/08/2023

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

class HousePrice:
    # initialize the object
    def __init__(self) -> None:
        self.data = pd.read_csv('Housing.csv')
        self.model = LinearRegression()
        self.PrepareData()
        self.TrainModel()
    
    # find the mean house price
    def GetMeanHousePrice(self) -> float:
        return self.data['price'].mean()
    
    # convert categorical variables to numerical variables
    def PrepareData(self) -> None:
        def binaryVariable(columnName):
            self.data[columnName] = self.data[columnName].map({'yes': 1, 'no': 0})
        def categoricalVariable(columnName):
            self.data[columnName] = self.data[columnName].map({'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2})
        binaryVariables = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
        for variable in binaryVariables:
            binaryVariable(variable)
        categoricalVariable('furnishingstatus')   

    # train the model using the training data
    def TrainModel(self) -> None:
        # select the features and the target
        Y = self.data['price']
        X = self.data.drop('price', axis=1)
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

        # fit the model
        self.model.fit(x_train, y_train)

        # test the model
        y_predicted = self.model.predict(x_test)
        mae = mean_absolute_error(y_test, y_predicted)
        priceMean = self.GetMeanHousePrice()
        relation = mae / priceMean
        print('MAE: %.6f' % mae)
        print('Ratio: %.6f' % relation)

    # predict the house price based on the input
    def PredictHousePriceFromInput(self, inputVariables) -> float:
        return self.model.predict([inputVariables])
    
if __name__ == '__main__':
    housePrice = HousePrice()
    predictedPrice = housePrice.PredictHousePriceFromInput([9960, 3, 2, 2, 1, -1, 1, -1, -1, 2, 1, 1]) #one row, 12 columns
    print(predictedPrice)
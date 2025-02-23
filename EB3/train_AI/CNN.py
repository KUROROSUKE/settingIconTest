import pandas as pd
from keras.layers import Dense
from keras.models import Sequential, save_model

data = pd.read_csv("train_AI/Data/label.csv")
print(data)

model = Sequential([
    Dense(256,"relu",input_shape=(1,)),
    Dense(16,"relu"),
    Dense(1,"relu")
])

model.fit(data)

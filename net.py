import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model():
    # прості дані для демонстрації
    X = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
    y = np.array([0.1, 0.4, 0.7, 0.9])

    model = Sequential()
    model.add(Dense(5, activation='relu', input_shape=(3,)))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=50, verbose=0)
    return model

def predict_rate(model, input_data):
    input_array = np.array([input_data])
    prediction = model.predict(input_array, verbose=0)[0][0]
    print(f"Прогноз нейромережі: {prediction:.4f} → ", end='')
    if prediction < 0.3:
        print("валюта помітно послаблюється")
    elif prediction < 0.6:
        print("валюта слабко змінюється")
    else:
        print("валюта зміцнюється")

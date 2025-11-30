import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def train_model():
    X = np.random.rand(300, 3)
    y = X[:, 0] * 1.5 - X[:, 1] * 0.7 + X[:, 2] * 0.9 + 0.1 * np.random.randn(300)

    model = Sequential([
        Input(shape=(3,)),
        Dense(10, activation='relu'),
        Dense(10, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=30, verbose=0)

    return model

def predict_rate(model, indicators):
    x = np.array(indicators).reshape(1, -1)
    prediction = model.predict(x, verbose=0)[0][0]

    if prediction > 0.6:
        trend = "валюта помітно зміцнюється"
    elif prediction < 0.4:
        trend = "валюта помітно послаблюється"
    else:
        trend = "валюта змінюється незначно або стабільна"

    print(f"Прогноз нейромережі: {prediction:.4f} → {trend}")
    return prediction, trend

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
df = pd.read_csv("homeprices(1).csv")
X = df[["area", "bedrooms"]]
y = df["price"]
model = LinearRegression()
model.fit(X, y)
with open("house_model.pkl", "wb") as f:
 pickle.dump(model, f)
print("Model trained and saved as house_model.pkl")
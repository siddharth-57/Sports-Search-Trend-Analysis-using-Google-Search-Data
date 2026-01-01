import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("reg1.csv")

# Convert the date column to a numerical format
start_date = datetime.strptime("1/1/2004", "%m/%d/%Y")
data["Date"] = (pd.to_datetime(data["Date"]) - start_date).dt.days

# Split the dataset into input and output
X = data.iloc[:, 0].values.reshape(-1, 1) # date
y = data.iloc[:, 1].values.reshape(-1, 1) # volume

# Create a linear regression model and fit it with the data
model = LinearRegression()
model.fit(X, y)

# Predict the next month's volume
next_month = [[(365 * 19) + 12]] # January 2024 (365 days in a year, 19 years elapsed, 12 months in a year)
predicted_volume = model.predict(next_month)

print("(cricket) The predicted volume for January 2024 is", predicted_volume[0][0])
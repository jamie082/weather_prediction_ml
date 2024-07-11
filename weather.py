import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from prophet import Prophet
import numpy as np
from prophet.plot import plot_plotly, plot_components_plotly
model = Prophet()
data = pd.read_csv("DailyDelhiClimateTrain.csv")
forecast_data = data.rename(columns = {"date": "ds", "meantemp": "y"})
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
plot_plotly(model, predictions)

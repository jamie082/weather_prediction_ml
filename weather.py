import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("DailyDelhiClimateTrain.csv")
#print(data.head())
#print(data.describe())
print(data.info())

figure = px.line(data, x="date",
                    y="meantemp",
                    title='Mean Temperature in Delhi over the Years')
figure.show()
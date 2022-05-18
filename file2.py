import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
graph = px.bar(df, x='Country', y='Per capita income')
graph.show()
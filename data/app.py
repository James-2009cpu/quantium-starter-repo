import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load your processed data
df = pd.read_csv("sales_output.csv")

# Make sure Date is in datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date (important for line chart)
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Sales": "Total Sales", "Date": "Date"}
)

# Build Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)

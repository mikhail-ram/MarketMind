import dash
from dash import dcc
from dash import html
from datetime import datetime as dt

external_script = ["https://tailwindcss.com/",
                   {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True

server = app.server

controls = html.Div(
    [
        html.H1("Welcome to MarketMind", className = "text-5xl font-bold p-10 text-center text-slate-300"),
        html.Div([
            # stock code input
        ]),
        html.Div(
            # Date range picker input
        ),
        html.Div([
            # Stock price button
            # Indicators button
            # Number of days of forecast input
            # Forecast button
        ]),
    ],
    className="controls"
)

plot = html.Div(
    [
        html.Div([
            # Logo
            # Company Name
        ],
        className="header"),
        html.Div(
            # Description
            id="description",
            className="description_ticker"
        ),
        html.Div([
            # Stock Price Plot
        ],
        id="graphs-content"),
        html.Div([
            # Indicator Plot
        ],
        id="main-content"),
        html.Div([
            # Forecast Plot
        ],
        id="forecast-content"),
    ],
    className="content"
)

app.layout = html.Div([
    controls,
    plot
], className="bg-gradient-to-t from-blue-950 to-slate-950 h-screen")

if __name__ == '__main__':
  app.run_server(debug=True)

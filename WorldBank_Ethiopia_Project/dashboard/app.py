"""
Interactive Dashboard for World Bank Ethiopia Capstone Project

This dashboard provides an interactive web interface to explore:
- Historical economic indicators
- Time series forecasts
- Trend analysis
- Cross-correlation analysis
- Model performance metrics

Run with: python dashboard/app.py
Access at: http://127.0.0.1:8050
"""

import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Ethiopia Economic Indicators Dashboard"

# Load data
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "datasets" / "cleaned" / "ethiopia_analytic_dataset.csv"

try:
    df = pd.read_csv(DATA_PATH)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df = df.sort_values('Year')
except Exception as e:
    print(f"Error loading data: {e}")
    df = pd.DataFrame()

# Indicator names and labels
INDICATORS = {
    'gdp_constant': 'GDP (Constant 2015 US$)',
    'gdp_growth': 'GDP Growth (Annual %)',
    'gdp_per_capita': 'GDP per Capita (Constant 2015 US$)',
    'inflation': 'Inflation (Annual %)',
    'unemployment': 'Unemployment (% of Labor Force)'
}

# Color palette
COLORS = {
    'gdp_constant': '#2E86AB',
    'gdp_growth': '#A23B72',
    'gdp_per_capita': '#06A77D',
    'inflation': '#F18F01',
    'unemployment': '#C73E1D'
}

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("🇪🇹 Ethiopia Economic Indicators Dashboard", 
                style={'textAlign': 'center', 'color': '#2E86AB', 'marginBottom': '10px'}),
        html.P("World Bank Development Indicators Analysis (1960-2024)",
               style={'textAlign': 'center', 'color': '#666', 'fontSize': '18px'}),
    ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'marginBottom': '20px'}),
    
    # Main content
    html.Div([
        # Left sidebar - Controls
        html.Div([
            html.H3("📊 Controls", style={'color': '#2E86AB', 'marginBottom': '20px'}),
            
            # Indicator selection
            html.Label("Select Indicator:", style={'fontWeight': 'bold', 'marginTop': '20px'}),
            dcc.Dropdown(
                id='indicator-dropdown',
                options=[{'label': label, 'value': key} for key, label in INDICATORS.items()],
                value='gdp_constant',
                style={'marginBottom': '20px'}
            ),
            
            # Year range selection
            html.Label("Year Range:", style={'fontWeight': 'bold', 'marginTop': '20px'}),
            dcc.RangeSlider(
                id='year-slider',
                min=int(df['Year'].dt.year.min()) if not df.empty else 1960,
                max=int(df['Year'].dt.year.max()) if not df.empty else 2024,
                value=[int(df['Year'].dt.year.min()) if not df.empty else 1960,
                       int(df['Year'].dt.year.max()) if not df.empty else 2024],
                marks={str(year): str(year) for year in range(1960, 2025, 10)},
                step=1
            ),
            
            # Show forecast toggle
            html.Label("Show Forecast:", style={'fontWeight': 'bold', 'marginTop': '30px'}),
            dcc.Checklist(
                id='forecast-toggle',
                options=[{'label': ' Display 10-year forecast', 'value': 'show'}],
                value=[],
                style={'marginBottom': '20px'}
            ),
            
            # Statistics panel
            html.Div(id='stats-panel', style={'marginTop': '30px', 'padding': '15px',
                                              'backgroundColor': '#f0f0f0', 'borderRadius': '5px'}),
            
        ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top',
                 'padding': '20px', 'backgroundColor': '#ffffff', 'borderRadius': '5px',
                 'marginRight': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        # Right side - Visualizations
        html.Div([
            # Time series plot
            dcc.Graph(id='time-series-plot', style={'height': '400px', 'marginBottom': '20px'}),
            
            # Statistics table
            html.Div(id='stats-table', style={'marginBottom': '20px'}),
            
            # Correlation heatmap
            dcc.Graph(id='correlation-heatmap', style={'height': '400px'}),
            
        ], style={'width': '70%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ], style={'padding': '20px'}),
    
    # Footer
    html.Div([
        html.P("World Bank Ethiopia Capstone Project | Data Source: World Bank Open Data",
               style={'textAlign': 'center', 'color': '#999', 'fontSize': '12px',
                      'marginTop': '40px', 'padding': '20px'})
    ])
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f5f5f5'})


# Callback for time series plot
@app.callback(
    Output('time-series-plot', 'figure'),
    [Input('indicator-dropdown', 'value'),
     Input('year-slider', 'value'),
     Input('forecast-toggle', 'value')]
)
def update_time_series(indicator, year_range, forecast_toggle):
    """Update time series plot based on selected indicator and year range"""
    if df.empty:
        return go.Figure()
    
    # Filter data by year range
    filtered_df = df[(df['Year'].dt.year >= year_range[0]) & 
                     (df['Year'].dt.year <= year_range[1])].copy()
    
    if filtered_df.empty or indicator not in filtered_df.columns:
        return go.Figure()
    
    # Create figure
    fig = go.Figure()
    
    # Plot historical data
    fig.add_trace(go.Scatter(
        x=filtered_df['Year'],
        y=filtered_df[indicator],
        mode='lines+markers',
        name=INDICATORS[indicator],
        line=dict(color=COLORS[indicator], width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{x|%Y}</b><br>%{y:,.2f}<extra></extra>'
    ))
    
    # Add forecast if enabled
    if 'show' in forecast_toggle and not filtered_df[indicator].isna().all():
        # Simple linear trend forecast (10 years)
        last_year = filtered_df['Year'].max()
        last_value = filtered_df[indicator].dropna().iloc[-1]
        
        # Calculate trend
        clean_data = filtered_df[[indicator, 'Year']].dropna()
        if len(clean_data) > 1:
            years_numeric = (clean_data['Year'] - clean_data['Year'].min()).dt.days
            slope = np.polyfit(years_numeric, clean_data[indicator], 1)[0]
            
            # Generate forecast years
            forecast_years = pd.date_range(start=last_year + pd.DateOffset(years=1),
                                          periods=10, freq='YS')
            forecast_values = []
            for i, year in enumerate(forecast_years):
                days_diff = (year - last_year).days
                forecast_val = last_value + slope * days_diff
                forecast_values.append(forecast_val)
            
            # Add forecast line
            fig.add_trace(go.Scatter(
                x=forecast_years,
                y=forecast_values,
                mode='lines',
                name='10-Year Forecast',
                line=dict(color=COLORS[indicator], width=2, dash='dash'),
                hovertemplate='<b>%{x|%Y}</b><br>Forecast: %{y:,.2f}<extra></extra>'
            ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': f'{INDICATORS[indicator]} Over Time',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        xaxis_title='Year',
        yaxis_title=INDICATORS[indicator],
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=50, r=50, t=80, b=50),
        legend=dict(x=0.02, y=0.98)
    )
    
    return fig


# Callback for statistics panel
@app.callback(
    Output('stats-panel', 'children'),
    [Input('indicator-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_stats_panel(indicator, year_range):
    """Update statistics panel"""
    if df.empty or indicator not in df.columns:
        return html.Div("No data available")
    
    # Filter data
    filtered_df = df[(df['Year'].dt.year >= year_range[0]) & 
                     (df['Year'].dt.year <= year_range[1])].copy()
    
    if filtered_df.empty:
        return html.Div("No data in selected range")
    
    data = filtered_df[indicator].dropna()
    
    if len(data) == 0:
        return html.Div("No data available")
    
    # Calculate statistics
    stats = {
        'Mean': f"{data.mean():,.2f}",
        'Median': f"{data.median():,.2f}",
        'Std Dev': f"{data.std():,.2f}",
        'Min': f"{data.min():,.2f}",
        'Max': f"{data.max():,.2f}",
        'First Value': f"{data.iloc[0]:,.2f}",
        'Last Value': f"{data.iloc[-1]:,.2f}",
    }
    
    # Calculate growth rate if applicable
    if len(data) > 1 and data.iloc[0] != 0:
        growth_rate = ((data.iloc[-1] / data.iloc[0]) - 1) * 100
        stats['Total Growth'] = f"{growth_rate:.1f}%"
    
    # Create HTML
    stats_html = [html.H4("📈 Statistics", style={'color': '#2E86AB', 'marginBottom': '15px'})]
    
    for key, value in stats.items():
        stats_html.append(
            html.Div([
                html.Span(key + ":", style={'fontWeight': 'bold', 'width': '120px', 'display': 'inline-block'}),
                html.Span(value, style={'color': '#333'})
            ], style={'marginBottom': '8px', 'fontSize': '14px'})
        )
    
    return html.Div(stats_html)


# Callback for statistics table
@app.callback(
    Output('stats-table', 'children'),
    [Input('year-slider', 'value')]
)
def update_stats_table(year_range):
    """Update comprehensive statistics table"""
    if df.empty:
        return html.Div()
    
    # Filter data
    filtered_df = df[(df['Year'].dt.year >= year_range[0]) & 
                     (df['Year'].dt.year <= year_range[1])].copy()
    
    if filtered_df.empty:
        return html.Div()
    
    # Calculate statistics for all indicators
    stats_data = []
    for key, label in INDICATORS.items():
        if key in filtered_df.columns:
            data = filtered_df[key].dropna()
            if len(data) > 0:
                stats_data.append({
                    'Indicator': label,
                    'Mean': f"{data.mean():,.2f}",
                    'Median': f"{data.median():,.2f}",
                    'Std Dev': f"{data.std():,.2f}",
                    'Min': f"{data.min():,.2f}",
                    'Max': f"{data.max():,.2f}"
                })
    
    if not stats_data:
        return html.Div()
    
    stats_df = pd.DataFrame(stats_data)
    
    return html.Div([
        html.H4("📊 Summary Statistics", style={'color': '#2E86AB', 'marginBottom': '10px'}),
        dash_table.DataTable(
            data=stats_df.to_dict('records'),
            columns=[{'name': col, 'id': col} for col in stats_df.columns],
            style_cell={'textAlign': 'left', 'padding': '10px', 'fontSize': '12px'},
            style_header={'backgroundColor': '#2E86AB', 'color': 'white', 'fontWeight': 'bold'},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#f9f9f9'
                }
            ]
        )
    ])


# Callback for correlation heatmap
@app.callback(
    Output('correlation-heatmap', 'figure'),
    [Input('year-slider', 'value')]
)
def update_correlation_heatmap(year_range):
    """Update correlation heatmap"""
    if df.empty:
        return go.Figure()
    
    # Filter data
    filtered_df = df[(df['Year'].dt.year >= year_range[0]) & 
                     (df['Year'].dt.year <= year_range[1])].copy()
    
    if filtered_df.empty:
        return go.Figure()
    
    # Select numeric columns
    numeric_cols = [col for col in INDICATORS.keys() if col in filtered_df.columns]
    corr_data = filtered_df[numeric_cols].corr()
    
    # Rename columns for display
    corr_data.index = [INDICATORS[col] for col in corr_data.index]
    corr_data.columns = [INDICATORS[col] for col in corr_data.columns]
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=corr_data.values,
        x=corr_data.columns,
        y=corr_data.index,
        colorscale='RdBu',
        zmid=0,
        text=corr_data.values,
        texttemplate='%{text:.2f}',
        textfont={"size": 12},
        colorbar=dict(title="Correlation")
    ))
    
    fig.update_layout(
        title={
            'text': 'Indicator Correlation Matrix',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        height=400,
        template='plotly_white',
        margin=dict(l=100, r=50, t=80, b=100)
    )
    
    return fig


# Run the app
if __name__ == '__main__':
    print("=" * 80)
    print("ETHIOPIA ECONOMIC INDICATORS DASHBOARD")
    print("=" * 80)
    print("\nStarting dashboard server...")
    print("Access the dashboard at: http://127.0.0.1:8050")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 80)
    
    app.run_server(debug=True, host='127.0.0.1', port=8050)


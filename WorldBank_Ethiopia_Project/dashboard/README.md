# Interactive Dashboard

## Overview

This interactive web dashboard provides a user-friendly interface to explore Ethiopia's economic indicators, forecasts, and analysis results from the World Bank Capstone Project.

## Features

- **Interactive Time Series Visualization**: Explore historical trends for all economic indicators
- **Year Range Filtering**: Select specific time periods to analyze
- **Forecast Visualization**: Toggle 10-year forecasts for any indicator
- **Real-time Statistics**: View mean, median, standard deviation, min, max, and growth rates
- **Correlation Analysis**: Interactive heatmap showing relationships between indicators
- **Summary Statistics Table**: Comprehensive statistics for all indicators

## Installation

Ensure you have installed all required packages:

```bash
pip install -r ../requirements.txt
```

The dashboard requires:
- `dash>=2.10.0`
- `plotly>=5.14.0`
- `pandas>=1.5.0`
- `numpy>=1.23.0`

## Running the Dashboard

1. Navigate to the project root directory:
   ```bash
   cd WorldBank_Ethiopia_Project
   ```

2. Run the dashboard:
   ```bash
   python dashboard/app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8050
   ```

## Usage

### Controls Panel (Left Sidebar)

- **Select Indicator**: Choose from:
  - GDP (Constant 2015 US$)
  - GDP Growth (Annual %)
  - GDP per Capita (Constant 2015 US$)
  - Inflation (Annual %)
  - Unemployment (% of Labor Force)

- **Year Range Slider**: Adjust the time period to analyze (1960-2024)

- **Show Forecast**: Toggle to display 10-year linear trend forecast

- **Statistics Panel**: Automatically updates with key statistics for the selected indicator

### Visualizations

- **Time Series Plot**: Interactive plot showing historical data and optional forecast
  - Hover over data points to see exact values
  - Zoom and pan using Plotly controls
  - Download plot as PNG

- **Summary Statistics Table**: Comprehensive statistics for all indicators in the selected year range

- **Correlation Heatmap**: Visual representation of relationships between economic indicators
  - Red indicates negative correlation
  - Blue indicates positive correlation
  - Intensity shows strength of relationship

## Technical Details

- **Framework**: Plotly Dash
- **Data Source**: `datasets/cleaned/ethiopia_analytic_dataset.csv`
- **Port**: 8050 (default)
- **Host**: 127.0.0.1 (localhost)

## Troubleshooting

### Dashboard won't start
- Ensure all dependencies are installed: `pip install -r ../requirements.txt`
- Check that the data file exists: `datasets/cleaned/ethiopia_analytic_dataset.csv`
- Verify Python version (3.7+)

### No data displayed
- Ensure the cleaned dataset has been generated (run notebook 01 first)
- Check file path is correct relative to project root

### Port already in use
- Change the port in `app.py`: `app.run_server(port=8051)`
- Or stop any other process using port 8050

## Notes

- The dashboard uses a simple linear trend for forecasts. For more sophisticated forecasts, refer to the forecasting notebooks (03_forecasting.ipynb and 04_dashboard_and_reporting.ipynb)
- All calculations are performed in real-time based on selected filters
- The dashboard is optimized for desktop viewing


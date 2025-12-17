# World Bank Ethiopia Capstone Project

## 📊 Project Overview

This project presents a comprehensive macroeconomic analysis of Ethiopia using World Bank Development Indicators (WDI) data from 1960 to 2024. The analysis covers data acquisition, cleaning, exploratory data analysis (EDA), time series forecasting using multiple methods (ARIMA, Holt-Winters, Prophet, and Machine Learning models), trendline analysis, cross-correlation analysis, and policy insights generation.

### Problem Statement

Ethiopia has experienced significant economic transformation over the past six decades. Understanding the trends, relationships, and future trajectories of key macroeconomic indicators is crucial for evidence-based policy making. This project aims to:

- Analyze historical trends in GDP, GDP growth, GDP per capita, inflation, and unemployment
- Identify relationships and lead-lag patterns between economic indicators
- Forecast future values using multiple time series and machine learning methods
- Generate actionable policy insights for sustainable economic development

### Key Objectives

1. **Data Collection & Cleaning**: Acquire and clean World Bank WDI data for Ethiopia
2. **Exploratory Data Analysis**: Visualize trends, distributions, and correlations
3. **Time Series Forecasting**: Implement ARIMA, Holt-Winters, and Prophet models
4. **Machine Learning Forecasting**: Apply Linear Regression, Random Forest, SVR, and XGBoost
5. **Advanced Analysis**: Calculate trendlines and cross-correlations
6. **Policy Insights**: Generate recommendations based on data-driven findings

---

## 📁 Project Structure

```
WorldBank_Ethiopia_Project/
│
├── datasets/
│   ├── raw/
│   │   └── ethiopia_wdi_raw.csv          # Raw World Bank WDI data
│   └── cleaned/
│       └── ethiopia_analytic_dataset.csv # Cleaned and processed dataset
│
├── dashboard/
│   ├── app.py                            # Interactive web dashboard (Plotly Dash)
│   └── README.md                          # Dashboard documentation
│
├── notebooks/
│   ├── 01_load_and_clean.ipynb           # Stage 1: Data acquisition and cleaning
│   ├── 02_eda.ipynb                      # Stage 2: Exploratory data analysis
│   ├── 03_forecasting.ipynb              # Stage 3: Time series forecasting (ARIMA, Holt-Winters, Prophet)
│   └── 04_dashboard_and_reporting.ipynb  # Stage 4: Dashboard, ML forecasting, and policy insights
│
├── forecasts/
│   ├── gdp_constant_arima.csv            # ARIMA forecasts for GDP
│   ├── gdp_constant_ml.csv               # ML forecasts for GDP
│   ├── unemployment_arima.csv             # ARIMA forecasts for unemployment
│   ├── unemployment_ml.csv                # ML forecasts for unemployment
│   ├── forecasts_ml.csv                   # Combined ML forecasts
│   └── ml_models_summary.csv              # ML model performance summary
│
├── models/                                # Saved ML models (joblib format)
│
├── src/                                   # Helper functions (optional)
│
├── README.md                              # This file
├── requirements.txt                      # Python dependencies
└── report.md                             # Comprehensive project report
```

---

## 🔄 Complete Pipeline

### Stage 1: Data Collection and Cleaning (`01_load_and_clean.ipynb`)

**Objectives:**
- Load raw World Bank WDI data for Ethiopia
- Transform data from wide to long format
- Handle missing values and data type conversions
- Validate data quality and ranges
- Export cleaned dataset for analysis

**Key Steps:**
1. Import libraries and load raw CSV data
2. Inspect data structure and quality
3. Melt data to long format
4. Pivot to create indicator columns
5. Handle missing values (forward fill, interpolation)
6. Convert data types and validate ranges
7. Export cleaned dataset

**Output:** `datasets/cleaned/ethiopia_analytic_dataset.csv`

---

### Stage 2: Exploratory Data Analysis (`02_eda.ipynb`)

**Objectives:**
- Visualize individual time series for each indicator
- Generate correlation heatmaps
- Calculate descriptive statistics
- Assess data quality and identify outliers
- Prepare data for modeling

**Key Steps:**
1. Load cleaned dataset
2. Plot individual time series (GDP, GDP growth, GDP per capita, inflation, unemployment)
3. Generate correlation matrix and heatmap
4. Calculate descriptive statistics (mean, median, std, min, max)
5. Assess skewness and kurtosis
6. Identify missing data patterns

**Key Insights:**
- GDP shows massive long-term growth (+115 billion USD from 1960-2024)
- GDP per capita increased by +676 USD per person
- GDP growth is highly volatile (mean 5.23%, std 5.28%)
- Inflation is chronically high (mean 14.6%) with extreme volatility
- Unemployment is low (mean 2.94%) but may reflect structural labor market characteristics

---

### Stage 3: Time Series Forecasting (`03_forecasting.ipynb`)

**Objectives:**
- Implement ARIMA, Holt-Winters, and Prophet forecasting models
- Perform train-test splits (last 5 years for testing)
- Evaluate models using RMSE and MAE metrics
- Compare model performance across indicators
- Generate future forecasts

**Key Steps:**
1. Prepare time series data with datetime indexing
2. Implement ARIMA(1,1,1) model evaluation
3. Implement Holt-Winters exponential smoothing
4. Implement Prophet forecasting
5. Calculate RMSE and MAE for each model
6. Create comparison tables
7. Generate future forecasts

**Models Implemented:**
- **ARIMA(1,1,1)**: AutoRegressive Integrated Moving Average
- **Holt-Winters**: Exponential smoothing with trend and seasonality
- **Prophet**: Facebook's time series forecasting tool

**Evaluation Metrics:**
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

---

### Stage 4: Dashboard, ML Forecasting, and Policy Insights (`04_dashboard_and_reporting.ipynb`)

**Objectives:**
- Create comprehensive visualization dashboard
- Calculate trendlines using linear regression
- Perform cross-correlation analysis
- Implement machine learning forecasting models
- Generate ARIMA forecasting dashboard
- Provide policy insights and recommendations

**Key Steps:**

1. **Comprehensive Visualization Dashboard**
   - Multi-panel plots for all indicators
   - Professional formatting and labels

2. **Trendline Analysis**
   - Calculate linear regression trendlines
   - Visualize trends with confidence intervals
   - Summarize trend directions and slopes

3. **Cross-Correlation Analysis**
   - Identify lead-lag relationships between indicators
   - Calculate optimal lag for indicator pairs
   - Visualize cross-correlation functions

4. **ARIMA Forecasting Dashboard**
   - Generate 10-year forecasts for key indicators
   - Plot historical data with forecast and confidence intervals
   - 4-panel dashboard visualization

5. **Machine Learning Forecasting**
   - Feature engineering (lags, rolling means)
   - Train-test split for time series
   - Implement Linear Regression, Random Forest, SVR, XGBoost
   - Hyperparameter tuning with RandomizedSearchCV
   - Model evaluation and comparison
   - Save best models and forecasts

6. **Policy Insights and Recommendations**
   - Generate insights based on key statistics
   - Analyze cross-correlation results
   - Provide actionable recommendations

**ML Models Implemented:**
- **Linear Regression**: Baseline linear model with feature scaling
- **Random Forest**: Ensemble tree-based model
- **SVR**: Support Vector Regression
- **XGBoost**: Gradient boosting (optional)

**Outputs:**
- `forecasts/forecasts_ml.csv`: ML forecasts for all indicators
- `forecasts/ml_models_summary.csv`: Model performance summary
- `models/*.joblib`: Saved best models

---

## 🔑 Key Insights

### Economic Growth
- **GDP Growth**: Ethiopia has maintained high average growth (5.23%) but with significant volatility
- **Structural Transformation**: GDP increased from 5.3B to 120B USD (constant 2015 USD) from 1960-2024
- **Per Capita Improvement**: GDP per capita increased by 676 USD, indicating productivity gains

### Inflation
- **Chronic High Inflation**: Mean inflation of 14.6% with extreme volatility (std 11.1%)
- **Shock Sensitivity**: Inflation spikes during conflict periods and global crises
- **Policy Challenge**: Requires coordinated monetary and fiscal policy

### Unemployment
- **Low Official Rate**: Mean unemployment of 2.94%
- **Structural Considerations**: High informal employment may mask true labor market conditions
- **Data Limitations**: Only 34 observations available

### Relationships
- **GDP Growth ↔ Inflation**: Negative correlation during stable periods
- **GDP Growth ↔ Unemployment**: Inverse relationship (Okun's Law)
- **GDP per Capita ↔ GDP**: Strong positive correlation

---

## 🎯 Forecasting Summary

### Best Performing Models

| Indicator | Best Model | RMSE | Notes |
|-----------|-----------|------|-------|
| GDP (constant) | Linear Regression | 8.04B USD | Strong trend component |
| GDP per Capita | Linear Regression | 24.01 USD | Excellent fit (R² = 0.96) |
| Unemployment | Linear Regression | 0.57% | Low volatility indicator |

### Forecast Highlights (2025-2034)
- **GDP**: Continued growth trajectory with increasing uncertainty
- **GDP per Capita**: Steady improvement expected
- **Inflation**: High volatility expected, requiring policy vigilance
- **Unemployment**: Relatively stable with minor fluctuations

---

## 🚀 How to Reproduce

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- 8GB+ RAM recommended for ML models

### Installation

1. **Clone the repository** (or download the project folder):
   ```bash
   git clone <repository-url>
   cd WorldBank_Ethiopia_Project
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

1. **Execute notebooks in order**:
   ```bash
   jupyter notebook notebooks/01_load_and_clean.ipynb
   jupyter notebook notebooks/02_eda.ipynb
   jupyter notebook notebooks/03_forecasting.ipynb
   jupyter notebook notebooks/04_dashboard_and_reporting.ipynb
   ```

2. **Expected outputs**:
   - Cleaned dataset: `datasets/cleaned/ethiopia_analytic_dataset.csv`
   - Forecasts: `forecasts/*.csv`
   - Saved models: `models/*.joblib`

### Running the Interactive Dashboard

The project includes an interactive web dashboard for exploring the data:

1. **Start the dashboard server:**
   ```bash
   python dashboard/app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:8050
   ```

**Dashboard Features:**
- 📊 Interactive time series visualization for all indicators
- 📅 Year range filtering (1960-2024)
- 🔮 Toggle 10-year forecasts
- 📈 Real-time statistics panel
- 🔗 Correlation heatmap
- 📋 Summary statistics table

For detailed dashboard documentation, see `dashboard/README.md`

### Running Individual Stages

Each notebook is self-contained and can be run independently, but they should be executed in order for the full workflow.

---

## 📦 Requirements & Installation

### Python Dependencies

See `requirements.txt` for the complete list. Key packages include:

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Time Series**: statsmodels, prophet
- **Machine Learning**: scikit-learn, xgboost
- **Utilities**: joblib (model saving)

### Installation Command

```bash
pip install -r requirements.txt
```

### Optional Dependencies

- **XGBoost**: For gradient boosting models (optional but recommended)
- **Jupyter Extensions**: For enhanced notebook experience

---

## 📊 Visual Examples

### Time Series Plots
- Individual indicator visualizations with trendlines
- Multi-panel dashboard showing all indicators
- Forecast plots with confidence intervals

### Correlation Analysis
- Heatmaps showing relationships between indicators
- Cross-correlation plots with optimal lag identification

### Forecasting Dashboards
- ARIMA forecasts with historical data
- ML model comparison visualizations

---

## 🔍 Key Challenges

1. **Missing Data**: Early years (1960s-1970s) have significant missing values
   - **Solution**: Forward fill and interpolation strategies

2. **Data Quality**: Some indicators have limited observations
   - **Solution**: Careful validation and documentation of limitations

3. **Volatility**: High volatility in GDP growth and inflation
   - **Solution**: Multiple forecasting models and confidence intervals

4. **Model Selection**: Different models perform best for different indicators
   - **Solution**: Comprehensive model comparison and selection

5. **Structural Breaks**: Economic shocks create non-stationarity
   - **Solution**: ARIMA differencing and robust ML models

---

## 📝 Data Sources

- **Primary Source**: World Bank Open Data
- **Dataset**: World Development Indicators (WDI)
- **Country**: Ethiopia (ETH)
- **Time Period**: 1960-2024
- **Indicators**:
  - GDP (constant 2015 US$)
  - GDP growth (annual %)
  - GDP per capita (constant 2015 US$)
  - Inflation, consumer prices (annual %)
  - Unemployment, total (% of total labor force)

---

## 👥 Authors

- Yeamlack Sisay

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- World Bank for providing open access to development data
- Python open-source community for excellent data science libraries
- Instructors and peers for feedback and support

---

## 📚 Additional Resources

- **Project Report**: See `report.md` for detailed methodology and findings
- **World Bank Data**: https://data.worldbank.org/
- **Documentation**: Each notebook contains detailed markdown explanations

---

## 🔄 Future Work

1. **Extended Forecasting**: Incorporate external variables (commodity prices, climate data)
2. **Regional Comparison**: Compare Ethiopia with peer countries
3. **Sectoral Analysis**: Break down GDP by economic sectors
4. **Real-time Dashboard**: Deploy interactive dashboard using Plotly Dash
5. **Deep Learning**: Experiment with LSTM and Transformer models
6. **Policy Simulation**: Build scenario analysis tools

---

## 📧 Contact

For questions or feedback, please contact [Yeamlacks@gmail.com]

---

**Last Updated**: December 17 2024

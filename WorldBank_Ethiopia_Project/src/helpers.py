"""
Helper functions for World Bank Ethiopia Capstone Project

This module contains reusable functions for:
- Data loading and validation
- Visualization utilities
- Forecasting wrappers
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def load_cleaned_data(data_path="../datasets/cleaned/ethiopia_analytic_dataset.csv"):
    """
    Load the cleaned Ethiopia analytic dataset.
    
    Parameters:
    -----------
    data_path : str
        Path to the cleaned dataset CSV file
        
    Returns:
    --------
    pd.DataFrame
        Cleaned dataset with Year as datetime index
    """
    df = pd.read_csv(data_path, index_col=0)
    df = df.reset_index().rename(columns={"index": "Year"})
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    df = df.sort_values("Year").set_index("Year")
    return df


def validate_data(df, indicator, min_val=None, max_val=None):
    """
    Validate data ranges for a given indicator.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset to validate
    indicator : str
        Column name to validate
    min_val : float, optional
        Minimum allowed value
    max_val : float, optional
        Maximum allowed value
        
    Returns:
    --------
    dict
        Validation results with counts and flags
    """
    results = {
        "total_values": len(df[indicator].dropna()),
        "missing_values": df[indicator].isna().sum(),
        "out_of_range": 0,
        "valid": True
    }
    
    if min_val is not None:
        below_min = (df[indicator] < min_val).sum()
        results["out_of_range"] += below_min
        if below_min > 0:
            results["valid"] = False
    
    if max_val is not None:
        above_max = (df[indicator] > max_val).sum()
        results["out_of_range"] += above_max
        if above_max > 0:
            results["valid"] = False
    
    return results


def plot_time_series(df, indicator, title=None, ylabel=None, figsize=(12, 6)):
    """
    Create a professional time series plot.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset with datetime index
    indicator : str
        Column name to plot
    title : str, optional
        Plot title (defaults to indicator name)
    ylabel : str, optional
        Y-axis label (defaults to indicator name)
    figsize : tuple
        Figure size (width, height)
        
    Returns:
    --------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    data = df[indicator].dropna()
    ax.plot(data.index, data.values, linewidth=2)
    
    if title is None:
        title = indicator.replace("_", " ").title()
    if ylabel is None:
        ylabel = indicator.replace("_", " ").title()
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig


def calculate_trendline(series):
    """
    Calculate linear trendline for a time series.
    
    Parameters:
    -----------
    series : pd.Series
        Time series data with datetime index
        
    Returns:
    --------
    dict
        Dictionary with slope, intercept, r_value, p_value, std_err
    """
    from scipy.stats import linregress
    
    data = series.dropna()
    if len(data) < 2:
        return None
    
    years = data.index.map(pd.Timestamp.toordinal)
    slope, intercept, r_value, p_value, std_err = linregress(years, data.values)
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_value': r_value,
        'r_squared': r_value ** 2,
        'p_value': p_value,
        'std_err': std_err
    }


def create_forecast_directory(base_path="../forecasts"):
    """
    Create forecast directory if it doesn't exist.
    
    Parameters:
    -----------
    base_path : str
        Base path for forecasts directory
    """
    Path(base_path).mkdir(parents=True, exist_ok=True)


def save_forecast(forecast_df, filename, base_path="../forecasts"):
    """
    Save forecast DataFrame to CSV.
    
    Parameters:
    -----------
    forecast_df : pd.DataFrame
        Forecast data to save
    filename : str
        Output filename
    base_path : str
        Base path for forecasts directory
    """
    create_forecast_directory(base_path)
    filepath = Path(base_path) / filename
    forecast_df.to_csv(filepath, index=True)
    print(f"Forecast saved to {filepath}")


def print_summary_statistics(df, indicator):
    """
    Print summary statistics for an indicator.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset
    indicator : str
        Column name
    """
    data = df[indicator].dropna()
    
    print(f"\n{indicator.replace('_', ' ').title()} Summary Statistics:")
    print("-" * 50)
    print(f"Count:     {len(data)}")
    print(f"Mean:      {data.mean():.2f}")
    print(f"Median:    {data.median():.2f}")
    print(f"Std Dev:   {data.std():.2f}")
    print(f"Min:       {data.min():.2f}")
    print(f"Max:       {data.max():.2f}")
    print(f"Missing:   {df[indicator].isna().sum()}")


# Set default style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


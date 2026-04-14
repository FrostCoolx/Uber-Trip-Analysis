# 🚕 Uber Trip Analysis & Demand Forecasting

## 📌 Project Overview
This project focuses on analyzing and predicting Uber trip demand using time-series and dispatcher data. The goal is to identify peak demand times, route efficiencies, and pricing patterns. By implementing a fully modular machine learning pipeline, this project transforms raw dispatch data into actionable insights and accurate demand forecasts.

## ⚙️ Pipeline Architecture
The project is structured as an automated, multi-file Python pipeline:
- **`data_cleaning.py`**: Standardizes formatting, handles missing values, and engineers time-series features (e.g., day of the week, weekend indicators).
- **`eda.py`**: Generates automated, high-quality visualizations to map out total trips over time, demand patterns by day, and operational efficiency (active vehicles vs. trips).
- **`models.py`**: Trains and evaluates predictive models, handling categorical encoding and train-test splits.
- **`main.py`**: The master execution script that runs the entire pipeline end-to-end.

## 📊 Models & Results
To predict the number of `trips` based on temporal features and `active_vehicles`, two advanced regression models were deployed:
1. **XGBoost Regressor**: Achieved a highly accurate Mean Absolute Percentage Error (MAPE) of **~8.90%**, capturing complex non-linear trends.
2. **Ensemble Model (XGBoost + Gradient Boosted Trees)**: Deployed via a `VotingRegressor` to improve stability, mitigate overfitting, and establish a robust, reliable forecasting system.

## 🛠️ Tech Stack
- **Languages:** Python
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn, XGBoost
- **Visualization:** Matplotlib, Seaborn

## 🚀 How to Run
1. Ensure your dataset (`Uber-Jan-Feb-FOIL.csv`) is placed in the `data/` directory.
2. Install the required dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn xgboost`
3. Execute the pipeline: `python main.py`
4. View the generated charts and model evaluation plots in the `outputs/` folder.

---
**Author:** Ashutosh Ranjan  
*M.Tech Data Science Portfolio Project*
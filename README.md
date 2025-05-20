# Vehicle-Sales-Forecasting

This project forecasts future vehicle sales using historical sales data across different regions and models. The goal is to help dealerships and motor companies like Isuzu improve inventory planning, budgeting, and marketing efforts.

## 📊 Project Objective
- Forecast monthly sales volumes for different vehicle models.
- Identify seasonal trends and spikes in demand.
- Build a user-friendly dashboard to visualize predictions.

## 📁 Project Structure
- `data/`: Sample CSV file containing historical vehicle sales.
- `notebooks/`: Jupyter Notebook for model development and evaluation.
- `src/`: Core Python scripts for data processing and forecasting.
- `dashboards/`: Optional Streamlit app for interactive visualization.
- `utils/`: Utility functions used throughout the project.

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/BrantonKM/vehicle_sales_forecasting.git
cd vehicle_sales_forecasting
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook notebooks/vehicle_sales_forecasting.ipynb
```

### 5. Run Streamlit App (Optional)
```bash
streamlit run dashboards/streamlit_app.py
```

## 📈 Tools & Libraries
- Python, pandas, numpy
- scikit-learn, Prophet
- matplotlib, seaborn
- Streamlit (for dashboards)

## 📬 Contact
For any inquiries or contributions, reach out.

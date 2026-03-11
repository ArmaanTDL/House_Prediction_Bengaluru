# 🏠 Bengaluru House Price Prediction

A comprehensive end-to-end Machine Learning project to predict residential property prices in Bengaluru, India. This application features a robust prediction engine powered by LightGBM and CatBoost, integrated into a clean and intuitive Flask-based web interface.

![App Preview](screenshots/app_preview.png)

## 🌟 Key Features

- **High-Accuracy ML Engine**: Utilizes an ensemble of LightGBM and CatBoost models for precise price estimation.
- **Interactive Web Interface**: A modern, responsive UI built with Flask, allowing users to input property details easily.
- **Detailed Data Analysis**: Includes exploratory data analysis (EDA) and sophisticated feature engineering blocks.
- **Dynamic Predictions**: Real-time price calculation based on location, area type, BHK, and square footage.
- **Smart Formatting**: Automatically displays prices in appropriate units (Lakhs/Crores) based on the Indian numbering system.

## 🛠️ Project Structure

The repository is organized as follows:

- `Bengaluru-House-Price-Prediction/`: Core application folder containing the trained model and UI templates.
  - `app.py`: Flask application for serving predictions.
  - `bengaluru_model.pkl`: The serialized machine learning model.
  - `templates/`: HTML templates for the frontend.
- `explanatory.ipynb`: Notebook containing Exploratory Data Analysis.
- `feature_extraction.py`: script for cleaning data and extracting premium features.
- `requirements.txt`: List of Python dependencies.
- `screenshots/`: Visual assets and application previews.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd House_Prediction
   ```

2. **Set up a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/python3  # On Mac/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To launch the web interface, navigate to the core application directory and run the Flask server:

```bash
cd Bengaluru-House-Price-Prediction
python app.py
```

The application will be available at `http://localhost:5002`.

## 📊 Methodology

1. **Data Cleaning**: Handled missing values, outliers, and inconsistent entries in the Bengaluru housing dataset.
2. **Feature Engineering**: Created interaction features and region-based aggregate features to improve model performance.
3. **Model Training**: Trained and tuned LightGBM and CatBoost models using offline cross-validation.
4. **Ensembling**: Implemented a stacking method to combine the strengths of multiple models, ensuring robust predictions across different property types.

---
*Created with focus on performance and usability.*

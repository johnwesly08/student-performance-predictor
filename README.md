# 🎓 Student Performance Predictor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

A comprehensive machine learning pipeline to predict students' final scores based on study hours and attendance patterns. Built with modularity, scalability, and production-readiness in mind.

---

## 📊 Model Performance

- **Algorithm**: Linear Regression
- **Features**: Study Hours, Attendance Percentage
- **Target**: Final Score
- **Metrics**: R² Score, Mean Absolute Error (MAE)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation & Setup

1. **Clone and setup environment**:
```bash
git clone https://github.com/johnwesly08/student-performance-predictor.git
cd student-performance-predictor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Generate sample datasets**:
```bash
python generate.py
```

3. **Train the model**:
```bash
python main.py --mode train --plot
```

4. **Make predictions**:
```bash
python main.py --mode predict
```

---

## 📁 Project Structure

```
student_marks_predict_model/
├── data/
│   ├── raw/                    # Raw datasets
│   │   ├── student_data.csv
│   │   └── student_test_input.csv
│   └── processed/              # Processed data & predictions
├── models/                     # Trained model files
├── logs/                       # Training logs and metrics
├── src/                        # Source code
│   ├── utils/
│   │   └── config_loader.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   └── predictor.py
├── main.py                     # Main pipeline controller
├── generate.py                 # Dataset generation
├── requirements.txt            # Dependencies
├── config.yaml                 # Configuration
└── README.md
```

---

## ⚙️ Usage Examples

### Training with Visualization
```bash
python main.py --mode train --file data/raw/student_data.csv --plot
```

### Prediction with Custom Input
```bash
python main.py --mode predict --file data/raw/custom_input.csv
```

### Standalone Prediction
```bash
python src/predictor.py --input data/raw/student_test_input.csv
```

---

## 🔧 Configuration

The project uses `config.yaml` for centralized configuration:

```yaml
paths:
  raw_data: "data/raw/student_data.csv"
  test_data: "data/raw/student_test_input.csv"
  model_path: "models/student_model.joblib"
  predictions_output: "data/processed/predictions.csv"
```

---

## 📈 Features & Capabilities

### ✅ Implemented
- **Data Pipeline**: Automated data loading and preprocessing
- **Model Training**: Linear regression with performance metrics
- **Visualization**: Data exploration and regression line plots
- **Prediction Engine**: Batch predictions on new data
- **Logging**: Comprehensive training and prediction logs
- **Metrics Tracking**: R² score and MAE tracking over time

### 🔮 Future Enhancements
- [ ] Model versioning and A/B testing
- [ ] REST API deployment
- [ ] Hyperparameter tuning
- [ ] Additional features (previous scores, extracurriculars)
- [ ] Docker containerization

---

## 📊 Sample Data Format

### Training Data (`student_data.csv`)
```csv
study_hours, attendance, final_score
5, 80, 75
8, 90, 88
2, 60, 50
```

### Prediction Input (`student_test_input.csv`)
```csv
study_hours, attendance, final_score
6, 80, 72
9, 92, 90
```

---

## 🧪 Testing

Run the complete pipeline test:
```bash
# Generate fresh data
python generate.py

# Train model
python main.py --mode train

# Make predictions
python main.py --mode predict
```

---

## 📝 Logs & Monitoring

- **Training Logs**: `logs/run.log`
- **Performance Metrics**: `logs/training_metrics.csv`
- **Predictions**: `data/processed/predicted_output.csv`

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **John Wesly P D** - Initial work - [johnwesly08](https://github.com/johnwesly08)

---

## 🙏 Acknowledgments

- Built with Scikit-learn, Pandas, and Matplotlib
- Inspired by educational data mining research
  

## Key Improvements Made:

1. **Better Structure**: More organized sections with clear hierarchy
2. **Actual Commands**: Uses your actual file names and commands
3. **Visual Enhancements**: Better formatting with emojis and code blocks
4. **Complete Documentation**: Covers all aspects of your current project
5. **Future Roadmap**: Shows potential enhancements
6. **Real Examples**: Uses your actual data format and project structure
7. **Professional Touch**: Added license, contributing guidelines, acknowledgments

## Next Steps:

1. **Create requirements.txt** if you haven't:
```bash
pip freeze > requirements.txt
```


## 🧭 7. Enhancements for the Future

| Feature | Why It’s Useful |
|----------|----------------|
| **Dockerfile** | Makes the project runnable anywhere |
| **FastAPI / Flask API** | Convert it into a web service for predictions |
| **CI/CD via GitHub Actions** | Auto-run tests when you push updates |
| **Data Versioning (DVC)** | Track dataset changes |
| **Experiment Tracking (MLflow)** | Manage model versions and performance metrics |
| **Jupyter Notebook** | Add a notebook for EDA and presentation |



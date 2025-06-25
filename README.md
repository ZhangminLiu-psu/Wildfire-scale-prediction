
# 🔥 Wildfire Severity Classification & Emergency Dispatch System Simulation

## 1. 📘 Project Description

This project uses basic machine learning tools to build a **binary classification system** using real-world wildfire incident data to predict whether a fire becomes **"large"** (defined as burns over 1000 acres). It also simulates a **fire response dispatch system** based on the predictions using core Python concepts like **classes**, **recursion**, and **queues**.

**Dataset citation:**  
> U.S. Forest Service. (2023). *Wildfire Incident Records Dataset* [CSV file].  
> [https://www.fs.usda.gov/data/wildfires/wf_incidents.csv](https://www.fs.usda.gov/data/wildfires/wf_incidents.csv) (Accessed: June 26, 2025)

**Technologies Used:**
- `pandas` for data handling and cleaning  
- `scikit-learn` for model training and evaluation  
- `matplotlib` / `seaborn` for visualization  
- Custom class design (`FireIncident`)  
- Python built-in `deque` and recursion for simulating dispatch

The prediction system is trained using **logistic regression**, with `class 1` assigned to “probability of large fire.” An 80/20 train-test split is used. Evaluation includes accuracy, confusion matrix, and a classification report.

---

## 2. 🔍 Project Significance

Wildfires pose a major threat to life, infrastructure, and environmental stability. Being able to predict whether a fire may become “large” helps with:
- Prioritizing emergency response resources
- Improving preparedness
- Enhancing situational awareness for first responders

This simulation project not only predicts high-risk fires, but also creates an automated response strategy using a lightweight, interpretable machine learning pipeline.

---

## 3. ⚙️ Installation & Usage

### Requirements:
- Python 3.9+
- pandas, matplotlib, seaborn, scikit-learn

### Install Libraries:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

### Run the Project:
```bash
python main.py
```

---

## 4. 🧾 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Main script with ML and simulation logic |
| `wf_incidents.csv` | Wildfire incident dataset |
| `README.md` | Project documentation |

---

## 5. 🔑 Key Functionalities

### 🔎 Prediction System
- **Target Variable:** `large_fire` (1 if `FINAL_ACRES > 1000`)
- **Features Used:**
  - `FATALITIES`
  - `INJURIES_TOTAL`
  - `STR_DESTROYED_TOTAL`
  - `fire_severity_score` (custom feature)
- **Classifier:** Logistic Regression
- **Evaluation Metrics:**
  - Accuracy
  - Confusion Matrix
  - Precision, Recall, F1-Score

### 🚒 Dispatch Simulation
- Predicted large fires are wrapped into `FireIncident` objects
- Stored in FIFO queue using `deque`
- Recursive function simulates dispatch teams to each fire

---

## 6. 📊 Results Summary

### Model Performance
| Metric | Value |
|--------|-------|
| Accuracy | 92–95% |
| Recall (large fire) | ~70% |
| F1-Score | Moderate (split-dependent) |

### Sample Output
```
Dispatching team 1 to -> Fire #208: LARGE | Acres: 2300.0, Severity: 5
Dispatching team 2 to -> Fire #415: LARGE | Acres: 1120.0, Severity: 2
...
All high-risk fires have been addressed.
```

---

## 7. 🧠 Python Concepts Applied

| Concept | How It's Used |
|---------|---------------|
| `class` | `FireIncident` to encapsulate fire data |
| `recursion` | `dispatch_fire_teams()` to simulate dispatch |
| `deque` | Queue of predicted large fires |
| `pandas` | Data filtering, feature creation |
| `sklearn` | Model training and evaluation |
| `matplotlib`, `seaborn` | Correlation heatmap, histogram |

---

## 8. 🧩 Discussion & Reflection

### Challenges:
- Real-world data had many missing values
- Simplifying model while preserving usefulness
- Integrating machine learning output into Python object simulation

### Key Achievements:
- Built a complete ML pipeline using real data
- Designed and applied custom features
- Used OOP and recursion creatively in a simulation

---

## 9. 🧾 Conclusion

This project shows:
- How ML can assist in disaster forecasting
- How core Python constructs can simulate real-world decision logic
- How to turn raw, messy data into meaningful insight

---

## 10. 🧪 Overall Quality of Report & Project

This project demonstrates thoughtful application of:
- Machine learning basics  
- Object-oriented programming (OOP)  
- Modular design and clear logic flow  

It handles real data issues like missing values, includes feature engineering, and uses recursion and data structures to simulate emergency logic.

---

## 💬 Final Note

Although this project was completed individually, it was not without challenges. I used Python documentation, tutorials, and AI-assisted debugging to overcome roadblocks — especially while integrating machine learning with OOP logic.

The topic was chosen based on the wildfire theme. I applied ML concepts from data science classes and Python structures (like classes and queues) from this semester. The process was demanding but rewarding, and I gained deeper understanding of how ML and OOP can work together in a practical system.

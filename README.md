Wildfire Severity Classification & Emergency Dispatch System Simulation

1. Project Description
This project uses basic machine learning tools to builds a binary classification system using real-world wildfire incident data to predict whether a fire becomes "large" (custom defined as burns over 1000 acres). It also simulates a fire response dispatch system based on the predictions using core Python concepts like classes, recursion, and queues.

U.S. Forest Service. (2023). Wildfire Incident Records Dataset [CSV file]. https://www.fs.usda.gov/data/wildfires/wf_incidents.csv (Accessed: June 26, 2025)

The project is implemented using the following:
Pandas for data handling and cleaning
Scikit-learn for model training and evaluation
Matplotlib / Seaborn for visualization
Custom class design (FireIncident) for fire response
Python's built-in deque and recursion for simulating dispatch queue

The prediction system is trained using logistic regression with class 1 assigned to “probability of large fire” and using 80% training, 20% testing, and evaluated using accuracy, confusion matrix, and a classification report.

2. Project Significance
Wildfires pose a major threat to life, infrastructure, and environmental stability. Being able to predict whether a fire may become severely “large” helps with: prioritizing emergency response resources, improving preparedness and enhance situational awareness for first-responders.

This project simulation not only predicting high-risk fires, but also creating an automated response strategy to support disaster management decisions using a lightweight but useful machine learning pipeline.

3. Installation & Usage

Requirements:
Python 3.9+
pandas, matplotlib, seaborn, scikit-learn

Install Required Libraries:
pip install pandas matplotlib seaborn scikit-learn

Run the Project:
python main.py

4. Project Structure

File	Description
main.py	Main script with model & logic comment
wf_incidents.csv	Raw wildfire incident dataset
Project description.md	Project description and instructions

5. Key Functionalities

Prediction System

Target Variable: large_fire (1 if FINAL_ACRES > 1000)

Features Used:
FATALITIES
INJURIES_TOTAL
STR_DESTROYED_TOTAL
fire_severity_score (custom derived feature)

Classifier Used: Logistic Regression

Evaluation Metrics:
Accuracy
Confusion Matrix
Precision / Recall / F1-score

Fire Dispatch Queue (Simulation)

Predicted high-risk fires are wrapped into FireIncident objects.
Stored in a first-in-first-out queue (deque)
Recursive function simulates dispatching teams to each fire.

6. Results Summary

Model Performance (Logistic Regression)

Metric	Value
Accuracy	92–95%
Recall (large fire)	~70%
F1-Score (large fire)	Moderate (depends on split)

Dispatch Simulation Output (Sample)
Dispatching team 1 to -> Fire #208: LARGE | Acres: 2300.0, Severity: 5
Dispatching team 2 to -> Fire #415: LARGE | Acres: 1120.0, Severity: 2
...
All high-risk fires have been addressed.

7. Python Concepts Applied

Concept	How It's Used
class	FireIncident to encapsulate fire data
recursion	dispatch_fire_teams() to simulate dispatch
deque (queue)	To prioritize predicted large fires
pandas	For data filtering, feature engineering
sklearn	For model training and accuracy evaluation
matplotlib, seaborn	For correlation heatmap & fire size histogram

8. Discussion & Reflection

Challenges Faced:
Real-world data had many missing values and unused columns with high level unpredictability
Needed to define a meaningful target variable and simplify the model
Need to learn how to incorporate ML module results to OOP classes and queue

Key Achievements:
Built a complete ML pipeline from real data.
Learned to engineer custom features for better prediction.
Applied Python OOP and recursion in a creative way.

9. Conclusion
This project is a practical demonstration of:
How basic ML models can assist in disaster risk forecasting
The use of Python programming constructs (classes, queues, recursion) to simulate real-world decisions
How to turn raw data into insight

10.Overall Quality of Report and Project

Personally, I think this project demonstrates a thoughtful application of core OOP and basic machine learning techniques, modules in python to a real-world issue. In terms of development and completeness, the project is fully developed: from data pre-processing to model training and prediction interpretation.

The workflow logic follows a well-defined machine learning pipeline: data cleaning, feature engineering, model fitting, evaluation and interpretation.

Features like the recursive fire dispatch system and visualizations help to enrich the system.

In terms of code quality, the code tries to be structured and commented, following a modular design pattern. Custom classes like FireIncident show encapsulation while logic such as build_response_queue() demonstrates use of data structures like queues and recursion. Edge cases (missing values, data imbalance) are handled, though relatively simply, but are considered.

In terms of writing and presentation, the report tries to be logically organized, and clear-structured. It explains the problem, solution approach, methods and results.

In relation to the machine learning outside scope of this python course, important concepts like binary classification, evaluation metrics are defined clearly. OOP techniques learned in this class is also identified and usage explained.

Final Note:
Although this project was completed individually, it was not without challenges. I made appropriate use of online Python documentation, tutorials, and AI-assisted debugging to overcome roadblocks — especially when integrating machine learning components with linked data structures.

When deciding on a project topic aligned with the wildfire theme, I chose to apply basic ML libraries introduced in my data science coursework and combine them with object-oriented programming and recursive structures covered this semester.

This project was demanding, but ultimately rewarding. I gained a much deeper understanding of Python, machine learning workflows, and how different programming concepts can work together in a meaningful application.

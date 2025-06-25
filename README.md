
Wildfire Severity Classification & Emergency Dispatch System Simulation

1. Project Description
This project uses basic machine learning tools to build a binary classification system using real-world wildfire incident data to predict whether a fire becomes "large" (burns over 1000 acres). It also simulates a fire response dispatch system based on the predictions using Python concepts like classes, recursion, and queues.

Dataset source:
U.S. Forest Service. (2023). Wildfire Incident Records Dataset [CSV file].
https://www.fs.usda.gov/data/wildfires/wf_incidents.csv (Accessed: June 26, 2025)

Used:
- pandas for handling data
- scikit-learn for modeling
- matplotlib / seaborn for charts
- FireIncident class for dispatch logic
- queue and recursion to simulate dispatch flow

Prediction is done using logistic regression with 80% of data used for training and 20% for testing. Results are evaluated with accuracy, confusion matrix and classification report.

2. Why it matters
Wildfires cause damage and disruption. If we can guess ahead of time which fires will become large, we can send help faster. This helps with emergency planning and safety. This project just shows a basic way to predict and then simulate how teams could be sent.

3. Installation and Running
- Requires: Python 3.9+, pandas, seaborn, matplotlib, scikit-learn
- To install:
pip install pandas matplotlib seaborn scikit-learn

- To run:
python main.py

4. Project Files
main.py - the main script
wf_incidents.csv - dataset
README.md - this file

5. What it does
ML Model:
Target: large_fire = 1 if fire is over 1000 acres
Features:
- FATALITIES
- INJURIES_TOTAL
- STR_DESTROYED_TOTAL
- fire_severity_score (custom sum of above)

Uses logistic regression. Reports accuracy, precision, recall, f1.

Dispatch simulation:
- Fires predicted as large get added to a queue
- FireIncident class holds info
- dispatch_fire_teams() uses recursion to simulate sending teams

6. Results
Model:
- Accuracy around 92–95%
- Recall on large fires ~70%

Example output:
Dispatching team 1 to -> Fire #208: LARGE | Acres: 2300.0, Severity: 5
Dispatching team 2 to -> Fire #415: LARGE | Acres: 1120.0, Severity: 2

7. Python used
class - FireIncident
recursion - dispatch loop
deque - for queueing
pandas - data prep
sklearn - modeling
matplotlib - graphs

8. Reflection
Problems:
- Missing data in the CSV
- Needed to simplify the model
- Took time to figure out how to combine ML and recursion

Learned:
- How to run a full ML pipeline
- Made a working simulation using Python logic
- Understood how ML results can be used in simulations

9. Final thoughts
Basic but practical use of ML and Python. Uses course material like classes, recursion, and simple data handling. Shows a start-to-finish project with real data.

10. Final Note
Did the project alone, but used online tutorials and AI for help when stuck, especially connecting ML results to Python class-based logic. The wildfire topic matched well with prediction, and I tried to use both course concepts and things I learned before. It was tough but I learned a lot and finished something useful.


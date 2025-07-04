
"""
Final Project: Predicting Large Wildfires + A Simple Priority Response System

Goal: Use wildfire incident data to predict whether a fire becomes 'large'
(defined as FINAL_ACRES > 1000) using basic damage-related features.
  Then use the acquired results to predict fire severity, which is used to
  build a large-fire response queue.

"""

#Data prediction Part

#Import pandas for data handling, matplotlib and seaborn for graph plotting
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import sklearn tools for basic data splitting and machine learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():
    # Data preperation and cleaning

    # Load the wildfire data
    df = pd.read_csv("wf_incidents.csv")

    # Keep only relevant columns needed for analysis and drop rows with missing fire size
    df = df[['FINAL_ACRES', 'FATALITIES', 'INJURIES_TOTAL', 'STR_DESTROYED_TOTAL', 'START_YEAR']].dropna()

    # Fill missing values for damage-related columns with 0 (assumes no damage if data missing)
    df[['FATALITIES', 'INJURIES_TOTAL', 'STR_DESTROYED_TOTAL']] = df[
        ['FATALITIES', 'INJURIES_TOTAL', 'STR_DESTROYED_TOTAL']
    ].fillna(0)

    # Feature Creating

    # Create a binary target. 1 if fire is "large" (> 1000 acres), if not, 0
    df['large_fire'] = (df['FINAL_ACRES'] > 1000).astype(int)

    # Create a custom feature that access damage - severity score by using sum of 3 related columns
    df['fire_severity_score'] = (
            df['FATALITIES'] + df['INJURIES_TOTAL'] + df['STR_DESTROYED_TOTAL']
    )

    # Check if large fire vs. non-large fire classes are balanced
    print("Target class distribution:")
    print(df['large_fire'].value_counts())

    # Define features and prediction target

    features = ['FATALITIES', 'INJURIES_TOTAL', 'STR_DESTROYED_TOTAL', 'fire_severity_score']
    X = df[features]
    y = df['large_fire']

    # Split data into training and testing sets(80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Logistic Regression Model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predictions and evaluate
    y_pred = model.predict(X_test)

    # Accuracy analysis
    acc = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {acc:.3f}")

    # Confusion matrix for deeper performance analysis
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Full classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Visualization

    # Plot: correlation heatmap between features and FINAL_ACRES
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[features + ['FINAL_ACRES']].corr(), annot=True, cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    # Plot: histogram to show distribution of fire sizes
    plt.figure(figsize=(6, 4))
    plt.hist(df['FINAL_ACRES'], bins=50, color='orange', edgecolor='black')
    plt.title("Distribution of Fire Sizes")
    plt.xlabel("Final Acres")
    plt.ylabel("Number of Fires")
    plt.tight_layout()
    plt.show()

    # Resonse system Part

    # Use class to keep track of fire attributes
    class FireIncident:
        def __init__(self, incident_id, acres, severity_score, predicted_large):
            self.incident_id = incident_id
            self.acres = acres
            self.severity_score = severity_score
            self.predicted_large = predicted_large

        # custom string output
        def __str__(self):
            if self.predicted_large:
                status = "LARGE"
            else:
                "small"
            return f"Fire #{self.incident_id}: {status} | Acres: {self.acres}, Severity: {self.severity_score}"

    # Takes test dataframe and predictions, builds a queue of FireIncident objects
    # where the model predicted a large fire.

    from collections import deque

    # Add large fire incidents to queue
    def build_response_queue(df, y_pred):

        queue = deque()
        for i, (idx, row) in enumerate(df.iterrows()):
            if y_pred[i] == 1:  # predicted as large fire
                incident = FireIncident(
                    incident_id=idx,
                    acres=row['FINAL_ACRES'],
                    severity_score=row['fire_severity_score'],
                    predicted_large=1
                )
                queue.append(incident)
        return queue

    # Create fire respond team queue
    def dispatch_fire_teams(queue, count=1):

        if not queue:
            print("All high-risk large fires have been addressed.")
            return
        fire = queue.popleft()
        print(f"Dispatching response team {count} to -> {fire}")
        dispatch_fire_teams(queue, count + 1)

    # Create response queue based on predicted large fires
    X_test_with_acres = X_test.copy()
    X_test_with_acres['FINAL_ACRES'] = df.loc[X_test.index, 'FINAL_ACRES']
    X_test_with_acres['fire_severity_score'] = df.loc[X_test.index, 'fire_severity_score']

    print("\n Building response queue for predicted large fires...")
    response_queue = build_response_queue(X_test_with_acres, y_pred)

    print("\n Dispatching emergency response teams:")
    dispatch_fire_teams(response_queue)


if __name__ == '__main__':
    main()



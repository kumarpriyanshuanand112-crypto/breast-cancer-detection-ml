import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import pickle

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

features = [
    'mean radius', 'mean perimeter', 'mean area',
    'mean concave points', 'mean concavity',
    'worst radius', 'worst perimeter', 'worst area',
    'worst concave points', 'worst concavity'
]

final_df = df[features + ["target"]]
X = final_df.drop(columns="target")
y = final_df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("Scaler", StandardScaler()),
    ("Tree", DecisionTreeClassifier(random_state=42))
])

pipeline.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Model saved")

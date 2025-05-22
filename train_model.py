import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: Load data
df = pd.read_csv('phishing.csv')

# Step 2: Separate features and label
X = df.drop('Result', axis=1)   # sab column as features except label
y = df['Result']                # label

# Step 3: Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save the model
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

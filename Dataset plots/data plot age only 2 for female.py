import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('diabetes_risk_prediction_dataset.csv')
    
# Filter for male entries
female_data = df[df['Gender'] == 'Female']

# Plotting Age against class for male
plt.figure(figsize=(30, 10))
pd.crosstab(female_data['Age'], female_data['class']).plot(kind='bar', stacked=True)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Class vs Age (Female)')
plt.xticks(rotation=45,size='8')

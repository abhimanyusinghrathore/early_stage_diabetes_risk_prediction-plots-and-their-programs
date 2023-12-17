import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('diabetes_risk_prediction_dataset.csv')
    
# Filter for male entries
male_data = df[df['Gender'] == 'Male']

# Plotting Age against class for male
pd.crosstab(male_data['Age'], male_data['class']).plot(kind='bar', stacked=True,figsize=(10, 5))
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Class vs Age (Male)')
plt.xticks(rotation=45,size='8')

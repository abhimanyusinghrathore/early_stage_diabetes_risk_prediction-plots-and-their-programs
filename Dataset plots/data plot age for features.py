import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('diabetes_risk_prediction_dataset.csv')
df1=df.drop('Age',axis=1)
df2=df1.drop('class',axis=1)

for column in df2.columns:
    plt.figure(figsize=(15, 15))
    pd.crosstab(df2[column], df1['class']).plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Class vs {column}')

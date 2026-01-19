import pandas as pd

data = {
    'Student': ['A', 'B', 'C', 'D'],
    'Marks': [78, 85, 90, 66]
}

df = pd.DataFrame(data)

print("Student Marks Data")
print(df)

print("\nAverage Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())

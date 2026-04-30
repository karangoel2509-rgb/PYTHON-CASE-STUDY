

import pandas as pd
import matplotlib.pyplot as plt
n = int(input("Enter number of students: "))
names = []
maths = []
science = []
english = []
for i in range(n):
    print(f"\nStudent {i+1}")
    names.append(input("Name: "))
    maths.append(int(input("Maths marks: ")))
    science.append(int(input("Science marks: ")))
    english.append(int(input("English marks: ")))
df = pd.DataFrame({
    'Name': names,
    'Maths': maths,
    'Science': science,
    'English': english
})
df['Total'] = df[['Maths','Science','English']].sum(axis=1)
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStd Dev:\n", df.std(numeric_only=True))
print("\nTop Performer:\n", df.loc[df['Total'].idxmax()])
print("\nLow Performer:\n", df.loc[df['Total'].idxmin()])
avg = df[['Maths','Science','English']].mean()
avg.plot(kind='bar', title='Average Marks')
plt.show()
df.set_index('Name')[['Maths','Science','English']].T.plot(title="Performance")
plt.show()
df['Total'].plot(kind='hist', title='Total Marks')
plt.show()
avg.plot(kind='pie', autopct='%1.1f%%', title='Subject Contribution')
plt.show()
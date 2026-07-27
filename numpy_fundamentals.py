import numpy as np


# Load CSV data
data = np.genfromtxt(
    "student_scores.csv",
    delimiter=",",
    skip_header=1
)


print("Dataset:")
print(data)


# Separate columns

hours = data[:,0]
attendance = data[:,1]
scores = data[:,2]


# Mean

mean_score = np.mean(scores)


# Standard deviation

std_score = np.std(scores)


# Correlation

correlation = np.corrcoef(hours, scores)


print("\nMean Score:")
print(mean_score)


print("\nStandard Deviation:")
print(std_score)


print("\nCorrelation between Hours and Score:")
print(correlation)
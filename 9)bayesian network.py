import numpy as np 
import pandas as pd 
from pgmpy.estimators import MaximumLikelihoodEstimator 
from pgmpy.models import BayesianModel 
from pgmpy.inference import VariableElimination 

# Load dataset 
heartDisease = pd.read_csv(r"C:\Users\HP\Downloads\dataset.csv") 

# Replace '?' with NaN and convert to numeric 
heartDisease = heartDisease.replace('?', np.nan) 
heartDisease['ca'] = pd.to_numeric(heartDisease['ca'], errors='coerce') 
heartDisease['thal'] = pd.to_numeric(heartDisease['thal'], errors='coerce') 

# Drop missing rows 
heartDisease.dropna(inplace=True) 

print('Sample instances from the dataset:') 
print(heartDisease.head()) 

print('\nAttributes and datatypes:') 
print(heartDisease.dtypes) 

# Define Bayesian Model structure (using 'gender' instead of 'sex') 
model = BayesianModel([ 
    ('age', 'heartdisease'), 
    ('gender', 'heartdisease'), 
    ('exang', 'heartdisease'), 
    ('cp', 'heartdisease'), 

    ('heartdisease', 'restecg'), 
    ('heartdisease', 'chol') 
]) 

print('\nLearning CPD using Maximum Likelihood Estimators...') 
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator) 

print('\nInferencing with Bayesian Network:') 
HeartDisease_infer = VariableElimination(model) 

print('\n1. Probability of HeartDisease given evidence: restecg=1') 
q1 = HeartDisease_infer.query(variables=['heartdisease'], evidence={'restecg': 1}) 
print(q1) 

print('\n2. Probability of HeartDisease given evidence: cp=2') 
q2 = HeartDisease_infer.query(variables=['heartdisease'], evidence={'cp': 2}) 
print(q2)

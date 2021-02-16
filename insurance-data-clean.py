# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:35:48 2020

@author: jimma
"""
import pandas as pd

PATH = "..\CSV file\insurance.csv"
df = pd.read_csv(PATH)

print(df.head())

df["smoker_classify"] = df.smoker.apply(lambda x: 1 if x == "yes" else 0)
df["gender_classify"] = df.sex.apply(lambda x: 1 if x == "male" else 0)
print(df)
print(df.info())

df.to_csv("new_insurance.csv")
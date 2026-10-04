# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path


# ============================================================
# Dataset Analysis
# ============================================================

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Dataset path
file_path = (
    project_folder
    / "dataset"
    / "Sleep_health_and_lifestyle_dataset.csv"
)

# Load dataset
df = pd.read_csv(file_path)


print("\n===== DATASET SHAPE =====")
print(df.shape)


print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())


print("\n===== FIRST 5 ROWS =====")
print(df.head())


print("\n===== DATASET INFORMATION =====")
print(df.info())


print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


print("\n===== BASIC STATISTICS =====")
print(df.describe())
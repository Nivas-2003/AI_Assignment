# 🌙 Sleep Reflex Agent

A dataset-based rule-based reflex agent that analyzes a user's sleeping pattern and provides an estimated Sleep Quality Score from 0 to 100.

## 📌 Project Overview

The Sleep Reflex Agent uses a sleep health and lifestyle dataset to identify the relationship between sleep duration and sleep quality.

Based on the observed patterns in the dataset, the agent uses condition-action rules to evaluate a user's sleep duration.

The web application allows the user to enter:

- Bedtime
- Wake-up time

The system calculates the total sleep duration and applies the reflex rules to generate:

- Sleep Quality Score
- Sleep Quality Category
- Agent Analysis
- Recommendation

## 🤖 How the Reflex Agent Works

The agent follows a simple condition-action architecture:

User Input
↓
Bedtime + Wake-up Time
↓
Calculate Sleep Duration
↓
Apply Dataset-Based Rules
↓
Apply Bedtime Heuristic
↓
Calculate Final Score
↓
Sleep Quality Category
↓
Recommendation

## 📊 Dataset

The project uses the **Sleep Health and Lifestyle Dataset**.

The dataset contains 374 records and 13 attributes, including:

- Person ID
- Gender
- Age
- Occupation
- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps
- Sleep Disorder

The dataset was analyzed to determine the relationship between sleep duration and sleep quality.

### Dataset observations

| Sleep Duration | Average Quality |
|---|---:|
| Less than 6 hours | 4.33 / 10 |
| 6 to <7 hours | 6.21 / 10 |
| 7 to <8 hours | 7.74 / 10 |
| 8 to 9 hours | 9.00 / 10 |

These observations were used to create the sleep-duration rules.

## 🧠 Reflex Rules

### Sleep Duration

| Sleep Duration | Base Score |
|---|---:|
| Less than 6 hours | 45 |
| 6 to <7 hours | 65 |
| 7 to <8 hours | 85 |
| 8 hours or more | 95 |

### Bedtime

Bedtime is used as a secondary heuristic factor.

| Bedtime | Adjustment |
|---|---:|
| 9:00 PM – 11:00 PM | 0 |
| 11:00 PM – 12:00 AM | -5 |
| After midnight | -10 |

### Final Categories

| Score | Category |
|---|---|
| 90–100 | Excellent |
| 75–89 | Good |
| 60–74 | Fair |
| 0–59 | Poor |

## 🌐 Website

The project includes a static web application built using:

- HTML
- CSS
- JavaScript

The website can be hosted using GitHub Pages.

## 📁 Project Structure

```text
Sleep-Reflex-Agent/
│
├── index.html
├── style.css
├── script.js
│
├── dataset/
│   └── Sleep_health_and_lifestyle_dataset.csv
│
├── analysis/
│   ├── dataset_analysis.py
│   └── sleep_analysis.py
│
├── agent/
│   └── sleep_agent.py
│
├── README.md
├── requirements.txt
└── .gitignore
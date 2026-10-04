# AQI Simple Reflex Agent

## Description

This project demonstrates a **Simple Reflex Agent** that observes the current
AQI (Air Quality Index) conditions for a selected Indian city and applies a
fixed set of condition-action rules to decide the AQI category. The agent
looks only at the **current** percept — it has no memory of past readings,
no learning, and no planning. That is what makes it a *simple reflex* agent
rather than a more advanced agent type.

The project is intentionally small: a Streamlit webpage, a tiny local
dataset, and one short Python file containing the agent's rules.

## How the Agent Works

```text
City Selection
      ↓
Current AQI Percept
      ↓
Condition
      ↓
Action
      ↓
AQI Category
```

- **Percept:** The current AQI value for the selected city (read from the
  local dataset).
- **Condition:** Which AQI range the value falls into (e.g. `101–200`).
- **Action:** Assign the matching AQI category (e.g. `"Moderate"`).

This is a direct implementation of the classic simple-reflex-agent pattern:

```text
PERCEPT → CONDITION → ACTION
```

For example:

```text
AQI = 163
   ↓
101 <= AQI <= 200
   ↓
Moderate
```

The rules (in `reflex_agent.py`) follow the **Indian CPCB National Air
Quality Index (NAQI)** standard:

| AQI Range | Category      |
|-----------|---------------|
| 0 – 50    | Good          |
| 51 – 100  | Satisfactory  |
| 101 – 200 | Moderate      |
| 201 – 300 | Poor          |
| 301 – 400 | Very Poor     |
| 401+      | Severe        |

## Technologies

- Python
- Streamlit
- Pandas

## Dataset

`data.csv` now covers **16 Indian cities**: Mumbai, Delhi, Hyderabad,
Bengaluru, Chennai, Kolkata, Pune, Ahmedabad, Jaipur, Lucknow, Patna,
Bhopal, Nagpur, Indore, Guwahati and Chandigarh.

- **AQI** values are based on real, publicly reported AQI readings for
  each city — the first 8 cities come from a real-time multi-city AQI
  snapshot (early December 2025), and the remaining 8 cities come from
  official **CPCB National Air Quality Index Bulletins** (CPCB, cpcb.nic.in),
  which publish a daily AQI value per city.
- **Temperature, Humidity, Wind Speed and Rainfall** are approximate
  December climate-normal values for each city, based on publicly known
  historical weather patterns/statistics for that city (city-level
  December climate averages).

Because this is a small educational demo (not a live data pipeline), the
values form a fixed, real-world-based **snapshot** rather than a live
feed, and the AQI values for different cities were not all necessarily
recorded on the exact same day. No values were invented out of thin air —
every number is grounded in publicly reported AQI/weather figures for
these cities, simplified into one representative row per city so the
agent has something concrete to react to.

Want even more cities? Just add another row to `data.csv` with the same
columns — the app and the agent automatically pick up any city present
in the file, no code changes required.

If you want to use your own data, just edit `data.csv` — as long as it
keeps the same column names (`City,Temperature,Humidity,WindSpeed,Rainfall,AQI`),
the app will work with no code changes.

## How to Run

```bash
git clone <repository-url>
cd aqi-reflex-agent
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints in your terminal (usually
`http://localhost:8501`).

## Example

```text
Select City: Hyderabad
[Predict AQI]

Temperature: 24 °C
Humidity: 55 %
Wind Speed: 8 km/h
Rainfall: 2 mm
Current AQI: 163

Predicted AQI: 163
AQI Category: Moderate

The agent determined the category based only on the current
AQI condition (Simple Reflex Agent: percept -> condition -> action).
```

## Limitations

This is a **simple educational demonstration** of the Simple Reflex Agent
concept from AI fundamentals. It is:

- **Not** an official or real-time AQI monitoring system.
- **Not** connected to any live weather/pollution API.
- Based on a small, fixed, illustrative dataset of 8 cities.
- Not a machine-learning project — the "prediction" is a set of fixed
  condition-action rules, not a trained model.

## Credits

Developed by Varun B.

This project was created as a learning project to demonstrate
the Simple Reflex Agent concept using AQI data.

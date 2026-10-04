"""
app.py
------
A very small Streamlit webpage that demonstrates a SIMPLE REFLEX AGENT
for AQI category prediction.

Flow:
    User selects a City
        -> Look up that city's environmental values from data.csv
        -> Send the current AQI value (the percept) to the reflex agent
        -> The agent applies condition-action rules
        -> Display the predicted AQI category
"""

import pandas as pd
import streamlit as st

from reflex_agent import predict_aqi

# ---------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------
DATA_PATH = "data.csv"
data = pd.read_csv(DATA_PATH)

# ---------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------
st.set_page_config(page_title="AQI Reflex Agent", page_icon="🌫️")

st.title("🌫️ AQI REFLEX AGENT")
st.caption("A Simple Reflex Agent that decides an AQI category from the current percept only.")

# ---------------------------------------------------------------------
# 1. City selection (the only input the user needs to give)
# ---------------------------------------------------------------------
city = st.selectbox("Select City", data["City"].tolist())

if st.button("Predict AQI"):

    # 2. Get this city's environmental values (the agent's percept source)
    row = data[data["City"] == city].iloc[0]
    temperature = row["Temperature"]
    humidity = row["Humidity"]
    wind_speed = row["WindSpeed"]
    rainfall = row["Rainfall"]
    aqi_value = row["AQI"]

    # 3. Show the current environmental readings for this city
    st.subheader(f"Current conditions in {city}")
    st.write(f"Temperature: {temperature} °C")
    st.write(f"Humidity: {humidity} %")
    st.write(f"Wind Speed: {wind_speed} km/h")
    st.write(f"Rainfall: {rainfall} mm")
    st.write(f"Current AQI: {aqi_value}")

    # 4. PERCEPT -> the Simple Reflex Agent -> ACTION
    category = predict_aqi(aqi_value)

    # 5. Display the result
    st.markdown("---")
    st.metric(label="Predicted AQI", value=int(aqi_value))
    st.success(f"AQI Category: **{category}**")
    st.write(
        "The agent determined the category based only on the current "
        "AQI condition (Simple Reflex Agent: percept -> condition -> action)."
    )

else:
    st.info("Select a city and click **Predict AQI** to run the agent.")

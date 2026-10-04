"""
reflex_agent.py
----------------
This file contains the SIMPLE REFLEX AGENT.

A Simple Reflex Agent works like this:

    PERCEPT -> CONDITION -> ACTION

It looks ONLY at the current percept (the current AQI value) and
applies a fixed set of condition-action rules to decide what to do.
It does NOT remember past percepts, it does NOT plan ahead, and it
does NOT learn. This keeps it as simple as possible.

AQI categories and ranges below follow the Indian CPCB National
Air Quality Index (NAQI) standard:
    0   - 50   -> Good
    51  - 100  -> Satisfactory
    101 - 200  -> Moderate
    201 - 300  -> Poor
    301 - 400  -> Very Poor
    401 - 500+ -> Severe
"""


def predict_aqi(aqi):
    """
    The Simple Reflex Agent's decision function.

    PERCEPT  : aqi (the current AQI value for the selected city)
    CONDITION: which range the aqi value falls into
    ACTION   : return the matching AQI category (a plain condition-action rule)

    Parameters
    ----------
    aqi : int or float
        The current AQI percept for a location.

    Returns
    -------
    str
        The AQI category decided by the agent's rules.
    """

    # ---- Condition-action rules (the "reflex" part of the agent) ----
    if aqi <= 50:
        category = "Good"
    elif aqi <= 100:
        category = "Satisfactory"
    elif aqi <= 200:
        category = "Moderate"
    elif aqi <= 300:
        category = "Poor"
    elif aqi <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    return category


# Small manual self-test when this file is run directly.
if __name__ == "__main__":
    test_values = [30, 75, 142, 250, 350, 450]
    for value in test_values:
        print(f"AQI = {value:>3}  ->  Category = {predict_aqi(value)}")

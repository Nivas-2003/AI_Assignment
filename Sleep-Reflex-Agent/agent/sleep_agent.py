# ============================================================
# Sleep Reflex Agent
# Dataset-Based Rule-Based Sleep Quality Analysis
# ============================================================


def calculate_sleep_duration(bedtime, wake_time):
    """
    Calculate sleep duration from bedtime and wake-up time.

    Time is represented as decimal hours.
    Example:
        22.5 = 10:30 PM
        6.5  = 6:30 AM
    """

    if wake_time <= bedtime:
        duration = (24 - bedtime) + wake_time
    else:
        duration = wake_time - bedtime

    return duration


# ============================================================
# Sleep Reflex Agent
# ============================================================

def sleep_reflex_agent(sleep_duration, bedtime):

    # --------------------------------------------------------
    # Rule 1: Determine base score from sleep duration
    # Based on analysis of the sleep dataset
    # --------------------------------------------------------

    if sleep_duration < 6:

        base_score = 45
        duration_level = "Poor"
        duration_analysis = "Sleep duration is below 6 hours."

    elif sleep_duration < 7:

        base_score = 65
        duration_level = "Fair"
        duration_analysis = "Sleep duration is between 6 and 7 hours."

    elif sleep_duration < 8:

        base_score = 85
        duration_level = "Good"
        duration_analysis = "Sleep duration is between 7 and 8 hours."

    else:

        base_score = 95
        duration_level = "Excellent"
        duration_analysis = (
            "Sleep duration is 8 hours or more, "
            "which is the highest-quality range observed "
            "in the dataset."
        )


    # --------------------------------------------------------
    # Rule 2: Analyze bedtime
    # --------------------------------------------------------

    if 21 <= bedtime <= 23:

        bedtime_adjustment = 0

        bedtime_level = "Ideal"

        bedtime_analysis = (
            "Bedtime is within the preferred range "
            "used by the reflex agent."
        )

    elif 23 < bedtime <= 24:

        bedtime_adjustment = -5

        bedtime_level = "Late"

        bedtime_analysis = (
            "Bedtime is relatively late."
        )

    elif bedtime < 5:

        bedtime_adjustment = -10

        bedtime_level = "Very Late"

        bedtime_analysis = (
            "Bedtime is after midnight and is considered "
            "very late by the reflex agent."
        )

    else:

        bedtime_adjustment = 0

        bedtime_level = "Early"

        bedtime_analysis = (
            "Bedtime is relatively early."
        )


    # --------------------------------------------------------
    # Calculate final score
    # --------------------------------------------------------

    final_score = (
        base_score +
        bedtime_adjustment
    )

    final_score = max(
        0,
        min(
            100,
            final_score
        )
    )


    # --------------------------------------------------------
    # Determine final category
    # --------------------------------------------------------

    if final_score >= 90:

        category = "Excellent"

    elif final_score >= 75:

        category = "Good"

    elif final_score >= 60:

        category = "Fair"

    else:

        category = "Poor"


    # --------------------------------------------------------
    # Generate recommendation
    # --------------------------------------------------------

    if sleep_duration < 6:

        advice = (
            "Try to increase your sleep duration "
            "to at least 7 hours."
        )

    elif sleep_duration < 7:

        advice = (
            "Try to increase your sleep duration "
            "to at least 7 hours for a better sleep pattern."
        )

    elif sleep_duration < 8:

        advice = (
            "Your sleep duration is in a good range. "
            "Maintaining a consistent sleep schedule is recommended."
        )

    else:

        advice = (
            "Your sleep duration is in the highest-quality "
            "range observed in the dataset."
        )


    if bedtime > 23 or bedtime < 5:

        advice += (
            " Consider maintaining an earlier and "
            "more consistent bedtime."
        )


    # --------------------------------------------------------
    # Return complete analysis
    # --------------------------------------------------------

    return {
        "score": final_score,
        "category": category,
        "base_score": base_score,
        "bedtime_adjustment": bedtime_adjustment,
        "duration_level": duration_level,
        "bedtime_level": bedtime_level,
        "duration_analysis": duration_analysis,
        "bedtime_analysis": bedtime_analysis,
        "advice": advice
    }


# ============================================================
# Test the Reflex Agent
# ============================================================

if __name__ == "__main__":

    print("\n========================================")
    print("SLEEP REFLEX AGENT TEST")
    print("========================================")


    test_cases = [

        # 10:30 PM → 6:30 AM
        (22.5, 6.5),

        # 11:00 PM → 6:00 AM
        (23.0, 6.0),

        # 12:30 AM → 6:30 AM
        (0.5, 6.5),

        # 10:00 PM → 5:00 AM
        (22.0, 5.0),

    ]


    for bedtime, wake_time in test_cases:

        duration = calculate_sleep_duration(
            bedtime,
            wake_time
        )

        result = sleep_reflex_agent(
            duration,
            bedtime
        )

        print("\n----------------------------------------")

        print(f"Bedtime        : {bedtime:.1f}")
        print(f"Wake-up Time   : {wake_time:.1f}")
        print(f"Sleep Duration : {duration:.1f} hours")

        print(f"Base Score     : {result['base_score']}/100")
        print(
            f"Bedtime Change : "
            f"{result['bedtime_adjustment']}"
        )

        print(f"Final Score    : {result['score']}/100")
        print(f"Category       : {result['category']}")

        print(
            f"Duration       : "
            f"{result['duration_analysis']}"
        )

        print(
            f"Bedtime        : "
            f"{result['bedtime_analysis']}"
        )

        print(
            f"Advice         : "
            f"{result['advice']}"
        )
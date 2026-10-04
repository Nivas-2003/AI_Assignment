// ============================================================
// Sleep Reflex Agent
// JavaScript implementation for GitHub Pages
// ============================================================


// ============================================================
// Calculate Sleep Duration
// ============================================================

function calculateSleepDuration(bedtime, wakeTime) {

    if (wakeTime <= bedtime) {

        return (24 - bedtime) + wakeTime;

    } else {

        return wakeTime - bedtime;

    }
}


// ============================================================
// Sleep Reflex Agent
// ============================================================

function sleepReflexAgent(
    sleepDuration,
    bedtime
) {

    let baseScore;
    let durationAnalysis;

    // --------------------------------------------------------
    // Sleep Duration Rules
    // Based on dataset analysis
    // --------------------------------------------------------

    if (sleepDuration < 6) {

        baseScore = 45;

        durationAnalysis =
            "Sleep duration is below 6 hours.";

    }

    else if (sleepDuration < 7) {

        baseScore = 65;

        durationAnalysis =
            "Sleep duration is between 6 and 7 hours.";

    }

    else if (sleepDuration < 8) {

        baseScore = 85;

        durationAnalysis =
            "Sleep duration is between 7 and 8 hours.";

    }

    else {

        baseScore = 95;

        durationAnalysis =
            "Sleep duration is 8 hours or more, " +
            "which is the highest-quality range " +
            "observed in the dataset.";

    }


    // --------------------------------------------------------
    // Bedtime Rules
    // --------------------------------------------------------

    let bedtimeAdjustment;
    let bedtimeAnalysis;


    if (bedtime >= 21 && bedtime <= 23) {

        bedtimeAdjustment = 0;

        bedtimeAnalysis =
            "Bedtime is within the preferred range.";

    }

    else if (bedtime > 23 && bedtime <= 24) {

        bedtimeAdjustment = -5;

        bedtimeAnalysis =
            "Bedtime is relatively late.";

    }

    else if (bedtime < 5) {

        bedtimeAdjustment = -10;

        bedtimeAnalysis =
            "Bedtime is after midnight and is considered " +
            "very late.";

    }

    else {

        bedtimeAdjustment = 0;

        bedtimeAnalysis =
            "Bedtime is relatively early.";

    }


    // --------------------------------------------------------
    // Final Score
    // --------------------------------------------------------

    let score =
        baseScore +
        bedtimeAdjustment;


    score =
        Math.max(
            0,
            Math.min(
                100,
                score
            )
        );


    // --------------------------------------------------------
    // Category
    // --------------------------------------------------------

    let category;


    if (score >= 90) {

        category = "Excellent";

    }

    else if (score >= 75) {

        category = "Good";

    }

    else if (score >= 60) {

        category = "Fair";

    }

    else {

        category = "Poor";

    }


    // --------------------------------------------------------
    // Recommendation
    // --------------------------------------------------------

    let advice;


    if (sleepDuration < 6) {

        advice =
            "Try to increase your sleep duration " +
            "to at least 7 hours.";

    }

    else if (sleepDuration < 7) {

        advice =
            "Try to increase your sleep duration " +
            "to at least 7 hours for a better sleep pattern.";

    }

    else if (sleepDuration < 8) {

        advice =
            "Your sleep duration is in a good range. " +
            "Maintaining a consistent sleep schedule " +
            "is recommended.";

    }

    else {

        advice =
            "Your sleep duration is in the " +
            "highest-quality range observed in the dataset.";

    }


    if (bedtime > 23 || bedtime < 5) {

        advice +=
            " Consider maintaining an earlier and " +
            "more consistent bedtime.";

    }


    return {

        score: score,

        category: category,

        baseScore: baseScore,

        bedtimeAdjustment: bedtimeAdjustment,

        durationAnalysis: durationAnalysis,

        bedtimeAnalysis: bedtimeAnalysis,

        advice: advice

    };
}


// ============================================================
// Analyze Sleep
// ============================================================

function analyzeSleep() {

    const bedtimeInput =
        document.getElementById(
            "bedtime"
        ).value;


    const wakeTimeInput =
        document.getElementById(
            "wakeTime"
        ).value;


    if (
        !bedtimeInput ||
        !wakeTimeInput
    ) {

        alert(
            "Please enter both bedtime and wake-up time."
        );

        return;

    }


    // Convert HH:MM to decimal hours

    const bedtimeParts =
        bedtimeInput.split(":");


    const wakeTimeParts =
        wakeTimeInput.split(":");


    const bedtime =
        parseInt(bedtimeParts[0]) +
        parseInt(bedtimeParts[1]) / 60;


    const wakeTime =
        parseInt(wakeTimeParts[0]) +
        parseInt(wakeTimeParts[1]) / 60;


    // Calculate duration

    const sleepDuration =
        calculateSleepDuration(
            bedtime,
            wakeTime
        );


    // Run agent

    const result =
        sleepReflexAgent(
            sleepDuration,
            bedtime
        );


    // --------------------------------------------------------
    // Display Results
    // --------------------------------------------------------

    document.getElementById(
        "score"
    ).textContent =
        result.score;


    document.getElementById(
        "category"
    ).textContent =
        result.category;


    document.getElementById(
        "duration"
    ).textContent =
        sleepDuration.toFixed(1) +
        " hours";


    document.getElementById(
        "advice"
    ).textContent =
        result.advice;


    document.getElementById(
        "durationAnalysis"
    ).textContent =
        result.durationAnalysis;


    document.getElementById(
        "bedtimeAnalysis"
    ).textContent =
        result.bedtimeAnalysis;


    document.getElementById(
        "displayBedtime"
    ).textContent =
        formatTime(
            bedtimeInput
        );


    document.getElementById(
        "displayWakeTime"
    ).textContent =
        formatTime(
            wakeTimeInput
        );

}


// ============================================================
// Format Time
// ============================================================

function formatTime(time) {

    const parts =
        time.split(":");


    let hours =
        parseInt(parts[0]);


    const minutes =
        parts[1];


    const period =
        hours >= 12
            ? "PM"
            : "AM";


    if (hours === 0) {

        hours = 12;

    }

    else if (hours > 12) {

        hours -= 12;

    }


    return (
        hours +
        ":" +
        minutes +
        " " +
        period
    );

}
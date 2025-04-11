from datetime import datetime, timedelta

MAX_DUTY_HOURS_PER_DAY = 10  # AI Rule Threshold

def check_violation(logs):
    """
    Check if total duty time exceeds 10 hours for a given day.
    Input: list of logs for a single pilot on a given day.
    Each log is a tuple (duty_start, duty_end)
    Output: True if violation, else False
    """
    total_duration = timedelta()

    for duty_start, duty_end in logs:
        start_dt = datetime.fromisoformat(duty_start)
        end_dt = datetime.fromisoformat(duty_end)
        total_duration += (end_dt - start_dt)

    return total_duration > timedelta(hours=MAX_DUTY_HOURS_PER_DAY)

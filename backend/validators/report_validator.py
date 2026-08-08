def validate_report(df):

    if df.empty:

        return False, "No session data available."

    return True, "Valid"
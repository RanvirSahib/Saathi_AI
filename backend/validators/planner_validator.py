def validate_study_plan(plan):

    if not plan:

        return False, "Study plan is empty."

    if len(plan) < 100:

        return False, "Study plan is too short."

    return True, "Valid"
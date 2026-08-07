from backend.services.dashboard_service import (
    get_dashboard_data
)

from backend.analytics.student_analytics import (
    get_student_analytics
)


def analytics():

    df = get_dashboard_data()

    return get_student_analytics(df)
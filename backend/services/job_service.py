from backend.repositories.job_repository import (
    create_job,
    update_status
)

from backend.repositories.job_repository import get_all_jobs


def start_analysis_job():

    job = create_job("Camera Analysis")

    update_status(

        job.id,

        "Running"

    )

    return job.id


def finish_analysis_job(job_id):

    update_status(

        job_id,

        "Completed"

    )

def fetch_jobs():

    return get_all_jobs()

def fail_analysis_job(job_id, error):

    update_status(

        job_id,

        "Failed"

    )
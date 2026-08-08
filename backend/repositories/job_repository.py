from backend.database.db import SessionLocal
from backend.models.analysis_job import AnalysisJob


def create_job(name):

    db = SessionLocal()

    try:

        job = AnalysisJob(

            job_name=name,

            status="Pending"

        )

        db.add(job)

        db.commit()

        db.refresh(job)

        return job

    finally:

        db.close()


def update_status(job_id, status):

    db = SessionLocal()

    try:

        job = db.query(AnalysisJob).filter(
            AnalysisJob.id == job_id
        ).first()

        if job:

            job.status = status

            db.commit()

    finally:

        db.close()



def get_all_jobs():

    db = SessionLocal()

    try:

        return (

            db.query(AnalysisJob)

            .order_by(AnalysisJob.created_at.desc())

            .all()

        )

    finally:

        db.close()
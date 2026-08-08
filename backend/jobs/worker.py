import threading

from backend.jobs.queue import (
    analysis_queue
)


def process_jobs():

    while True:

        job = analysis_queue.get()

        print(
            "Processing Job:",
            job
        )

        analysis_queue.task_done()


worker = threading.Thread(

    target=process_jobs,

    daemon=True

)

worker.start()
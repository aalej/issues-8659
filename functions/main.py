# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn,tasks_fn
from firebase_admin import initialize_app

# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world from python!")

@tasks_fn.on_task_dispatched()
def backup_a_pod(req: tasks_fn.CallableRequest) -> str:
    """Grabs Astronomy Photo of the Day (APOD) using NASA's API."""
from celery import Celery
from celery.decorators import periodic_task
from datetime import timedelta
from local_settings import RABBITMQ_PORT, RABBITMQ_DEFAULT_USER, \
                           RABBITMQ_DEFAULT_PASS, RABBITMQ_DEFAULT_HOST
from task_requests import TaskRequests

app = Celery("tasks", broker="amqp://{}:{}@{}:{}".format(RABBITMQ_DEFAULT_USER,
                                                         RABBITMQ_DEFAULT_PASS,
                                                         RABBITMQ_DEFAULT_HOST,
                                                         RABBITMQ_PORT))


@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    hour = TaskRequests()._get_previus_hour()
    ads = TaskRequests().get_current_hour_active_ads(hour)

    post_data = {}
    for ad in ads:
        post_data[str(ad["id"])] = {}
        ad_events_data = TaskRequests().get_events_data(hour, ad["id"])

        for event in ad_events_data:
            if str(event["station_id"]) not in post_data[str(ad["id"])]:
                post_data[str(ad["id"])][str(event["station_id"])] = {"hour": hour,
                                                                      "viewer": 0,
                                                                      "holder": 0,
                                                                      "btn_usr": 0,
                                                                      "reached": 0
                                                                      }
            post_data[str(ad["id"])][str(event["station_id"])][event["type"]] += 1

        for station_key in post_data[str(ad["id"])]:
            feedback = {
                "ad_id": ad["id"],
                "station_id": int(station_key),
                "hour": hour,
                "viewers": post_data[str(ad["id"])][station_key]["viewer"],
                "holders": post_data[str(ad["id"])][station_key]["holder"],
                "button_usrs": post_data[str(ad["id"])][station_key]["btn_usr"],
                "reached": post_data[str(ad["id"])][station_key]["reached"]
            }
            TaskRequests().post_feedback_data(feedback)

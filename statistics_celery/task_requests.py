import requests
import os
from datetime import datetime, timedelta
import json


class TaskRequests(object):
    def __init__(self):
        self.token = os.environ.get("WORKER_TOKEN")
        self.screenbit_api_events_url = os.environ.get("SCREENBIT_API_EVENTS_URL")
        self.screenbit_api_active_ads_url = os.environ.get("SCREENBIT_API_ACTIVE_ADS_URL")
        self.screenbit_api_feedbacks_url = os.environ.get("SCREENBIT_API_FEEDBACKS_URL")

    def _create_request_header(self):
        return {'Authorization': 'BIT_TOKEN {}'.format(self.token)}

    def _url_assembler(self, url=None, hour=None, ad_id=None):
        url += "?"
        if hour:
            url += "hour=" + hour + "&"
        if ad_id:
            url += "ad_id=" + str(ad_id) + "&"
        return url

    def _get_previus_hour(self):
        date = datetime.now() - timedelta(hours=1)
        str_hour = str(date.hour)
        if len(str_hour) == 1:
            str_hour = "0" + str_hour
        return str_hour

    def _check_response(self, response):
        if response.status_code == 404:
            return False
        else:
            return True
    """                             REQUESTS                                 """

    def get_current_hour_active_ads(self, hour):
        """ get all active ads for present hour """
        headers = self._create_request_header()
        url = self._url_assembler(self.screenbit_api_active_ads_url, hour)

        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.content.decode())
        return dict_data

    def get_events_data(self, hour, ad_id):
        """ Request will return all ad events for present hour """
        headers = self._create_request_header()
        url = self._url_assembler(self.screenbit_api_events_url, hour, ad_id)

        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.content.decode())
        return dict_data

    def post_feedback_data(self, data):
        headers = self._create_request_header()
        url = self._url_assembler(self.screenbit_api_feedbacks_url)

        response = requests.post(url, headers=headers, data=data)
        return response

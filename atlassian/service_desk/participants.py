import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Participants(ServiceDesk):
    def get_request_participants(self, issue_id_or_key, start=0, limit=50):
        """
        Get request participants

        :param issue_id_or_key: str
        :param start: OPTIONAL: int
        :param limit: OPTIONAL: int
        :return: Request participants
        """
        url = 'rest/servicedeskapi/request/{}/participant'.format(issue_id_or_key)
        params = {}
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return (self.get(url, params=params) or {}).get('values')

    def add_request_participants(self, issue_id_or_key, users_list):
        """
        Add users as participants to an existing customer request
        The calling user must have permission to manage participants for this customer request

        :param issue_id_or_key: str
        :param users_list: list
        :return:
        """
        url = 'rest/servicedeskapi/request/{}/participant'.format(issue_id_or_key)
        data = {'usernames': users_list}

        return self.post(url, data=data)

    def remove_request_participants(self, issue_id_or_key, users_list):
        """
        Remove participants from an existing customer request
        The calling user must have permission to manage participants for this customer request

        :param issue_id_or_key: str
        :param users_list: list
        :return:
        """
        url = 'rest/servicedeskapi/request/{}/participant'.format(issue_id_or_key)
        data = {'usernames': users_list}

        return self.delete(url, data=data)

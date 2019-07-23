import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Approvals(ServiceDesk):
    def get_approvals(self, issue_id_or_key, start=0, limit=50):
        """
        Get all approvals on a request, for a given request ID/Key

        :param issue_id_or_key: str
        :param start: OPTIONAL: int
        :param limit: OPTIONAL: int
        :return:
        """
        url = 'rest/servicedeskapi/request/{}/approval'.format(issue_id_or_key)
        params = {}
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return (self.get(url, headers=self.experimental_headers, params=params) or {}).get('values')

    def get_approval_by_id(self, issue_id_or_key, approval_id):
        """
        Get an approval for a given approval ID

        :param issue_id_or_key: str
        :param approval_id: str
        :return:
        """
        url = 'rest/servicedeskapi/request/{0}/approval/{1}'.format(issue_id_or_key, approval_id)

        return self.get(url, headers=self.experimental_headers)

    def answer_approval(self, issue_id_or_key, approval_id, decision):
        """
        Answer a pending approval

        :param issue_id_or_key: str
        :param approval_id: str
        :param decision: str
        :return:
        """
        url = 'rest/servicedeskapi/request/{0}/approval/{1}'.format(issue_id_or_key, approval_id)
        data = {'decision': decision}

        return self.post(url, headers=self.experimental_headers, data=data)

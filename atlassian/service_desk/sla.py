import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class SLA(ServiceDesk):
    def get_sla(self, issue_id_or_key, start=0, limit=50):
        """
        Get the SLA information for a customer request for a given request ID or key
        A request can have zero or more SLA values
        IMPORTANT: The calling user must be an agent

        :param issue_id_or_key: str
        :param start: OPTIONAL: int
        :param limit: OPTIONAL: int
        :return: SLA information
        """
        url = 'rest/servicedeskapi/request/{}/sla'.format(issue_id_or_key)
        params = {}
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return (self.get(url, params=params) or {}).get('values')

    def get_sla_by_id(self, issue_id_or_key, sla_id):
        """
        Get the SLA information for a customer request for a given request ID or key and SLA metric ID
        IMPORTANT: The calling user must be an agent

        :param issue_id_or_key: str
        :param sla_id: str
        :return: SLA information
        """
        url = 'rest/servicedeskapi/request/{0}/sla/{1}'.format(issue_id_or_key, sla_id)

        return self.get(url)

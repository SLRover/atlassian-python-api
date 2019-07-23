import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Queues(ServiceDesk):
    def get_queue_settings(self, project_key):
        """
        Get queue settings on project

        :param project_key: str
        :return:
        """
        url = 'rest/servicedeskapi/queues/{}'.format(project_key)

        return self.get(url, headers=self.experimental_headers)

    def get_queues(self, service_desk_id, include_count=False, start=0, limit=50):
        """
        Returns a page of queues defined inside a service desk, for a given service desk ID.
        The returned queues will include an issue count for each queue (represented in issueCount field)
        if the query param includeCount is set to true (defaults to false).

        Permissions: The calling user must be an agent of the given service desk.

        :param service_desk_id: str
        :param include_count: bool
        :param start: int
        :param limit: int
        :return: a page of queues
        """
        url = 'rest/servicedeskapi/servicedesk/{}/queue'.format(service_desk_id)
        params = {}

        if include_count is not None:
            params['includeCount'] = bool(include_count)
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return self.get(url, headers=self.experimental_headers, params=params)

    def get_issues_in_queue(self, service_desk_id, queue_id, start=0, limit=50):
        """
        Returns a page of issues inside a queue for a given queue ID.
        Only fields that the queue is configured to show are returned.
        For example, if a queue is configured to show only Description and Due Date,
        then only those two fields are returned for each issue in the queue.

        Permissions: The calling user must have permission to view the requested queue,
        i.e. they must be an agent of the service desk that the queue belongs to.

        :param service_desk_id: str
        :param queue_id: str
        :param start: int
        :param limit: int
        :return: a page of issues
        """
        url = 'rest/servicedeskapi/servicedesk/{0}/queue/{1}/issue'.format(service_desk_id, queue_id)
        params = {}

        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return self.get(url, headers=self.experimental_headers, params=params)

import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Transitions(ServiceDesk):
    def perform_transition(self, issue_id_or_key, transition_id, comment=None):
        """
        Perform a customer transition for a given request and transition ID.
        An optional comment can be included to provide a reason for the transition.

        :param issue_id_or_key: str
        :param transition_id: str
        :param comment: OPTIONAL: str
        :return: None
        """
        log.warning('Performing transition...')
        data = {'id': transition_id, 'additionalComment': {'body': comment}}
        url = 'rest/servicedeskapi/request/{}/transition'.format(issue_id_or_key)

        return self.post(url, headers=self.experimental_headers, data=data)

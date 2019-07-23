import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Info(ServiceDesk):
    def get_info(self):
        """ Get info about Service Desk app """

        return self.get('rest/servicedeskapi/info')

    def get_service_desks(self):
        """
        Returns all service desks in the Jira Service Desk application
        with the option to include archived service desks

        :return: Service Desks
        """
        service_desks_list = self.get('rest/servicedeskapi/servicedesk')

        return service_desks_list.get('values')

    def get_service_desk_by_id(self, service_desk_id):
        """
        Returns the service desk for a given service desk ID

        :param service_desk_id: str
        :return: Service Desk
        """

        return self.get('rest/servicedeskapi/servicedesk/{}'.format(service_desk_id))

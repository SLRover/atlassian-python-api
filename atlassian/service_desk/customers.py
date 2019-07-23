import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Customers(ServiceDesk):
    def create_customer(self, full_name, email):
        """
        Creating customer user

        :param full_name: str
        :param email: str
        :return: New customer
        """
        log.warning('Creating customer...')
        data = {'fullName': full_name, 'email': email}

        return self.post('rest/servicedeskapi/customer', headers=self.experimental_headers, data=data)

    def get_customer_request(self, issue_id_or_key):
        """
        Get single request

        :param issue_id_or_key: str
        :return: Customer request
        """

        return self.get('rest/servicedeskapi/request/{}'.format(issue_id_or_key))

    def get_my_customer_requests(self):
        """ Returning requests where you are the assignee """

        return (self.get('rest/servicedeskapi/request') or {}).get('values')

    def create_customer_request(self, service_desk_id, request_type_id, values_dict, raise_on_behalf_of=None):
        """
        Creating customer request

        :param service_desk_id: str
        :param request_type_id: str
        :param values_dict: str
        :param raise_on_behalf_of: str
        :return: New request
        """
        log.warning('Creating request...')
        data = {
            "serviceDeskId": service_desk_id,
            "requestTypeId": request_type_id,
            "requestFieldValues": values_dict
        }

        if raise_on_behalf_of:
            data["raiseOnBehalfOf"] = raise_on_behalf_of

        return self.post('rest/servicedeskapi/request', data=data)

    def get_customer_request_status(self, issue_id_or_key):
        """
        Get customer request status name

        :param issue_id_or_key: str
        :return: Status name
        """
        request = (self.get('rest/servicedeskapi/request/{}/status'.format(issue_id_or_key)) or {}).get('values')
        status = (request[0].get('status') or {})

        return status

    def get_customer_transitions(self, issue_id_or_key):
        """
        Returns a list of transitions that customers can perform on the request

        :param issue_id_or_key: str
        :return:
        """
        url = 'rest/servicedeskapi/request/{}/transition'.format(issue_id_or_key)

        return self.get(url, headers=self.experimental_headers)

    def add_customers(self, service_desk_id, list_of_usernames):
        """
        Adds one or more existing customers to the given service desk.
        If you need to create a customer, see Create customer method.

        Administer project permission is required, or agents if public signups
        and invites are enabled for the Service Desk project.

        :param service_desk_id: str
        :param list_of_usernames: list
        :return: the customers added to the service desk
        """
        url = 'rest/servicedeskapi/servicedesk/{}/customer'.format(service_desk_id)
        data = {'usernames': list_of_usernames}

        return self.post(url, headers=self.experimental_headers, data=data)

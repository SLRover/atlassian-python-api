import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Organizations(ServiceDesk):
    def get_organisations(self, service_desk_id=None, start=0, limit=50):
        """
        Returns a list of organizations in the Jira instance. If the user is not an agent,
        the resource returns a list of organizations the user is a member of.

        :param service_desk_id: OPTIONAL: str Get organizations from single Service Desk
        :param start: OPTIONAL: int The starting index of the returned objects.
                     Base index: 0. See the Pagination section for more details.
        :param limit: OPTIONAL: int The maximum number of users to return per page.
                     Default: 50. See the Pagination section for more details.
        :return:
        """
        url_without_sd_id = 'rest/servicedeskapi/organization'
        url_with_sd_id = 'rest/servicedeskapi/servicedesk/{}/organization'.format(service_desk_id)
        params = {}
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        if service_desk_id is None:
            return self.get(url_without_sd_id, headers=self.experimental_headers, params=params)
        else:
            return self.get(url_with_sd_id, headers=self.experimental_headers, params=params)

    def get_organization(self, organization_id):
        """
        Get an organization for a given organization ID

        :param organization_id: str
        :return: Organization
        """
        url = 'rest/servicedeskapi/organization/{}'.format(organization_id)

        return self.get(url, headers=self.experimental_headers)

    def get_users_in_organization(self, organization_id, start=0, limit=50):
        """
        Get all the users of a specified organization

        :param organization_id: str
        :param start: OPTIONAL: int
        :param limit: OPTIONAL: int
        :return: Users list in organization
        """
        url = 'rest/servicedeskapi/organization/{}/user'.format(organization_id)
        params = {}
        if start is not None:
            params['start'] = int(start)
        if limit is not None:
            params['limit'] = int(limit)

        return self.get(url, headers=self.experimental_headers, params=params)

    def create_organization(self, name):
        """
        To create an organization Jira administrator global permission or agent permission is required
        depending on the settings

        :param name: str
        :return: Organization data
        """
        log.warning('Creating organization...')
        url = 'rest/servicedeskapi/organization'
        data = {'name': name}

        return self.post(url, headers=self.experimental_headers, data=data)

    def add_organization(self, service_desk_id, organization_id):
        """
        Adds an organization to a servicedesk for a given servicedesk ID and organization ID

        :param service_desk_id: str
        :param organization_id: int
        :return:
        """
        log.warning('Adding organization...')
        url = 'rest/servicedeskapi/servicedesk/{}/organization'.format(service_desk_id)
        data = {'organizationId': organization_id}

        return self.post(url, headers=self.experimental_headers, data=data)

    def remove_organization(self, service_desk_id, organization_id):
        """
        Removes an organization from a servicedesk for a given servicedesk ID and organization ID

        :param service_desk_id: str
        :param organization_id: int
        :return:
        """
        log.warning('Removing organization...')
        url = 'rest/servicedeskapi/servicedesk/{}/organization'.format(service_desk_id)
        data = {'organizationId': organization_id}

        return self.delete(url, headers=self.experimental_headers, data=data)

    def delete_organization(self, organization_id):
        """
        Deletes an organization for a given organization ID

        :param organization_id:
        :return:
        """
        log.warning('Deleting organization...')
        url = 'rest/servicedeskapi/organization/{}'.format(organization_id)

        return self.delete(url, headers=self.experimental_headers)

    def add_users_to_organization(self, organization_id, users_list):
        """
        Adds users to an organization
        users_list is a list of strings

        :param organization_id: str
        :param users_list: list
        :return:
        """
        log.warning('Adding users...')
        url = 'rest/servicedeskapi/organization/{}/user'.format(organization_id)
        data = {'usernames': users_list}

        return self.post(url, headers=self.experimental_headers, data=data)

    def remove_users_from_organization(self, organization_id, users_list):
        """
        Removes users from an organization
        users_list is a list of strings

        :param organization_id: str
        :param users_list: list
        :return:
        """
        log.warning('Removing users...')
        url = 'rest/servicedeskapi/organization/{}/user'.format(organization_id)
        data = {'usernames': users_list}

        return self.delete(url, headers=self.experimental_headers, data=data)

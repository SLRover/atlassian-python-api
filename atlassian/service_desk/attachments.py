import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Attachments(ServiceDesk):
    def create_attachment(self, service_desk_id, issue_id_or_key, filename, public=True, comment=None):
        """
        Add attachment as a comment.

        Setting attachment visibility is dependent on the user's permission. For example,
        Agents can create either public or internal attachments, while Unlicensed users can only create internal
        attachments, and Customers can only create public attachments.

        An additional comment may be provided which will be prepended to the attachments.

        :param service_desk_id: str
        :param issue_id_or_key: str
        :param filename: str, name, if file in current directory or full path to file
        :param public: OPTIONAL: bool (default is True)
        :param comment: OPTIONAL: str (default is None)
        :return: Request info
        """
        log.warning('Creating attachment...')

        # Create temporary attachment
        temp_attachment_id = self.attach_temporary_file(service_desk_id, filename)

        # Add attachments
        return self.add_attachment(issue_id_or_key, temp_attachment_id, public, comment)

    def attach_temporary_file(self, service_desk_id, filename):
        """
        Create temporary attachment, which can later be converted into permanent attachment

        :param service_desk_id: str
        :param filename: str
        :return: Temporary Attachment ID
        """
        headers = {'X-Atlassian-Token': 'no-check', 'X-ExperimentalApi': 'opt-in'}
        url = 'rest/servicedeskapi/servicedesk/{}/attachTemporaryFile'.format(service_desk_id)

        with open(filename, 'rb') as file:
            result = self.post(url, headers=headers, files={'file': file}).get('temporaryAttachments')
            temp_attachment_id = result[0].get('temporaryAttachmentId')

            return temp_attachment_id

    def add_attachment(self, issue_id_or_key, temp_attachment_id, public=True, comment=None):
        """
        Adds temporary attachment that were created using attach_temporary_file function to a customer request

        :param issue_id_or_key: str
        :param temp_attachment_id: str, ID from result attach_temporary_file function
        :param public: bool (default is True)
        :param comment: str (default is None)
        :return:
        """
        log.warning('Adding attachment')
        data = {
            'temporaryAttachmentIds': [temp_attachment_id],
            'public': public,
            'additionalComment': {'body': comment}
        }
        url = 'rest/servicedeskapi/request/{}/attachment'.format(issue_id_or_key)

        return self.post(url, headers=self.experimental_headers, data=data)

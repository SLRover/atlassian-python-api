import logging
from atlassian.service_desk import ServiceDesk

log = logging.getLogger(__name__)


class Comments(ServiceDesk):
    def create_request_comment(self, issue_id_or_key, body, public=True):
        """
        Creating request comment

        :param issue_id_or_key: str
        :param body: str
        :param public: OPTIONAL: bool (default is True)
        :return: New comment
        """
        log.warning('Creating comment...')
        data = {"body": body, "public": public}

        return self.post('rest/servicedeskapi/request/{}/comment'.format(issue_id_or_key), data=data)

    def get_request_comments(self, issue_id_or_key):
        """
        Get all comments in issue

        :param issue_id_or_key: str
        :return: Issue comments
        """

        return self.get('rest/servicedeskapi/request/{}/comment'.format(issue_id_or_key))

    def get_request_comment_by_id(self, issue_id_or_key, comment_id):
        """
        Get single comment by ID

        :param issue_id_or_key: str
        :param comment_id: str
        :return: Single comment
        """

        return self.get('rest/servicedeskapi/request/{0}/comment/{1}'.format(issue_id_or_key, comment_id))

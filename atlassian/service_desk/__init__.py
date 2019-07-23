from atlassian.rest_client import AtlassianRestAPI
from .info import Info
from .approvals import Approvals
from .attachments import Attachments
from .comments import Comments
from .customers import Customers
from .organisations import Organizations
from .participants import Participants
from .queues import Queues
from .sla import SLA
from .transitions import Transitions


class ServiceDesk(AtlassianRestAPI):
    pass
    # info = Info
    # approvals = Approvals
    # attachments = Attachments
    # comments = Comments
    # customers = Customers
    # organisations = Organizations
    # participants = Participants
    # queues = Queues
    # sla = SLA
    # transitions = Transitions

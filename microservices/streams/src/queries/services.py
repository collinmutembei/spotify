from dependency_injector.wiring import (
    Provide,
)

from src.queries.repository import (
    StreamQueryServiceRepository,
)

from minos.aggregate import (
    Event,
)
from minos.common import (
    Inject,
)
from minos.cqrs import (
    QueryService,
)
from minos.networks import (
    Request,
    Response,
    ResponseException,
    enroute,
)


class StreamQueryService(QueryService):
    """StreamQueryService class."""

    @Inject()
    def __init__(self, repository: StreamQueryServiceRepository, **kwargs):
        super().__init__(**kwargs)
        self.repository = repository

    @enroute.rest.query("/streams", "GET")
    async def get_stream(self, request: Request) -> Response:
        """Get a Stream instance.

        :param request: A request instance..
        :return: A response exception.
        """
        raise ResponseException("Not implemented yet!")

    @enroute.broker.event("StreamCreated")
    async def stream_created(self, request: Request) -> None:
        """Handle the Stream creation events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("StreamUpdated")
    async def stream_updated(self, request: Request) -> None:
        """Handle the Stream update events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("StreamDeleted")
    async def stream_deleted(self, request: Request) -> None:
        """Handle the Stream deletion events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)
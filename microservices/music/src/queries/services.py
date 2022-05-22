from dependency_injector.wiring import (
    Provide,
)

from src.queries.repository import (
    SongQueryServiceRepository,
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


class SongQueryService(QueryService):
    """SongQueryService class."""

    @Inject()
    def __init__(self, repository: SongQueryServiceRepository, **kwargs):
        super().__init__(**kwargs)
        self.repository = repository

    @enroute.rest.query("/songs", "GET")
    async def get_song(self, request: Request) -> Response:
        """Get a Song instance.

        :param request: A request instance..
        :return: A response exception.
        """
        raise ResponseException("Not implemented yet!")

    @enroute.broker.event("SongCreated")
    async def song_created(self, request: Request) -> None:
        """Handle the Song creation events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("SongUpdated")
    async def song_updated(self, request: Request) -> None:
        """Handle the Song update events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("SongDeleted")
    async def song_deleted(self, request: Request) -> None:
        """Handle the Song deletion events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)
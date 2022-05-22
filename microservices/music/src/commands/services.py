from minos.cqrs import (
    CommandService,
)
from minos.networks import (
    Request,
    Response,
    ResponseException,
    enroute,
)

from ..aggregates import (
    SongAggregate,
)


class SongCommandService(CommandService):
    """SongCommandService class."""

    @enroute.rest.command("/songs", "POST")
    @enroute.broker.command("CreateSong")
    async def create_song(self, request: Request) -> Response:
        """Create a new ``Song`` instance.

        :param request: The ``Request`` instance.
        :return: A ``Response`` instance.
        """
        try:
            music = await SongAggregate.create()
            return Response(music)
        except Exception as exc:
            raise ResponseException(f"An error occurred during Song creation: {exc}")
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
    StreamAggregate,
)


class StreamCommandService(CommandService):
    """StreamCommandService class."""

    @enroute.rest.command("/streams", "POST")
    @enroute.broker.command("CreateStream")
    async def create_stream(self, request: Request) -> Response:
        """Create a new ``Stream`` instance.

        :param request: The ``Request`` instance.
        :return: A ``Response`` instance.
        """
        try:
            stream = await StreamAggregate.create()
            return Response(stream)
        except Exception as exc:
            raise ResponseException(f"An error occurred during Stream creation: {exc}")
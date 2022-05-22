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
    PersonAggregate,
)


class PersonCommandService(CommandService):
    """PersonCommandService class."""

    @enroute.rest.command("/persons", "POST")
    @enroute.broker.command("CreatePerson")
    async def create_person(self, request: Request) -> Response:
        """Create a new ``Person`` instance.

        :param request: The ``Request`` instance.
        :return: A ``Response`` instance.
        """
        try:
            people = await PersonAggregate.create()
            return Response(people)
        except Exception as exc:
            raise ResponseException(f"An error occurred during Person creation: {exc}")
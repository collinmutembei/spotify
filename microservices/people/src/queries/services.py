from dependency_injector.wiring import (
    Provide,
)

from src.queries.repository import (
    PersonQueryServiceRepository,
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


class PersonQueryService(QueryService):
    """PersonQueryService class."""

    @Inject()
    def __init__(self, repository: PersonQueryServiceRepository, **kwargs):
        super().__init__(**kwargs)
        self.repository = repository

    @enroute.rest.query("/persons", "GET")
    async def get_person(self, request: Request) -> Response:
        """Get a Person instance.

        :param request: A request instance..
        :return: A response exception.
        """
        raise ResponseException("Not implemented yet!")

    @enroute.broker.event("PersonCreated")
    async def person_created(self, request: Request) -> None:
        """Handle the Person creation events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("PersonUpdated")
    async def person_updated(self, request: Request) -> None:
        """Handle the Person update events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("PersonDeleted")
    async def person_deleted(self, request: Request) -> None:
        """Handle the Person deletion events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)
from dependency_injector.wiring import (
    Provide,
)

from src.queries.repository import (
    AccountQueryServiceRepository,
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


class AccountQueryService(QueryService):
    """AccountQueryService class."""

    @Inject()
    def __init__(self, repository: AccountQueryServiceRepository, **kwargs):
        super().__init__(**kwargs)
        self.repository = repository

    @enroute.rest.query("/accounts", "GET")
    async def get_account(self, request: Request) -> Response:
        """Get a Account instance.

        :param request: A request instance..
        :return: A response exception.
        """
        raise ResponseException("Not implemented yet!")

    @enroute.broker.event("AccountCreated")
    async def account_created(self, request: Request) -> None:
        """Handle the Account creation events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("AccountUpdated")
    async def account_updated(self, request: Request) -> None:
        """Handle the Account update events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)

    @enroute.broker.event("AccountDeleted")
    async def account_deleted(self, request: Request) -> None:
        """Handle the Account deletion events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        event: Event = await request.content()
        print(event)
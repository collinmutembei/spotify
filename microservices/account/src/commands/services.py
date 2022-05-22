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
    AccountAggregate,
)


class AccountCommandService(CommandService):
    """AccountCommandService class."""

    @enroute.rest.command("/accounts", "POST")
    @enroute.broker.command("CreateAccount")
    async def create_account(self, request: Request) -> Response:
        """Create a new ``Account`` instance.

        :param request: The ``Request`` instance.
        :return: A ``Response`` instance.
        """
        try:
            account = await AccountAggregate.create()
            return Response(account)
        except Exception as exc:
            raise ResponseException(f"An error occurred during Account creation: {exc}")
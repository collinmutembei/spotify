from uuid import (
    UUID,
)

from minos.aggregate import (
    Aggregate,
    RootEntity,
)


class Account(RootEntity):
    """Account RootEntity class."""


class AccountAggregate(Aggregate[Account]):
    """AccountAggregate class."""

    @staticmethod
    async def create() -> UUID:
        """Create a new instance."""
        accounts = await Account.create()
        return accounts
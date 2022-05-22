from uuid import (
    UUID,
)

from minos.aggregate import (
    Aggregate,
    RootEntity,
)


class Person(RootEntity):
    """Person RootEntity class."""


class PersonAggregate(Aggregate[Person]):
    """PersonAggregate class."""

    @staticmethod
    async def create() -> UUID:
        """Create a new instance."""
        people = await Person.create()
        return people
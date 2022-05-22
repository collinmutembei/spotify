from uuid import (
    UUID,
)

from minos.aggregate import (
    Aggregate,
    RootEntity,
)


class Stream(RootEntity):
    """Stream RootEntity class."""


class StreamAggregate(Aggregate[Stream]):
    """StreamAggregate class."""

    @staticmethod
    async def create() -> UUID:
        """Create a new instance."""
        stream = await Stream.create()
        return stream
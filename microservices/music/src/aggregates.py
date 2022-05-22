from uuid import (
    UUID,
)

from minos.aggregate import (
    Aggregate,
    RootEntity,
)


class Song(RootEntity):
    """Song RootEntity class."""


class SongAggregate(Aggregate[Song]):
    """SongAggregate class."""

    @staticmethod
    async def create() -> UUID:
        """Create a new instance."""
        music = await Song.create()
        return music
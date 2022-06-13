import sys
import unittest

from src import (
    Song,
    SongCommandService,
)

from minos.networks import (
    InMemoryRequest,
    Response,
)
from tests.utils import (
    build_dependency_injector,
)


class TestSongCommandService(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire_and_setup_injections()

    async def asyncTearDown(self) -> None:
        await self.injector.unwire_and_destroy_injections()

    def test_constructor(self):
        service = SongCommandService()
        self.assertIsInstance(service, SongCommandService)

    async def test_create_song(self):
        service = SongCommandService()

        request = InMemoryRequest({})
        response = await service.create_song(request)

        self.assertIsInstance(response, Response)

        observed = await response.content()
        expected = Song(
            created_at=observed.created_at,
            updated_at=observed.updated_at,
            uuid=observed.uuid,
            version=observed.version,
        )

        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
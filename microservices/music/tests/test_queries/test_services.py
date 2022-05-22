import sys
import unittest

from src import (
    SongQueryService,
)

from tests.utils import (
    build_dependency_injector,
)


class TestSongQueryService(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire_and_setup_injections()

    async def asyncTearDown(self) -> None:
        await self.injector.unwire_and_destroy_injections()

    def test_constructor(self):
        service = SongQueryService()
        self.assertIsInstance(service, SongQueryService)


if __name__ == '__main__':
    unittest.main()
import sys
import unittest

from src import (
    Song,
)

from tests.utils import (
    build_dependency_injector,
)


class TestSong(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire_and_setup_injections()

    async def asyncTearDown(self) -> None:
        await self.injector.unwire_and_destroy_injections()

    def test_constructor(self):
        obj = Song()
        self.assertIsInstance(obj, Song)


if __name__ == '__main__':
    unittest.main()
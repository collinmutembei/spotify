import sys
import unittest

from src import (
    Person,
)

from tests.utils import (
    build_dependency_injector,
)


class TestPerson(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire_and_setup_injections()

    async def asyncTearDown(self) -> None:
        await self.injector.unwire_and_destroy_injections()

    def test_constructor(self):
        obj = Person()
        self.assertIsInstance(obj, Person)


if __name__ == '__main__':
    unittest.main()
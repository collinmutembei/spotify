import sys
import unittest

from src import (
    Person,
    PersonCommandService,
)

from minos.networks import (
    InMemoryRequest,
    Response,
)
from tests.utils import (
    build_dependency_injector,
)


class TestPersonCommandService(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire_and_setup_injections()

    async def asyncTearDown(self) -> None:
        await self.injector.unwire_and_destroy_injections()

    def test_constructor(self):
        service = PersonCommandService()
        self.assertIsInstance(service, PersonCommandService)

    async def test_create_person(self):
        service = PersonCommandService()

        request = InMemoryRequest({})
        response = await service.create_person(request)

        self.assertIsInstance(response, Response)

        observed = await response.content()
        expected = Person(
            created_at=observed.created_at,
            updated_at=observed.updated_at,
            uuid=observed.uuid,
            version=observed.version,
        )

        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
from minos.common import (
    Config,
    Injectable,
    SetupMixin,
)
from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    sessionmaker,
)

from src.queries.models import (
    Base,
)

@Injectable("account_repository")
class AccountQueryServiceRepository(SetupMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/account_query_db".format(**kwargs))
        self.session = sessionmaker(bind=self.engine)()

    async def _setup(self) -> None:
        Base.metadata.create_all(self.engine)

    @classmethod
    def _from_config(cls, *args, config: Config, **kwargs):
        return cls(*args, **(config.get_database_by_name("query")) | kwargs)
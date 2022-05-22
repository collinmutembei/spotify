__author__ = ""
__email__ = ""
__version__ = "1.0.0"

from .aggregates import (
    Person,
)
from .cli import (
    main,
)
from .commands import (
    PersonCommandService,
)
from .queries import (
    PersonQueryService,
    PersonQueryServiceRepository,
)
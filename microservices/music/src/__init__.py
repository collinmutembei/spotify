__author__ = ""
__email__ = ""
__version__ = "1.0.0"

from .aggregates import (
    Song,
)
from .cli import (
    main,
)
from .commands import (
    SongCommandService,
)
from .queries import (
    SongQueryService,
    SongQueryServiceRepository,
)
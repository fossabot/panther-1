from collections import defaultdict
from dataclasses import dataclass
from datetime import timedelta

throttling_storage = defaultdict(int)


@dataclass(repr=False, eq=False, match_args=False)
class Throttling:
    rate: int
    duration: timedelta

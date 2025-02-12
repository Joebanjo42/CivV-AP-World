from dataclasses import dataclass
from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle

class ProgressionStyle(Choice):
    display_name = "Progression Style"


@dataclass
class CivVOptions(PerGameCommonOptions):
    pass
from typing import Dict, List, NamedTuple

class CivVRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, CivVRegionData] = {
    "Menu" : CivVRegionData(["Default"])
}
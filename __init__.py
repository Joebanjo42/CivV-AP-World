# world/mygame/__init__.py

# import settings
from typing import List, Optional
from .Tech_Array import list_of_tech_keys
from .options import CivVOptions  # the options we defined earlier
from .items import CivVItem, item_table  # data used below to add items to the World
from .locations import CivVLocation, location_table_data  # same as above
from .regions import region_data_table
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess

# class MyGameSettings(settings.Group):
#     class RomFile(settings.SNESRomPath):
#         """Insert help text for host.yaml here."""

#     rom_file: RomFile = RomFile("CivilizationV.sfc")

base_id = 1
offset = 140319

def run_client(url: Optional[str] = None):
    print("Running CivV Client")
    from .CivVClient import main
    launch_subprocess(main, name="CivV Client")

components.append(
    Component("CivV Client", func=run_client, component_type=Type.CLIENT)
)


class CivVWorld(World):
    """Insert description of the world/game here."""
    game = "Civilization V"  # name of the game/world
    options_dataclass = CivVOptions  # options the player can set
    options: CivVOptions  # typing hints for option results
    # settings: typing.ClassVar[MyGameSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(item_table.keys(), base_id + offset)}
    location_name_to_id = {name: id for
                           id, name in enumerate(location_table_data.keys(), base_id + offset)}
    
    def create_item(self, name) -> CivVItem:
        return CivVItem(name, item_table[name][1], self.item_name_to_id[name], self.player)
    
    def create_items(self) -> None:
        item_pool: List[CivVItem] = []
        item_pool.append(self.create_item("Pottery"))
        for name, item in item_table.items():
            item_pool.append(self.create_item(name))
        self.multiworld.itempool += item_pool
    
    def create_regions(self) -> None:
        menu_reigion = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_reigion)

        main_region = Region("Main", self.player, self.multiworld)
        main_region.add_locations({"Pottery": 140320}, CivVLocation)
        for location, id in location_table_data.items():
            main_region.add_locations({location : id +  offset}, CivVLocation)
        self.multiworld.regions.append(main_region)

        menu_reigion.connect(main_region)
        return
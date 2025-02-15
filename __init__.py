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
        for name, item in item_table.items():
            item_pool.append(self.create_item(name))
        self.multiworld.itempool += item_pool
    
    def create_regions(self) -> None:
        menu_reigion = Region("Menu", self.player, self.multiworld)
        ancient_region = Region("Ancient", self.player, self.multiworld)
        classical_region = Region("Classical", self.player, self.multiworld)
        medieval_region = Region("Medieval", self.player, self.multiworld)
        renaissance_region = Region("Renaissance", self.player, self.multiworld)
        industrial_region = Region("Industrial", self.player, self.multiworld)
        modern_region = Region("Modern", self.player, self.multiworld)
        postmodern_region = Region("Postmodern", self.player, self.multiworld)
        future_region = Region("Future", self.player, self.multiworld)

        # for location, era in enumerate({location : era})

        self.multiworld.regions.append(menu_reigion)

        main_region = Region("Main", self.player, self.multiworld)
        for location, id in location_table_data.items():
            if id[1] == 1:
                ancient_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 2:
                classical_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 3:
                medieval_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 4:
                renaissance_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 5:
                industrial_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 6:
                modern_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 7:
                postmodern_region.addlocations({location : id + offset}, CivVLocation)
            if id[1] == 8:
                future_region.addlocations({location : id + offset}, CivVLocation)
        self.multiworld.regions.append(ancient_region)
        self.multiworld.regions.append(classical_region)
        self.multiworld.regions.append(medieval_region)
        self.multiworld.regions.append(renaissance_region)
        self.multiworld.regions.append(industrial_region)
        self.multiworld.regions.append(modern_region)
        self.multiworld.regions.append(postmodern_region)
        self.multiworld.regions.append(future_region)


        menu_reigion.connect(ancient_region)
        ancient_region.connect(classical_region)
        classical_region.connect(medieval_region)
        medieval_region.connect(renaissance_region)
        renaissance_region.connect(industrial_region)
        industrial_region.connect(modern_region)
        modern_region.connect(postmodern_region)
        postmodern_region.connect(future_region)
        return
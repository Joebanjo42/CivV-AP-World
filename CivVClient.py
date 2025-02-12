import Utils
import asyncio
import logging
import socket
from .tuner import Tuner
from .items import CivVItemData
from typing import Dict

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from NetUtils import ClientStatus
from .tuner import TunerErrorException, TunerTimeoutException

ADDRESS = "127.0.0.1"
PORT = 4318

class CivVCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class CivVContext(CommonContext):
    game = "Civilization V"
    items_handling = 0b111
    command_processor = CivVCommandProcessor
    tuner: Tuner
    firetuner_task = None
    processing_multiple_items = False
    item_id_to_civ_item: Dict[int, CivVItemData] = {}
    current_index = 0
    current_location_index = 0
    item_offset = 140319
    logger = logger
    locatiions_to_send = []

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.tuner = Tuner(logger)

    async def server_auth(self, password_requested = False):
        if password_requested and not self.password:
            await super(CivVContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class CivVManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Civilization V Client"
        self.ui = CivVManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            logger.info("Connected:")

async def firetuner_task(ctx: CivVContext):
    cont = True
    while cont == True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        server_address = (ADDRESS, PORT)
        loop = asyncio.get_event_loop()
        await loop.sock_connect(sock, server_address)

        while not ctx.exit_event.is_set():
            if not ctx.slot:
                await asyncio.sleep(3)
                continue
            else:
                if ctx.processing_multiple_items == True:
                    await asyncio.sleep(3)
                else:
                    await handle_recieve_items(ctx, sock, loop)
                    await asyncio.sleep(3)
                    await handle_checked_location(ctx, sock, loop)
                    await asyncio.sleep(3)
                    # await handle_goal_complete(ctx)
        cont = False
        sock.close()

async def handle_recieve_items(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    try:
        if len(ctx.items_received) - ctx.current_index > 1:
            ctx.processing_multiple_items = True

        for index, network_item in enumerate(ctx.items_received):

            if index >= ctx.current_index:
                # logger.info(ctx.items_received[0])
                # logger.info(f"Item: {ctx.current_index}")
                current_item = ctx.items_received[ctx.current_index]
                await ctx.tuner.send_command(f"AddTech({current_item[0] - ctx.item_offset + 81})", sock, loop)
                # await ctx.tuner.send_command("AddGold()", sock, loop)
                await asyncio.sleep(0.02)
                ctx.current_index += 1
            await asyncio.sleep(0.02)
        
        ctx.processing_multiple_items = False
    finally:
        ctx.processing_multiple_items = False

async def handle_checked_location(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    result : str
    loc_list = []
    result = await ctx.tuner.send_command("GetItemsToSend()", sock, loop)
    result_list = result.split(",")
    for location in range(0, len(result_list)):
        if result_list[location] == '0' or result_list[location] == '':
            continue
        elif location in loc_list:
            continue
        else:
            loc_list.append(location)
    for index in range(0, len(loc_list)):
        if index >= ctx.current_location_index:
            loc = int(loc_list[index])
            ctx.locatiions_to_send.append(loc + ctx.item_offset)
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": ctx.locatiions_to_send}])
            ctx.current_location_index += 1


async def handle_goal_complete(ctx: CivVContext):
    logger.info("Handle Goal Called")

def main(connect=None, password=None, name=None):
    Utils.init_logging("Civiliazation V Client")
    

    async def _main(connect, password, name):
        ctx = CivVContext(connect, password)
        ctx.auth = name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        
        if gui_enabled:
            ctx.run_gui()
        await asyncio.sleep(1)

    
        ctx.firetuner_task = asyncio.create_task(firetuner_task(ctx), name="FireTuner")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.firetuner_task:
            await asyncio.sleep(3)
            await ctx.firetuner_task

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password, name))
    colorama.deinit()
    
    
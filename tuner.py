import socket
import asyncio
from logging import Logger

ADDRESS = "127.0.0.1"
PORT = 4318

CLIENT_PREFIX = "APSTART:"
CLIENT_POSTFIX = ":APEND"


def decode_mixed_string(data):
    return ''.join(chr(b) if 32 <= b < 127 else '' for b in data)


class TunerException(Exception):
    pass


class TunerTimeoutException(TunerException):
    pass


class TunerErrorException(TunerException):
    pass


class TunerConnectionException(TunerException):
    pass

class Tuner:
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def __parse_response(self, response: str) -> str:
        """Parses the response from the tuner socket"""
        split = response.split(CLIENT_PREFIX)
        if len(split) > 1:
            start = split[1]
            end = start.split(CLIENT_POSTFIX)[0]
            return end
        elif "ERR:" in response:
            raise TunerErrorException(response.replace("?", ""))
        else:
            return ""


    async def send_command(self, command_string: str, sock: socket.socket, loop: asyncio.AbstractEventLoop):
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.setblocking(False)

        prefix_string = "GameCore.Game."
        command_string = prefix_string + command_string
        b_command_string = command_string.encode()
        # self.logger.info(command_string)

        command_prefix = b"CMD:0:"
        delimmiter = b"\x00"
        full_command = b_command_string
        message = command_prefix + full_command + delimmiter
        message_length = len(message).to_bytes(1,byteorder='little')

        message_header = message_length + b"\x00\x00\x00\x03\x00\x00\x00"
        data = message_header + command_prefix + full_command + delimmiter 

        # server_address = (ADDRESS, PORT)
        # loop = asyncio.get_event_loop()
        try:
            # await loop.sock_connect(sock, server_address)
            await loop.sock_sendall(sock, data)
            await asyncio.sleep(0.02)

            received_data = await self.async_recv(sock)
            response = decode_mixed_string(received_data)
            return self.__parse_response(response)
        
        except sock.timeout:
            self.logger.debug('Timeout while receiving data')
            raise TunerTimeoutException
        except Exception as e:
            self.logger.debug(f'Error occured while receiving data: {str(e)}')
            connection_errors = [
                "The remote computer refused the network connection"
            ]
            if any(error in str(e) for error in connection_errors):
                raise TunerConnectionException(e)
            else:
                raise TunerException(e)
            # sock.close()
        # sock.connect(server_address)
        # sock.sendall(data)

        # await asyncio.sleep(1)
        
        # received_data = self.sock.recv(4069)
        # self.logger.info(received_data)
        # response = decode_mixed_string(received_data)
        # parsed_response = self.__parse_response(response)
        # self.logger.info("Hello")
        # self.logger.info(parsed_response)
        # sock.close()
        # return

    async def async_recv(self, sock, timeout=2.0, size=4096 * 2):
        response = await asyncio.wait_for(asyncio.get_event_loop().sock_recv(sock, size), timeout)
        return response
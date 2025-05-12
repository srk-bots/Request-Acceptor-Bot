from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTP Health check server
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


def run_health_server():
    server = HTTPServer(('', 8000), HealthCheckHandler)
    server.serve_forever()


# Start the health check server in a separate thread
threading.Thread(target=run_health_server, daemon=True).start()


class Bot(Client):
    def __init__(self):
        super().__init__(
            "vj join request bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')


Bot().run()

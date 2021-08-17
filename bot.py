import logging
from pyrogram import Client
from Config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

app = Client(
     'ForceSubscribe',
      bot_token = Config.1991551750:AAGqmsGTN2dkLAsX2riMs2oNNniTWECTuUI,
      api_id = Config.2693321,
      api_hash = Config.896fca4c49c96d923ed9680f55411f01,
      plugins = plugins
)

app.run()

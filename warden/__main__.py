from __future__ import annotations

import os

from warden import bot

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot.build().run()

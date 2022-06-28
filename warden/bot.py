from __future__ import annotations

__all__: tuple[str, ...] = ("build",)

import crescent

from warden import config
from warden import plugins


def build() -> crescent.Bot:
    bot = crescent.Bot(config.TOKEN, banner=None)

    for plugin in plugins.PLUGINS:
        bot.plugins.load(plugin)

    return bot

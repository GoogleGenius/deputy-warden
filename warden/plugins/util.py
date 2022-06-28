from __future__ import annotations

__all__: tuple[str, ...] = ()

import crescent

from crescent.ext import docstrings

plugin = crescent.Plugin()


@plugin.include
@docstrings.parse_doc
@crescent.command
async def ping(ctx: crescent.Context) -> None:
    """Replies with bot latency"""
    await ctx.respond(f"Pong! `{ctx.app.heartbeat_latency * 1000:.0f}ms`")

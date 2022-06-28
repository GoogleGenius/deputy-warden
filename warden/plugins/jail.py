from __future__ import annotations

__all__: tuple[str, ...] = ()

import crescent
import hikari

from crescent.ext import docstrings

plugin = crescent.Plugin()


@plugin.include
@docstrings.parse_doc
@crescent.command
async def jail(ctx: crescent.Context, user: hikari.User) -> None:
    """Place a user in jail

    Parameters
    ----------
    user : hikari.User
        The user to place in jail
    """
    await ctx.respond(f"{user.mention} is in jail!")

from typing import Literal

from pydantic import BaseModel

from states.common.relic import RewardRelic


class Treasure(BaseModel):
    """The treasure object."""

    message: str
    relics: list[RewardRelic]
    can_proceed: bool


class TreasureState(BaseModel):
    """The state when the scenario is in the treasure room."""

    state_type: Literal["treasure"]
    treasure: Treasure

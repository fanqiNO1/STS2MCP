from pydantic import BaseModel

from states.common.card import HandCard
from states.player.pile_card import PileCards
from states.player.orb import Orb


class CombatPlayerState(BaseModel):
    """The combat-specific state of the player."""

    energy: int
    max_energy: int
    stars: int
    # cards
    hand: list[HandCard]
    # piles
    draw_pile_count: int
    discard_pile_count: int
    exhaust_pile_count: int
    draw_pile: PileCards
    discard_pile: PileCards
    exhaust_pile: PileCards
    # orbs
    orbs: list[Orb]
    orb_slots: int
    orb_empty_slots: int

from typing import Literal

from pydantic import BaseModel, Field, model_validator

from states.player import PlayerState
from states.scenario import ScenarioState


class RunState(BaseModel):
    """The state of the current run."""

    act: int
    floor: int
    ascension: int

    def to_markdown(self) -> str:
        """Convert the run state to a markdown string."""
        return f"**Act {self.act}** | Floor {self.floor} | Ascension {self.ascension}"


class GameState(BaseModel):
    """The state of the game."""

    # gamemode
    game_mode: Literal["singleplayer", "multiplayer"]

    # common fields
    run: RunState | None = None
    player: PlayerState | None = None

    # scenario-specific fields
    scenario_state: ScenarioState = Field(discriminator="state_type")

    def to_markdown(self, is_diff: bool = False) -> str:
        """Convert the game state to a markdown string."""
        pass

    @model_validator(mode="before")
    @classmethod
    def from_json_state(cls, json_state: dict) -> dict:
        """Create a GameState instance from a JSON state."""
        game_state = dict()
        scenario_state = dict()

        # get game mode
        game_mode = json_state.get("game_mode", "singleplayer")
        game_state["game_mode"] = game_mode

        # parse scenario-specific fields
        for key in json_state:
            if key in ["run", "player"]:
                game_state[key] = json_state[key]
            else:
                scenario_state[key] = json_state[key]
        game_state["scenario_state"] = scenario_state
        return game_state

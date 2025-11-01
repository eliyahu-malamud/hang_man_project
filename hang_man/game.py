
def init_state(secret: str, max_tries: int) -> dict:
    return {'secret': secret, 'display': [], 'guessed': {}, 'guesses_wrong': 0, 'max_tries': max_tries}

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    pass
def apply_guess(state: dict, ch: str) -> bool:
    pass
def is_won(state: dict) -> bool:
    pass
def is_lost(state: dict) -> bool:
    pass
def render_display(state: dict) -> str:
    pass
def render_summary(state: dict) -> str:
    pass
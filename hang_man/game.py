
def init_state(secret: str, max_tries: int) -> dict:
    display = []
    for i in range(len(secret)):
        display.append('_')
    return {'secret': secret, 'display': display, 'guessed': set(), 'wrong_guesses': 0, 'max_tries': max_tries}

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1 and ch not in guessed and ch.isalpha():
        return True, 'valid input!'
    elif ch in guessed:
        return False, 'you already guessed this letter you need to enter a new one!'
    else:
        return False, 'invalid input you need to enter a single letter!'

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state['secret']:
        return True
    else:
        return False

def is_won(state: dict) -> bool:
    if state['secret'] == ''.join(state['display']):
        return True
    else:
        return False

def is_lost(state: dict) -> bool:
    if state['wrong_guesses'] >= state['max_tries']:
        return True
    else:
        return False

def render_display(state: dict) -> str:
    return ' '.join(state['display'])

def render_summary(state: dict) -> str:
    return f'the secret word is: {state['secret']}. your guesses are {state['guessed']}'
from hang_man import game

def prompt_guess() -> str:
    return input('please enter a single letter to guess:')

def print_status(state: dict) -> None:
    print(f'secret word: {game.render_display(state)}. letters that you guessed: {state['guessed']}. remaining tries: {state['max_tries'] - state['wrong_guesses']}.')

def print_result(state: dict) -> None:
    if game.is_won(state):
        print('you wind!')
    elif game.is_lost(state):
        print('you lost!')
    print(game.render_summary(state))
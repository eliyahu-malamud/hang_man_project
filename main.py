from hang_man import words, game, io

def play(words_l: list[str], max_tries: int = 10) -> None:
    secret_word = words.choose_secret_word(words_l)
    game_dict = game.init_state(secret_word, max_tries)
    while True:
        while True:
            players_guess = io.prompt_guess()
            if game.validate_guess(players_guess, game_dict['guessed'])[0]:
                print(game.validate_guess(players_guess, game_dict['guessed'])[1])
                break
            if not game.validate_guess(players_guess, game_dict['guessed'])[0]:
                print(game.validate_guess(players_guess, game_dict['guessed'])[1])
        game_dict['guessed'].add(players_guess)
        if game.apply_guess(game_dict, players_guess):
            print('well done!! you guessed right.')
            for i in range(len(game_dict['secret'])):
                if game_dict['secret'][i] == players_guess:
                        game_dict['display'][i] = players_guess
        elif not game.apply_guess(game_dict, players_guess):
            print('wrong guess!')
            game_dict['wrong_guesses'] += 1
        io.print_status(game_dict)
        if game.is_won(game_dict) or game.is_lost(game_dict):
            io.print_result(game_dict)
            break


if __name__ == "__main__":
    words_list = words.words_list_english
    play(words_list)


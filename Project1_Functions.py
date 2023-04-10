# restart or close game


def restart():
    while True:
        play = input('Wanna play again chief? [y/n]: ').lower()
        if play == 'no' or play == 'n':
            print('\nCya around :)')
            return False
        elif play == 'yes' or play == 'y':
            print('\n____RESTARTING____\n')
            break
        else:
            print('you know the drill...\nValid answer only bro\n')

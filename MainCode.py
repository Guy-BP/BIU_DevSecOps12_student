import random
from Functions import restart

# List of available songs
songs = ['big in japan', 'sultans of swing', 'black hole sun', 'jail house rock',
         'ring of fire', 'johnny b goode', 'age of aquarius', 'sweet home alabama',
         'winds of change', 'black magic woman']

# Let the user choose to start the game
while True:
    print('\nR U READY TO PLAY? [y/n]\n')
    start_game = input('(minimal knowledge of music is required): ').lower()

    if start_game == 'no' or start_game == 'n':
        print(':(\nGoodbye')
        exit()
    elif 'n' != start_game != 'no' and 'y' != start_game != 'yes':
        print('Please insert a valid answer homie\n')
        continue
    else:

        # Select a random song
        song = random.choice(songs)

        # Create a list of underscores to represent the hidden song
        hidden_song = ['_' if char != ' ' else ' ' for char in song]

        # Initialize the score counter
        score = 0

        # Create a list of the user's previous guesses
        pre_guess = []

        # Loop until the full song is guessed
        while ''.join(hidden_song) != song:

            # Print the hidden phrase, current score and previous guesses
            print(f'\nYour previous guesses:\n{pre_guess}\n')
            print(' '.join(hidden_song))
            print(f'\nScore: \n {score}\n')

            # Ask the user to guess a letter and keep track of previous guesses
            guess = input('Enter a letter, 1 letter only: ').lower()

            # Check if the guess is valid
            if len(guess) != 1:
                print('did I not say 1 letter only??')
                continue

            # Check if the guess is correct
            found_letter = False
            for i in range(len(song)):
                if song[i].lower() == guess:
                    hidden_song[i] = song[i]
                    found_letter = True

            # Check if the guess has been previously made
            if pre_guess.__contains__(guess):
                print('\nYou already tried this one buddy...')
            else:
                pre_guess.append(guess)

                # Add or sub score
                if found_letter:
                    score += 5
                    print('\ntov ahi!')
                else:
                    score -= 1
                    print('\nwala lo ahi...')

        # Print the final result
        print(f'\nAhla gever! you guessed the song "{song}"!\n Your final score is: {score}\n')

    # ask the user if he wants to play again
    if restart() is False:
        exit()

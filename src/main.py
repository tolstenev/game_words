# Copyright 2023 Gleb Tolstenev
#
# main.py contain source code for game "Words"
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# "Words" is an ordinary game in which you need to say words starting with the
# last letter of the previous word.

rules = """                "Words"
This game is for two players.
You need to type words starting with
the last letter of the word by your opponent.
The words should not be repeated.

Example:
Player 1 types the word "cat". Player 2 should
type the word starting with 't'.
Player 2 types the word "tea". Player 1 should
type the word starting with 'a' etc.

If you don't know the word or
you want to stop the game, enter "idk".
"""
print(rules)


def get_name():
    name = str(input())
    while len(name.split()) == 0:
        print("Please enter at least one word of your name.")
        name = str(input("Enter name: "))
    words_in_name = name.split()
    words_in_name = [word.capitalize() for word in words_in_name]
    name = " ".join(words_in_name)
    return name


def get_word_from(player_name):
    while True:
        word = str(input(f"{player_name}: "))
        word = word.strip().lower()
        if len(word.split()) != 1:
            print("Please enter one word.")
            continue
        if not word.isalpha():
            print("The word must contain only alphabetic letters.")
            continue
        break
    return word


def twist(player_name, opponent_name, opponent_score,
          previous_word, stop_word, used_words):
    if previous_word[-1] in ['ь', 'ъ', 'ы'] or \
       previous_word[-1] in ['x']:
        necessary_letter = [previous_word[-1], previous_word[-2]]
    else:
        necessary_letter = [previous_word[-1]]
    while True:
        word = get_word_from(player_name)
        if word == stop_word:
            print(f"\nCongratulations, {opponent_name}!",
                  f"\nThe number of your words: {opponent_score}\n")
            return "code_win"
        if previous_word[-1] in ['ь', 'ъ', 'ы'] or \
           previous_word[-1] in ['x']:  # Russian and English letter
            if word[0] not in necessary_letter:
                print(f"{player_name}, your word must start with",
                      f"'{previous_word[-1]}' or "
                      f"'{previous_word[-2]}'")
                continue
        elif word[0] != previous_word[-1]:
            print(f"{player_name}, your word must start with",
                  f"'{previous_word[-1]}'")
            continue
        if word in used_words:
            print(f"{player_name}, the \"{word}\" was used.",
                  "Enter another word.")
            continue
        break
    return word


def play_game(player_1, player_2, score_1, score_2, stop_word):
    used_words = list()
    print(f"\n{player_1} and {player_2} start the game!\n")
    word_1 = get_word_from(player_1)
    used_words.append(word_1)
    score_1 += 1
    if word_1 == stop_word:
        print("Exiting the game...")
    else:
        while True:
            word_2 = twist(player_2, player_1, score_1,
                           word_1, stop_word, used_words)
            if word_2 == "code_win":
                break
            used_words.append(word_2)
            score_2 += 1
            word_1 = twist(player_1, player_2, score_2,
                           word_2, stop_word, used_words)
            if word_1 == "code_win":
                break
            used_words.append(word_1)
            score_1 += 1


def get_players_name():
    print("Player 1, enter your name: ", end="")
    player_1 = get_name()
    print(f"Hello, {player_1}!")
    print("Player 2, enter your name: ", end="")
    player_2 = get_name()
    print(f"Hello, {player_2}!")
    return [player_1, player_2]


stop_word = "idk"
score_1 = 0
score_2 = 0
players = get_players_name()
player_1 = players[0]
player_2 = players[1]

while True:
    play_game(player_1, player_2, score_1, score_2, stop_word)
    answer = input("Do you want to play one more time? [yes/no]: ")
    if answer in ["yes", "Yes", "YES", "y", "Y"]:
        continue
    else:
        print("Exit the game...")
        break

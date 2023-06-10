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
This game for two players. An ordinary game
in which you need to say words starting with
the last letter of the previous word.

Example:
Player 1 type the word "cat". Player 2 should
type the word starting with 't'.
Player 2 type the word "tea". Player 1 should
type the word starting with 'a' etc.

If you don't know the word or
you want to stop the game enter stop_word 
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
    word = str(input(f"{player_name}, enter the word: "))
    while len(word.split()) != 1:
        print("Please enter one word.")
        word = str(input(f"{player_name}, enter the word: "))
    while not word.isalpha():
        print("The word must contain only alphabetic letters.")
        word = str(input(f"{player_name}, enter the word: "))
    word = word.strip().lower()
    return word


def twist(player_name, opponent_name, opponent_score,
          previous_word, stop_word, used_words):
    while True:
        word = get_word_from(player_name)
        if word == stop_word:
            print(f"\nCongratulate {opponent_name}!",
                  f"You are win with score {opponent_score}!")
            return "code_win"
        if word[0] != previous_word[-1]:
            print(f"{player_name}, your word must start with",
                  f"'{previous_word[-1]}'")
            continue
        else:
            if word in used_words:
                print(f"{player_name}, the \"{word}\" was used.",
                      "Enter another word.")
                continue
            break
    return word


print("Player 1 enter your name: ", end='')
player_1 = get_name()
print(f"Hello, {player_1}!")

print("Player 2 enter your name: ", end='')
player_2 = get_name()
print(f"Hello to you too, {player_2}!")

print(f"\n{player_1} and {player_2} start the game!\n")

stop_word = "idk"
used_words = []
score_1 = 0
score_2 = 0
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

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

# An ordinary game in which you need to say words starting with the last letter
# of the previous word.

def word_from_player(player_name, opponent_name, opponent_score,
                     previous_word, stop_word, used_words):
    while True:
        word = str(input(f"{player_name}: "))
        if word == stop_word:
            print(f"\nCongratulate {opponent_name}! You are win with score {opponent_score}!")
            return "code_win"
        if word[0] != previous_word[-1]:
            print(f"{player_name}, your word must start with '{previous_word[-1]}'")
            continue
        else:
            if word in used_words:
                print(f"{player_name}, the \"{word}\" was used. Enter another word.")
                continue
            break
    return word


rules = """                "Words"
This game for two players. An ordinary game
in which you need to say words starting with
the last letter of the previous word.
 
Example:
Player 1 type the word "cat". Player 2 should
type the word starting with 't'.
Player 2 type the word "tea". Player 1 shold
type the word starting witn 'a' etc.

If you don't know the word or
you want to stop the game enter stop_word 
"""
print(rules)

name_1 = str(input("Player 1 enter your name: ")).capitalize()
print(f"Hello, {name_1}!")
name_2 = str(input("Player 2 enter your name: ")).capitalize()
print(f"Hello to you too, {name_2}!")

print(f"\n{name_1} and {name_2} start the game!\n")

stop_word = "idk"
used_words = []
score_1 = 0
score_2 = 0
word_1 = str(input(f"{name_1}, enter the word: "))
used_words.append(word_1)
score_1 += 1

if word_1 == stop_word:
    print("Exiting the game...")
else:
    while True:
        word_2 = word_from_player(name_2, name_1, score_1,
                                  word_1, stop_word, used_words)
        if word_2 == "code_win":
            break
        used_words.append(word_2)
        score_2 += 1
        word_1 = word_from_player(name_1, name_2, score_2,
                                  word_2, stop_word, used_words)
        if word_1 == "code_win":
            break
        used_words.append(word_1)
        score_1 += 1


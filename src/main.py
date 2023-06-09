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
you want to stop the game enter "idk" 
"""
print(rules)

print("Start the game!\n")

word_1 = str(input("Player 1, enter the word: "))

if word_1 == "idk":
    print("Exiting the game...")
else:
    word_2 = str(input("Player 2, enter the word: "))
    while True:
        if word_2 == "idk":
            print("\nCongratulate Player 1! You are win!")
            break
        if word_2[0] != word_1[-1]:
            print("Player 2, your word must start with", word_1[-1])
            word_2 = str(input("Player 2: "))
            continue
        word_1 = str(input("Player 1: "))
        if word_1 == "idk":
            print("Congratulate Player 2! You are win!")
            break
        while word_1[0] != word_2[-1]:
            print("\nPlayer 1, your word must start with", word_2[-1])
            word_1 = str(input("Player 1: "))
            continue
        word_2 = str(input("Player 2: "))

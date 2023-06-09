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

word_p1 = str(input("Player 1, enter the word: "))
word_p2 = str(input("Player 2, enter the word: "))
while True:
    if word_p2 == "idk":
        print("Congratulate Player 1! You are win!")
        break
    else:
        while word_p2[0] != word_p1[-1]:
            print("Player 2, your word must start with last letter "
                  "of player's 1 word")
            word_p2 = str(input("Player 2, enter the word: "))
        word_p1 = str(input("Player 1, enter the word: "))
    if word_p1 == "idk":
        print("Congratulate Player 2! You are win!")
        break
    else:
        while word_p1[0] != word_p2[-1]:
            print("Player 1, your word must start with last letter "
                  "of player's 2 word")
            word_p1 = str(input("Player 1, enter the word: "))
        word_p2 = str(input("Player 2, enter the word: "))


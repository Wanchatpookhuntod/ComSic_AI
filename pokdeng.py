import random
import pandas as pd
import numpy as np

basic_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

spades = []
redheart = []
diamond= []
cubs = []

for i in basic_card:
    spades.append(['S', i]) # spades
    redheart.append(['R', i]) # redheart
    diamond.append(['D', i]) # diamond
    cubs.append(['C', i]) # cubs

all_card = spades + redheart + diamond + cubs

for i in range(34):
    random.shuffle(all_card)

number_player = 4
player = []
number_card = 0

card1 = []
card2 = []

number_player += 1

for i in range(2):
    for j in range(number_player):

        if i == 0:
            card1.append(all_card[number_card])
        if i == 1:
            card2.append(all_card[number_card])
        number_card += 1

df = pd.DataFrame()
df["card1"] = card1
df["card2"] = card2
df["card3"] = ""
df["score-2"] = ""
df["score-E"] = ""
df["win/lost"]= ""

def convertToInt(n):
    c = 0
    if n == "J" or n == "Q" or n == "K" :
        c = 10
    elif n == "A":
        c = 1
    else:
        c = n
    return c

# first round ===
for i in range(number_player):
    score = (convertToInt(df.loc[i, "card1"][1]) + convertToInt(df.loc[i, "card2"][1])) % 10

    df["score-2"][i] = [df.loc[i, "card1"][0],
                    df.loc[i, "card2"][0],
                    score]

# check win first round ===
for i in range(number_player - 1):
    if (df.iloc[-1]["score-2"][2] > df.iloc[i]["score-2"][2]) and (df.iloc[-1]["score-2"][2] >= 8) :
        df["win/lost"][i] = "no"

    elif (df.iloc[i]["score-2"][2] > df.iloc[-1]["score-2"][2]) and (df.iloc[i]["score-2"][2] >= 8):
        df["win/lost"][i] = "win"

    elif (df.iloc[i]["score-2"][2] >= 8) and (df.iloc[i]["score-2"][2] == df.iloc[-1]["score-2"][2]):
        df["win/lost"][i] = "always"

    else:
        df["win/lost"][i] = ""

print(df, "\n")

# secound round ===
if df.iloc[-1]["score-2"][2] < 8:
    for i in range(number_player):
        if df["score-2"][i][-1] < 4:
            df["card3"][i] = all_card[number_card]
            number_card += 1

        else:
            df["card3"][i] = [None, 0]

        score = (convertToInt(df.loc[i, "card1"][1]) +
                 convertToInt(df.loc[i, "card2"][1]) +
                 convertToInt(df.loc[i, "card3"][1])) % 10

        df["score-E"][i] = [df.loc[i, "card1"][0],
                          df.loc[i, "card2"][0],
                          df.loc[i, "card3"][0],
                          score]

else:
    print(f"เจ้ามือป๊อก {df.iloc[-1]['score-2'][2]}")


# chenck win secound round
if df.iloc[-1]["score-2"][2] < 8:
    for i in range(number_player - 1):
        if df["win/lost"][i] != "win":
            if df.iloc[i]["score-E"][3] > df.iloc[-1]["score-E"][3]:
                df["win/lost"][i] = "win"

            elif df.iloc[i]["score-E"][3] == df.iloc[-1]["score-E"][3]:
                df["win/lost"][i] = "alway"

            else:
                df["win/lost"][i] = "lost"


    print(df.iloc[:-1])
print("\nไพ่เจ้ามือ", "=" * 20)
print(df.iloc[-1][:-1])




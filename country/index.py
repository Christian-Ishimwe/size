#programn for comparing countries acccording their land mass

from logo import vs 
from logo import title
from data import game
import random
game_continue=True
score=0
country_b=random.choice(game)
print(title)
while game_continue is True:
    country_a=country_b
    country_b=random.choice(game)
    if country_a==country_b:
        country_b=random.choice(game)
    # print(country_a)
    # print(country_b)
    def coun(country):
        country_name=country["country"]
        country_capital=country["city"]
        return f"the country is {country_name}, it's capital city is {country_capital}"
    print(f"compare A: {coun(country_a)}")
    print(vs)
    print(f"against B: {coun(country_b)}")
    guess=input("Which country have large landmass: 'A' or 'B'\n").lower()
    if guess!="a" and guess!="b":
        game_continue=False
        print(f"Wrong input, your final score is {score}")
        exit()
    country_asize=country_a["size"]
    country_bsize=country_b["size"]
    def conclude(guess,country_asize,country_bsize):
        if country_bsize>country_asize:
            if guess=="b":
                return True
            else:
                return False
        else:
            if guess=="a":
                return True
            else:
                return False
    is_correct=conclude(guess,country_asize,country_bsize)
    if is_correct==True:
        score+=1
        print(f"You got it Right! Your current score is {score}")
    else:
        game_continue=False
        print(f"You are wrong! The final score is {score}")
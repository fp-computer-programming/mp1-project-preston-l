# Author: PCL 10/28/22

#Nouns: w17 w18 w19(s-plural) w25 w26 w27 w28 w29
#Places: w3 w8 w15 w20 w21 w22 w23 w30
#Adjectives: w1 w2 w4 w5 w11 w12 w13 w14
#Verbs: w6(ed) w7(ing) w9 w10 w16(ed)

#recieving inputs for all of the madlib words and assigning them variables
w1 = input("adj")
w2 = input("adj")
w3 = input("place")
w4 = input("adj")
w5 = input("adj")
w6 = input("verb - ed")
w7 = input("verb - ing")
w8 = input("place")
w9 = input("verb")
w10 = input("verb")
w11 = input("adj")
w12 = input("adj")
w13 = input("adj")
w14 = input("adj")
w15 = input("place")
w16 = input("verb - ed")
w17 = input("noun")
w18 = input("noun")
w19 = input("noun - s")
w20 = input("place")
w21 = input("place")
w22 = input("place")
w23 = input("place")
w24 = input("name")
w25 = input("noun - group name")
w26 = input("noun")
w27 = input("noun")
w28 = input("noun")
w29 = input("noun")
w30 = input("place")

# creating the completed mablib with the inputs as a variable to be printed later after checking the inputted words
madlib = """The Jesuits were a """+w1+""" group of """+w2+""" people.
They were formed in """+w3+""" 1540 by a originally """+w4+""" and """+w5+""" man named Ignatius of Loyola.
During the early parts of ignatius's life he """+w6+""" in material pleasures,
until one day when """+w7+""" by a cannonball defending the city of """+w8+""".
This caused Ignatius to be bedridden with nothing else to do except """+w9+""" books about the lives of saints and Jesus which he had available.
This led to a """+w10+""" in Ignatius, he no longer wanted to live as a """+w11+""" and """+w12+""" man,
but instead as a  """+w13+""" and """+w14+""" man repenting for his sins following in the way of the saints he read about.
He started this journey by heading to """+w15+""" in Spain and """+w16+""" all his sins to the statue of the Virgin Mary.
Over the course of the next year Ignatius lived as a beggar with little """+w17+""" and """+w18+""",
attending mass and spending """+w19+""" praying every day.
After this he spent the next year going on pilgrimage to """+w20+""" and stopping at """+w21+""", """+w22+""", and """+w23+""" along the way.
For the next 12 or so years Ignatius spent his life studying in many different major cities,
during this time met """+w24+""" and several other key figures who would become co-founders of the """+w25+""".
This group would go on to take vows of """+w26+""", """+w27+""", and """+w28+""".
Eventually in 1556 Ignatius passed away leading the Jesuits till his last moments and was canonized as the """+w29+""" saint 68 years later.
The Jesuits would then continue to go on to form 189 institutions of higher learning to this day including """+w30+"""."""

#checking if input w1 is equal to any other adjective inputs
if w1 == w2 or w1 == w4 or w1 == w5 or w1 == w11 or w1 == w12 or w1 == w13 or w1 == w14:
    print("You cannot use the same inputs")
#checking if input w2 is equal to any other adjective inputs
elif w2 == w1 or w2 == w4 or w2 == w5 or w2 == w11 or w2 == w12 or w2 == w13 or w2 == w14:
    print("You cannot use the same inputs")
#checking if input w4 is equal to any other adjective inputs
elif w4 == w1 or w4 == w2 or w4 == w5 or w4 == w11 or w4 == w12 or w4 == w13 or w4 == w14:
    print("You cannot use the same inputs")
#checking if input w5 is equal to any other adjective inputs
elif w5 == w1 or w5 == w2 or w5 == w4 or w4 == w11 or w4 == w12 or w4 == w13 or w4 == w14:
    print("You cannot use the same inputs")
#checking if input w11 is equal to any other adjective inputs
elif w11 == w1 or w11 == w2 or w11 == w4 or w11 == w5 or w11 == w12 or w11 == w13 or w11 == w14:
    print("You cannot use the same inputs")
#checking if input w12 is equal to any other adjective inputs
elif w12 == w1 or w12 == w2 or w12 == w4 or w12 == w5 or w12 == w11 or w12 == w13 or w12 == w14:
    print("You cannot use the same inputs")
#checking if input w13 is equal to any other adjective inputs
elif w13 == w1 or w13 == w2 or w13 == w4 or w13 == w5 or w13 == w11 or w13 == w12 or w13 == w14:
    print("You cannot use the same inputs")
#checking if input w14 is equal to any other adjective inputs
elif w14 == w1 or w14 == w2 or w14 == w4 or w14 == w5 or w14 == w11 or w14 == w12 or w14 == w13:
    print("You cannot use the same inputs")
#checking if input w3 is equal to any other place inputs
elif w3 == w8 or w3 == w15 or w3 == w20 or w3 == w21 or w3 == w22 or w3 == w23 or w3 == w30:
    print("You cannot use the same inputs")
#checking if input w8 is equal to any other place inputs
elif w8 == w3 or w8 == w15 or w8 == w20 or w8 == w21 or w8 == w22 or w8 == w23 or w8 == w30:
    print("You cannot use the same inputs")
#checking if input w15 is equal to any other place inputs
elif w15 == w3 or w15 == w8 or w15 == w20 or w15 == w21 or w15 == w22 or w15 == w23 or w15 == w30:
    print("You cannot use the same inputs")
#checking if input w20 is equal to any other place inputs
elif w20 == w3 or w20 == w8 or w20 == w15 or w20 == w21 or w20 == w22 or w20 == w23 or w20 == w30:
    print("You cannot use the same inputs")
#checking if input w21 is equal to any other place inputs
elif w21 == w3 or w21 == w8 or w21 == w15 or w21 == w20 or w21 == w22 or w21 == w23 or w21 == w30:
    print("You cannot use the same inputs")
#checking if input w22 is equal to any other place inputs
elif w22 == w3 or w22 == w8 or w22 == w15 or w22 == w20 or w22 == w21 or w22 == w23 or w22 == w30:
    print("You cannot use the same inputs")
#checking if input w23 is equal to any other place inputs
elif w23 == w3 or w23 == w8 or w23 == w15 or w23 == w20 or w23 == w21 or w23 == w22 or w23 == w30:
    print("You cannot use the same inputs")
#checking if input w30 is equal to any other place inputs
elif w30 == w3 or w30 == w8 or w30 == w15 or w30 == w20 or w30 == w21 or w30 == w22 or w30 == w23:
    print("You cannot use the same inputs")
#checking if input w17 is equal to any other noun inputs
elif w17 == w18 or w17 == w19 or w17 == w25 or w17 == w26 or w17 == w27 or w17 == w28 or w17 == w29:
    print("You cannot use the same inputs")
#checking if input w18 is equal to any other noun inputs
elif w18 == w17 or w18 == w19 or w18 == w25 or w18 == w26 or w18 == w27 or w18 == w28 or w18 == w29:
    print("You cannot use the same inputs")
#checking if input w19 is equal to any other noun inputs
elif w19 == w17 or w19 == w18 or w19 == w25 or w19 == w26 or w19 == w27 or w19 == w28 or w19 == w29:
    print("You cannot use the same inputs")
#checking if input w25 is equal to any other noun inputs
elif w25 == w17 or w25 == w18 or w25 == w19 or w25 == w26 or w25 == w27 or w25 == w28 or w25 == w29:
    print("You cannot use the same inputs")
#checking if input w26 is equal to any other noun inputs
elif w26 == w17 or w26 == w18 or w26 == w19 or w26 == w25 or w26 == w27 or w26 == w28 or w26 == w29:
    print("You cannot use the same inputs")
#checking if input w27 is equal to any other noun inputs
elif w27 == w17 or w27 == w18 or w27 == w19 or w27 == w25 or w27 == w26 or w27 == w28 or w27 == w29:
    print("You cannot use the same inputs")
#checking if input w28 is equal to any other noun inputs
elif w28 == w17 or w28 == w18 or w28 == w19 or w28 == w25 or w28 == w26 or w28 == w27 or w28 == w29:
    print("You cannot use the same inputs")
#checking if input w29 is equal to any other noun inputs
elif w29 == w17 or w29 == w18 or w29 == w19 or w29 == w25 or w29 == w26 or w29 == w27 or w29 == w28:
    print("You cannot use the same inputs")
#checking if input w6 is equal to any other verb inputs
elif w6 == w7 or w6 == w9 or w6 == w10 or w6 == w16:
    print("You cannot use the same inputs")
#checking if input w7 is equal to any other verb inputs
elif w7 == w6 or w7 == w9 or w7 == w10 or w7 == w16:
    print("You cannot use the same inputs")
#checking if input w9 is equal to any other verb inputs
elif w9 == w6 or w9 == w7 or w9 == w10 or w9 == w16:
    print("You cannot use the same inputs")
#checking if input w10 is equal to any other verb inputs
elif w10 == w6 or w10 == w7 or w10 == w9 or w10 == w16:
    print("You cannot use the same inputs")
#checking if input w16 is equal to any other verb inputs
elif w16 == w6 or w16 == w7 or w16 == w9 or w10 == w16:
    print("You cannot use the same inputs")
else:
    print(madlib)

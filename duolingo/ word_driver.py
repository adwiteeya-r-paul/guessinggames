from words import Words
from random import randint

word_list = []
def reading_file(file_name):

    read = open(file_name, "r")

    for line in read:

        line_strip = line.strip()
        line_split = line_strip.split(",")

        w1 = Words(line_split[0],line_split[1])
        word_list.append(w1)

    read.close()
    return word_list

def writing_file(file_name,wlist):
    write = open(file_name, "w")

    for line in word_list:
        string = str(line)+ "\n"
        write.write(string)

    write.close()

reading_file("words.txt")
writing_file("words.txt", word_list)


def choose_language(wlist):
    language = input("Which language do you want to do today? Type F for French, G for German, B for Bengali!")
    if language == "F":
        x1 = 0
        y1 = 9
        translate(wlist, x1, y1)
    elif language == "G":
        x1 = 10
        y1 = 19
        translate(wlist, x1,y1)
    elif language == "B":
        x1 = 20
        y1 = 22
        translate(wlist, x1, y1)
    else:
        print("Please follow instructions!")
        choose_language(wlist)

def translate(wlist, x1,y1):
    x = randint(x1,y1)
    y = input("Guess the meaning: " + str(word_list[x].word)+ " ")
    while y != word_list[x].meaning:
        print("Sorry. You're wrong."+ " ")
        y = input("Try again!"+ " ")
    print("Congrats!")
    z = input("To try more words, type YES!"+ " ")
    if z == "YES":
        translate(wlist,x1,y1)
    else:
        print("You are doing amazing! Keep up the good work!")

choose_language(word_list)















import string

try:
    import cPickle as pickle
except Exception:
    import pickle

global m

print("Hey!players!Welcome to my game!!!Player1 please choose your level:")

while True:
    level=input("your level is(you can only choose:s/n/h):")
    if level!="s" and level!="n" and level!="h":
        print("Wrong input!")
        continue
    else:
        break

if level=="s":
    WORDLIST_FILENAME = "simple.txt"
    file = open('simple.txt')
    content = file.read()
    s = [i for i in content if str.isprintable(i)]
    s2 = ''.join(s)

    while True:
        print("Player1 can choose one of them:",s2," ")
        print("Player1 please enter your favorite one(Initial capital): ")
        m =input("").format(str)
        if m in content:
            print("****************************************************************************s\n"*10)
            print("ok!game setting finished, Have fun!:)")
            file.close()
            break
        else:
            print("Sorry,please enter again!")
            continue
        
elif level=="n":
    WORDLIST_FILENAME = "normal.txt"
    file = open('normal.txt')
    content = file.read()
    s = [i for i in content if str.isprintable(i)]
    s2 = ''.join(s)
    while True:
        print("Player1 can choose one of them:",s2," ")
        print("Player1 please enter your favorite one(Initial capital): ")
        m =input("").format(str)
        if m in content:
            print("****************************************************************************s\n"*10)
            print("ok!game setting finished, Have fun!:)")
            file.close()
            break
        else:
            print("Sorry,please enter again!")
            continue
        
elif level=="h":
    WORDLIST_FILENAME = "hard.txt"
    file = open('hard.txt')
    content = file.read()
    s = [i for i in content if str.isprintable(i)]
    s2 = ''.join(s)
    while True:
        print("Player1 can choose one of them:",s2," ")
        print("Player1 please enter your favorite one(Initial capital): ")
        m =input("").format(str)
        if m in content:
            print("****************************************************************************s\n"*10)
            print("ok!game setting finished, Have fun!:)")
            file.close()
            break
        else:
            print("Sorry,please enter again!")
            continue
        
else:
    print("sorry!your level is wrong!please try again!")
    quit()

with open("strokes.txt", 'r') as f:
    strokes = pickle.loads(f.read().encode('utf-8'))

# written by Wang SiYi（M19W7332） and Cai ZiCheng（M1927089)

# def text1():
#     WORDLIST_FILENAME = "simple.txt"
#
# def text2():
#     WORDLIST_FILENAME = "normal.txt"
#
# def text3():
#     WORDLIST_FILENAME = "hard.txt"


def askForInput(word, guessed, pic):

    print(pic)
    print("Letters already guessed: {}".format(" ".join(list(guessed))))
    print("The current state of your guess: {}".format(showWord(word, guessed)))
    characters = frozenset("ABCDEFGHIGKLMNOPQRSTUVWXYZ")
    while True:
        ans = input("What is your next letter? (or type your guess) :")
        ans = ans.strip()
        ans = ans.upper()
        if len(ans) > 1:
            if len(ans) == len(word):
                if all([ele in characters for ele in ans]):
                    return ans
                else:
                    print("Invalid entry: enter a word that is a alphabeta string.")
            else:
                print("Invalid entry: enter a word that exists {} characters.".format(len(word)))

        elif len(ans) == 1:
            if ans in characters:
                if ans not in guessed:
                    return ans
                else:
                    print("Invalid entry: enter a single letter you have not already guessed.")
            else:
                print("Invalid entry: enter a single letter that is a alphabeta character.")
        else:
            print("Invalid entry: enter a single alphabeta letter or guess a  alphabeta word.")


def getWordList(minLength, maxLength):

    wordList = []

    with open(WORDLIST_FILENAME, 'r') as f: # iterate the file from top to bottom
        for line in f:
            line = line.strip()
            line = line.strip("%") # remove plurals
            if len(line) >= minLength and len(line) <= maxLength:
                wordList.append(line)

    return wordList


def selectWord(minLength, maxLength):

    wordList = getWordList(minLength, maxLength)
    word = m
    return word.upper()


def printBanner(word):

    print("YOU WILL GUESS A WORD WITH {} LETTERS!".format(len(word)))


def theEnd(word, wrong_times):
    if wrong_times < len(strokes):
        print("Congratulations! You win!!")
        print("The word was {}".format(" ".join(list(word))))
    else:
        print("Sorry, you lose!")
        print("The word was {}".format(" ".join(list(word))))

    print("---------------------")


def showWord(word, guessed):

    word = word.upper()
    word_hint = ["_" if ele not in guessed else ele for ele in word]
    return " ".join(word_hint)

    
def main():
    print("WELCOME TO HANGMAN!")
    print("---------------------")
    minLength = 6
    maxLength = 10
    word = selectWord(minLength, maxLength)
    word = word.upper()
    printBanner(word)
    guessed = set()
    wrong_times = 0

    while wrong_times < len(strokes):

        ans = askForInput(word, guessed, strokes[wrong_times])

        if len(ans) == 1:
            numAns = word.count(ans)
            print("There is {} {}!".format(numAns, ans))
            guessed.add(ans)
            if all([ele in guessed for ele in word]):
                break
            if numAns == 0:
                wrong_times += 1
        elif len(ans) == len(word):
            if ans == word:
                break
            else:
                wrong_times += 1
                print("the word you guessed is wrong!")

    theEnd(word, wrong_times)

if __name__ == "__main__":
    main()

# written by Hu WenKai（M19W7187）
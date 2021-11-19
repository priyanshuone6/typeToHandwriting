# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:52:19 2020

@author: Arvind Krishna
@ github.com/ArvindAROO
"""
from pathlib import Path

from PIL import Image

BG = Image.open("imagesFiles/bg.png").convert("RGB")
# creating the instance of background image
sizeOfSheet = BG.width
gap, _ = 50, 25
# size of each image or character

# these are the only allowed characters
allowedChars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890"


def writeIt(char):
    """Takes indivial chars and adds them to image"""
    global gap, _
    if char == "\n":
        gap = 50
        _ += 200
    else:
        # this will generate and open the image file
        char.lower()
        cases = Image.open("imagesFiles/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases


def caller(word):
    global gap, _
    if gap > sizeOfSheet - 100 * (len(word)):
        gap = 50
        _ += 200
    # print("word revieced by caller is {} and its size is {}".format(word, len(word)))
    # this works on a word by word process
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += "upper"
            elif letter == ".":
                letter = "fullstop"
            elif letter == "!":
                letter = "exclamation"
            elif letter == "?":
                letter = "question"
            elif letter == ",":
                letter = "comma"
            elif letter == "(":
                letter = "braketop"
            elif letter == ")":
                letter = "braketcl"
            elif letter == "-":
                letter = "hiphen"
            writeIt(letter)


# naming the character
# upper is appended to upper case characters
def dataHandling(Input):
    """Handles the input"""
    wordlist = Input.split(" ")
    for i in wordlist:
        caller(i)
        writeIt("space")
    writeIt("\n")


def main():
    global _, BG
    try:
        image_list = []
        num = 1
        fileName = input("Enter file name: ")
        with open(fileName, "r") as File:
            for line in File:
                dataHandling(line)
                if _ + 225 >= BG.size[1]:
                    image_name = str(num).rjust(3, "0") + ".png"
                    print("Saving", image_name)
                    BG.save(f"output/{image_name}")
                    image_list.append(BG)  # Make pdf

                    BG = Image.open("imagesFiles/bg.png").convert("RGB")  # Make pdf
                    _ = 25
                    num += 1

        if _ > 25:
            image_name = str(num).rjust(3, "0") + ".png"
            print("Saving", image_name)
            BG.save(f"output/{image_name}")
            image_list.append(BG)  # Make pdf

        # Make pdf
        image_list[0].save(
            Path(fileName).resolve().stem + ".pdf",
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=image_list[1:],
        )

    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()

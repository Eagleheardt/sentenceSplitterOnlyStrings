def sentence_splitter(aFile):
    try:
        fr = open(aFile, 'r')
        lines = fr.read()
        fr.close()
        words = lines.split()
        titles = ["Mr.","Mrs.","Sr.","Dr.","Jr.","e.g.","i.e."]

        nDex = 0
        for x in words:
            theWord = x
            try:
                if theWord in(titles):
                    print(theWord,end=" ")
                elif theWord.endswith(".") and words[nDex+1] == " " and words[nDex+2].islower():
                    print(theWord,end="")
                elif theWord.endswith(".") and words[nDex+1].isdigit():
                    print(theWord, end="")
                elif theWord.endswith("..."):
                    print(theWord)
                elif theWord.endswith("."):
                    print(theWord)
                elif theWord.endswith("?"):
                    print(theWord)
                elif theWord.endswith("!"):
                    print(theWord)
                else:
                    print(theWord,end=" ")
            except Exception:
                pass

            nDex += 1

        print(words[-1])

    except IOError:
        print("Invalid file.")
        exit()

uInputFileName = input("Enter your file: ")
sentence_splitter(uInputFileName)


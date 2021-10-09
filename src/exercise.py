def main():
    #write your code below this line
    while True:
        text = input()
        if (text != ""):
            text_split = text.split()
            for word in text_split:
                if "av" in word:
                    print(word)
        else:
            break

if __name__ == '__main__':
    main()

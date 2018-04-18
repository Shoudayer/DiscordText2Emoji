from sys import argv

def genEmojis(message):
    EmojiNumbers=['zero','one','two','three','four','five','six','seven','eight','nine']
    if message=='':
        message = input("texte :")
    for char in message:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            print(":regional_indicator_"+char.lower()+": ", end='')
        elif char.lower() in '0123456789':
            i=int(char.lower())
            print(":"+str(EmojiNumbers[i])+":",end='')
        else:
            print (char,end='')

if __name__ == '__main__':
    passedArg1=''
    try:
        if(str(argv[1])!=''):
            passedArg1=argv[1]
    except IndexError:
        pass
    genEmojis(passedArg1)
    a=input()

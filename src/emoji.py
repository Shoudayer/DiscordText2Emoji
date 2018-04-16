from sys import argv

def genEmojis(chaine):
  if chaine=='':
    chaine = input("texte :")
  for char in chaine:
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
      print(":regional_indicator_"+char.lower()+": ", end='')
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

import random
import hashlib

def mcls(): # 2 lines down
    print("\n" * 2)

def chooseLang(): #choose language to use in software
    print("        Language | Linguagem        ")
    print("------------------------------------")
    print("- ( 1 ) English   (EN-US)          -")
    print("                                    ")
    print("- ( 2 ) Português (PT-BR)          -")
    print("------------------------------------")

def menuEn(): #Tool menu in english
    print("               TOOLS                ")
    print("------------------------------------")
    print("- ( 1 ) Password Generator         -")
    print("- ( 2 ) Hash Generator (TEXT)      -")
    print("------------------------------------")

def menuPt(): #Tool menu in portuguese
    print("            FERRAMENTAS             ")
    print("------------------------------------")
    print("- ( 1 ) Gerador de Senha Segura    -")
    print("- ( 2 ) Gerador de Hash (TEXTO)    -")
    print("------------------------------------")

def genPassHardUS(size): #function to generate the password (english language)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    specialAlphabet = "!@#$"
    upperalphabet = alphabet.upper()
    pwLen = size
    pwList = []

    for i in range(pwLen // 3):
        pwList.append(alphabet[random.randrange(len(alphabet))])
        pwList.append(specialAlphabet[random.randrange(len(specialAlphabet))])
        pwList.append(upperalphabet[random.randrange(len(upperalphabet))])
        pwList.append(str(random.randrange(10)))
    for i in range(pwLen - len(pwList)):
        pwList.append(alphabet[random.randrange(len(alphabet))])

    random.shuffle(pwList)
    pwString = "".join(pwList)

    print("Your password is:" , pwString)
    choiceGenPassSoft = input("\nDo you want to save it to a file? (Y/N): ")
    if (choiceGenPassSoft == "y"):
        nameText = input("Name of new file: ")
        if (nameText == ""):
            nameText = ("Password")

        nameFile = open(nameText + ".txt", "w")
        nameFile.write("Your password: " + pwString)
        nameFile.close()

        input("\nPress ENTER to close this window...")

    if (choiceGenPassSoft == "n"):
        print("Alright!")

        input("\nPress ENTER to close this window...")

def genPassHardBR(size): #function to generate the password (portuguese language)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    specialAlphabet = "!@#$"
    upperalphabet = alphabet.upper()
    pwLen = size
    pwList = []

    for i in range(pwLen // 3):
        pwList.append(alphabet[random.randrange(len(alphabet))])
        pwList.append(specialAlphabet[random.randrange(len(specialAlphabet))])
        pwList.append(upperalphabet[random.randrange(len(upperalphabet))])
        pwList.append(str(random.randrange(10)))
    for i in range(pwLen - len(pwList)):
        pwList.append(alphabet[random.randrange(len(alphabet))])

    random.shuffle(pwList)
    pwString = "".join(pwList)

    print("Sua senha é:" , pwString)
    choiceGenPassSoft = input("\nVocê deseja salvar a senha em um novo arquivo? (S/N): ")
    if (choiceGenPassSoft == "s"):
        nameText = input("Nome do novo arquivo: ")
        if (nameText == ""):
            nameText = ("Senha")

        nameFile = open(nameText + ".txt", "w")
        nameFile.write("Sua senha: " + pwString)
        nameFile.close()

        input("\nPressione ENTER para fechar a janela...")

    if (choiceGenPassSoft == "n"):
        print("Tudo bem!")

        input("\nPressione ENTER para fechar a janela...")

def genHashFileMenu():
    print("------------------------------------")
    print("- ( 1 ) SHA-256                    -")
    print("- ( 2 ) MD5                        -")
    print("------------------------------------")

def genHashFileTxtSHA256BR():
    message = input("\ndigite o texto: ")
    m = hashlib.sha256(message.encode('utf-8')).hexdigest()
    print("resultado (SHA-256): ", m)
    input("\nPressione ENTER para fechar a janela...")

def genHashFileTxtMD5BR():
    message = input("\ndigite o texto: ")
    m = hashlib.md5(message.encode('utf-8')).hexdigest()
    print("resultado (MD5): ", m)
    input("\nPressione ENTER para fechar a janela...")




def genHashFileTxtSHA256US():
    message = input("\ntype your text: ")
    m = hashlib.sha256(message.encode('utf-8')).hexdigest()
    print("result (SHA-256): ", m)
    input("\nPress ENTER to close this window...")

def genHashFileTxtMD5US():
    message = input("\ntype your text: ")
    m = hashlib.md5(message.encode('utf-8')).hexdigest()
    print("result (MD5): ", m)
    input("\nPress ENTER to close this window...")
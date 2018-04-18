import random
import hashlib

def mcls(): # 2 lines down
    print("\n" * 2)




#### ------------------- PASSWORD GEN FUNCTION (English) -------------------
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




#### ------------------- PASSWORD GEN FUNCTION (Portuguese) -------------------
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




#### ------------------- HASH FUNCTION (English) -------------------
def genHashTxtSHA256US(): #function to generate the TEXT hash (SHA-256)  (english language)
    message = input("\ntype your text: ")
    m = hashlib.sha256(message.encode('utf-8')).hexdigest()
    print("result (SHA-256): ", m)
    input("\nPress ENTER to close this window...")

def genHashTxtMD5US(): #function to generate the TEXT hash (MD5)  (english language)
    message = input("\ntype your text: ")
    m = hashlib.md5(message.encode('utf-8')).hexdigest()
    print("result (MD5): ", m)
    input("\nPress ENTER to close this window...")

def genHashFileSHA256US(): #function to generate the FILE hash (SHA-256)  (english language)
    hashNameFile = input ("Type the file name (with the file extension): ")
    blockSize = 65536   # 2^16
    hasher = hashlib.sha256()
    with open(hashNameFile, 'rb') as afile:
        buf = afile.read(blockSize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blockSize)
    print("result (SHA-256): " + hasher.hexdigest())
    input("\nPress ENTER to close this window...")

def genHashFileMD5US(): #function to generate the FILE hash (MD5)  (english language)
    hashNameFile = input ("Type the file name (with the file extension): ")
    blockSize = 65536   # 2^16
    hasher = hashlib.md5()
    with open(hashNameFile, 'rb') as afile:
        buf = afile.read(blockSize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blockSize)
    print("result (MD5): " + hasher.hexdigest())
    input("\nPress ENTER to close this window...")




#### ------------------- HASH FUNCTION (Portuguese) -------------------
def genHashTxtSHA256BR(): #function to generate the TEXT hash (SHA-256)  (portuguese language)
    message = input("\ndigite o texto: ")
    m = hashlib.sha256(message.encode('utf-8')).hexdigest()
    print("resultado (SHA-256): ", m)
    input("\nPressione ENTER para fechar a janela...")

def genHashTxtMD5BR(): #function to generate the TEXT hash (MD5)  (portuguese language)
    message = input("\ndigite o texto: ")
    m = hashlib.md5(message.encode('utf-8')).hexdigest()
    print("resultado (MD5): ", m)
    input("\nPressione ENTER para fechar a janela...")


def genHashFileSHA256BR(): #function to generate the FILE hash (SHA-256)  (portuguese language)
    hashNameFile = input ("Digite o nome do arquivo desejado (com a extensão do arquivo): ")
    blockSize = 65536   # 2^16
    hasher = hashlib.sha256()
    with open(hashNameFile, 'rb') as afile:
        buf = afile.read(blockSize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blockSize)
    print("resultado (SHA-256): " + hasher.hexdigest())
    input("\nPressione ENTER para fechar a janela...")


def genHashFileMD5BR(): #function to generate the FILE hash (MD5)  (portuguese language)
    hashNameFile = input ("Digite o nome do arquivo desejado (com a extensão do arquivo): ")
    blockSize = 65536   # 2^16
    hasher = hashlib.md5()
    with open(hashNameFile, 'rb') as afile:
        buf = afile.read(blockSize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blockSize)
    print("resultado (MD5): " + hasher.hexdigest())
    input("\nPressione ENTER para fechar a janela...")
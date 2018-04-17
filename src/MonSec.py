import dep  # Import file "dep" (dependencies)

print("\nMonSec v0.3.0 [Monteiro Innovation - 2018]\n")

rpt = True  # var for exception handling

dep.chooseLang()
mainLang = input("Language: ")

# ------------------ ENGLISH ------------------

if (mainLang == "en-us" or mainLang == "en" or mainLang == "1"):
    dep.mcls()
    dep.menuEn()

    mainOpt = input("\nChoose an option: ")

    if (mainOpt == '1'):
        while (rpt == True):
            try:
                passSize = int(input("\ntype how many digits the password will have: "))
                dep.genPassHardUS(passSize)
                rpt = False
            except:
                print("Invalid value! Type just NUMBERS.")

    if (mainOpt == '2'):
        dep.mcls()
        dep.genHashMenu()
        hashGenOpt = input("Choose an option: ")

        if (hashGenOpt == '1'):
            dep.genHashTxtSHA256US()

        if (hashGenOpt == '2'):
            dep.genHashTxtMD5US()

    if (mainOpt == '3'):
        dep.mcls()
        dep.genHashMenu()
        hashGenOpt = input("Choose an option: ")

        if (hashGenOpt == '1'):
            while (rpt == True):
                try:
                    dep.genHashFileSHA256US()
                    rpt = False
                except:
                    print ("File not found! Try again...\n")

        if (hashGenOpt == '2'):
            while (rpt == True):
                try:
                    dep.genHashFileMD5US()
                    rpt = False
                except:
                    print ("File not found! Try again...\n")

# ------------------ PORTUGUESE ------------------

if (mainLang == "pt-br" or mainLang == "pt" or mainLang == "2"):
    dep.mcls()
    dep.menuPt()

    mainOpt = input("\nEscolha uma opção: ")

    if (mainOpt == '1'):
        while (rpt == True):
            try:
                passSize = int(input("\nInsira o número de digitos que deseja ter na senha: "))
                dep.genPassHardBR(passSize)
                rpt = False
            except:
                print("Valor inválido! Digite apenas NÚMEROS.")


    if (mainOpt == '2'):
        dep.mcls()
        dep.genHashMenu()
        hashGenOpt = input("Escolha uma opção: ")

        if (hashGenOpt == '1'):
            dep.genHashTxtSHA256BR()

        if (hashGenOpt == '2'):
            dep.genHashTxtMD5BR()

    if (mainOpt == '3'):
        dep.mcls()
        dep.genHashMenu()
        hashGenOpt = input("Escolha uma opção: ")

        if (hashGenOpt == '1'):
            while (rpt == True):
                try:
                    dep.genHashFileSHA256BR()
                    rpt = False
                except:
                    print ("Arquivo não encontrado! Tente novamente...\n")

        if (hashGenOpt == '2'):
            while (rpt == True):
                try:
                    dep.genHashFileMD5BR()
                    rpt = False
                except:
                    print ("Arquivo não encontrado! Tente novamente...\n")
import dep  # Import file "dep" (dependencies)

print("\nMonSec v0.2.0 [Monteiro Innovation - 2018]\n")

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
        dep.genHashFileMenu()
        hashGenOpt = input("Choose an option: ")

        if (hashGenOpt == '1'):
            dep.genHashFileTxtSHA256US()

        if (hashGenOpt == '2'):
            dep.genHashFileTxtMD5US()

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
        dep.genHashFileMenu()
        hashGenOpt = input("Escolha uma opção: ")

        if (hashGenOpt == '1'):
            dep.genHashFileTxtSHA256BR()

        if (hashGenOpt == '2'):
            dep.genHashFileTxtMD5BR()
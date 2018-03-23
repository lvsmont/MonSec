import dep  # Import file "dep" (dependencies)

print("\nMonSec v0.1.1 [Monteiro Innovation - 2018]\n")

rpt = True  # var for exception handling

dep.chooseLang()
mainLang = input("Language: ")

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

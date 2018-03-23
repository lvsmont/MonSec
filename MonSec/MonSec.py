import dep

print("\nMonSec v0.1 [Monteiro Innovation - 2018]\n")

dep.chooseLang()
mainLang = input("Language: ")

if (mainLang == "en-us" or mainLang == "en" or mainLang == "1"):
    dep.mcls()
    dep.menuEn()

    mainOpt = int(input("\nChoose an option: "))

    if (mainOpt == 1):
        tamanhoPass = int(input("\ntype how many digits the password will have: "))
        dep.genPassHardUS(tamanhoPass)


if (mainLang == "pt-br" or mainLang == "pt" or mainLang == "2"):
    dep.mcls()
    dep.menuPt()

    mainOpt = int(input("\nEscolha uma opção: "))

    if (mainOpt == 1):
        tamanhoPass = int(input("\nInsira o número de digitos que deseja ter na senha: "))
        dep.genPassHardBR(tamanhoPass)
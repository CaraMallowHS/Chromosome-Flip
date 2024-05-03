def flip_chromosome(chrom):
    chrom = chrom.lower()
    if chrom=="a":
        return "T"
    elif chrom=="c":
        return "G"
    elif chrom=="t":
        return "A"
    else:
        return "C"
    
global chromlist
while(True):
    print()
    menu = int(input("""-------\nMenu: \n 1. 염기서열 입력하기,\n 2. 염기서열 전사과정 거치기\n 3.원래대로 되돌리기\n 4. 종료\n-------\n"""))
    if menu ==1:
        add = input("염색체 속 염기서열을 입력해 주십시오 \n")
        chromlist = [*add]
    elif menu ==2:
        changedchrom = list(map(flip_chromosome, chromlist))

        newchrom = ""
        for chrom in changedchrom:
            newchrom += chrom
        print(newchrom, "\n")
    elif menu == 3:
        orgchrom = ""
        for chrom in chromlist:
            orgchrom += chrom.upper()
        print(orgchrom, "\n")
    elif menu==4:
        print("종료.")
        break

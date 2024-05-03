chromosomelist = []

while(True):
    print()
    menu = int(input("1. 염기서열 입력하기, 2. 염기서열 전사과정 거치기, 3.원래대로 되돌리기, 4. 종료"))
    if menu ==1:
        add = input("염색체 속 염기서열을 입력해 주십시오 \n")
        chromosomelist.append(add)
    elif menu ==2:
        """a를 t로, c를 g로, t를 a로, g를 c로 바꾸기 기능 """
    elif menu == 3:
        """원래대로 되돌리는 기능"""
    else:
        break
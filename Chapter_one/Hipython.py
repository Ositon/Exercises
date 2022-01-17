#PLAY WITH ME BABY

print('       *      \n      **      \n     ****     \n    ******     \n   ********     ')

def Mydrag():
    if num==1:
        print('       *      ')
    if num==2:
        print('      **      ')
    if num==3:
        print('     ****     ')
    if num==4:
        print('    ******     ')
    if num==5:
        print('   ********     ')

'''while True:
    num=int(input('Ingresa una numero entre 1 y 5: \nCero para Salir\n:'))
    if num==0:
     break'''
'''option=False
while not option:
    num=int(input('Ingresa una numero entre 1 y 5: \nCero para Salir\n:'))
    Mydrag()
    if num==0:
        option=True'''
num=None
while num!=0:
    num=int(input('Ingresa una numero entre 1 y 5: \nCero para Salir\n:'))
    Mydrag()

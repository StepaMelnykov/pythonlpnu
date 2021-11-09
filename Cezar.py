alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*/'
alfavit_UA = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ1234567890*()/'
krok = int(1)       #крок на який проходитеме зміщення
while True:

    message = input("Повідомлення для шифрування: ").upper()        #повідомлення що буде штфруватися
    itog = ''
    lang = input('Виберіть мову UA/EN: ')       #пишемо капслоком мову UA або EN


    if lang == 'UA':
        for i in message:
            mesto = alfavit_UA.find(i)
            new_mesto = mesto + krok                #мова шифрування укр переміщуєм крок на 1 вперід
            if i in alfavit_UA:
                itog += alfavit_UA[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EN.find(i)
            new_mesto = mesto + krok                        #тосаме тіки з англ мовою
            if i in alfavit_EN:
                itog += alfavit_EN[new_mesto]
            else:
                itog += i
    print(itog)                 #виводим те що вийшло
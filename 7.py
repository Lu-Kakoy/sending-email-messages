# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они
# отправляются от одного и того же пользователя(администрации или
# службы поддержки). Тем не менее должна быть возможность сменить
# его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
# Создайте функцию send_email, которая принимает 2 обычных
# аргумента: сообщение и получатель и 1 обязательно именованный
# аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# 1. Проверка на корректность e-mail отправителя и получателя.
# 2. Проверка на отправку самому себе.
# 3. Проверка на отправителя по умолчанию.
# standart_sender = 'sender@yandex.ru'
# sender = 'sender@yandex.ru'





def fun1(sender):                                                                                                       # Проверка на корректность e-mail отправителя
    if sender.find('@') == -1:
        print('все  плохо1')        #<<<флаги для выявления ошибок в отдельных частях кода
        st1 = 0
    else:
        # print('все хорошо1')
        if sender.endswith('.ru') == True:
            # print('все хорошо2')
            st1 = 1
        elif sender.endswith('.com') == True:
            # print('все хорошо3')
            st1 = 1
        else:
            print('почта указана не верно')
            st1 = 0
    return st1



def fun2(recipient):                                                                                                    # Проверка на корректность e-mail получателя
    if recipient.find('@') == -1:
        # print('все плохо2')
        st2 = 0
    else:
        # print('все хорошо1')
        if recipient.endswith('.ru'):
            # print('все хорошо2')
            st2 = 1
        elif recipient.endswith('.com'):
            # print('все хорошо3')
            st2 = 1
        else:
            print('почта указана не верно')
            st2 = 0
    return st2


def fun3(sender, recipient):                                                                                            # Проверка на отправку самому себе
    if sender == recipient:
        print('нельзя отправить сообщение себе!')
        st3 = 0
    else:
        print('почта отправителя не является почтой получателя')
        st3 = 1
    return st3


def fun4(standart_sender, sender):                                                                                      # Проверка на отправителя по умолчанию
    if standart_sender == sender:
        print(f'для отправки сообщения использована стандартная почта отправителя - {standart_sender}')
    else:
        print(f'для отправки сообщения использована почта отличная от стандартной - {sender}')



def start():
    choice1 = ''
    mail = {}
    number_of_messages = 0
    while choice1 != 'end':         # Для завершения работы программы нужно написать "end"
        choice1 = input('''
        1 - написать письмо
        2 - посмотреть почту
        выбор: 
        ''')
        if choice1 == '1':
            end = ''
            standart_sender = 'sender@yandex.ru'
            while end != 'end':
                # print('этап - 1')
                # sender = 'sender@yandex.ru'
                # recipient = 'recipient@gmail.com'
                # message1 = 'Hello World, i came for you.'
                sender = input('введите адрес электронной почты отправителя: ')
                recipient = input('Введите адрес электронной почты получателя: ')            # прием данных пользователя
                message1 = input('введите сообщение: ')
                stage1 = fun1(sender)                                   #<<< Проверка на корректность e-mail отправителя
                if stage1 == 1:
                    while True:
                        # print('этап - 2')
                        stage2 = fun2(recipient)                         #<<< Проверка на корректность e-mail получателя
                        if stage2 == 1:
                            # print('этап - 3')
                            stage3 = fun3(sender, recipient)                       #<<< Проверка на отправку самому себе
                            if stage3 == 1:
                               # print('на 3 этапе все хорошо')
                               fun4(standart_sender, sender)                   #<<< Проверка на отправителя по умолчанию
                               number_of_messages += 1         #<Используется для присвоения уникальных ключей для писем и их дальнейшего извлечения
                               message2 = f'отправитель - {sender}: {message1} получатель - {recipient}'
                               mail[number_of_messages] = message2
                               end = 'end'
                               break
                            else:
                                break
        elif choice1 == '2':
            choice2 = int(input(f'''у вас {number_of_messages} писем, какое хотите прочесть?
выбор: '''))
            print(mail.get(choice2, 'такого письма нет!'))


start()


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



# email2 = email1.count

# test1 = 'st@roka'

# test2 = test1.find('@')
# print(test2)

def fun1(sender):
    if sender.find('@') == -1:
        print('все  плохо1')
        st1 = 0
    else:
        print('все хорошо1')
        if sender.endswith('.ru') == True:
            print('все хорошо2')
            st1 = 1
        elif sender.endswith('.com') == True:
            print('все хорошо3')
            st1 = 1
        else:
            print('почта указана не верно')
            st1 = 0
    return st1

# fun1(sender)

# print('''
# 2
# ''')

# recipient = 'sender@gmail.com'

def fun2(recipient):
    if recipient.find('@') == -1:
        print('все плохо2')
        st2 = 0
    else:
        print('все хорошо1')
        if recipient.endswith('.ru') == True:
            print('все хорошо2')
            st2 = 1
        elif recipient.endswith('.com') == True:
            print('все хорошо3')
            st2 = 1
        else:
            print('почта указана не верно')
            st2 = 0
    return st2

# fun2(recipient)

# print('''
# 3
# ''')

def fun3(sender, recipient):
    if sender == recipient:
        print('нельзя отправить сообщение себе!')
        st3 = 0
    else:
        print('почта отправителя не является почтой получателя')
        st3 = 1
    return st3

# fun3(sender, recipient)

# print('''
# 4
# ''')

def fun4(standart_sender, sender):
    if standart_sender == sender:
        print(f'для отправки сообщения использована стандартная почта отправителя - {standart_sender}')
    else:
        print(f'для отправки сообщения использована почта отличная от стандартной - {sender}')

# fun4(standart_sender, sender)


def start():
    choice1 = ''
    end = ''
    mail = {}
    number_of_messages = 0
    while choice1 != 'end':
        choice1 = ''
        choice1 = input('''
        1 - написать письмо
        2 - посмотреть почту
        выбор: 
        ''')
        if choice1 == '1':
            end = ''
            standart_sender = 'sender@yandex.ru'
            while end != 'end':
                print('этап - 1')
                # sender = 'sender@yandex.ru'
                sender = input('введите адрес электронной почты отправителя: ')
                # recipient = 'recipient@gmail.com'
                recipient = input('Введите адрес электронной почты получателя: ')
                # message1 = 'Hello World, i came for you.'
                message1 = input('введите сообщение: ')
                stage1 = fun1(sender)

                if stage1 == 1:
                    while True:
                        print('этап - 2')
                        stage2 = fun2(recipient)
                        if stage2 == 1:
                            print('этап - 3')
                            stage3 = fun3(sender, recipient)
                            if stage3 == 1:
                               print('на 3 этапе все хорошо')
                               fun4(standart_sender, sender)
                               number_of_messages += 1
                               message2 = (f'отправитель - {sender}: {message1} получатель - {recipient}')
                               mail[number_of_messages] = message2
                               end = 'end'
                               break
                            else:
                                break

                        else:
                            # print('введите корректный адрес получателя')
                            recipient = input('Введите корректный адрес электронной почты получателя: ')
                else:
                    # print('введите корректный адрес отправителя')
                    sender = input('введите корректный адрес электронной почты отправителя: ')
        elif choice1 == '2':
            choice2 = int(input(f'''у вас {number_of_messages} писем, какое хотите прочесть?
выбор: '''))
            print(mail.get(choice2, 'такого письма нет!'))


start()











































# Codewars, Chekio
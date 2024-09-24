def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    a = "@"
    suffix = ('.com', '.ru', '.net')
    x = recipient.find(a)
    z = sender.find(a)
    is_true = True
    if x == -1 or z == -1 :
        is_true = False
    else:
        is_true1 = recipient.endswith(suffix)
        is_true2 = sender.endswith(suffix)
        if is_true1 == False or is_true2 == False :
            is_true = False

    if is_true == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient :
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com' :
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

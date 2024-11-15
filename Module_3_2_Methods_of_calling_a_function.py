def send_email(message = type(str), recipient = type(str), *,sender = 'university.help@gmail.com'):
    if not all (('@' in recipient and '@' in sender and
                 recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'),
                 sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}.')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}.')
    else: print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: {sender} на адрес: {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print()
send_email('Здравствуйте, если вы получили это сообщение, значит задание выполнено верно!', 'HomeWork@gmail.com')
send_email('Здравствуйте, вы получили это письмо связи с тем, что наш университет сменил почтоый адрес.', 'Home1Work@mail.ru',
           sender='UrbanUniversity@helper.com')
send_email('Здравствуйте, необходимо исправить ошибки в адресе электронной почты', 'Home1Work@mail.ru', sender='UrbanUniversity@helper.org')
send_email('Здравствуйте, необходимо исправить ошибки в адресе электронной почты', 'Home1Work@mail.su', sender='UrbanUniversity@helper.ru')
send_email('Напоминаю самому себе о вебинаре', 'HomeWork@gmail.com', sender='HomeWork@gmail.com')
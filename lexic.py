from settings import total_tasks
n = total_tasks
# RU: dict[str, dict[str, str]] = {}
lex: dict[str:str] = {
        # admin
        'adm_review': 'Принять ВСЕ файлы от',
        'msg_to_admin': '📩 Сообщение от',
        'msg_from_admin': 'Сообщение от администратора:',
        'deleted': 'Удалено, вот бекап до удаления',
        'adm_reject': '',
        'wrong_rej_form': 'Неверный формат: каждая новая строка должна начинаться с числа и '
                          'оканчиваться переносом строки.\nНапиши причину отказа снова.',
        'adm_help': 'Команды, доступные админу (123 заменить на нужный айди слитно):'
                    '\n\n- Получить файлы юзера (фото и видео), вместо status указать в каком статусе нужны файлы - review, accept или reject:'
                    '\n<code>files id123 status</code>'
                    '\n\n- Отправить "Сообщение от администратора" юзеру по айди:'
                    '\n<i>Ответить на любое сообщение, в котором есть айди (сообщ. от бота, или написать самому <code>id123</code> и ответить на свое сообщение)</i>'
                    '\n\n- Принять файлы без кнопок:'
                    '\n<code>accept id123</code>'
                    '\n\n- Отклонить файлы без кнопок:'
                    '\n<code>reject id123</code> (далее ответом написать причины отказа)'
                    '\n\n- Получить tsv со ссылками на скачивание всего, что юзер скинул'
                    '\n<code>tsv id123</code>'
                    '\n\n- Получить базы данных (это 4 разные  команды)'
                    '\n<code>send bd / send logs / send info / send all</code>'
                    '\n\n- Количество админов: {}, валидаторов: {}',

        # users
        'help': '⚙️ По вопросам проверки заданий и проблем с ботом пишите @its_dmitrii'
                '\n\nСписок команд:'
                '\n/help - помощь'
                '\n/next - следующее задание'
                '\n/status - посмотреть список моих заданий'
                '\n/cancel - отменить отправку файла'
                '\n/personal - указать данные'
                '\n/instruct - посмотреть инструкцию',

        # команда отмены
        'cancel': 'Укажите через пробел номера заданий (две цифры), для которых вы хотите отменить отправку файла. Пример сообщения:'
                  '\n\n01 02 16',
        'cancel_fail': 'Нет файлов, которые вы можете удалить',
        'cancel_ok': 'Ок. Удалены ваши файлы из заданий: ',
        'cancel_not_found': 'Задания под следующими номерами либо уже отправлены на проверку, либо вы их не присылали: ',
        'cancel_wrong_form': 'Неверный формат. Я ожидаю номера заданий через пробел.',

        'no_ref': 'Ссылка недействительна. Спросите ссылку у того, кто привел вас к нам.',
        'start': 'Привет!\n\n'
                 'Мы собираем фото для <b>обучения нейросети</b> распознавать эмоции. '
                 f'Вам предстоит выполнить {n} заданий. В каждом будет дан фото-пример и краткое описание, что нужно заснять. '
                 f'Когда вы выполните все {n} заданий - ваши файлы будут отправлены нам <b>на проверку</b>.\n\n'
                 'Если какие-либо задания будут выполнено не правильно - мы их отклоним и попросим вас переделать (не все, а только неправильно выполненные). '
                 f'Когда все {n} заданий будут успешно приняты - вы получите уведомление, и после этого в течение недели вы получите <b>оплату</b>.\n'
                 
                 f'\n<b>Сами задания</b> - нужно {n} фотографий: 3 выражения лица с 5 ракурсов'
                 '\n<b>3 выражения:</b>'
                     '\n- Нейтральное (без улыбки, рот закрыт)'
                     '\n- Улыбка (с зубами или без - не важно)'
                     '\n- Показать зубы (четко видны оба ряда зубов)'
                     '\n<b>5 ракурсов:</b>'
                     '\n- Спереди (анфас),'
                     '\n- Левый профиль (90 градусов)'
                     '\n- Правый профиль'
                     '\n- Левый угол (~ 45 градусов)'
                     '\n- Правый угол'                 
                 
                 '\n\nМожете нажать:'
                 '\n/next для выдачи следующего задания'
                 '\n/status для просмотра статуса ваших заданий'
                 '\n/help для поддержки'
                 '\n/cancel чтобы отменить отправку файла.'
                 '\n\nПрежде чем продолжить, пожалуйста, ознакомьтесь с нашей <b>политикой конфиденциальности</b> и нажмите кнопку ✅.',

        'pol_agree': 'С политикой ознакомлен и согласен',
        'instuct_agree': 'С требованиями ознакомлен',
        'start_again': 'Чтобы увидеть список команд, нажмите /help',
        'ban': 'Вам заблокирован доступ к заданиям.',
        'vert': 'Нужно снимать вертикально, а не горизонтально. Пожалуйста, переделайте.',
        'horiz': 'Нужно снимать горизонтально, а не вертикально. Пожалуйста, переделайте.',
        'big_file': 'Файлы тяжелее 50 Мегабайт не принимаются.',
        'small_file': 'Вес файла всего {} Мб, это слишком низкое качество. Пожалуйста, снимите в высоком качестве.',
        'privacy_missing': 'Нажмите галочку, чтобы согласиться с политикой конфиденциальности.',
        'instruct1': 'Для съемки вам нужен второй человек, так как нам требуется расстояние около 1м.'
                     'Ознакомьтесь с <b>требованиями</b> к отправляемым файлам:\n'
                    '\n<u>1. Чистая камера</u>: Убедитесь, что объектив не загрязнен.'
                    '\n<u>2. Разрешение от 4К</u>: Не менее 2100х3800 пикселей. Нужно снимать на основную камеру телефона, не на селфи-камеру.'
                    '\n<u>3. Открытое лицо:</u> Ваше лицо на фото полностью открыто, ничем не прикрыто и не обрезано.'
                    '\n<u>4. Хорошее освещение:</u> Без засветов, бликов на лице или затемнений. Белый или желтый свет.'
                    '\n<u>5. Посторонние:</u> В кадре не должно быть других людей (ни живых, ни на картинках), даже их волос или рук.'
                    '\n<u>6. Съёмка:</u> Запрещены любые фильтры/эффекты/маски.'
                    '\n<u>7. Запрещено на голове:</u> наушники, маски, темные очки, головные уборы (кроме религиозных), рисунки на лице, странные костюмы.'
                    '\n<u>8. Отражения:</u> На фоне и рядом с вами не должно быть зеркал и иных предметов, где вы будете отражаться.',

        'full_hd': 'Нужно отправлять файл <b>без сжатия</b>. Если не знаете как, то'
                   ' <a href="https://www.youtube.com/embed/qOOMNJ0gIss">посмотрите пример</a> (9 сек).',
        'instruct2': 'Можете приступать к выполнению - нажмите команду /next и бот покажет вам следующее задание, после чего сделайте фото и отправьте в этот чат.',

        'album': 'Отправляйте файлы по одному, не группой',
        'receive': 'Получен файл для задания {}.\nНажмите /next для следующего задания',

        'all_sent': 'Спасибо! Вы отправили все нужные файлы. Ожидайте проверки вашей работы.\n'
                    'Нажмите команду /personal, чтобы указать ваш пол и возраст, если еще не указывали.',
        'no_more': 'Нет доступных заданий',
        'reject': 'Мы проверили вашу работу. К сожалению, часть файлов не прошла проверку. Ознакомьтесь с нашими '
                  'комментариями и нажмите команду /next для получения задания.'
                  '\nДалее в каждой строке номер неверно выполненного задания и комментарий к нему:',
        'all_approved': 'Ура! Ваш сет успешно прошел первую проверку на качество.\n'
                        'В течение 1-2 дней мы более внимательно проверим вашу работу. Возможно, потребуется внести новые исправления. '
                        'Если всё сделано правильно, то с вами свяжется человек, от которого вы получили приглашение. Ваш айди: ',

        # персуха
        'age': 'Укажите ваш возраст - две цифры слитно',
        'age_bad': 'Неверный формат, я ожидаю две цифры',
        'gender': 'Укажите ваш пол. Отправьте одну латинскую букву: m (мужской) или f (женский)',
        'gender_bad': 'Неверный формат, я ожидаю одну латинскую букву: m или f',
        'race': 'Укажите вашу расу',
        'fio': 'Укажите ваше ФИО',
        'fio_bad': 'Неверный формат, я ожидаю два или три слова',
        'country': 'Напишите вашу страну проживания',
        # 'fio_bad': 'Неверный формат, я ожидаю два или три слова',
        'pd_ok': 'Ваши данные сохранены.',

        'tlk_ok': 'Ваши данные сохранены. '
                  'Введите следующие данные в интерфейсе задания на Толоке (коснитесь код, чтобы скопировать):'
                  '\nПроверочный код: <code>B54U83</code>'
                  '\nTelegram-id: <code>{}</code>',

        #  тесты

        # шаблоны
        'user_pd':     {
                  "referral": None,
                  "first_start": None,
                  "accept_date": None,
                  "tg_username": None,
                  "tg_fullname": None,
                  "lang_tg": None,
                  "lang": None,
                  "tasks": None,
                  "reject": 0,
                  "total_sent": 0,
                  "last_sent": None,
                  "status": None,
                  "fio": None,
                  "age": None,
                  "gender": None,
                  "country": None,
                  "race": None,
                },

        'log': 'inn',

}

ami = "01.03.02"

hello_mes = "Привет! Я могу предоставить текущую статистику " \
            "о числе поданных заявлений на кафедру КТ университета ИТМО. Также можно запросить информацию " \
            "об отдельном абитуриенте или получить ответы на некоторые FAQ. " \
            "Если у меня что-то отвалилось и не работает, пожалуйста, постучитесь сюда - @matveich19\n" \
            "Список доступных команд:\n" \
            "/stats - статистика поданных заявлений\n" \
            "/search ФИО - поиск абитуриента\n" \
            "/new - новые заявки за день\n" \
            "/faq - ответы на некоторые FAQ\n" \
            "/links - разные полезные ссылки\n" \
            "/help - помощь"

tip_mes = "Формат команды: /search ФИО"
error_mes = "Неизвестная команда. /help"
not_found_mes = "По вашему запросу ничего не найдено"
too_many_abits = "Найдено слишком большое количество заявок. Попробуйте уточнить запрос"
no_abits = "На сегодня пока нет новых заявок"

links_mes = "Подробности о кафедре — http://codeforces.com/blog/entry/52921\n" \
            "Наш паблик с новостями ВК — https://vk.com/ct_ifmo\n" \
            "Чат со студентами КТ, которые готовы ответить на любые вопросы — " \
            "https://t.me/joinchat/AAAAAEM_TwDXkGr4DiXyLg\n" \
            "Канал для важных вопросов и объявлений — https://telegram.me/ct_2017\n" \
            "FAQ для абитуриентов — https://vk.com/away.php?to=http%3A%2F%2Fct.ifmo.ru%" \
            "2Fru%2Fpage%2F17003%2FFAQ_dlya_abiturientov.htm&post=-131616069_178&cc_key=\n" \
            "Викиконспекты - http://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%" \
            "D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0\n" \
            "МЕМЫ - https://vk.com/ktmemes\n" \
            "Куча полезных конспектов по 1 курсу - " \
            "https://drive.google.com/drive/folders/0B68xxdocwxnDMjRDNklhWktsa0U\n" \
            "Учебные будни - https://vk.com/sleepingkt"

faq = "*Если количество олимпиадников будет больше, чем количество бюджетных мест?*\n" \
      "Среди олимпиадников конкурс не проводится. Будут зачислены на бюджет все абитуриенты, " \
      "имеющие право поступления БВИ вне зависимости от количества мест.\n\n" \
      "*К чему готовиться перед поступлением?*\n" \
      "1 сентября -- на КТ вступительный тест на распределение по группам. Будут задания по математике " \
      "(уровня последних из ЕГЭ, несложные олимпиадные задания) и задания по программированию вида написать " \
      "программу (уровня несложных олимпиадных, возможно что-то на бинпоиск, дп, графы, строки). " \
      "Группы формируются по результатам теста, но можно переводиться между группами по результатам семестра.\n\n" \
      "*Как проходит распределение по группам?*\n" \
      "По результатам вступительного теста на распределение по группам, который проводится в день первокурсника " \
      "(~1 сентября). (см. предыдущий вопрос)\n\n" \
      "*Если я напишу эту работу очень плохо меня отчислят?*\n" \
      "Нет, вы просто будете зачислены в слабую группу.\n\n" \
      "*Если меня зачислят в группу слабее/сильнее, чем я хотел, могу ли я перевестись?*\n" \
      "Можете. Если вы хотите в сильную группу, вы должны доказать, что вы можете освоить программу сильной группы, " \
      "а именно сдать сессию очень хорошо. Если вы хотите облегчить себе жизнь, то ничего делать не придется. " \
      "Можно нам просто рассказать об этом.\n\n" \
      "*А когда заселение в общежитие?*\n" \
      "Заселение будет в 20-х числах августа, точную дату всем сообщат ближе к этому времени.\n\n" \
      "*Я отправляю документы по почте. Через какую службу это лучше сделать?*\n" \
      "DHL скорее всего будет оптимальным вариантом: быстро (до 3 дней), надежно и недорого. Для абитуриентов " \
      "у них есть специальное предложение по доставке за 650 рублей.\n\n\n" \
      "*С сессией дела обстоят следующим образом:*\n" \
      "1. В течении семестра вы, возможно, получаете баллы на практиках/лабах/etc. (не для всех предметов верно)\n" \
      "2. Если препод не говорит обратное, то вы допущены ко всем экзаменам, независимо от результатов семестра" \
      " и прошлых сессий\n" \
      "3. Если на момент окончания сессии сданы не все зачётные/экзаменационные предметы, у вас долги\n" \
      "4. Долги сдаются тому же преподавателю по договоренности с ним\n" \
      "5. Если вас вызвали на кафедральную комиссию — вы, скорее всего, отчислены\n" \
      "К слову, пересдач не менее, чем одна. Можно пытаться закрыть предмет на комиссии, но это сложнее;" \
      " к тому же после отчисления с комиссии нельзя восстановиться\n" \
      "А вообще преподаватель обычно в самом начале семестра говорит условия сдачи предмета, в т.ч. на 3/4/5\n" \
      "(via @faerytea)"

from main import *

hero_kachestvo_imen = "Добрый"
hero_imen = "человек"
place1_imen = "дом"
place2_imen = "кремль"
action1_inf = "думать"
action2_inf = "жить"
action3_inf = "какать"
hero2_imen = "домоправительница"
hero2_dop = "умная"
subject1_imen = "ложка"
subject2_imen = "кошка"
subject4_imen = "чеснок"
subject5_imen = "ястреб"
subject6_imen = "печень"
hero_got_rod = get_rod(hero_imen)
hero2_dop_tvar = tvar(hero2_dop)
place1_vin = vin(place1_imen)
action1_proshed_vr = change_time_verb(action1_inf, "past", hero_got_rod)
place2_rod = rod(place2_imen)
place2_vin = vin(place2_imen)
hero_kachestvo_rod = rod(hero_kachestvo_imen)
hero_rod = rod(hero_imen)
hero2_rod = rod(hero2_imen)
hero2_got_rod = get_rod(hero2_imen)
hero2_sam = change_rod("сама", hero2_got_rod, "past")
print(hero2_sam)
day = random.choice(["вчера", "сегодня", "на прошлой неделе", "в прошлом месяце"])
prichina = random.choice([f"{change_rod('мыть', hero2_got_rod, 'past')} зебру", f"{change_rod('пробивать', hero2_got_rod, 'past')} прессак медведю"])
subject1_vin = vin(subject1_imen)
subject1_rod = rod(subject1_imen)
subject2_vin = vin(subject2_imen)
subject2_rod = rod(subject2_imen)
subject1_rod = rod(subject1_imen)
subject4_vin = vin(subject4_imen)
subject5_vin = vin(subject5_imen)
subject5_rod = rod(subject5_imen)
subject5_tvar = tvar(subject5_imen)
subject6_rod = rod(subject6_imen)


kasha_is_topora = f"""
{hero_kachestvo_imen} {hero_imen} шёл на {place1_vin}. {action1_proshed_vr} в пути, {action2_inf} хочется. Дошёл до {place2_rod}, постучал в крайнюю избу:
- Пустите {action3_inf} {hero_kachestvo_rod} {hero_rod} Дверь отворила {hero2_imen}.
- Заходи, {hero_kachestvo_imen}.
- А нет ли у тебя, {hero2_imen}, перекусить чего? У {hero2_rod} всего вдоволь, а {hero_rod} поскупилась накормить, прикинулась {hero2_dop_tvar}.
- Ох, {hero_kachestvo_imen} {hero_imen}, и {hero2_sam} {day} ещё ничего не ела: {prichina}.
- Ну, нет так нет,- {hero_imen} говорит. Тут он приметил под лавкой {subject1_imen}.
- Коли нет ничего иного, можно {action3_inf} {subject2_vin} и из {subject1_vin}.

{hero2_imen} руками всплеснула:
- Как так из {subject1_rod} {subject2_vin} {action3_inf}?
- А вот как, дай-ка {subject4_imen}.
{hero2_imen} принесла {subject4_vin}, {hero_imen} вымыл {subject1_vin}, опустил в {subject4_vin}, налил воды и поставил на огонь.
{hero2_imen} на {hero_rod} глядит, глаз не сводит.

Достал {hero2_imen} ложку, помешивает варево. Попробовал.
- Ну, как? - спрашивает {hero2_imen}.
- Скоро будет готова, - {hero_imen} отвечает, - жаль вот только, что посолить нечем.
- Соль-то у меня есть, посоли.
{hero_imen} посолил, снова попробовал.
- Хороша! Ежели бы сюда да горсточку {subject5_rod}! {hero2_imen} засуетилась, принесла откуда-то мешочек {subject5_rod}.
- Бери, заправь как надобно. Заправил варево {subject5_tvar}. Варил, варил, помешивал, попробовал. Глядит {hero2_imen} на {hero_imen}а во все глаза, оторваться не может.
- Ох, и каша хороша! - облизнулся {hero_imen}.- Как бы сюда да чуток {subject6_rod} - было бы и вовсе объедение.
Нашлось у старухи и масло.

Сдобрили {subject2_vin}.
- Ну, {hero2_imen}, теперь подавай хлеба да принимайся за ложку: станем {subject2_vin} есть!
- Вот уж не думала, что из {subject1_rod} эдакую добрую {subject2_vin} можно сварить, - дивится {hero2_imen}.
Поели вдвоем {subject2_vin}. {hero2_imen} спрашивает:
- Служивый! Когда ж {subject1_vin} будем есть?
- Да, вишь, он не уварился,- отвечал {hero_imen},- где-нибудь на дороге доварю да позавтракаю!
Тотчас припрятал {subject1_vin} в ранец, распростился с хозяйкою и пошёл в иную {place2_vin}.

Вот так-то {hero_imen} и {subject2_rod} поел и {subject1_vin} унёс!
"""
print(kasha_is_topora)

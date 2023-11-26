import json

import psycopg2
import requests

# url = 'https://api.hh.ru/employers'
# params = {
#             "page": 0,
#             "text": 'яндекс',
#             "per_page": 99,
#             "only_with_vacancies" : True
#         }
# req = requests.get(url, params)
# all_data = json.loads(req.content.decode("utf-8"))
# req.close()
# vaca_url = []
#
# print(all_data)
#
# for item in all_data['items']:
#     vaca_url.append(item['vacancies_url'])
# new_req = requests.get(vaca_url[2])
# data = json.loads(new_req.content.decode("utf-8"))
# new_req.close()


vacancies = 0
params = {
    "page": 0,
    "text": 'сбер',
    "per_page": 1,
    "only_with_vacancies": True
}
new_req = requests.get('https://api.hh.ru/vacancies', params)

data = json.loads(new_req.content.decode("utf-8"))

var = {'id': '89762378', 'premium': False, 'name': 'Бухгалтер', 'department': None, 'has_test': False,
       'response_letter_required': False, 'area': {'id': '160', 'name': 'Алматы', 'url': 'https://api.hh.ru/areas/160'},
       'salary': {'from': 250000, 'to': 450000, 'currency': 'KZT', 'gross': False},
       'type': {'id': 'open', 'name': 'Открытая'},
       'address': {'city': 'Алматы', 'street': 'улица Жамакаева', 'building': '99', 'lat': 43.218803, 'lng': 76.946013,
                   'description': None, 'raw': 'Алматы, улица Жамакаева, 99', 'metro': None, 'metro_stations': [],
                   'id': '13884624'}, 'response_url': None, 'sort_point_distance': None,
       'published_at': '2023-11-22T09:08:59+0300', 'created_at': '2023-11-22T09:08:59+0300', 'archived': False,
       'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=89762378',
       'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/89762378?host=hh.ru',
       'alternate_url': 'https://hh.ru/vacancy/89762378', 'relations': [],
       'employer': {'id': '9844082', 'name': 'Yandex-invest', 'url': 'https://api.hh.ru/employers/9844082',
                    'alternate_url': 'https://hh.ru/employer/9844082',
                    'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/6089614.jpeg',
                                  '90': 'https://hhcdn.ru/employer-logo/6089613.jpeg',
                                  'original': 'https://hhcdn.ru/employer-logo-original/1117254.jpeg'},
                    'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9844082', 'accredited_it_employer': False,
                    'trusted': True}, 'snippet': {
        'requirement': 'Знание IC Бухгалтерия. Опыт работы бухгалтером. Навыки работы с MS Office (WORD, EXCEL). Навык работы в многозадачном режиме. ',
        'responsibility': 'Работа с первичной документацией(в базе 1С): Расчет заработной платы, оплата налогов. Работа с трудовыми договорами и сайтом Енбек.кз. '},
       'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
       'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
       'professional_roles': [{'id': '18', 'name': 'Бухгалтер'}], 'accept_incomplete_resumes': True,
       'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
       'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
       'adv_context': None}

conn = psycopg2.connect(
    host="localhost",
    database="employers_vacancies",
    user="vinsentenkidu",
    password="12345678"
)
cur = conn.cursor()

cur.execute("INSERT INTO employers (id, name, url, vacancies_url, open_vacancies) VALUES (%s, %s, %s, %s, %s)",
            (1, "aboba", "/aboba", "/anana", 4))
cur.execute(
            "INSERT INTO employees (id, first_name, last_name, position, years, description) VALUES (%s, %s, %s, %s, %s, %s)",
            (split_list[0], split_list[1], split_list[2], split_list[3], split_list[4], split_list[5]))

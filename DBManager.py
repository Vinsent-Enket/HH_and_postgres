from datetime import datetime
import psycopg2


class DBManager:

    def __init__(self, asd):
        self.conn = psycopg2.connect(
            host="localhost",
            database="employers_vacancies",
            user="vinsentenkidu",
            password="12345678"
        )
        self.cur = self.conn.cursor()
        self.asd = asd
        self.first_launch()

    def first_launch(self):
        """хорошо бы наверное сделать проверку на наличие всех столбцов..."""
        self.cur.execute("CREATE TABLE IF NOT EXISTS employers (id INTEGER PRIMARY KEY, name VARCHAR, url VARCHAR,  vacancies_url VARCHAR, open_vacancies INTEGER);")
        self.conn.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS vacancies (id INTEGER PRIMARY KEY,"
                         "name VARCHAR,"
                         "area VARCHAR,"
                         "salary INTEGER,"
                         "published_at DATE,"
                         "employer_id INTEGER,"
                         "requirement VARCHAR,"
                         "employment VARCHAR,"
                         "url VARCHAR);")
        self.conn.commit()

    def employer_init(self, data, count):
        """Получаем массив с реквеста"""
        for item in data['items']:
            id = int(item['id'])
            name = item['name']
            url = item['alternate_url']
            vacancies_url = item['vacancies_url']
            count_vacancies = count
            print(type(id))
            print(id, name, url, vacancies_url, count_vacancies)
            inserting = "INSERT INTO employers(id, name, url, vacancies_url, open_vacancies) VALUES (%s, %s, %s, %s, %s)"
            self.cur.execute(inserting,(id, name, url, vacancies_url, count_vacancies))
            self.conn.commit()

    def vacancies_init(self, data):
        """Получаем массив с реквеста"""
        for item in data['items']:
            id = int(item['id'])
            name = item['name']
            area = item['area']['name']
            try:
                salary = int(item['salary']['from'])
            except TypeError:
                salary = 0
            employer_id = int(item['employer']['id'])
            requirement = item['snippet']['requirement']
            published_at = self.str_date_conv(item['published_at'])
            url = item['alternate_url']
            employment = item['employment']['name']
            inserting = "INSERT INTO vacancies (id, name, area, salary, published_at, employer_id, requirement, employment, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cur.execute(inserting,(id, name, area, salary, published_at, employer_id, requirement, employment, url))
            self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """Просто получаем данные"""
        self.cur.execute("select * from employers")
        deta = self.cur.fetchall()
        return deta

    def get_all_vacancies(self):
        """Просто получаем данные"""

        self.cur.execute("select * from vacancies")
        deta = self.cur.fetchall()
        return deta

    def get_avg_salary(self):
        """Использовал оба варианта подстановки переменной в sql запрос"""
        user_answers = input("Какую минимальную зп поставим в фильтр? \n-->")
        select_query = "select * from vacancies where salary > %s"
        self.cur.execute(select_query, (user_answers,))
        deta = self.cur.fetchall()
        return deta

    def get_vacancies_with_keyword(self):
        """Использовал оба варианта подстановки переменной в sql запрос"""
        user_answer = input("какое слово должно присутствовать в вакансии?\n -->")
        where_query = f"select * from vacancies where name ilike '%{user_answer}%'"
        self.cur.execute(where_query)

        deta = self.cur.fetchall()
        return deta

    @staticmethod
    def str_date_conv(data_str):
        """
        Конвертер из строкового значения
        :param data_str:
        :return:
        """
        format_date = datetime.strptime(data_str[:-5], "%Y-%m-%dT%H:%M:%S")

        return format_date


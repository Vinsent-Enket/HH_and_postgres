from DBManager import DBManager
from hh_responses_classes import Employer_response, Vacancies_response

data_tabl = DBManager("asdasd")


def printing_vacancies(data):
    for row in data:
        print("------------------------")
        print("id = ", row[0])
        print("Название = ", row[1])
        print("Локация = ", row[2])
        print("Зарплата = ", row[3])
        print("Дата публикации = ", str(row[4]))
        print("employer_id = ", row[5])
        print("Описание вакансии = ", row[6])
        print("Занятость = ", row[7])
        print("url вакансии = ", row[8])
        user_answer = input("нажмите любую клавишу что-бы продолжить или 0 чтобы выйти")
        if user_answer == "0":
            break


while True:
    user_answer = int(input('Добрый день, что желаете сделать?\n'
                            '{1} Получить список всех компаний и количество вакансий\n'
                            '{2} Получить список всех вакансий и их параметров\n'
                            '{3} Получить список вакансий по ключевому слову\n'
                            '{4} Получить список вакансий выше заданной зп\n'
                            '{5} Добавить новую компанию и её вакансии\n'
                            '{0} выход\n'
                            '--> '))

    if user_answer == 1:
        data = data_tabl.get_companies_and_vacancies_count()
        for row in data:
            print("------------------------")
            print("id = ", row[0])
            print("Название = ", row[1])
            print("Адрес компании = ", row[2])
            print("Адрес вакансий компании = ", row[3])
            print("Количество вакансий = ", row[4])
            input("нажмите любую клавишу что-бы продолжить")

    elif user_answer == 2:
        data = data_tabl.get_all_vacancies()
        printing_vacancies(data)

    elif user_answer == 3:
        data = data_tabl.get_vacancies_with_keyword()
        printing_vacancies(data)
    elif user_answer == 4:
        print(data_tabl.get_avg_salary())
    elif user_answer == 5:
        # нужно сделать подтверждение перед добавлением
        user_answer = input("Какую компанию будем добавлять? \n-->")
        employers_data = Employer_response(user_answer)
        # сделать проверку на то, есть ли вообще вакансии
        vacancies_data = Vacancies_response(employers_data.vacancies_url)
        data_tabl.employer_init(employers_data.data, vacancies_data.count)
        data_tabl.vacancies_init(vacancies_data.data)
        print(
            f"Была добавлена компания {employers_data.data['items'][0]['name']} с количеством вакансий - {vacancies_data.count}")
    elif user_answer == 0:
        break
    else:
        print('команда не распознана')

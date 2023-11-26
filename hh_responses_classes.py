import json
from abc import ABC, abstractmethod

import requests


class HeadHunter_response(ABC):
    """
    Абстрактный класс для запросов к hh
    """
    @abstractmethod
    def get_request(self):
        pass


class Employer_response(HeadHunter_response):
    """
    Класс для получения информации о работодателе у которого есть вакансии
    """
    def __init__(self, name: str):
        self.params = {
            "page": 0,
            "text": name,
            "per_page": 1,
            "only_with_vacancies": True
        }
        self.data = self.get_request()
        self.vacancies_url = self.data['items'][0]['vacancies_url']

    def get_request(self):


        req = requests.get('https://api.hh.ru/employers', self.params)
        data = json.loads(req.content.decode("utf-8"))
        return data


class Vacancies_response(HeadHunter_response):
    """
    Класс для получения информации о вакансиях конкретного работодателя
    """
    def __init__(self, url):
        self.url = url
        self.params = {
            "page": 0,
            "per_page": 100
        }
        self.data = self.get_request()
        self.count = len(self.data['items'])
        print("это длинна списка вакансий", self.count)

    def get_request(self):
        req = requests.get(self.url, self.params)
        data = json.loads(req.content.decode("utf-8"))
        return data


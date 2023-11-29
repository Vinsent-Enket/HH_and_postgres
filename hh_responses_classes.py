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
    def __init__(self, req: dict):
        params_setting = {
            "page": 0,
            "per_page": 1,
            "only_with_vacancies": True
        }
        self.params = {}
        self.params.update(params_setting)
        self.params.update(req)
        self.is_vacancies = True

        self.data = self.get_request()
        if self.data['items']:
            self.vacancies_url = self.data['items'][0]['vacancies_url']
        else:
            self.is_vacancies = False

    def get_request(self):
        req = requests.get('https://api.hh.ru/employers', self.params)
        data = json.loads(req.content.decode("utf-8"))
        return data


class Vacancies_response(HeadHunter_response):
    """
    Класс для получения информации о вакансиях конкретного работодателя
    """
    def __init__(self, url=None, req=None):
        self.url = url
        self.params = {
            "page": 0,
            "per_page": 100
        }
        if url:
            self.data = self.get_request()
        else:
            self.params.update(req)
            self.url = 'https://api.hh.ru/vacancies'
            self.data = self.get_request()
            self.employer_data = self.data['items'][0]['employer']

        self.count = len(self.data['items'])

    def get_request(self):
        req = requests.get(self.url, self.params)
        data = json.loads(req.content.decode("utf-8"))
        return data


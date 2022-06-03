from find_area_id import get_id_region
from statistics_hh import Statistics
from parser_hh import parser
from pprint import pprint
import json


class HH():
    def __init__(self):
        self.city = 'Уфа'
        self.search_line = 'python Developer'
        self.region_id = 99
        self.stat = Statistics()

    def __str__(self):
        ret = f'Город поиска: \t {self.city}\n'
        ret += f'Строка поиска: \t {self.search_line}\n'
        return ret

    def search(self):
        parser(self.stat, region_id=self.region_id, search_line=self.search_line)
        return str(self.stat.get_stat())


if __name__ == '__main__':
    hh = HH()
    stat = Statistics()
    DOMAIN = 'https://api.hh.ru/'
    url_area = f'{DOMAIN}areas/113'
    hh.region_id = get_id_region(url_area, hh.city)
    url_vacancies = f'{DOMAIN}vacancies'
    parser(stat, region_id=hh.region_id, search_line=hh.search_line, url_vacancies=url_vacancies)
    pprint(stat.get_stat())
    with open('statistic.json', 'w') as f:
        json.dump(stat.get_stat(), f)

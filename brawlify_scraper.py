from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment

source = requests.get('https://brawlify.com/league/').text
soup = BeautifulSoup(source, 'lxml')

wb = Workbook()
ws = wb.active
ws.title = "Power League Stats"
ws.append(['Brawler', 'Win Rate', 'Map', 'Map Type'])

for header_cell_tuple in ws['A1:D1']:
    for header_cell in header_cell_tuple:
        header_cell.font = Font(size=14, bold=True)
        header_cell.alignment = Alignment(horizontal='center')

for map_info in soup.findAll('div', class_="row event-recommendation justify-content-center align-content-center"):
    for brawler_info in map_info.findAll('a', class_="link event-brl event-brl-img opacity mb-1 mx-1"):
        brawler_name = brawler_info.get('title')
        win_rate = int(brawler_info.text.strip()[0:2])/100
        brawlify_map = map_info.find_previous('a', class_="link opacity event-title-text event-title-map mb-0").get("title")
        brawlify_map_type = map_info.find_previous('a', class_= "link opacity event-title-gamemode" ).get('title')
        ws.append([brawler_name, win_rate, brawlify_map, brawlify_map_type])

    for brawler_info in map_info.findAll('a', class_="link event-brl event-brl-img opacity mx-1"):
        brawler_name = brawler_info.get('title')
        win_rate = int(brawler_info.text.strip()[0:2]) / 100
        brawlify_map = map_info.find_previous('a', class_="link opacity event-title-text event-title-map mb-0").get("title")
        brawlify_map_type = map_info.find_previous('a', class_="link opacity event-title-gamemode").get('title')
        ws.append([brawler_name, win_rate, brawlify_map, brawlify_map_type])

wb.save("Power_League_Stats.xlsx")
wb.close()
#

from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook

source = requests.get('https://brawlify.com/league/').text
soup = BeautifulSoup(source, 'lxml')

wb = load_workbook('Pokemon_List.xlsx')
ws = wb.active
ws.title = "Pokemon Info"
ws.append(['Name','Number', 'Type', 'Generation'])


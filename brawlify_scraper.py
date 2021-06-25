from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment


# This function will do the heavy lifting when it comes to finding brawlers within a particular map
def find_brawlers(section):
    for brawler_info in section:
        brawler_name = brawler_info.get('title')
        # 67% Will be converted to be 67 when the string is spliced
        win_rate = int(brawler_info.text.strip()[0:2]) / 100
        brawlify_map = map_info.find_previous('a', class_="link opacity event-title-text event-title-map mb-0").get(
            "title")
        brawlify_map_type = map_info.find_previous('a', class_="link opacity event-title-gamemode").get('title')
        ws.append([brawler_name, win_rate, brawlify_map, brawlify_map_type])


source = requests.get('https://brawlify.com/league/').text
soup = BeautifulSoup(source, 'lxml')

# Create a new workbook altogether, if previous information is stored in an excel file, it will be deleted after a save
wb = Workbook()

# Utilize the default sheet in the new excel workbook
ws = wb.active

# Title the worksheet as appropriate and declare the header titles
ws.title = "Power League Stats"
ws.append(['Brawler', 'Win Rate', 'Map', 'Map Type'])

# Declare all header titles to be centered and bolded
for header_cell_tuple in ws['A1:D1']:
    for header_cell in header_cell_tuple:
        header_cell.font = Font(size=14, bold=True)
        header_cell.alignment = Alignment(horizontal='center')

# For all maps and map types, append the brawlers listed
for map_info in soup.findAll('div', class_="row event-recommendation justify-content-center align-content-center"):
    upper_brawlers = map_info.findAll('a', class_="link event-brl event-brl-img opacity mb-1 mx-1")
    lower_brawlers = map_info.findAll('a', class_="link event-brl event-brl-img opacity mx-1")
    find_brawlers(upper_brawlers)
    find_brawlers(lower_brawlers)

# This file will be rewritten if it already contains data
wb.save("Power_League_Stats.xlsx")
wb.close()

#

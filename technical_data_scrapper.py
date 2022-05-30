from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
# WEB SOURCES
# tools_web = 'https://github.com/AnanthaRajuC/Useful-Softwares-Tools-list'
# libs_web = 'https://github.com/gamtiq/frontend-tools'
# langs_web = 'https://gist.github.com/turicas/d5f8ce3ceb99f43a11b1e4e7fb2a2bf9'
# website = 'https://github.com/Developer-Y/cs-video-courses'


stop_words = [ 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was']

def scrap_tools():
    tools_web = 'https://github.com/AnanthaRajuC/Useful-Softwares-Tools-list'
    driver_path = 'chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(tools_web)
    tools_lst = []
    for tables in range(1,13):
        temp_path = "//table["+str(tables)+"]/tbody/tr/td[1]"
        table_element = driver.find_elements(By.XPATH, temp_path)
        for tool in table_element:
            tools_lst.append([tool.text])
    field = ['DeveloperTools']
    with open('tools.csv', 'w', encoding="utf-8", newline='') as file:
        write = csv.writer(file)
        write.writerow(field)
        write.writerows(tools_lst)

def scrap_developer_frameworks():
    libs_web = 'https://github.com/gamtiq/frontend-tools'
    driver_path = 'chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(libs_web)
    tech_tools = []
    headings = driver.find_elements(By.XPATH, "//article/ul[2]/li/a")
    js_run_time = driver.find_elements(By.XPATH, "//article/ul[4]/li/a")
    js_variant = driver.find_elements(By.XPATH, "//article/ul[5]/li/a")
    js_framework = driver.find_elements(By.XPATH, "//article/ul[6]/li/a")
    libraries = driver.find_elements(By.XPATH, "//article/ul[7]/li/a")
    for tool in headings:
        tech_tools.append([tool.text])
    for js in js_run_time:
        tech_tools.append([js.text])
    for variant in js_variant:
        tech_tools.append([variant.text])
    for framework in js_framework:
        tech_tools.append([framework.text])
    for lib in libraries:
        tech_tools.append([lib.text])
    field = ['FrameworksAndLibraries']
    with open('frameworks.csv', 'w', encoding="utf-8", newline='') as file:
        write = csv.writer(file)
        write.writerow(field)
        write.writerows(tech_tools)

def scrap_programming_languages():
    langs_web = 'https://gist.github.com/turicas/d5f8ce3ceb99f43a11b1e4e7fb2a2bf9'
    driver_path = 'chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(langs_web)
    headings=driver.find_elements(By.XPATH, "//tbody/tr/td[2]")
    prog_langs_lst = []
    for match in headings:
        prog_langs_lst.append([match.text])
        # course_domains.append()
    field = ['ProgrammingLanguages']
    with open('prog_langs.csv', 'w', encoding="utf-8", newline='') as file:
        write = csv.writer(file)
        write.writerow(field)
        write.writerows(prog_langs_lst)

def scrap_technical_courses():
    website = 'https://github.com/Developer-Y/cs-video-courses'
    driver_path = 'chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(website)
    courses_lst = []
    for course in range(1,13):
        temp_path = "//ul["+str(course)+"]/li"
        table_element = driver.find_elements(By.XPATH, temp_path)
        for elements in table_element:
            if elements.text:
                courses_lst.append([elements.text])
    field = ['Courses']
    with open('courses.csv', 'w', encoding="utf-8", newline='') as file:
        write = csv.writer(file)
        write.writerow(field)
        write.writerows(courses_lst)

scrap_tools()
scrap_developer_frameworks()
scrap_programming_languages()
scrap_technical_courses()

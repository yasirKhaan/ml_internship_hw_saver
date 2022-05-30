import pandas as pd
from fuzzywuzzy import process
import csv

class MLInterTest():
    def __init__(self):
        self.raw_data = pd.read_csv('Raw_Skills_Dataset.csv')
        self.technical_data = pd.read_csv('Example_Technical_Skills.csv')
        self.courses = pd.read_csv('courses.csv')
        self.frameworks = pd.read_csv('frameworks.csv')
        self.prog_langs = pd.read_csv('prog_langs.csv')
        self.tools = pd.read_csv('tools.csv')

        self.raw_skills = self.raw_data['RAW DATA'].to_list()
        self.tech_skills = self.technical_data['Technology Skills'].to_list()
        self.course_skills = self.courses['Courses'].to_list()
        self.framework_skills = self.frameworks['FrameworksAndLibraries'].to_list()
        self.prog_langs_skills = self.prog_langs['ProgrammingLanguages'].to_list()
        self.tool_skills = self.tools['DeveloperTools'].to_list()

    def tech_skills_sorter_approach_1(self):
        self.main_list = self.tech_skills + self.course_skills + self.framework_skills + self.prog_langs_skills + self.tool_skills
        technical_skills = []
        for skill in self.raw_skills:
            print('*************', skill, '*************')
            function = process.extractBests(skill, self.main_list, limit=1)
            for threshold in function:
                if threshold[1] >= 85:
                    print("< --- THRESHOLD --- >", threshold)
                    technical_skills.append([skill])
        field = ['Technical Skills']
        with open('technical_skills_filtered.csv', 'w', encoding="utf-8", newline='') as file:
            write = csv.writer(file)
            write.writerow(field)
            write.writerows(technical_skills)

    def non_technical_skills_sorter(self):
        app2_tech_skills = []
        for skill in self.raw_skills:
            print('*************', skill, '*************')
            function = process.extractBests(skill, self.tech_skills, limit=1)
            for threshold in function:
                if threshold[1] <= 60:
                    print("< --- THRESHOLD --- >", threshold)
                    app2_tech_skills.append([skill])
        field = ['Non Technical Skills']
        with open('non_technical_skills_filtered.csv', 'w', encoding="utf-8", newline='') as file:
            write = csv.writer(file)
            write.writerow(field)
            write.writerows(app2_tech_skills)
mlintern = MLInterTest()
mlintern.tech_skills_sorter_approach_1()
mlintern.non_technical_skills_sorter()

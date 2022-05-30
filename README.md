# ml_internship_hw_saver

I have defined purpose of every file and function in document as well.


MY APPROACH:
Overview:
I came up with a very time consuming but an interesting approach.
First of all I scrap data from web using selenium, Scrapped data contain technical courses, developer tools, programming languages and frameworks.
Main purpose of scrapping was to add keywords of technical data in backend so I will compare it with raw skills.
I also attempted to solve portion named (“If you have a life, ignore this.”), But unfortunately, I am not getting expected answer, but still non-technical skills are being separated into another csv.
What Coding Files Contain:
I have attached 2 python files.
1-	technical_data_scrapper.py
2-	main.py
Let’s talk about technical_data_scrapper.py.
1-	In header section all the github repositories are mentioned from where I scrapped data.
2-	scrap_tools() scrap all the tools from table of github repo, table contain tools like SaaS, PaaS etc. This function scrapped almost 50 records, more can be scrapped.
3-	scrap_developer_frameworks() scrap all the frameworks, variants and libraries of both frontend and backend but mostly frontend from github repo. This function scrapped around 65 records of frameworks.
4-	scrap_programming_languagues() scrap almost 700 programming languages from github repository.
5-	scrap_technical_courses() scrap courses with title, This function scrapped around 600 records of technical courses, which play a vital role in identifying technical keywords from raw_data.
6-	All this scrapped data is being stored in separate csv files, which will be use in main.py.
Now let’s talk about main.py.
1-	Class named MLInternTest() is being initialized.
2-	In constructor section all the csv files are being read and respective columns are assigned to variable using pandas.
3-	tech_skills_sorter() is the function where we can see self.main_list is initialized in first line, this self.main_list is addition of all the lists of scrapped data.
4-	Now self.main_list contains data of programming languages, technical courses, frameworks and libraries and tools.
5-	Here Fuzzy Matching is being used for matching string on the basis of certain threshold.
6-	First loop is iterate over each raw_skill, and each skill on next line is being checked in self.main_list for string match using fuzzy module.
7-	Threshold is set for greater than or equal to 85.
8-	If any of those each skill from raw_skill crosses that threshold then that skill is being added to technical_skills, which is a final list of technical skills.
9-	After completing iteration, new csv file will create named technical_skills_filtered.csv and all the data of technical_skills will be added to technical_skills_filtered.csv.
I also tried to attempt that “If you have a life, ignore this.” section in function named non_technical_skills_sorter().
In this function almost workflow is same like tech_skills_sorter()  but the only difference is of threshold which was 85 in tech_skills_sorter() and it is less than or equal to 65 in non_technical_skills_sorter().
After completing iteration, new csv file will create named non_technical_skills_filtered.csv and all the data of app2_tech_skills will be added to non_technical_skills_filtered.csv.

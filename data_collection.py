import scrapperGlassdoor as sg 
import pandas as pd 

path = "C:/Users/athar/AppData/Local/Programs/Python/Python38/chromedriver"

df = sg.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
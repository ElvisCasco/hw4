#pip install --upgrade git+https://github.com/ElvisCasco/process_data.git
#pip install upgrade pip
file_name = "C:/EC/BSE/DSDM/Term 1/21DM004 Computing for Data Science/sample_diabetes_mellitus_data.csv"
from process_data import *

data = process_data.load_data(file_name)
print(data)
git 
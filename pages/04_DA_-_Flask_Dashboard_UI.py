import pandas as pd
from helper import template_app as temp_app

# capstone case
case = 'Flask Dashboard UI'

# read data & data preparation
caps = pd.read_csv('data-input/da_flask_dashboard.csv')

# build app
temp_app.app(case, caps)
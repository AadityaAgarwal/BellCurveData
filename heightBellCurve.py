import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff

data=pd.read_csv('height.csv')
fig=ff.create_distplot([data['Weight(Pounds)'].tolist()],['weight']#,show_hist=False
)
fig.show()
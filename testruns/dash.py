import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objects as go
# import plotly.express as px
import pandas as pd
import json
from django.core.serializers import serialize
from integrations.models import TestRunResults
from pandas.io.json import json_normalize


from django.core import serializers


# data_table = TestRunResults.objects.all().values('body_test')
# serialized_data = serializers.serialize('json', data_table)
# #serialized_data = serialize("json", data_table)
serialized_data = serializers.serialize('json', TestRunResults.objects.all(), fields=('body_test'))
df = pd.read_json(serialized_data, orient='records')
df2 = json_normalize(df, record_path = ['fields'])


import json
with open(serialized_data, 'r') as f:
    data = json.loads(f.read())

d = json.loads(serialized_data)
df_nested_list = pd.json_normalize(d, record_path = ['fields'])





events=TestRunResults.objects.only('body_test')

df2['body_test.1']




TestRunResults.objects.values('body_test')

pd.read_json(TestRunResults.objects.values('body_test'))
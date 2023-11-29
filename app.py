from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# EDA
df = pd.read_csv('AutoCare_dados.csv')

contagem_estados = df['uf_local'].value_counts()
pie_estados = px.pie(values=contagem_estados.values, names=contagem_estados.index, title='Distribuição de Pacientes por Estado')

contagem_valores = df['declaracao_de_comparecimento'].value_counts()
pie_valores = px.pie(values=contagem_valores.values, names=contagem_valores.index, title='Distribuição de Declarações de Comparecimento')

contagem_origens = df['origem_atestado'].value_counts()
bar_origens = px.bar(x=contagem_origens.index, y=contagem_origens.values, title='Distribuição de Origens de Atestado', labels={'x':'Origem do Atestado', 'y':'Número de Casos'})

contagem_motivacao = df['tipo_motivacao'].value_counts()
bar_motivacao = px.bar(x=contagem_motivacao.index, y=contagem_motivacao.values, title='Distribuição de Tipos de Motivação', labels={'x':'Tipo de Motivação', 'y':'Número de Casos'})

contagem_especialidade = df['especialidade_medico'].value_counts()
bar_especialidade = px.bar(x=contagem_especialidade.index, y=contagem_especialidade.values, title='Distribuição de Atestados por Especialidade Médica', labels={'x':'Especialidade Médica', 'y':'Número de Atestados'})

contagem_uf_crm = df['uf_crm'].value_counts()
bar_uf_crm = px.bar(x=contagem_uf_crm.index, y=contagem_uf_crm.values, title='Distribuição de Atestados por UF do CRM do Médico', labels={'x':'UF do CRM', 'y':'Número de Atestados'})

box_dias_ausentes = px.box(df, y='dias_ausentes', title='Distribuição de Dias Ausentes')

contagem_departamento = df['departamento'].value_counts()
bar_departamento = px.bar(x=contagem_departamento.index, y=contagem_departamento.values, title='Distribuição de Atestados por Departamento', labels={'x':'Departamento', 'y':'Número de Atestados'})



# Dashboard
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(className='main-container', children=[
    html.H1('Statistics'),

    html.Div(className='section-container', children=[
        html.Div(className='pie-container', children=[
            dcc.Graph(id='pie_estados', figure=pie_estados),
            dcc.Graph(id='pie_valores', figure=pie_valores)
        ]),
        html.Div(className='bar-container', children=[
            dcc.Graph(id='bar_origens', figure=bar_origens),
            dcc.Graph(id='bar_motivacao', figure=bar_motivacao),
            dcc.Graph(id='bar_especialidade', figure=bar_especialidade),
            dcc.Graph(id='bar_uf_crm', figure=bar_uf_crm),
            dcc.Graph(id='bar_departamento', figure=bar_departamento)
        ]),
        html.Div(className='box-container', children=[
            dcc.Graph(id='box_dias_ausentes', figure=box_dias_ausentes)
        ])
    ]),
])

@app.callback(
    Output('pie_estados', 'figure'),
    Output('pie_valores', 'figure'),
    Output('bar_origens', 'figure'),
    Output('bar_motivacao', 'figure'),
    Output('bar_especialidade', 'figure'),
    Output('bar_uf_crm', 'figure'),
    Output('bar_departamento', 'figure'),
    Output('box_dias_ausentes', 'figure'),
    Input('hist_columns', 'value')
)
def update_output(value):
    contagem_estados = df[value].value_counts()
    pie_estados = px.pie(values=contagem_estados.values, names=contagem_estados.index)

    contagem_valores = df[value].value_counts()
    pie_valores = px.pie(values=contagem_valores.values, names=contagem_valores.index)

    contagem_origens = df[value].value_counts()
    bar_origens = px.bar(x=contagem_origens.index, y=contagem_origens.values)

    contagem_motivacao = df[value].value_counts()
    bar_motivacao = px.bar(x=contagem_motivacao.index, y=contagem_motivacao.values)

    contagem_especialidade = df[value].value_counts()
    bar_especialidade = px.bar(x=contagem_especialidade.index, y=contagem_especialidade.values)

    contagem_uf_crm = df[value].value_counts()
    bar_uf_crm = px.bar(x=contagem_uf_crm.index, y=contagem_uf_crm.values)

    contagem_departamento = df[value].value_counts()
    bar_departamento = px.bar(x=contagem_departamento.index, y=contagem_departamento.values)

    box_dias_ausentes = px.box(df, y=value)

    return pie_estados, pie_valores, bar_origens, bar_motivacao, bar_especialidade, bar_uf_crm, bar_departamento, box_dias_ausentes

if __name__ == '__main__':
    app.run_server(debug=True)
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from datetime import datetime as dt
import locale

def find_date(string):
    """Замена 'Январь 2021' -> '2021-01-01'."""
    # Вероятно существует более эффективный и короткий вариант,
    # пыталась сделать с помощью pd.to_datetime(), но не вышло,
    # тк название месяца на кирилице.
    month = {'январь': '01', 'февраль': '02', 'март': '03',
             'апрель': '04', 'май': '05', 'июнь': '06',
             'июль': '07', 'август': '08', 'сентябрь': '09',
             'октябрь': '10', 'ноябрь': '11', 'декабрь': '12'}

    string = string.split()
    if string[0].lower() in month.keys():
        return f'{string[1]}-{month[string[0].lower()]}-01'
    return None
def format_date(df):
    """Заполнение стлобца month."""
    df['month'] = pd.NaT
    month = ''

    for item in df.index:
        string = find_date(df.loc[item, 'status'])
        if string is not None:
            month = string
        df.loc[item, 'month'] = month

def read_data(filename, sheet_name):
    """Чтение и подготовка DataFrame."""
    try:
        df = pd.read_excel(filename, sheet_name=sheet_name)
    except FileNotFoundError:
        return None

    # Очистка от 'лишних' символов.
    df.replace('-', np.nan, inplace=True)
    df.replace('НЕТ', np.nan, inplace=True)

    # Добавление колонки с месяцем заключения сделки.
    format_date(df)

    # Удаление строк с названием месяца.
    df = df.dropna(subset=['client_id'])

    # Изменение формата данных.
    df['client_id'] = df['client_id'].astype('int')
    df['receiving_date'] = pd.to_datetime(df['receiving_date'])
    df['month'] = pd.to_datetime(df['month'])

    return df

def question1(df):
    data = df[(df['receiving_date'].dt.month == 7)
                  & (df['receiving_date'].dt.year == 2021)
                  & (df['status'] == 'ОПЛАЧЕНО')]
    sum = data['sum'].sum()
    print('Вопрос 1.')
    print('Общая выручка за ИЮЛЬ 2021 года: ' + str(round(sum, 2))  + '\n')

def question2(df):
    data = df[(df['status'] == 'ОПЛАЧЕНО')].groupby(pd.Grouper(key='receiving_date', axis=0, freq='M')).sum()
    serias = data['sum']
    serias.index = serias.index.map(lambda seria: seria.month_name())
    serias.plot(kind='bar',
                title='Изменение выручки компании за год')
    print('Вопрос 2.')
    plt.show()

def question3(df):
    data = df[(df['receiving_date'].dt.month == 9)
              & (df['receiving_date'].dt.year == 2021)].groupby('sale')
    aggregated = data.agg({'sum': 'sum'})
    print('Вопрос 3.')
    print(f'За СЕНТЯБРЬ 2021 наибольшую прибыль принес менеджер: {aggregated['sum'].idxmax()}\n'
          f'В размере: {aggregated['sum'].max()}\n')

def question4(df):
    data = df[(df['receiving_date'].dt.month == 10)
             & (df['receiving_date'].dt.year == 2021)].groupby('new/current')
    aggregated = data.agg({'new/current': 'count'})
    print(f'В октябре преобладал тип сделок: "{aggregated['new/current'].idxmax()}"\n'
          f'Колличество: {aggregated['new/current'].max()}\n')

def question5(df):
    data = df[(df['month'].dt.month == 5)
              & (df['receiving_date'].dt.year == 2021)
              & (df['receiving_date'].dt.month == 6)
              & (df['document'] == 'оригинал')]
    print(data['document'].count())



df = read_data('data.xlsx', 'Лист1')

if df is None:
    print('Файла с таким именем не существует')
else:
    # question1(df)
    # question2(df)
    question3(df)
    question4(df)
    question5(df)

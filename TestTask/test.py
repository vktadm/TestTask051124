# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def print_file(data):
    file = open('output.txt', 'a')
    file.write(data)
    file.close()

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

    file_data = f'Вопрос 1.\nОбщая выручка за ИЮЛЬ 2021 года: {str(round(sum, 2))}\n\n'
    print_file(file_data)

def question2(df):
    data = df[(df['status'] == 'ОПЛАЧЕНО')].groupby(pd.Grouper(key='receiving_date', axis=0, freq='ME'))
    serias = data.agg({'sum': 'sum'})['sum']
    serias.index = serias.index.map(lambda seria: seria.month_name())
    serias.plot(kind='bar', title='Изменение выручки компании за год')

    plt.savefig('gist.png')

    file_data = 'Вопрос 2.\nГистограмма с результатами в файле gist.png\n\n'
    print_file(file_data)

def question3(df):
    data = df[(df['receiving_date'].dt.month == 9)
              & (df['receiving_date'].dt.year == 2021)].groupby('sale')
    aggregated = data.agg({'sum': 'sum'})

    file_data = f'Вопрос 3.\nЗа СЕНТЯБРЬ 2021 наибольшую прибыль принес менеджер: {aggregated['sum'].idxmax()}\n'\
                f'В размере: {aggregated['sum'].max()}\n\n'
    print_file(file_data)

def question4(df):
    data = df[(df['receiving_date'].dt.month == 10)
             & (df['receiving_date'].dt.year == 2021)].groupby('new/current')
    aggregated = data.agg({'new/current': 'count'})

    file_data = (f'Вопрос 4.\nВ октябре преобладал тип сделок: "{aggregated['new/current'].idxmax()}"\n'
                 f'Количество: {aggregated['new/current'].max()}\n\n')
    print_file(file_data)

def question5(df):
    data = df[(df['month'].dt.month == 5)
              & (df['receiving_date'].dt.year == 2021)
              & (df['receiving_date'].dt.month == 6)
              & (df['document'] == 'оригинал')]
    file_data = f'Вопрос 5.\nКоличество оригиналов договоров за май: {data['document'].count()}'
    print_file(file_data)



df = read_data('data.xlsx', 'Лист1')

if df is None:
    print('Файла с таким именем не существует')
else:
    question1(df)
    question2(df)
    question3(df)
    question4(df)
    question5(df)

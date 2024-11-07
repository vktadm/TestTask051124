## Результаты выполнения тестового задания
***
1.1 - Уровень владения 7 баллов. Знаю и применяю на практике базовый Python
(структуры данных, циклы, ветвления, генераторы, try-except, функции, ООП, декораторы).

1.2 - Уровень владения 8 баллов. Использую функции, могу строить графики, сводные таблицы.
***
### Задания на логику
#### Задача 2.1
```python
sum = 40
sum = sum / 2
sum = sum - (sum / 100) * 80
# Ответ: 4
```
#### Задача 2.2
```python
q_company = 5 # 5 рекламных компаний
q_day = 24 # 24 рабочих дня
q_hour = 6 # 6 часов
income = 120 # 120$
hour_cost = None # необходимо узнать

# income = hour_cost * count_hour * count_day * count_company
hour_cost = income / (q_company * q_day * q_hour)
q_company = 9
q_hour = 8
income = 216

q_day = income / (q_company * q_hour * hour_cost)

# Ответ: 18
```
#### Задача 2.3

q1 - РБ уникальные для компании 1 = 60 \
q2 - РБ уникальные для компании 2 \
q12 - РБ, используемые в компании 1 и 2

q12 = 3 * q2 \
200 = 80 + 60 + q2 + q12 -> q2 = 60 - q12

q12 = 3 * (60 - q12) \
q12 = 45

**Ответ:** 45

#### Задача 2.4

|      | Instagram | Facebook | Youtube |
|------|-----------|----------|---------|
| Ann  | True      | False    | + True  |
| Djon | + False   | True     | True    |
| Kate | False     | + True   | True    |
| Tom  | + True    | True     | False   |

**Ответ:** предпочтения совпадают у Джона и Кейт
#### Задача 2.5
(sum1_4 + sum5) / 5 = 80
sum1_4 / 4 = 78

**Ответ:** 88 баллов
#### Задача 2.6
```python
s = 260
v1 = 80
v2 = 100

t2_t1 = s * (v2 - v1) / (v1 * v2) * 60
```
**Ответ:** 39 минут
***
### Практическая часть 
* [Файл с результами выполнеия кода](https://github.com/vktadm/TestTask051124/blob/master/TestTask/output.txt)
* [Практическая часть Python](https://github.com/vktadm/TestTask051124/blob/master/TestTask/test.py)

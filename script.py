import numpy as np
import pandas as pd
import pathlib
from sqlalchemy import create_engine

table = pd.read_excel("test_it_risks.xlsx", header=1)

table['Имя'] = table['Имя'].str.replace(r'.*Якутия.*', 'АО АК Якутия')
table['Имя'] = table['Имя'].str.replace(r'.*((Сибирь)|(СИБИРЬ)).*', 'АО АК Сибирь')
table['Имя'] = table['Имя'].str.replace(r'.*((Deutche)|(DEUTSCHE)).*', 'Deutsche Lufthansa Aktiengesellschaft')
table['Имя'] = table['Имя'].str.replace(r'.*BSP.*', 'BSP')
table['Имя'] = table['Имя'].str.replace(r'.*Аэромар.*Сочи.*', 'ООО Аэромар-Краснодар Ф-л Сочи')
table['Имя'] = table['Имя'].str.replace(r'.*Аэромар.*Анапа.*', 'ООО Аэромар-Краснодар ОП Анапа')
table['Имя'] = table['Имя'].str.replace(r'.*Аэромар.*Уфа.*', 'ООО Аэромар-Уфа')
table['Имя'] = table['Имя'].str.replace(r'.*Аэромар.*Петербург.*', 'ООО Аэромар-Санкт-Петербург')
table['Имя'] = table['Имя'].str.replace(r'.*Газпромбанк.*', 'АО "Газпромбанк"')
table['Имя'] = table['Имя'].str.replace(r'.*((Победа)|(ПОБЕДА)).*', 'ООО АК "Победа"')
table['Имя'] = table['Имя'].str.replace(
    r'.*(("Россия")|("РОССИЯ")|(РОССИЯ АО)|(Авиакомпания Россия)).*', 'АО АК "Россия"'
)
table['Имя'] = table['Имя'].str.replace(r'.*Аэромар.*Краснодар.*', 'ООО Аэромар-Краснодар')
table['Имя'] = table['Имя'].str.replace(r'Аэромар$', 'АО "Аэромар"')
table['Имя'] = table['Имя'].str.replace(r'^[^С].*Газпром авиа.*', 'ООО Газпром авиа')
table['Имя'] = table['Имя'].str.replace(r'ООО "((А-ТЕХНИКС)|(А-Техникс))".*', 'ООО "А-ТЕХНИКС"')
table['Имя'] = table['Имя'].str.replace(
    r'.*((ПАО.*Сбербанк)|(Сбербанк.*ПАО)|(ПАО.*СБЕРБАНК)).*', 'ПАО "Сбербанк России"'
)
table['Имя'] = table['Имя'].str.replace(r'^[ПСс].*((овкомбанк)|(ОВКОМБАНК)).*', 'ПАО "Совкомбанк"')
table['Имя'] = table['Имя'].str.replace(r'.*((ВОЛГА-ДНЕПР)|(Волга-Днепр)).*', 'ООО "Волга-Днепр Техникс Москва"')
table['Имя'] = table['Имя'].str.replace(r'^Б.*ВТБ.*', 'БАНК ВТБ(ПАО)')

path = pathlib.Path(__file__).parent.resolve()
engine = create_engine(f'sqlite:///{path}/db.sqlite')

table.to_sql('aeroflot_task', con=engine)

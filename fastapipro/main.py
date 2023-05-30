from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql as pymysql
import pandas as pd
import numpy as np

conn = pymysql.connect(user='root', password='123456', host='localhost', database='douban')
cursor = conn.cursor()
df = None
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def test():
    return {"Hello world"}


@app.get('/movie/{id}')
async def get_movie_by_rank(id: int):
    sql = f'select * from movies where id = {id}'
    cursor.execute(sql)
    result = cursor.fetchall()[0][:-1]
    return {"data": result}


# @app.get('/getMovie/{begin_id}/{end_id}')
def get_all_movie():
    global df
    sql = f'select * from movies where id <= 100'
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame({'title': [item[0] for item in results],
                       'author': [item[1] for item in results],
                       'year': [item[2] for item in results],
                       'score': [item[3] for item in results],
                       'country': [item[4] for item in results],
                       'type': [item[5] for item in results]
                       })
    df.replace('', np.NAN).fillna(
        {'title': '未知', 'author': '未知', 'year': 2014, 'score': 9.5, 'country': '未知', 'type': '未知'})


@app.get('/country')
async def get_country_list():
    global df
    get_all_movie()
    df['count'] = 1
    country_list = df.groupby('country').agg({'count': 'count'}).sort_values(['count'], ascending=False)
    country_list.to_dict()
    return {'data': country_list.to_dict()['count']}


@app.get('/year')
async def get_year_list():
    global df
    get_all_movie()
    df['count'] = 1
    year_list = df.groupby('year').agg({'count': 'count'}).sort_values(['count'], ascending=False)
    return {'data': year_list.to_dict()['count']}


@app.get('/type')
async def get_year_list():
    global df
    get_all_movie()
    df['count'] = 1
    year_list = df.groupby('type').agg({'count': 'count'}).sort_values(['count'], ascending=False)
    return {'data': year_list.to_dict()['count']}


@app.get('/author')
async def get_year_list():
    global df
    get_all_movie()
    df['count'] = 1
    year_list = df.groupby('author').agg({'count': 'count'}).sort_values(['count'], ascending=False)
    return {'data': year_list.to_dict()['count']}


@app.get('/movie/author/{author}')
async def get_movie_by_author(author: str):
    sql = 'select * from movies where author like "%{}%"'.format(author)
    cursor.execute(sql)
    results = cursor.fetchall()
    return {'data': results}

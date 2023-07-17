import psycopg2
import requests

pg_data = {
    'host': 'postgres',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

query = 'SELECT "token" FROM public."User" WHERE id=1 ORDER BY id ASC;'

data = {"username": "administrator", "password": "password", "code": None}
url = 'http://zipline:3003/api/auth/login'
r = requests.post(url, json=data)
print(r.status_code)
# print(r.text)
with psycopg2.connect(**pg_data) as conn:
    with conn.cursor() as cur:

        cur.execute(query)
        result = cur.fetchone()
if result:
    print(f'Token: {result[0]}')
else:
    print('NO RESULTS:')
    print(result)

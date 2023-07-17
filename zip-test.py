import os
import sys

import psycopg2
import requests

pg_data = {
    'host': 'postgres',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}
query = 'SELECT "token" FROM public."User" WHERE id=1 ORDER BY id ASC;'

zip_data = {
    'username': 'administrator',
    'password': 'password',
    'code': None,
}
zip_url = 'http://zipline:3003/api/auth/login'

r = requests.post(zip_url, json=zip_data)
r.raise_for_status()
# print(r.cookies)


with psycopg2.connect(**pg_data) as conn:
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchone()

if not result:
    print('No Results')
    sys.exit(1)

print(f'{result[0]}')
os.environ['ZIPLINE_TOKEN'] = result[0]

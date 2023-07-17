import psycopg2

data = {
    'host': 'postgres',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

query = 'SELECT "token" FROM public."User" WHERE id=1 ORDER BY id ASC;'

with psycopg2.connect(**data) as conn:
    with conn.cursor() as cur:

        cur.execute(query)
        result = cur.fetchone()
if result:
    print(f'Token: {result[0]}')
else:
    print('NO RESULTS:')
    print(result)

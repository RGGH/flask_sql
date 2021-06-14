# connect to Raspberry Pi ("remote Postgresql Server")

import psycopg2

def get_all_jobs():
  conn = conn = psycopg2.connect(
    host="192.168.1.9",
    database="jobs",
    user="user3",
    password="password3")
  cur = conn.cursor()
  cur.execute("SELECT * FROM listings")
  jobs = cur.fetchall()
  cur.close()
  conn.close()
  return jobs


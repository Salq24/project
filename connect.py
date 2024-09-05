import datetime
import mysql.connector

__cnx = None

def connect_sql():
  print("connecting sql")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='root', database='ana_groceries')

  return __cnx
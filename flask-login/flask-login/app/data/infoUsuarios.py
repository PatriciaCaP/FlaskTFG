from flask import request

class Usuarios:

   def __init__(self, db):
      self.db = db

   def addUsuario(self,nombre,email,password):
      if nombre and email and password:
            cursor = self.db.cursor()
            sql = "INSERT INTO usuarios (nombre,email,password) VALUES (%s,%s,%s)"
            data = (nombre,email,password)
            cursor.execute(sql,data)
            self.db.commit()
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello I am Alive!"

def run():
  app.run(host = '0.0.0.0', port = 8000)

def Keep_Alive():
  t = Thread(target = run)
  t.start()
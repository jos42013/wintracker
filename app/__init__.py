# Point D'entrée de l'application Flask
from flask import Flask, render_template
from config import Config
from routes import app

app.config.from_object(Config)
app.run(debug=True)
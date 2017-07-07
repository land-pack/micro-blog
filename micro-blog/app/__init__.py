from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

"""
If you are wondering why the import statement is at the end and not at 
the beginning of the script as it is always done, the reason is to avoid 
circular references, because you are going to see that the views module 
needs to import the app variable defined in this script. Putting the 
import at the end avoids the circular import error.
"""
from app import views, models

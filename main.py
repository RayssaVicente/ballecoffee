from flask import Flask
from routes.home import home_route
import os
print(os.getcwd())  # Mostra o diretório de trabalho atual
from flask import Flask
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))


app.register_blueprint(home_route)





app.run(debug=True)
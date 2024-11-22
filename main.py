from flask import Flask
from routes.home import home_route
from routes.receitas import receitas_routes


app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(receitas_routes, url_prefix='/receitas')

app.run(debug=True)
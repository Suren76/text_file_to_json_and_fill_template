from flask import Flask
import flaskcode
from config import PATH_TO_PROJECT_FOLDR

app = Flask(__name__)
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = str(PATH_TO_PROJECT_FOLDR)
app.register_blueprint(flaskcode.blueprint, url_prefix='/edit')

@app.route('/')
def hello():
    return "Hi. if you want to edit files please follow the <a href='/edit'>link</a>"

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)

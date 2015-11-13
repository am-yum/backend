from flask import Flask, request, json
from flask.ext.mysql import MySQL

app = Flask(__name__)


# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'DEA'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# conn = mysql.connect()
# cursor = conn.cursor()

# hard coding, sample of json
json_data={
	"dst_ip":"0.0.0.0",
	"dst_port":80,
	"dst_ctry":"JP",
	"dst_lat":"hoge",
	"dst_long":"hoge",
	"src_ip":"1.0.0.0",
	"src_port":88,
	"src_ctry":"US",
	"src_lat":"foo",
	"src_long":"foo",
	"protocol":"http",
	"traffic":1000
}

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/data/", methods=['GET', 'POST'])
def data():
	return json.dumps(json_data,indent=4)

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
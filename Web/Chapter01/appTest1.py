from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

if __name__ == "__main__":
	app.run(host="0.0.0.0")	 # 모든 아이피 처리 가능

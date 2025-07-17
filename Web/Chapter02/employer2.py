from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

contacts = []
@app.route('/')
def index():
	return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit():
	name = request.form.get('name')
	phone = request.form.get('phone')
	email = request.form.get('email')
	contacts.append({'name':name, 'phone':phone, 'email':email})
	return f"<h3>입력 완료: {name}-{phone}-{email}</h3><br><a href='/'>돌아가기</a>"

@app.route('/list')
def view():
	if contacts:
		df = pd.DataFrame(contacts)
		table = df.to_html(index=False, border=1)
	else:
		table = "<p>저장된 데이터가 없습니다.</p>"
	return f"{table}<br><a href='/'>돌아가기</a>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

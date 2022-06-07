from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
	return render_template('main.html')

@app.route('/script.js', methods=['POST', 'GET'])
def script():
	return render_template('script.js')

if __name__ == '__main__':
	app.run("0.0.0.0", 5000, debug=False)

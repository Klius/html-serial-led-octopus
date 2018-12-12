from flask import Flask,render_template,request
import ser
app = Flask(__name__)
com = ser.ser('COM3','9600')


@app.route('/')
def hello_world():
    return render_template('index.html')
	
@app.route('/api/0.1/send/')
def sendToArduino():
	matrix = request.args.get('matrix', '')
	com.sendToArduino(matrix)
	return matrix
	

if __name__ == '__main__':
   app.run(debug = True)
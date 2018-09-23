from flask import Flask, render_template 

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

if __name__=="__main__":
	app.run(debug=True)
	  #Luanches the page on the port specified
	#import os
	#HOST = os.environ.get('SERVER_HOST', 'localhost')
	#try:
	#	PORT = int(os.environ.get('SERVER_PORT', '5555'))
	#except ValueError:
	#	PORT = 5555
        #End of launch the page code
	#app.run(HOST,PORT)
	
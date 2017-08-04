from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/', methods=['POST'])
def ropasi():
	
	session['rock'] = request.form['rock']
	session['paper'] = request.form['paper']
	session['scissor'] = request.form['scissor']
	print session['rock']
	rock = session['rock']
	paper = session['paper']
	scissor = session['scissor']
	print rock
	print paper
	print scissor
	redirect('/', rock= rock, scissor = scissor, paper = paper)


app.run(debug=True)
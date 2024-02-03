from flask import Flask, render_template, jsonify, redirect, url_for, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    random_num = random.randint(0, 1800)
    print(random_num)
    return render_template('index.html', random_number=random_num)

@app.route('/get_random_number')
def get_random_number():
    random_num = random.randint(0, 1900)
    return jsonify({'random_number': random_num})

if __name__ == '__main__':
    app.run()

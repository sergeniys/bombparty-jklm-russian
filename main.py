from flask import Flask, render_template, request, jsonify
import random
import consolbomb as bomber


app = Flask(__name__)
historsis = []
f = open(r'russian.txt').readlines()
phrase = ''

@app.route('/')
def indexhome():
    return render_template('indexhome.html')

@app.route('/game')
def index():
    return render_template('index_no_input.html')

def create_word():
    word = bomber.create()
    global phrase
    phrase = word
    return {'word': word}

@app.route('/create_word', methods=['GET'])
def generate_word():
    return jsonify(create_word())



@app.route('/check_numbers', methods=['POST'])
def check_numbers():
    data = request.get_json()
    text = str(data.get('text', '')).lower()[:-1]
    hasNumbers = False
    print('до', phrase, text)
    #print(str(text.lower())[:-1] == "число")

    if phrase in text:
        print('1')
    if f'{text}\n' in f:
        print('2')
    if text not in historsis:
        print('3')

    if phrase in text and f'{text}\n' in f and text not in historsis:
        print('работает')
        historsis.append(text)
        hasNumbers = True


    return jsonify({'hasNumbers': hasNumbers})

if __name__ == '__main__':
    app.run(debug=True)

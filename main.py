from flask import Flask, render_template, request, jsonify

import consolbomb as bomber


app = Flask(__name__)
f = open(r'russian.txt').readlines()
params = {'historsis': [], 'phrase': '', 'nick': '', }

@app.route('/save_nick', methods=['POST'])
def save_nick():
    global params
    data = request.get_json()
    params['nick'] = data.get('nick')

    if params['nick'] == '':
        params['nick'] = "unnamed"
    return ('', 204)

@app.route('/leaders')
def leaders():
    leaders_data = []
    with open('leaders.txt', 'r') as leaders_file:
        for line in leaders_file:
            nick, score = line.strip().split(',')
            leaders_data.append({'nick': nick, 'score': score})
    return render_template('leaders.html', leaders=leaders_data)
@app.route('/')
def indexhome():
    return render_template('indexhome.html')

@app.route('/game')
def index():
    return render_template('index_no_input.html')

def create_word():
    word = bomber.create()
    global params
    params['phrase'] = word
    return {'word': word}

@app.route('/create_word', methods=['GET'])
def generate_word():
    return jsonify(create_word())



@app.route('/check_numbers', methods=['POST'])
def check_numbers():
    global params
    data = request.get_json()
    text = str(data.get('text', '')).lower()[:-1]
    hasnumbers = False
    #print('до', phrase, text, nick)
    # #print(str(text.lower())[:-1] == "число")
    #
    # if phrase in text:
    #     print('1')
    # if f'{text}\n' in f:
    #     print('2')
    # if text not in historsis:
    #     print('3')

    if params['phrase'] in text and f'{text}\n' in f and text not in params['historsis']:

        params['historsis'].append(text)
        hasnumbers = True


    return jsonify({'hasNumbers': hasnumbers})

if __name__ == '__main__':
    app.run(debug=True)

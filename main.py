from flask import Flask, render_template, request, jsonify
import consolbomb as bomber
from datetime import datetime

app = Flask(__name__)
f = open(r'russian.txt').readlines()
params = {'historsis': [], 'phrase': '', 'nick': '', 'score': 0}

@app.route('/save_nick', methods=['POST'])
def save_nick():
    global params
    data = request.get_json()
    print(data)
    params['nick'] = data.get('nick')

    if params['nick'] == '':
        params['nick'] = "unnamed"
    return ('', 204)


@app.route('/leaders')
def leaders():
    leaders_data = []
    with open(r'leaders.txt') as leaders_file:
        for line in leaders_file:
            try:
                nick, score, date = line.strip().split(',')
                leaders_data.append({'nick': nick, 'score': int(score), 'date': date})
            except:
                pass

    sorted_leaders_data = sorted(leaders_data, key=lambda x: x['score'], reverse=True)

    return render_template('leaders.html', leaders=sorted_leaders_data)



@app.route('/')
def indexhome():
    return render_template('indexhome.html')

@app.route('/game')
def index():
    return render_template('index_no_input.html')

@app.route('/need-computer')
def indexcomp():
    return render_template('need-computer.html')

def create_word():
    word = bomber.create()
    global params
    params['phrase'] = word
    return {'word': word}

@app.route('/create_word', methods=['GET'])
def generate_word():
    return jsonify(create_word())



@app.route('/score', methods=['POST'])
def save_score():
    global params
    data = request.get_json()
    params['score'] = data['score']
    if  params['score'] == 0:
        return ('', 204)
    # Добавьте текущую дату в формате 'dd.mm.yyyy'
    current_date = datetime.now().strftime('%d.%m.%Y')
    with open('leaders.txt', 'a') as f:
        f.write(f'\n{params["nick"]},{params["score"]},{current_date}')

    return ('', 204)




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

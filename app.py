
from models import *
from random import randrange
from flask import request,abort
setupDb()

ques = Question("Which country won the 2022 World Cup?",'sports','{"Ghana":1,"Argentina":2,"Botswana":3}','Argentina')
ques.add()

ques1 = Question("Who is the GOAT?",'sports','{"Ronaldo":1,"Messi":2}','Messi')
ques1.add()

ques3 = Question("Is Africa country?","general knowledge",'{"True":1,"False":2}','False')
ques3.add()

ques4 = Question("The first black president of the USA is?","politics",'{"George Bush":1,"Barack Obama":2,"Trump":3,"Joe Biden":4}','Barack Obama')
ques4.add()



@app.route('/')
@app.route('/home')
@app.route('/home/')
def home():
    return render_template('home.html',title='Home')


@app.route('/play')
@app.route('/play/')
def play_selection():
    return render_template('option.html',title="Select")

@app.route('/play/<string:select>')
@app.route('/play/<string:select>/')
def play_select(select):
    icons = {'sports':'football','general knowledge':'book','science':'atom','politics':'flag','random':'earth'}
    return render_template('game.html',title=f'{select}',icon=icons[f'{select}'.lower()],selected=f'{select}'.capitalize())


@app.route('/questions/<string:type>',methods=['POST'])
def get_questions(type):

    data_return = []
    try:
        data = [ques.question_format() for ques in Question.query.filter(Question.type == f"{type}".lower()).all()]
        if type == 'Random':
            
            data = [ques.question_format() for ques in Question.query.all()]
            return jsonify(data[randrange(0,len(data)-1,1)])
        for ques in data:
            if ques['id'] not in request.get_json() or len(request.get_json()) < 1:
                data_return.append(ques)
        print(data_return[0])
        return jsonify(data_return[0])
    except:
        abort(404)



@app.errorhandler(404)
def now_found(error):
    return jsonify({"success":False})
from bottle import route ,run, template

@route('/')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def greet(name='nobuhara'):
    return template ('Hello {{name}}, how are you?', name=name)

run(host='localhost',port=8080, debug=True)
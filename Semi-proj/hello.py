from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) #템플릿 뿌려주기 위해 render_template() 메소드 사용
from flask import Flask
from flask import render_template
from BmobUtils import QueryUtils

app = Flask(__name__)
beanList=[]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/name')
def hello(name=None):
    user = {'nickname': '盛开'}  # fake user
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=beanList)


if __name__ == '__main__':
    beanList=[]
    beanList=QueryUtils.queryBmob('HXBean')
    # print(beanList)
    app.run()

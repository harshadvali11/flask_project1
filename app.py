#Create Application Instance
# Application instance is an Object of Flask Class
# So Import Flask Class
# Flask class will take one arguement that is Name of current Module
# standard way to represent current module name is __name__

from flask import Flask

AI=Flask(__name__)

# create one view function and decorate it with route method of AI

@AI.route('/wish')
def wish():
    return 'This is my first flask View Function'

@AI.route('/second')
def second():
    return 'Second View Function'

if __name__=='__main__':
    AI.run(debug=True,host='192.168.15.33',port=5001)











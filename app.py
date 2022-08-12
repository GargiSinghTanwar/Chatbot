#importing libraries
from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat

app = Flask(__name__)

qa_pairs = [
    ['(.*)name(.*)',['hello my name is Bibble, whats your name ']],
    ['(.*)food(.*)',['which type of food do you prefer now north indian,south indian,chinese,italian']],
    ['(.*)(hi|Hello)(.*)',['hello how can i help you']],
    ['(.*)(north indian|south indian|chinese|italian)(.*)',['I like chinese']],
    ['(.*)(sport|play|hobbie)(.*)',['I love to play cricket']],
    ['(.*)(love/talk)(.*)',['I am love to talk new people']],
    ['(.*)',['sorry i dont know this']]
    
]

cb = Chat(qa_pairs)

@app.route("/",methods= ["GET","POST"])
def chatbot_responses():
    response = ''
    if request.method == 'POST':
        msg = request.form['message']
        response = cb.respond(msg)
    return render_template('index.html',response1 = response)

if __name__=="__main__":
    app.run(debug=True)
    

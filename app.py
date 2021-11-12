# app.py (서버 > 클라이언트 응답; POST방식)
from fuctions import predict
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
 # print('Input: {}'.format(sentence))
  #print('Output: {}'.format(predicted_sentence))
@app.route('/test', methods=['POST'])

def test_post():

    title_receive = request.form['title_give']
    print(title_receive)
    result=predict(title_receive)
    return jsonify({'result':result, 'msg':'이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug = True)
'''
    $.ajax({
        type: "POST",
        url: "/test",
        data: {title_give: '봄날은간다'},
        success: function(response){
            console.log(response)
        }
    })'''
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/Hello')
def Hello():
    return "Hello everyone"

@app.route('/Fake_news_predication', methods=['POST'])
def Fake_news_predication():
    data = request.form.get('message')

    if data is None:
        return jsonify({'error': 'Missing "message" field in the request'}), 400

    result = util.Fake_news_detecation([data])

    estimated_probability = result[0][0]
    predication_value = result.tolist()

    if estimated_probability >0.5:
        info = "This is Fake News"
        m = [1]
    
    else:
        info = "This is real news"
        m = [0]
    

    response = jsonify({
        'estimated': predication_value,
        'result' : info,
        'result_m': m
    })

    return response

if __name__ == '__main__':
    util.load_saved_artificats()
    app.run()

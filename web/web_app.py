from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M')

    r = requests.get('http://database:5000/ds18b20')
    data = r.json()

    template_data = {
        'title': 'Hello',
        'time': now_str,
        'data': f'{data[0]["timestamp"]}: {data[0]["temperature"]}°C'
    }

    return render_template('index.html', **template_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

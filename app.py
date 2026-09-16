import os
import csv
import io
import json
import time
from collections import deque
from threading import Lock, Thread
from flask import Flask, Response, render_template
from sensors import reading


def create_app(start_sampler=True):
    app = Flask(__name__)
    app.config.update(APP_TITLE='Sensor Dashboard',APP_DESCRIPTION='Live temperature and humidity simulation.')
    history = deque(maxlen=300)
    lock = Lock()

    def sample():
        index = 0
        while True:
            with lock:
                history.append(reading(index))
            index += 1
            time.sleep(1)

    if start_sampler:
        Thread(target=sample,daemon=True).start()
    else:
        history.append(reading(0))

    @app.get('/')
    def index():
        return render_template('index.html',title='Live readings')

    @app.get('/stream')
    def stream():
        def events():
            previous = None
            while True:
                with lock:
                    latest = dict(history[-1]) if history else None
                if latest and latest != previous:
                    yield 'data: '+json.dumps(latest)+'\n\n'
                    previous = latest
                else:
                    yield ': heartbeat\n\n'
                time.sleep(1)
        return Response(events(),mimetype='text/event-stream',headers={'Cache-Control':'no-cache','X-Accel-Buffering':'no'})

    @app.get('/export')
    def export():
        with lock:
            items = list(history)
        output = io.StringIO()
        writer = csv.DictWriter(output,fieldnames=['timestamp','temperature','humidity'])
        writer.writeheader()
        writer.writerows(items)
        return Response(output.getvalue(),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=sensor-readings.csv'})

    return app


if __name__ == '__main__':
    create_app().run(host=os.getenv('HOST','127.0.0.1'),port=5000,threaded=True)

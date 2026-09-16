import json
from app import create_app
from sensors import reading


def test_sensor_ranges_and_exports():
    for i in range(100):
        value = reading(i)
        assert 18 <= value['temperature'] <= 26
        assert 40 <= value['humidity'] <= 60
    client = create_app(start_sampler=False).test_client()
    assert client.get('/').status_code == 200
    assert b'timestamp,temperature,humidity' in client.get('/export').data
    response = client.get('/stream',buffered=False)
    first = next(response.response).decode()
    assert 'temperature' in json.loads(first.removeprefix('data: ').strip())
    response.close()

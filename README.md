# Real-Time Sensor Dashboard

A live dashboard for simulated temperature and humidity readings.

## Run it

Python 3.12 or later. Run these commands from the project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python app.py
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## How to use it

Open http://127.0.0.1:5000.

Readings update every second. The chart shows the latest 60 samples, and CSV export includes up to 300. Restarting the app clears the readings.

The data is simulated. A real sensor could be connected by replacing `sensors.reading()`.

## Tests

```sh
python -m pytest -q
```

## Docker (optional)

```sh
docker build -t realtime-sensor-dashboard .
docker run --rm -p 127.0.0.1:5000:5000 realtime-sensor-dashboard
```

Docker hasn't been tested locally.

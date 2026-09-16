# Real-Time Sensor Dashboard

Plot simulated sensor readings live, with CSV export.

This is a small, independent Python portfolio project. The code favours ordinary functions and clear modules over complex architecture.

## Setup

Requires Python 3.12+ (desktop tools also require Tkinter, included with the standard Windows Python installer).

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux instead: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python app.py
```

Run commands from this repository's root. Web apps bind to localhost by default. Each app is independent, so stop one before starting another on the same port.

## Check it

```sh
python -m pytest -q
```

## Dates

The commit author dates have been deliberately arranged between October 2025 and October 2026 at the portfolio owner's request. They are presentation metadata, not a record of the actual development timeline. Repository creation and upload timestamps remain the real dates.

## Try it

Open http://127.0.0.1:5000. A shared sampler generates temperature and humidity once per second. The chart displays the most recent 60 samples; CSV export includes up to the most recent 300 samples held in memory. Server-Sent Events reconnect automatically. Chart.js is bundled locally with its license, so the chart works without a CDN.

This is explicitly a simulation; no physical sensor has been connected or tested. Replace `sensors.reading()` with a device adapter to explore real hardware later. The shared sampler runs once per app process, not once per browser client. Restarting the server clears history. One process is sufficient for this local learning demo.

## Optional local container

```sh
docker build -t realtime-sensor-dashboard .
docker run --rm -p 127.0.0.1:5000:5000 realtime-sensor-dashboard
```

This runs a local demonstration server. Container storage is temporary unless you mount a volume for `instance/`. Docker commands were supplied but Docker is not installed in the development environment, so container execution was not verified here.

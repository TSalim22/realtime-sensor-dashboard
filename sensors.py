import math
import random
from datetime import datetime, timezone


def reading(index):
    return {'timestamp':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'temperature':round(22+3*math.sin(index/15)+random.uniform(-.3,.3),2),
        'humidity':round(50+8*math.cos(index/19)+random.uniform(-1,1),2)}

import json
from models.Rate import Rate
rate_list = Rate.load_rate()
for rate in rate_list:
    print(rate._get_id())
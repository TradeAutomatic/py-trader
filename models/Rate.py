from models.MySQL import MySQL
import json
class Rate :
    """
        C'est la classe qui permet de gérer les différentes
        cotations des paires
    """
    #Contient les dernières cotations qui ont été chargé de la base de données
    rate_list = []

    #Les Symboles
    symbole_EURUSD = "EURUSD"


    def __init__(self):
        self._open = 0.0
        self._close = 0.0
        self._high = 0.0
        self._low = 0.0
        self._time = 0.0
        self._period = ""
        self._symbol = ""
        self._id = ""
        self._tick_volume = 0
        
        #Les attributs selon les indicateurs technique
        pass
    
    
    #Les getteurs

    def _get_open(self):
        return self._open
        pass
    def _get_close(self):
        return self._close
        pass
    def _get_high(self):
        return self._high
        pass
    def _get_low(self):
        return self._low
        pass
    def _get_time(self):
        return self._time
        pass
    def _get_period(self):
        return self._period
        pass
    def _get_symbol(self):
        return self._symbol
        pass
    def _get_id(self):
        return self._id
        pass
    def _get_tick_volume(self):
        return self._tick_volume
        pass

    #Les setters

    def _set_open(self, open_value):
        self._open = open_value
        pass
    def _set_close(self, close_value):
        self._close = close_value
        pass
    def _set_high(self, high_value):
        self._high = high_value
        pass
    def _set_low(self, low_value):
        self._low = low_value
        pass
    def _set_time(self, time_value):
        self._time = time_value
        pass
    def _set_period(self, period_value):
        self._period = period_value
        pass
    def _set_symbol(self, symbol_value):
        self._symbol = symbol_value
        pass
    def _set_id(self, id_value):
        self._id = id_value
        pass
    def _set_tick_volume(self, tick_volume_value):
        self._tick_volume = tick_volume_value
        pass

    open = property(_get_open, _set_open)
    close = property(_get_close, _set_close)
    high = property(_get_high, _set_high)
    low = property(_get_low, _set_low)
    time = property(_get_time, _set_time)
    period = property(_get_period, _set_period)
    symbol = property(_get_symbol, _set_symbol)
    id = property(_get_id, _set_id)
    tick_volume = property(_get_tick_volume, _set_tick_volume)

    #Les interactions avec la base de données
    def load_rate(symbol="EURUSD", period = "15"):
        mysql = MySQL()
        result = mysql.select(table_name="price", where_clause={"valeur":"\"period\":\""+str(period)+"\"", "id":symbol}, mode="like")
        rate_list = []
        for rate in result:
            tmp = Rate.json_to_rate(rate[1])
            tmp._set_id(rate[0])
            rate_list.append(tmp)
        return rate_list

    def json_to_rate(json_str):
        rate = Rate()
        tmp = json.loads(json_str)
        rate._set_symbol(tmp["symbol"])
        rate._set_open(tmp["open"])
        rate._set_close(tmp["close"])
        rate._set_high(tmp["high"])
        rate._set_low(tmp["low"])
        rate._set_tick_volume(tmp["tick_volume"])
        rate._set_time(tmp["time"])
        rate._set_period(tmp["period"])
        return rate        


    load_rate = staticmethod(load_rate)
    json_to_rate = staticmethod(json_to_rate)

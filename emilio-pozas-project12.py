class Flight:
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay,arr_delay):
        self.flight_number = flight_number
        self.origin_ID = origin_ID
        self.dest_ID = dest_ID
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.dep_delay = dep_delay
        self.arr_delay = arr_delay

    
    def get_arrdelay(self):
        return self.arr_delay
    
    def get_depdelay(self):
        return self.dep_delay
    
    def is_ontime(self):
        if self.dep_delay <= 0 and self.arr_delay <= 0:
            return True
        else:
            return False
    
class ScheduledFlight(Flight):
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay, CRSDepTime, CRSArrTime):
        super().__init__(flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay)
        self.CRSDepTime = CRSDepTime
        self.CRSArrTime = CRSArrTime
        
import pandas as pd
columns_to_read = [
    'DepDelay', 'ArrDelay', 'Flight_Number_Reporting_Airline', 'Distance',
    'CarrierDelay', 'WeatherDelay', 'CRSDepTime', 'CRSArrTime',
    'DepTime', 'ArrTime', 'Origin',
    'Dest', 'AirTime'
]
col_types = {
    'Flight_Number_Reporting_Airline': 'int64',
    'Origin': 'object',
    'Dest' : 'object',
    'DepTime': 'float64',
    'DepDelay': 'float64',
    'ArrTime': 'float64',
    'ArrDelay': 'float64',
    'Distance': 'float64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
    'CRSDepTime' : 'float64',
    'CRSArrTime' : 'float64',
    'AirTime' : 'float64'
}
myDF = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv", usecols =columns_to_read, dtype=col_types, nrows=100 )
myDF.head()
myDF.shape

longlistofflights = []
for index, row in myDF.iterrows():
    myflight = ScheduledFlight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_ID = row['Origin'],
        dest_ID = row['Dest'],
        dep_time = row['DepTime'],
        arr_time = row['ArrTime'],
        dep_delay = row['DepDelay'],
        arr_delay = row['ArrDelay'],
        CRSDepTime = row['CRSDepTime'],
        CRSArrTime = row['CRSArrTime']
    )
    longlistofflights.append(myflight)
    
ontime_count = {}
ontime_boolean = {}

for myflight in longlistofflights:
    if myflight.dest_ID not in ontime_count:
        ontime_count[myflight.dest_ID] = 0
    
    if myflight.is_ontime():
        ontime_count[myflight.dest_ID] += 1

for myflight in longlistofflights:
    if myflight.dest_ID not in ontime_boolean:
        ontime_boolean[myflight.dest_ID] = []
    ontime_boolean[myflight.dest_ID].append(myflight.is_ontime())
    
ontime_count
ontime_boolean

class Flight:
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay,arr_delay):
        self.flight_number = flight_number
        self.origin_ID = origin_ID
        self.dest_ID = dest_ID
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.dep_delay = dep_delay
        self.arr_delay = arr_delay

    
    def get_arrdelay(self):
        return self.arr_delay
    
    def get_depdelay(self):
        return self.dep_delay
    
    def is_ontime(self):
        if self.dep_delay <= 0 and self.arr_delay <= 0:
            return True
        else:
            return False
        
    def is_delayed(self):
        if self.dep_delay >= 0 or self.arr_delay >= 0:
            return True
        else:
            return False
        
class ScheduledFlight(Flight):
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay, CRSDepTime, CRSArrTime):
        super().__init__(flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay)
        self.CRSDepTime = CRSDepTime
        self.CRSArrTime = CRSArrTime

delayed_count = {}
for myflight in longlistofflights:
    if myflight.dest_ID not in delayed_count:
        delayed_count[myflight.dest_ID] = 0
    
    if myflight.is_delayed():
        delayed_count[myflight.dest_ID] += 1
        
delayed_count

class Flight_Air(Flight): 
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay, air_time):
        super().__init__(flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay, arr_delay)
        self.air_time = air_time
    
    def get_airtime(self):
        return self.air_time
    
longlistofflights_extra = []
for index, row in myDF.iterrows():
    myflight = Flight_Air(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_ID = row['Origin'],
        dest_ID = row['Dest'],
        dep_time = row['DepTime'],
        arr_time = row['ArrTime'],
        dep_delay = row['DepDelay'],
        arr_delay = row['ArrDelay'],
        air_time = row['AirTime']
    )
    longlistofflights_extra.append(myflight)
    
air_timeDest = {}
for myflight in longlistofflights_extra:
    if myflight.dest_ID not in air_timeDest:
        air_timeDest[myflight.dest_ID] = []
    air_timeDest[myflight.dest_ID].append(myflight.get_airtime())
air_timeDest
average_airtime = {myairport: sum(myairtime)/len(myairtime) for myairport, myairtime in air_timeDest.items()}
average_airtime
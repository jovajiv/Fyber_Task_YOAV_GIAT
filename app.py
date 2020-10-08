from flask import Flask, request
from collections import OrderedDict
import requests
import json

app = Flask(__name__)

# CONSTANTS
DATE = 0
VALUE = 1


@app.route('/')
def hello_world():
    return json.dumps({})


@app.errorhandler(404)
def page_not_found(err):
    return json.dumps({})


# used to test the status of the remote api server being used by us.
@app.route('/status')
def status():
    try:
        url = 'https://disease.sh/v3/covid-19/historical/'
        r = requests.get(url, verify=True, timeout=3)
        print(r.status_code)
        if r.status_code == 200:
            print("server is responding")
            return json.dumps({"status": "success"})
        else:
            print("Remote API has issues, 'https://disease.sh/v3/covid-19/historicall/',return code is {} instead of 200".format(r.status_code))
            return json.dumps({"status": "failure"})
    except:
        return json.dumps({"status": "failure"})


# full url request :
# curl localhost:8080/recoveredPeak?country=ukraine
# curl localhost:8080/deathsPeak?country=ukraine
# curl localhost:8080/newCasesPeak?country=israel
#
# returns json answer : {"country": "israel", "method": "cases", "date": "9/23/20", "value": 11316}
# where value is the peak daily change detected within the last 30 days
# if exception is thrown, return  {}
@app.route('/<query>Peak')
def peak(query):
    try:

        # response.raise_for_status()
        country = request.args.get('country', "")
        print(country)
        response = requests.get("https://disease.sh/v3/covid-19/historical/" + country + "?lastdays=30")
        if response.ok:
            requested_info = query_type()
            ordered_json_response = response.json(object_pairs_hook=OrderedDict)['timeline'][requested_info[query]]  #pairs are now orderd tuples.   OrderedDict([('9/7/20', 133975), ('9/8/20', 137565),....}
            list_of_pairs = list(ordered_json_response.items())              ## [('9/7/20', 133975), ('9/8/20', 137565), ('9/9/20', 141097),...] list format
            print(list_of_pairs)
            print(type(list_of_pairs))
            pair=max_pair_by_val(list_of_pairs)     # pair=(date_of_max_diff, max_diff)
            ordered_json_reply=OrderedDict([("country", country), ("method", requested_info[query]), ("date", pair[DATE]), ("value", pair[VALUE])])
            return json.dumps(ordered_json_reply)
        else:
            return json.dumps({})
    except:
        return json.dumps({})


# this function returns a dictionary that translates the query the user inputs in the url,
# to the respective name according to 3rd party api.
def query_type():
    switcher = {
        'newCases': "cases",
        'recovered': "recovered",
        'deaths':   "deaths"
    }
    return switcher


# this function receives a list of tuple pairs. [(key1,val1) , (key2,val2) , (key3,val3)...]
# returns the pair (key,diff) whose diff (curr_elemnt_val - prev_elemnt_val) is maximal.
def max_pair_by_val(list):
    max_diff = 0
    max_index = 0
    for index in range(0, len(list)-1):
        temp_diff=list[index+1][VALUE]-list[index][VALUE]
        if temp_diff > max_diff:
            max_index = index+1
            max_diff = temp_diff

    return list[max_index][DATE], max_diff


if __name__ == '__main__':
    app.run(port=11000)


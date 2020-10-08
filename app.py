from flask import Flask,jsonify,request
from collections import OrderedDict
import requests
import json

app = Flask(__name__)

#CONSTANTS
DATE=0
VALUE=1

@app.route('/')
def hello_world():
    response = requests.get("https://disease.sh/v3/covid-19/all")
    print(type(response.json()))
    return response.json()
    #print (type(response.status_code))
    #return 'Hello World!'


@app.errorhandler(404)
def page_not_found(error):
    return json.dumps({})

#used to test the status of the remote api server being used by us.
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
            print("Remote API has issues , 'https://disease.sh/v3/covid-19/historicall/'  ,return code is {} instead of 200".format(r.status_code))
            return json.dumps({"status": "failure"})
    except:
        return json.dumps({"status": "failure"})

    #print (type(response.status_code))
    #return 'Hello World!'



# @app.route('/newCasesPeakcountry=<country>')
# def hello_world3(country):
#     try:
#         response = requests.get("https://disease.sh/v3/covid-19/historical/"+country+"?lastdays=30")
#         response.raise_for_status()
#         if response.ok:
#             print(response.json())
#             ordered_json_response=response.json(object_pairs_hook=OrderedDict)['timeline']['cases']  #pairs are now orderd tuples.   OrderedDict([('9/7/20', 133975), ('9/8/20', 137565),....}
#             print(ordered_json_response)
#             max_diff=0
#             max_tuple=pop_first_item(ordered_json_response)         # TODO: handle case of empty tuple....
#
#
#             print(max_tuple[1])
#             print(max_diff)
#             print(max_tuple[0])
#             print(max_tuple)
#             print({"aa":300,"bb":400})
#             for key in ordered_json_response.keys():
#                 print(key)
#                 if ordered_json_response[key] - max_tuple[1] > max_diff :
#                     max_diff=ordered_json_response[key] - max_tuple[1]
#                     print("max diff is {}".format(max_diff))
#                     max_tuple=(key,ordered_json_response[key])
#                     print("max diff is {}".format(max_tuple[1]))
#             return {key:max_diff}
#
#
#
#             print(type(ordered_json_response.values()))
#             temp=numpy.array(list(ordered_json_response.values()))
#             print(temp)
#             print('hello')
#             print(max(numpy.diff(temp)))
#             print(numpy.diff(temp))
#             #return {"country":country,"method":"newCasesPeak","date":,"value":}
#
#
#
#             # cases=first_item(ordered_json_response)
#             # max_pair=(cases[0],0)
#             # prev_max=0
#             # for key in ordered_json_response.keys():
#             #     print(key)
#             #     ordered_json_response[key]
#
#
#             # print(cases[1])
#             # print(type(cases))
#             return ordered_json_response
#             #print (type(response.status_code))
#             #return 'Hello World!'
#         else:
#             return "API failed to respond"
#     except requests.exceptions.HTTPError as e:
#         return (e).__str__()



#
# @app.route('/newCasesPeakcountrys=<country>')
# def newCasesPeak(country):
#     try:
#         response = requests.get("https://disease.sh/v3/covid-19/historical/"+country+"?lastdays=30")
#         response.raise_for_status()
#         if response.ok:
#             ordered_json_response=response.json(object_pairs_hook=OrderedDict)['timeline']['cases']  #pairs are now orderd tuples.   OrderedDict([('9/7/20', 133975), ('9/8/20', 137565),....}
#             list_of_pairs = list(ordered_json_response.items())              ## [('9/7/20', 133975), ('9/8/20', 137565), ('9/9/20', 141097),...] list format
#             print(list_of_pairs)
#             print(type(list_of_pairs))
#             pair=max_pair_by_val(list_of_pairs)     # pair=(date_of_max_diff, max_diff)
#             ordered_json_reply=OrderedDict([("country",country),("method","newCasesPeak"),("date",pair[DATE]), ("value",pair[VALUE])])
#             return json.dumps(ordered_json_reply)
#         else:
#             return "API failed to respond"
#     except requests.exceptions.HTTPError as e:
#         return (e).__str__()


#full url request :
# curl localhost:8080/recoveredPeak?country=ukraine
# curl localhost:8080/deathsPeak?country=ukraine
# curl localhost:8080/newCasesPeak?country=israel

# returns json answer : {"country": "israel", "method": "cases", "date": "9/23/20", "value": 11316}
# if exception is thrown, return  {}
@app.route('/<query>Peak')
def recoveredPeak(query):
    try:

        #response.raise_for_status()
        country = request.args.get('country', "")
        print(country)
        response = requests.get("https://disease.sh/v3/covid-19/historical/" + country + "?lastdays=30")
        if response.ok:
            requested_info=queryType(query)
            ordered_json_response=response.json(object_pairs_hook=OrderedDict)['timeline'][requested_info[query]]  #pairs are now orderd tuples.   OrderedDict([('9/7/20', 133975), ('9/8/20', 137565),....}
            list_of_pairs = list(ordered_json_response.items())              ## [('9/7/20', 133975), ('9/8/20', 137565), ('9/9/20', 141097),...] list format
            print(list_of_pairs)
            print(type(list_of_pairs))
            pair=max_pair_by_val(list_of_pairs)     # pair=(date_of_max_diff, max_diff)
            ordered_json_reply=OrderedDict([("country",country),("method",requested_info[query]),("date",pair[DATE]), ("value",pair[VALUE])])
            return json.dumps(ordered_json_reply)
        else:
            return json.dumps({})
    except:
        return json.dumps({})


# this function returns a dictionary that translates the query the user inputs in the url,
# to the respective name according to 3rd party api.
def queryType(type):
    switcher= {
        'newCases': "cases",
        'recovered': "recovered",
        'deaths':   "deaths"
    }
    return switcher;




# @app.route('/deathsPeakcountrys=<country>')
# def recoveredPeak(country):
#     try:
#         response = requests.get("https://disease.sh/v3/covid-19/historical/"+country+"?lastdays=30")
#         response.raise_for_status()
#         if response.ok:
#             ordered_json_response=response.json(object_pairs_hook=OrderedDict)['timeline']['deaths']  #pairs are now orderd tuples.   OrderedDict([('9/7/20', 133975), ('9/8/20', 137565),....}
#             list_of_pairs = list(ordered_json_response.items())              ## [('9/7/20', 133975), ('9/8/20', 137565), ('9/9/20', 141097),...] list format
#             print(list_of_pairs)
#             print(type(list_of_pairs))
#             pair=max_pair_by_val(list_of_pairs)     # pair=(date_of_max_diff, max_diff)
#             ordered_json_reply=OrderedDict([("country",country),("method","newCasesPeak"),("date",pair[DATE]), ("value",pair[VALUE])])
#             return json.dumps(ordered_json_reply)
#         else:
#             return "API failed to respond"
#     except requests.exceptions.HTTPError as e:
#         return (e).__str__()



#this function receives a list of tuple pairs. [(key1,val1) , (key2,val2) , (key3,val3)...]
#returns the pair (key,diff) whose diff (curr_elemnt_val - prev_elemnt_val) is maximal.
def max_pair_by_val(list):
    max_diff=0;
    max_index=0;
    for index in range(0,len(list)-1):
        temp_diff=list[index+1][VALUE]-list[index][VALUE]
        if temp_diff > max_diff:
            max_index=index+1
            max_diff=temp_diff

    return (list[max_index][DATE],max_diff)

#def using_reduce(list):
#    max_diff=0;
#    print (functools.reduce(lambda pair1, pair2: (pair2[DATE],max_diff) if pair1[VALUE]-pair2[VALUE] > max_diff  , list))



@app.route('/code')
def hello_world2():
    temp = request.args.get('qqq',None)
    print(temp)
    response = requests.get("https://disease.sh/v3/covid-19/all")
    print(type(response.json()))
    return jsonify(response.status_code)
    #print (type(response.status_code))
    #return 'Hello World!'


def pop_first_item(dict):
    return dict.popitem(last=False);



if __name__ == '__main__':
    app.run(port=8080)

#TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a int.
#127.0.0.1 - - [07/Oct/2020 09:45:46] "GET / HTTP/1.1" 500 -
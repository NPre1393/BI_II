import re, os, json
from yaml import load, dump, load_all
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

#'GV12 Production'

root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/"

def formatWKSpts(wkspts):
    pass

def writeToFile(fname, dict_to_write, count):
    keys_1 = ['Aufford QR-Code-Eingabe', 'Fläche Ref-A', 'Fläche Bund', 'Kreis Ø19,2-1', 'Kreis Ø19,2-2', 'Zylinder Ø4,5-B', 'Distanz Z4,8', 'Kreis Ref-B']
    keys_auf = ['Eingabeaufforderung', 'Eingabe', 'Datum/Zeit']
    keys_fl = ['Zentrum A', 'Mitte Z', 'Ebenheit', 'Standardabweichung', '3D WKS Punkte', 'Datum/Zeit']
    keys_bund = ['Zentrum A', 'Mitte Z', 'Ebenheit', 'Standardabweichung', 'Parallelität', '3D WKS Punkte', 'Datum/Zeit']
    keys_kreis = ['Mitte X', 'Mitte Y', 'Zentrum A', 'Mitte Z', 'Radius', 'Durchmesser', 'Rundheit', 'Standardabweichung', 'Konzentrizität', '3D WKS Punkte', 'Datum/Zeit']
    keys_zylinder = ['Position X', 'Position Y', 'Position A', 'Position Z', 'Radius', 'Durchmesser', 'Richtung', 'Neigung', 'Zylinderform', 'Standardabweichung', '3D WKS Punkte', 'Datum/Zeit']
    keys_dist = ['Distanz Z', 'Datum/Zeit']
    keys_kreis2 = ['Mitte X', 'Mitte Y', 'Zentrum A', 'Mitte Z', 'Radius', 'Durchmesser', 'Rundheit', 'Standardabweichung', '3D WKS Punkte', 'Datum/Zeit']
    #print(dict_to_write.keys())
    keys = [keys_auf, keys_fl, keys_bund, keys_kreis, keys_kreis, keys_zylinder, keys_dist, keys_kreis2]
    with open(str(fname)+"_mvudata_"+str(count), 'a') as file:
        for i in range(0,len(keys_1)):
            keyword = keys_1[i]
            key_list = keys[i]
            for key in key_list:
                data = dict_to_write[keyword][key]
                file.write('{0}: {1} {2}\n'.format(keyword, key, data))
                print(data)

    #for key, val in dict_to_write.items():
    #file.write('{0},{1},{2}\n'.format(key, val[0], val[1]))    


def query_prod(filename):
    file_type = ''
    docs = load_all(filename)
    concept_name = ''

    for item in docs:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='log':
                file_type = item['log']['trace']['cpee:name']
                concept_name = item['log']['trace']['concept:name']
                #print('Concept Name: ', item['log']['trace']['concept:name'])
                #print('Cpee Name: ', item['log']['trace']['cpee:name'])
        break

    if file_type == 'GV12 Production':
        prods = {}
        counter = 0
        for item in docs:
            itemKeys = item.keys()
            for i, t in enumerate(itemKeys):
                if t=='event':
                    if item['event']['id:id'] == 'a3':
                        if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                            if 'list' in item['event'].keys():
                                if item['event']['list']['data_receiver'][0]['name'] == 'result':
                                    prods = item['event']['list']['data_receiver'][0]['data']['raw']
                                    writeToFile(concept_name, prods, counter)
                                    counter += 1
                                    prods = {}       
    

"""
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        #file_size = os.path.getsize(dirName+'/'+fname)
        item = open(dirName+'/'+fname, 'r')    
        #cn,ft,uuid = query_prod(item)
"""
fileName = open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/0bd12865-0d40-4a22-bc6f-b16510787d7f.xes.yaml")
query_prod(fileName)
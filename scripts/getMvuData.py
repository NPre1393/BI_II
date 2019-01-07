import re, os, json
from yaml import load, dump, load_all
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

#'GV12 Production'

root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/"

def writeToFile(fname, cn, ok, nok):
    with open(fname, 'a') as file:
        file.write('{0};{1};{2}\n'.format(cn, ok, nok))

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
        break
    print(concept_name)
    if file_type == 'GV12 Production':
        prods = {}
        counter = 0
        nok_counts = 0
        ok_counts = 0

        for item in docs:
            itemKeys = item.keys()
            for i, t in enumerate(itemKeys):
                if t=='event':
                    if item['event']['id:id'] == 'a3':
                        if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                            if 'list' in item['event'].keys():
                                if item['event']['list']['data_receiver'][0]['name'] == 'result':  
                                    if item['event']['list']['data_receiver'][0]['data']['results']:    
                                        nok_counts = 0
                                        ok_counts = 0         
                                        for key in item['event']['list']['data_receiver'][0]['data']['results'].keys():
                                            for key2 in item['event']['list']['data_receiver'][0]['data']['results'][key].keys():
                                                if item['event']['list']['data_receiver'][0]['data']['results'][key][key2]['status'] == 'ok':
                                                    ok_counts+=1
                                                if item['event']['list']['data_receiver'][0]['data']['results'][key][key2]['status'] == 'nok':
                                                    nok_counts+=1
                       
        return(concept_name, ok_counts, nok_counts)    
    return("a", "a", "a")

flname = "mvu_oks_new.csv"

for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        #file_size = os.path.getsize(dirName+'/'+fname)
        item = open(dirName+'/'+fname, 'r')
        cn, ok, nok = query_prod(item)
        if not cn == "a":
            writeToFile(flname, cn, ok, nok)
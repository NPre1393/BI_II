import re, os, json
from yaml import load, dump, load_all
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def query_orderproc(stream):
    prod_count = 0
    prods = []
    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                    if 'list' in item['event'].keys():
                        if item['event']['list']['data_receiver'][0]['name'] == 'url':
                            #print(str(item['event']['list']['data_receiver'][0]['data']))
                            nr_str = str(item['event']['list']['data_receiver'][0]['data'])
                            nr = nr_str.split('/')[5]
                            prod_count += 1
                            prods.append(nr)
    return(prods)

def query_proc(stream):
    proc_vx = {}

    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                    if 'list' in item['event'].keys():
                        if item['event']['list']['data_receiver'][0]['name'] == 'dataelements':
                            nr = item['event']['list']['data_receiver'][0]['data']['CPEE-INSTANCE'].split('/')[5]
                            if item['event']['trace:id'] in proc_vx.keys():
                                #proc_vx[item['event']['trace:id']].append(item['event']['list']['data_receiver'][0]['data']['CPEE-INSTANCE'])
                                proc_vx[item['event']['trace:id']].append(nr)
                            else:
                                proc_vx[item['event']['trace:id']] = nr
    #print(proc_vx)
    return(proc_vx)


def query_main(filename):
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
        return(query_proc(docs), 'p')
    if file_type == 'GV12 Turn Production':
        return(query_proc(docs), 't')
    if file_type == 'GV12 Order Processing':
        return(query_orderproc(docs), 'o')

    return({},'a')

root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/"
procs = {}
turn_procs = {}
order_proc = []
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        file_size = os.path.getsize(dirName+'/'+fname)
        if not file_size > 10000000:
            item = open(dirName+'/'+fname, 'r')
            
            process,identifier = query_main(item)
            if process:
                if identifier == 'p':
                    #procs.append(process)
                    procs.update(process)
                elif identifier == 't':
                    #turn_procs.append(process)
                    turn_procs.update(process)
                elif identifier == 'o':
                    order_proc.append(process)

print(order_proc)
#print(procs)
#print(turn_procs)

d1 = {int(k):int(v) for k,v in procs.items()}
d2 = {int(k):int(v) for k,v in turn_procs.items()}
procs2 = {}
turn_procs2 = {}

for key in sorted(d1.keys()):
    procs2[key] = d1[key]

for key in sorted(d2.keys()):
    turn_procs2[key] = d2[key]

print(procs2)
print(turn_procs2)

for item in procs2.keys():
    if not str(item) in order_proc[0]:
        print(item)

#order_proc = open('/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/5046b379-757d-44ea-8bcd-3f24023bff5c.xes.yaml', 'r')
#gv12_prod = open('/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/0bd12865-0d40-4a22-bc6f-b16510787d7f.xes.yaml', 'r')

#docs = load_all(order_proc)
#prod_count, prods = query_orderproc(docs)
#gv12_docs = load_all(gv12_prod)
#query_proc(gv12_docs)
#print(prod_count)
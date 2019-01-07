import re, os, json
from collections import OrderedDict
from yaml import load, dump, load_all

"""
# for production files

def writeToFile(fname, dict_to_write):
    with open(fname, 'a') as file:
        file.write('\n')
        for key, val in dict_to_write.items():
            file.write('{0};'.format(key))
            for elem in val:
                if type(elem) == dict:
                    file.write('{0};{1};'.format(elem[list(elem.keys())[0]][0],elem[list(elem.keys())[0]][1]))
                else:
                    file.write('{0};'.format(elem))
    with open(fname, 'rb+') as file:
        file.seek(-1, os.SEEK_END)
        file.truncate()          
"""
def writeToFile(fname, dict_to_write):
    with open(fname, 'a') as file:
        file.write('\n')
        for key, val in dict_to_write.items():
            if len(val[0]) != 29:
                val[0] = val[0][0:19]+'.000'+val[0][19:len(val[0])]
            if len(val[1]) != 29:
                val[1] = val[1][0:19]+'.000'+val[1][19:len(val[1])]
            file.write('{0};{1};{2}'.format(key, val[0], val[1]))

def query_orderproc(stream):
    prod_count = 0
    prods = []
    qrs = []
    queue = []
    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                    if 'list' in item['event'].keys():
                        if item['event']['list']['data_receiver'][0]['name'] == 'url':
                            #print(str(item['event']['list']['data_receiver'][0]['data']))
                            nr_str = str(item['event']['list']['data_receiver'][0]['data'])
                            nr = int(nr_str.split('/')[5])
                            prod_count += 1
                            prods.append(nr)
                if item['event']['cpee:lifecycle:transition'] == 'activity/calling':
                    if item['event']['id:id'] == 'a2':
                        if 'list' in item['event'].keys():
                            if 'data_send' in item['event']['list'].keys():
                                qrs.append(int(item['event']['list']['data_send'][3]['value'][26:29]))
                                queue.append(json.loads(item['event']['list']['data_send'][3]['value'])['queue'])
    return(prods, qrs, queue)

def query_prod(stream):

    qc1 = {}
    qc2 = {}
    qr_status = {}
    qc = []
    query_prods = {}
    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['id:id'] == 'a3':
                    #print(item['event']['cpee:uuid'])
                    if item['event']['cpee:lifecycle:transition'] == 'dataelements/change':
                        if 'list' in item['event'].keys():
                            if item['event']['list']['data_changer'][0] == 'qc2': 
                                if 'qc1' in item['event']['list']['data_values'].keys():
                                    qc1 = item['event']['list']['data_values']['qc1']
                                    qc2 = item['event']['list']['data_values']['qc2']
                                    qr_status[item['event']['list']['data_values']['queue']] = [item['event']['list']['data_values']['qr'][-3:],item['event']['list']['data_values']['status']]
                                else: 
                                    return("")
    #print(qc1)                 
    #print(qr_status)
    if qr_status:
        qr_status[list(qr_status.keys())[0]].append("NULL")
    

        for item in qc1:
            if list(item.keys())[0] == 'comment':
                qr_status[list(qr_status.keys())[0]][2] = item[list(item.keys())[0]]
            else:
                qr_status[list(qr_status.keys())[0]].append(float([x for x in item.values()][0]))

        meas_dict = {}

        if type(qc2) == dict:
            for item in qc2.keys():
                for key in qc2[item].keys():
                    meas_dict = {}
                    meas_dict[item+key] = []
                    meas_dict[item+key].append(qc2[item][key]['status'])
                    meas_dict[item+key].append(qc2[item][key]['on_scale_from_zero_to_one'])
                    qr_status[list(qr_status.keys())[0]].append(meas_dict)
                
            #print(item+key, qc2[item][key]['status'], qc2[item][key]['on_scale_from_zero_to_one'])

    return(qr_status) 

def query_turn_prod(stream):
    turn_prod = {}
    timestamp = ""
    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['id:id'] == 'a1':
                    if item['event']['cpee:lifecycle:transition'] == 'activity/calling':
                        if 'list' in item['event'].keys():
                            turn_prod[json.loads(item['event']['list']['data_send'][3]['value'])['queue']] = [item['event']['time:timestamp']]
                    if item['event']['cpee:lifecycle:transition'] == 'activity/done':
                        if turn_prod.keys():
                            key = list(turn_prod.keys())[0]
                            turn_prod[key].append(item['event']['time:timestamp'])
    return(turn_prod)

def query_machining(stream):
    operations = OrderedDict()
    operations_counter = 0
    queue_id = []
    prog_block = ""
    counter = 1
    act_blocks = {}
    for item in stream:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t=='event':
                if item['event']['id:id'] == 'a1':
                    if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                        if 'list' in item['event'].keys():
                            if item['event']['list']['data_receiver'][0]['data']: 
                                if item['event']['list']['data_receiver'][0]['data'][0]['name'] == 'Program/actBlock':
                                    prog_block = item['event']['list']['data_receiver'][0]['data'][0]['value']
                                    operations[prog_block] = []
                                else:
                                    prog_block = counter
                                    operations[prog_block] = []
                                    counter += 1
                                for op in item['event']['list']['data_receiver'][0]['data']:
                                    operations[prog_block].append((op['name'], op['value'], op['timestamp']))
                                    operations_counter += 1
                                    if op['name'] in act_blocks.keys():
                                        act_blocks[op['name']] += 1
                                    else:
                                        act_blocks[op['name']] = 1
                if item['event']['id:id'] == 'external':
                    if item['event']['cpee:lifecycle:transition'] == 'dataelements/change':
                        if 'list' in item['event'].keys():
                            if 'data_values' in item['event']['list']:
                                if item['event']['list']['data_values']['queue']:
                                    queue_id.append(item['event']['list']['data_values']['queue'])
                                    queue_id.append(item['event']['trace:id'])
    return(queue_id, operations, operations_counter, act_blocks)

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
                uuid = item['log']['trace']['cpee:uuid']
        break

    prods = ""
    qrs = ""
    queue = ""
    acts = ""

    #if file_type == 'GV12 Order Processing':
    #    prods, qrs, queue = query_orderproc(docs)
    #if file_type == 'GV12 Production':
    #    prods = query_prod(docs)
    if file_type == 'GV12 Turn Production':
        prods = query_turn_prod(docs)

    #if file_type == 'GV12 Turn Machining':
    #    queue, prods, qrs, acts = query_machining(docs)
        #print(prods.keys())
    
    return(prods)

root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/"
#prod_measures = "prod_measurements2.csv"
mach_ts = "machining_times_c.csv"
production = {}
machining = {}
production_vx = {}
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        file_size = os.path.getsize(dirName+'/'+fname)
        item = open(dirName+'/'+fname, 'r')    
        prods= query_main(item)
        
        if prods:
            writeToFile(mach_ts, prods)



#prod_file = "Output_prod.csv"
#prodvx_file = "Output_prodvx.csv"
#mach_file = "Output_mach.csv"


#writeToFile(prod_file, production)
#writeToFile(prodvx_file, production_vx)
#writeToFile(mach_file, machining)

#prods, qrs, queue = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/5046b379-757d-44ea-8bcd-3f24023bff5c.xes.yaml", "r"))
#prod_qrs = list(zip(prods,qrs))
#print(prod_qrs)
#qr_prods = dict(zip(queue,prod_qrs))
#print(qr_prods)
#p,q,r,s= query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/0edda924-f913-4cf9-9f78-cec7ff64c3a7.xes.yaml","r"))
#print(p)
#p, q, qu = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/0b71f47d-ed2e-45e2-9530-02b68e89be60.xes.yaml", "r"))
#p1, q1, qu1, acts1 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/1e9f5725-bb53-4d80-8da6-e14e84fd0540.xes.yaml", "r"))
#print(qr_prods[128], qr_prods[184], qr_prods[36], qr_prods[91])
#print(p)
#print(q)
#print(qu)
#print(len(p1['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
#p2, q2, qu2, acts2 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/1b998f05-e820-4418-bf2d-2a927b33595a.xes.yaml", "r"))
#print(len(p2['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
#p3, q3, qu3, acts3 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/9cd024b9-dba2-4676-bec7-fde13f294cf6.xes.yaml", "r"))
#print(len(p3['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
"""
TODO: union between each NC act/block
change tupels in machining to dicts or need postprocessing

"""
#print(acts1, acts2, acts3)
#print(q1, q2, q3)
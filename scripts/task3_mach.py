from yaml import load_all

def query_machining(stream, info):
    queue_id = []
    if type(info) == list:
        operations = {}
    else:
        operations = []
    for item in stream:
        for i, t in enumerate(item.keys()):
            if t == 'event':
                if item['event']['id:id'] == 'a1':
                    if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                        if 'list' in item['event'].keys():
                            if item['event']['list']['data_receiver'][0]['data']: 
                                for op in item['event']['list']['data_receiver'][0]['data']:
                                    if op['name'] == info:
                                        operations.append((op['value'], op['timestamp']))
                if item['event']['id:id'] == 'external':
                    if item['event']['cpee:lifecycle:transition'] == 'dataelements/change':
                        if 'list' in item['event'].keys():
                            if 'data_values' in item['event']['list']:
                                if item['event']['list']['data_values']['queue']:
                                    queue_id.append(item['event']['list']['data_values']['queue'])
                                    queue_id.append(item['event']['trace:id'])
    return(queue_id, operations)

def query_main(filename, info):
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

    if file_type == 'GV12 Turn Machining':
        queue, prods = query_machining(docs, info)
        #print(prods.keys())
    
    return(prods, queue)
"""
root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/"
prod_measures = "prod_measurements2.csv"
production = {}
machining = {}
production_vx = {}
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        file_size = os.path.getsize(dirName+'/'+fname)
        item = open(dirName+'/'+fname, 'r')    
        prods, qrs, queue, acts = query_main(item)
        
        if prods:
            machining[queue[0]] = len(prods['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9'])
            print(machining[queue[0]])
            #writeToFile(prod_measures, prods)

p1, q1, qu1, acts1 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/1e9f5725-bb53-4d80-8da6-e14e84fd0540.xes.yaml", "r"))
print(len(p1['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
p2, q2, qu2, acts2 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/1b998f05-e820-4418-bf2d-2a927b33595a.xes.yaml", "r"))
print(len(p2['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
p3, q3, qu3, acts3 = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/9cd024b9-dba2-4676-bec7-fde13f294cf6.xes.yaml", "r"))
print(len(p3['F_ROUGH("SCHLICHTER-A-L","",1,0.035,3,100,2,0,54274,5,19,90,0.1,9']))
"""
# speedOvr      6a93292c-262b-430e-bc48-4e75c08766b5.xes.yaml
# feedRateOvr   135d4313-6c7b-4da7-b334-9b065e4a667a.xes.yaml
#machining, queue = query_main(open("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/1e9f5725-bb53-4d80-8da6-e14e84fd0540.xes.yaml", "r"), 'State/actToolLength1')

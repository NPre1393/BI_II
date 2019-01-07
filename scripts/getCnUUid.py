import re, os, json
from yaml import load, dump, load_all
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

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

    return(concept_name, file_type, uuid)

root_dir = "/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/"
production = {}
machining = {}
production_vx = {}
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        file_size = os.path.getsize(dirName+'/'+fname)
        item = open(dirName+'/'+fname, 'r')    
        cn,ft,uuid = query_main(item)
        if ft == 'GV12 Turn Machining':
            machining[uuid] = [cn, ft]
        elif ft == 'GV12 Production':
            production[uuid] = [cn, ft]
        elif ft == 'GV12 Turn Production':
            production_vx[uuid] = [cn, ft]

print(production)
print(production_vx)
print(machining)

prod_file = "Output_prod.csv"
prodvx_file = "Output_prodvx.csv"
mach_file = "Output_mach.csv"

def writeToFile(fname, dict_to_write):
    with open(fname, 'a') as file:
        for key, val in dict_to_write.items():
            file.write('{0},{1},{2}\n'.format(key, val[0], val[1]))

#writeToFile(prod_file, production)
#writeToFile(prodvx_file, production_vx)
#writeToFile(mach_file, machining)
print(len(production))
print(len(production_vx))
print(len(machining))



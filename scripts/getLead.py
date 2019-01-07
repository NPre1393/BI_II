import re, os, json
from yaml import load, dump, load_all
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

#lead_file = ("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/22350aee-2bf0-42d7-94a0-bdc1b989538e.xes.yaml")
#lead_file = ("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A3/gv12/logs/parts/95f92a8a-5bc6-4772-ac7e-93380e1f05ab.xes.yaml")
lead_file = ("/home/hailegebressi/Documents/Uni/DataScience/Sem2/BIII/A1-2/assignments/lowerhousing/logs/production/part1/C/7395b0d4-8d4f-4136-ba37-baebd55f4161.xes.yaml")
def query_mach(stream):
    x_lead = []
    y_lead = []
    z_lead = []
    leadx = 0
    leady = 0
    leadz = 0

    docs = load_all(stream)
    for item in docs:
        itemKeys = item.keys()
        for i, t in enumerate(itemKeys):
            if t == 'event':
                if item['event']['cpee:lifecycle:transition'] == 'activity/receiving':
                    if 'list' in item['event'].keys():
                        if 'data_receiver' in item['event']['list'].keys():
                            if item['event']['list']['data_receiver'][0]['data']:
                                for it in item['event']['list']['data_receiver'][0]['data']:
                                    #act_name = item['event']['list']['data_receiver'][0]['data'][0]['name']
                                    if not type(it) == str:
                                        #print(it.keys())
                                        act_name = it['name']
                                        #act_val = item['event']['list']['data_receiver'][0]['data'][0]['value']
                                        act_val = it['value']
                                        if act_name == 'Axis/X/aaLeadP':
                                            leadx = act_val
                                            x_lead.append(float(act_val))
                                            y_lead.append(leady)
                                            z_lead.append(leadz)
                                        elif act_name == 'Axis/Y/aaLeadP':
                                            leady = act_val
                                            x_lead.append(leadx)
                                            y_lead.append(float(act_val))
                                            z_lead.append(leadz)
                                        elif act_name == 'Axis/Z/aaLeadP':
                                            leadz = act_val
                                            x_lead.append(leadx)
                                            z_lead.append(float(act_val))
                                            y_lead.append(leady)
    return(x_lead, y_lead, z_lead)

x, y, z = query_mach(open(lead_file,'r'))
print(len(x), len(y), len(z))
xs = np.array(x, dtype=float)
ys = np.array(y, dtype=float)
zs = np.array(z, dtype=float)

#mat = np.array((x,y,z), dtype=float)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)
plt.show()



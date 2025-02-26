import yaml

from datetime import datetime  
from yaml import SafeLoader
  
def datetime_constructor(loader, node):  
    value = loader.construct_scalar(node)  
    return datetime.strptime(value, '%Y-%m-%d')  
  
yaml.add_constructor('!datetime', datetime_constructor, Loader=SafeLoader)  

date_file='/nfs/home/yuanmiaomiao/TryPython/YAML/date.yaml'
with open(date_file, 'r') as file:  
    data = yaml.safe_load(file)  

print(data)
  

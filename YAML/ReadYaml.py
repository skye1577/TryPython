import yaml  

config_file='/nfs/home/yuanmiaomiao/TryPython/YAML/config.yaml'
  
with open(config_file, 'r') as file:  
    data = yaml.safe_load(file)  
  
print(data)  
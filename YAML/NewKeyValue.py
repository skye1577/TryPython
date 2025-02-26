import yaml  

config_file='/nfs/home/yuanmiaomiao/TryPython/YAML/config.yaml'

with open(config_file,"r") as file:
    data = yaml.safe_load(file)

print(data)



data['person']['hobbies'] = 'reading'
data['person']['job'] = 'engineer'
  
with open(config_file, 'w') as file:  
    yaml.safe_dump(data,file)  


print("DONE")  
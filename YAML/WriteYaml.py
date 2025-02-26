import yaml  

data = {  
    'name': 'Jane Doe',  
    'age': 28,  
    'skills': ['Python', 'Web Development', 'DevOps']  
}  

output_file='output.yaml'
  
with open(output_file, 'w') as file:  
    yaml.dump(data, file)  
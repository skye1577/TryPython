from mako.template import Template


input_info = 'hello'

t = Template(input_info)

data = t.render()

print(data)
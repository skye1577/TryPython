from mako.template import Template
import argparse


parser = argparse.ArgumentParser(description="Generate a C program template.")
parser.add_argument("--filename", required=True, help="Output filename")
parser.add_argument("--author", required=True, help="Author name")
parser.add_argument("--description", required=True, help="File description")

args = parser.parse_args()


# 渲染模板所需的变量
template_vars = {
    "filename": args.filename,
    "author":  args.author,
    "description": args.description,
    "info": "Successed"
}

# 模板文件路径
template_file = "c_template.mako"

# 加载模板
template = Template(filename=template_file)

# 渲染模板并生成 C 程序
output = template.render(**template_vars)

# 将生成的 C 程序写入文件
with open(template_vars["filename"], "w") as f:
    f.write(output)

print(f"Generated {template_vars['filename']} successfully!")

import os
from mako.template import Template

# 指定输出目录
output_dir = "/nfs/home/yuanmiaomiao/TryPython/Mako/alu_cmodel"
os.makedirs(output_dir, exist_ok=True)  # 创建目录（如果不存在）

# 定义要生成的文件列表
output_files = [
    {"filename": "and.c", "author": "xxx", "description": "Basic logic functions", "module_name": "and", "op": "&&", "data_type": "int"},
    {"filename": "or.c", "author": "xxx", "description": "Basic logic functions", "module_name": "or", "op": "||", "data_type": "int"},
    {"filename": "xor.c", "author": "xxx", "description": "Basic logic functions", "module_name": "xor", "op": "^", "data_type": "int"},
    {"filename": "int32_add.c", "author": "yyy", "description": "Basic integer functions", "module_name": "int32_add", "op": "+", "data_type": "int"},
    {"filename": "int32_sub.c", "author": "yyy", "description": "Basic integer functions", "module_name": "int32_sub", "op": "-", "data_type": "int"},
    {"filename": "int32_mul.c", "author": "yyy", "description": "Basic integer functions", "module_name": "int32_mul", "op": "*", "data_type": "int"},
    {"filename": "int32_div.c", "author": "yyy", "description": "Basic integer functions", "module_name": "int32_div", "op": "/", "data_type": "int"},
    {"filename": "fp32_add.c", "author": "zzz", "description": "Basic single-precision float-point functions", "module_name": "fp32_add", "op": "+", "data_type": "float"},
    {"filename": "fp32_sub.c", "author": "zzz", "description": "Basic single-precision float-point functions", "module_name": "fp32_sub", "op": "-", "data_type": "float"},
    {"filename": "fp32_mul.c", "author": "zzz", "description": "Basic single-precision float-point functions", "module_name": "fp32_mul", "op": "*", "data_type": "float"},
    {"filename": "fp32_div.c", "author": "zzz", "description": "Basic single-precision float-point functions", "module_name": "fp32_div", "op": "/", "data_type": "float"},
]


# 模板文件路径
module_template_file='/nfs/home/yuanmiaomiao/TryPython/Mako/template/alu_template.mako'
main_template_file='/nfs/home/yuanmiaomiao/TryPython/Mako/template/main_template.mako'

# 加载模板
module_template = Template(filename=module_template_file)
main_template = Template(filename=main_template_file)

# 生成模块文件
for file in output_files:
    output_path = os.path.join(output_dir, file["filename"])
    output = module_template.render(**file)
    with open(output_path, "w") as f:
        f.write(output)
    print(f"Generated {file['filename']} successfully!")

# 生成主函数文件
main_output_path = os.path.join(output_dir, "main.c")
main_output = main_template.render(output_files=output_files, output_dir=output_dir, os=os)
with open(main_output_path, "w") as f:
    f.write(main_output)
print("Generated main.c successfully!")
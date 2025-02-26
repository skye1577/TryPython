# 定义变量
PYTHON = python3
GCC = gcc
CFLAGS = -Wall -Wextra -std=c99
OUTPUT_DIR = /nfs/home/yuanmiaomiao/TryPython/Mako/alu_cmodel
GENERATED_FILES = $(wildcard ${OUTPUT_DIR}/*.c)
EXECUTABLES = $(patsubst ${OUTPUT_DIR}/%.c, %, ${GENERATED_FILES})

GENERATE_PYTHON = generate_alu.py
MAIN_FILE = main.c

# 默认目标：生成、编译并运行所有 C 程序
all: generate build run

# 生成所有的 C 程序
generate:
	@echo "Generating C programs..."
	${PYTHON} ${GENERATE_PYTHON}
	@echo "C programs generated successfully!"


# 编译所有生成的 C 程序
build: ${GENERATED_FILES}
	@echo "Compiling C programs..."
	@for file in ${GENERATED_FILES}; do \
		output=$$(basename $$file .c); \
		${GCC} ${CFLAGS} -o ${OUTPUT_DIR}/$$output $$file; \
		echo "Compiled $$file to ${OUTPUT_DIR}/$$output"; \
	done
	@echo "C programs compiled successfully!"

# 生成调用主函数
compile_main: 
	@echo "Compiling C programs..."
	${GCC} ${OUTPUT_DIR}/${MAIN_FILE} -o main; \
	@echo "C main programs compiled successfully!"

# 执行所有生成的 C 程序
run: ${EXECUTABLES}
	@echo "Running C programs..."
	@for exe in ${EXECUTABLES}; do \
		echo "Running ${OUTPUT_DIR}/$$exe..."; \
		${OUTPUT_DIR}/$$exe; \
	done

# 清理生成的文件和可执行文件
clean:
	@echo "Cleaning up..."
	rm -rf ${OUTPUT_DIR}
	@echo "Cleanup complete!"

# 防止与文件名冲突
.PHONY: all generate build run clean
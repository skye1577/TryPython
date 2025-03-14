/*
 * File: main.c
 * Author: Generated by Mako
 * Description: Main function to call all ALU operations
 */

#include <stdio.h>

// Include all generated module headers
% for file in output_files:
#include "${os.path.abspath(os.path.join(output_dir, file['filename']))}"
% endfor

int main() {
    // Test data
    int int_src1 = 10, int_src2 = 5;
    float float_src1 = 10.5, float_src2 = 5.5;

    // Call all ALU functions
    % for file in output_files:
    printf("${file['module_name']}: ");
    % if file['data_type'] == 'int':
    printf("%d\n", ${file['module_name']}(int_src1, int_src2));
    % else:
    printf("%f\n", ${file['module_name']}(float_src1, float_src2));
    % endif
    % endfor

    return 0;
}
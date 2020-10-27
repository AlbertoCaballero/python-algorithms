import os

# Compile a C o C++ file and rename to samename.cgi
def compileAndRename(f):
    # Check file extension and compile
    if f.endswith('.c'):
        os.system('gcc ' + f)
        os.system('mv a.out ' + f.replace('c', 'cgi'))
    elif f.endswith('.cpp'):
        os.system('g++ ' + f)
        os.system('mv a.out ' + f.replace('cpp', 'cgi'))
    

# List of file in current directory
dir = os.listdir()
# Print the array
print(dir, '\n')

# For every file in directory
for f in dir:
    compileAndRename(f)

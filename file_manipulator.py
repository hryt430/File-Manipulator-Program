import sys
import os

# 関数を定義する
def reverse_inputfile(input_path, output_path):
    with open(input_path) as f:
        contents = f.read()
        reverse_contents = contents[::-1]
    
    with open(output_path, "x") as f:
        f.write(reverse_contents)
    
def copy_inputfile(input_path, output_path):
    with open(input_path) as f:
        contents = f.read()
    
    with open(output_path, "w") as f:
        f.write(contents)

def duplicate_inputfile(input_path, n):
    with open(input_path) as f:
        contents = f.read()
        duplicate_contents = contents * int(n)
    
    with open(input_path, "a") as f:
        f.write(duplicate_contents)

def replace_inputfile(input_path, needle, newString):
    with open(input_path) as f:
        contents = f.read()
        replace_contents = contents.replace(needle, newString)
    
    with open(input_path ,"w") as f:
        f.write(replace_contents)

# パラメーターが正しいか確かめて返す
def validate_data(argv):
    if len(argv) < 2:
        print("Invalid argument: function is required")
        return False

    function = argv[1]
    
    if function == "reverse" or function == "copy":
        if len(argv) != 4:
            print(f"Invalid argument: {function} requires 2 arguments")
            return False
        input_path, output_path = argv[2], argv[3]
        if not os.path.exists(input_path):
            print("Invalid argument: Input path does not exist")
            return False
        else:
            return (input_path, output_path)

    elif function == "duplicate":
        if len(argv) != 4:
            print(f"Invalid argument: {function} requires 2 arguments")
            return False
        input_path, duplicate_number = argv[2], argv[3]
        if int(duplicate_number) < 0:
            print("Invalid argument: Negative number is not allowed")
            return False
        if not os.path.exists(input_path) or not duplicate_number.isdigit():
            print("Invalid argument: Input path does not exit or int argumet is required")
            return False
        else:
            return (input_path, int(duplicate_number))
    
    elif function == "replace":
        if len(argv) != 5:
            print(f"Invalid argument: {function} requires 3 arguments")
            return False
        input_path, needle, newString = argv[2], argv[3], argv[4]
        if not os.path.exists(input_path):
            print("Invalid argument: Input path does not exist")
            return False
        else:
            return (input_path, needle, newString)
    else:
        print(f"Invalid argument: {function} does not exist")
        return False

# 関数を辞書型で管理
functions = {
    "reverse": reverse_inputfile,
    "copy": copy_inputfile,
    "duplicate": duplicate_inputfile,
    "replace": replace_inputfile
}

def main():
    argv = sys.argv

    params = validate_data(argv)
    if params:
        func = argv[1]
        functions[func](*params)

if __name__ == "__main__":
    main()
    
        
    

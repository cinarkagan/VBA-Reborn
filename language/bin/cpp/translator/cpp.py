import sys
import os

def translate_line(line):
    line = line.strip()
    if line.startswith("'"):
        line = ""
    elif line.startswith("Dim "):
        line = line.replace("Dim ","")
        line = "std::string "+line+";"
    elif line.startswith("Set "):
        line = line.replace("Set ","")
        line = line.split()
        varName = line[0]
        varVal = line[2]
        line = varName+" = "+varVal+";"
    elif line.startswith("Echo "):
        line = line.replace("Echo ","")
        if line.endswith(" as Dim"):
            line = line.replace(" as Dim","")
            line = "std::cout << "+line+" << std::endl;"
        else:
            line = "std::cout << "+line+" << std::endl;"
    return line+"\n"

def translate(path):
    vbf = open(path,'r')
    cppf = open("temp.cpp","w")
    cppf.write("#include <iostream>\n")
    cppf.write("int main(){\n")
    for line in vbf:
        line = translate_line(line)
        cppf.write(line)
    cppf.write("return 0;\n")
    cppf.write("}\n")

if len(sys.argv) == 2:
    path = sys.argv[1]
    translate(path)
    os.system("g++ temp.cpp")
    os.system('del /f "temp.cpp"')

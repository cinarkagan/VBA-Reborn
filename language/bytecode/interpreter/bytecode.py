import base64
import sys

variables = []

def decompile_file(filename):
    file = open(filename,"r")
    o = open("temp.vb","w")
    for i in file:
        i=i.strip()
        i_b1 = i.encode("ascii")
        i_base64_1 = base64.b64encode(i_b1)
        i_bytes = i_base64_1.decode("ascii")
        o.write(i+"\n")

def parse_line(line):
    line = line.strip()
    #Commenting
    if line.startswith("'"):
        pass
    else:
        # Echo Function
        if line.startswith("Echo "):
            line = line.replace("Echo ","")
            text_to_echo = ""
            if line.endswith(" as Dim"):
                line = line.replace(" as Dim","")
                text_to_echo = variables[line]
            else:
                text_to_echo = line
            print(text_to_echo)
        # Dim
        if line.startswith("Dim "):
            line = line.replace("Dim ","")
            var_to_def = line
            variables[var_to_def] = ""
        if line.startswith("Set "):
            line = line.replace("Set ","")
            line = line.split()
            varName = line[0]
            varVal = line[2]
            # line[1] == '='
            variables[varName] = varVal
     


if len(sys.argv) == 2:
    decompile_file(sys.argv[1])
    f = open("temp.vb")
    for line in f:
        parse_line(line)
    os.system('del /f "temp.vb"')
import base64
import sys
def decompilee_file(filename):
    file = open(filename,"r")
    o = open("decompiled.vbc","w")
    for i in file:
        i=i.strip()
        i_b1 = i.encode("ascii")
        i_base64_1 = base64.b64encode(i_b1)
        i_bytes = i_base64_1.decode("ascii")
        o.write(i+"\n")

if len(sys.argv) == 2:
    decompile_file(sys.argv[1])
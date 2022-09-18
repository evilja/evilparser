import os,json

class crystal:
    def __init__(self) -> "Create Crystal Object":
        config = {

                }
        _DIDYOUMEAN_HARDNESS = 5
        self._DIDYOUMEAN_HARDNESS = _DIDYOUMEAN_HARDNESS
        self.config = config
    def syntax(self) -> "Syntax of Parser, Used by Parser Version Changer":
        createVar = "vex type name;\n"
        createVal = "spec value;\n"
        return [createVar, createVal]
    def remove(self, path:"Path to eparse file", vexName:"Name of the variable to remove") -> None: 
        with open(path, mode="r", encoding='utf-8') as f:
            lines = f.readlines()
        with open(path, mode="w", encoding='utf-8') as f:
            inVex = False
            popno = 0
            for line in lines:
                if "vex" in line and vexName in line:
                    inVex = True
                    lines.pop(popno)
                    popno += 1
                    continue
                if inVex and line.startswith("vex "):
                    inVex = False
                if inVex:
                    lines.pop(popno)
                popno += 1
    def didyoumean(self, typeofvar):
        typesofvar =  ["int","integer","float","double","String","char*", "bool", "boolean", "char[]","char[]*","char*[]","int[]","int[]*","int*[]","float[]","float[]*","float*[]","bool[]","bool[]*","bool*[]","void","void(*)","json","jsob","json*","dict"]
        print("Could not find variable type \033[0;31m" + typeofvar + "\033[0m")
        g_01 = typesofvar
        typeofvar = typeofvar.lower()
        for i in range(self._DIDYOUMEAN_HARDNESS):
            for letter in typeofvar:
                for x in g_01:
                    if not letter in x:
                        g_01.remove(x)
        if len(g_01) == 0:
            exit()
        print("\033[1;33mDid you mean one of these\033[0m: " , end="")
        fp = 0
        for g in g_01:
            fp += 1
            if fp == 1 and not len(g_01) == 1:
                g = "\033[32m" + g + "\033[0m"
            elif g_01.index(g) + 1 == len(g_01):
                if len(g_01) == 1:
                    g = "\033[32m" +g + "\033[0m?\n"
                else:
                    g = " \033[0mor \033[32m" + g + "\033[0m?\n"
            else:
                g = "\033[0m, \033[32m" + g
            print(g, end="")
        exit()

    def add(self,configfile:"Path to eparse file",nameOfVar:"Variable name to add",typeofVar:"Variable type to add",valueOfVar:"Variable value to add") -> None:
        vartypes =  ["int","integer","float","double","String","char*", "bool", "boolean", "char[]","char[]*","char*[]","int[]","int[]*","int*[]","float[]","float[]*","float*[]","bool[]","bool[]*","bool*[]","void","void(*)","json","jsob","json*","dict"]
        if typeofVar not in vartypes:
            self.didyoumean(typeofVar)
        with open(configfile, mode="a+", encoding='utf-8') as f:
            f.write("vex " + typeofVar + " " + nameOfVar + ";\n")
            if type(valueOfVar) == list:
                for x in valueOfVar:
                    f.write("spec " + str(x) + ";\n")
            else:
                f.write("spec " + str(valueOfVar) + ";\n")
    def get(self, path:"Path to eparse file") -> None:
        if not os.path.exists(path):
            raise Exception("Path does not exist")
        with open(path, mode="r", encoding='utf-8') as f:
            lines = f.readlines()
        currentname = "NOTKNOWNYET"
        currentsituation = "NOTKNOWNYET"
        for line in lines:
            line = line.strip()
            if line.startswith("//") or line == "":
                continue
            if line.startswith("vex "):
                if not line.endswith(";"):
                    print("at " + path)
                    print("at " + line,end=" ")
                    print(lines.index(line + "\n"))
                    print("; excepted but not found")
                    raise Exception("; expected but not found")
                currentname = line.split(" ")[2].replace(";","")
                currentvartype = line.split(" ")[1]
                if currentvartype in ["int","integer"]:
                    currentsituation = "int"
                elif currentvartype in ["float","double"]:
                    currentsituation = "float"
                elif currentvartype in ["String","char*"]:
                    currentsituation = "string"
                elif currentvartype in ["bool","boolean"]:
                    currentsituation = "bool"
                elif currentvartype in ["char[]","char[]*","char*[]"]:
                    self.config[currentname] = []
                    currentsituation = "chararray"
                elif currentvartype in ["int[]","int[]*","int*[]"]:
                    self.config[currentname] = []
                    currentsituation = "intarray"
                elif currentvartype in ["float[]","float[]*","float*[]"]:
                    self.config[currentname] = []
                    currentsituation = "floatarray"
                elif currentvartype in ["bool[]","bool[]*","bool*[]"]:
                    self.config[currentname] = []
                    currentsituation = "boolarray"
                elif currentvartype in ["void","void(*)"]:
                    currentsituation = "void"
                elif currentvartype in ["json","jsob","json*","dict"]:
                    self.config[currentname] = {}
                    currentsituation = "json"
                else:
                    print("at " + path)
                    print("at " + line,end=" ")
                    print("line " + str(lines.index(line + "\n")))
                    self.didyoumean(currentvartype) 
                continue
            if currentsituation == "NOTKNOWNYET":
                continue
            if not line.startswith("spec"):
                print("at " + path)
                print("at " + line,end=" ")
                print(lines.index(line + "\n"))
                print("type expected but not given")
            if currentsituation == "int":
                self.config[currentname] = int(line[5:].replace(";",""))
            elif currentsituation == "float":
                self.config[currentname] = float(line[5:].replace(";",""))
            elif currentsituation == "string":
                self.config[currentname] = line[5:].replace(";","")
            elif currentsituation == "bool":
                self.config[currentname] = bool(line[5:].replace(";",""))
            elif currentsituation == "json":
                self.config[currentname] = json.loads(line[5:].replace(";",""))
            elif currentsituation == "chararray":
                self.config[currentname].append(line[5:].replace(";",""))
            elif currentsituation == "intarray":
                self.config[currentname].append(int(line[5:].replace(";","")))
            elif currentsituation == "floatarray":
                self.config[currentname].append(float(line[5:].replace(";","")))
            elif currentsituation == "boolarray":
                self.config[currentname].append(bool(line[5:].replace(";","")))
            elif currentsituation == "void":
                self.config[currentname] = None
            else:
                print("at " + path)
                print("at " + line,end=" ")
                print(lines.index(line + "\n"))
                print("unknown situation")
                raise Exception("unknown situation")
        return self.config
    def getVar(self, path:"Path to eparse file", varname:"Name of the variable to get") -> "Variable":
        self.get(path)
        return self.config[varname]

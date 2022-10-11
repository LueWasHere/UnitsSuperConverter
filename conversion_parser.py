from typing import final


def parse(parsse, hctd_src, aliases): # hctd stands for hyper conversion text document. see conversions.hctd
    parsse = parsse.split(' ')
    unit = ""
    to = ""
    amount = ""
    try:
        amount = int(parsse[0])
    except:
        return "Fail. Enter a number. Conversion structure: [amount of units] [initial unit] [new, converted unit]"
    try:
        unit = parsse[1]
        to = parsse[2]
    except:
        return "Fail. Conversion structure: [amount of units] [initial unit] [new, converted unit]"

    # for i in range()

    abstract = ["sub", "add", "mul", "div"] # Why do we use words instead of symbols in the .hctd file? readablity, and also universiality when getting custom units from users on telegram
    rep = ["-", "+", "*", "/"]
    i =0
    while i != len(hctd_src)-1:
        print(i)
        try:
            if to == hctd_src[i][1] and unit == hctd_src[i][0]:
                break
            else:
                i += 1
            try:
                print(f"{aliases[unit}]")
                
            except:
                pass
        except:
            i += 1
    if i == len(hctd_src)-1:
        return f'Cannot convert between {unit} and {to}'
    print(i)
    print(to)
    print(unit)
    build_expression = ""
    expressions = []
    num = None
    for z in range(2, len(hctd_src[i])):
        print(hctd_src[i][z])
        try:
            num = int(hctd_src[i][z])
        except:
            num = None
        try:
            print(hctd_src[i][z])
            if hctd_src[i][z] == unit:
                build_expression += str(amount)
            elif hctd_src[i][z] == to:
                raise ValueError("Error while parsing hctd, cannot use the conversion unit in a hctd expression") # Better name: 'error: you can't convert to the same unit!'
            elif num != None:
                build_expression += str(num)
            elif hctd_src[i][z] in abstract:
                build_expression += rep[abstract.index(hctd_src[i][z])]
            elif hctd_src[i][z][len(hctd_src[i][z])-1] == ",":
                build_expression += hctd_src[i][z][0:len(hctd_src[i][z])-1]
                expressions.append(build_expression)
                build_expression = ""
            elif hctd_src[i][z] == "result":
                pass
        except:
            pass
    print(expressions)
    final_expression = "(" * len(expressions)
    for i in range(0, len(expressions)):
        final_expression += f"{expressions[i]})"
    print(final_expression)
    return str(eval(final_expression)) + " " + to

def parse_hctd(parsse):
    print("PARSING")
    keep = parsse.split('\n')
    parsse = []
    comment = False
    def_alias = False
    build = ""
    i = 0
    aliases = {}
    
    while i != len(keep):
        for j in range(0, len(keep[i])):
            if keep[i][j] == '#':
                comment = True
            elif keep[i][j]+keep[i][j+1] == "*_":
                def_alias = True
            if comment == False:
                build += keep[i][j]
        comment = False
        def_alias = False
        parsse.append(build)
        build = ""
        i += 1
    for i in range(0, len(parsse)):
        parsse[i] = parsse[i].split(" ")
    print(f"END: {parsse}")
    return [parsse, aliases]

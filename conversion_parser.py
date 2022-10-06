def parse(parsse, hctd_src):
    parsse = parsse.split(' ')
    unit = ""
    to = ""
    amount = ""
    try:
        amount = int(parsse[0])
    except:
        return "Fail, Enter a number. Conversion structure: [amount of units] [unit to convert] [unit to convert to]"
    try:
        unit = parsse[1]
        to = parsse[2]
    except:
        return "Fail. Conversion structure: [amount of units] [unit to convert] [unit to convert to]"
    
    #for i in range()

    abstract = ["sub", "add", "mul", "div"]
    rep = ["-", "+", "*", "/"]
    return f"{amount}{rep}"
    
def parse_hctd(parsse):
    parsse = parsse.split('\n')
    for i in range(0, len(parsse)):
        parsse[i] = parsse[i].split(" ")
    for i in range(0, len(parsse)):
        try:
            if parsse[i][0] == '#':
                parsse.remove(parsse[i])
        except:
            print(f"Err in {parsse}")
    return parsse
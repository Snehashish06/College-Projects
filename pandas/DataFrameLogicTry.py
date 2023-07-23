def create_dataframe(FrameObject: dict):
    vals = FrameObject.values()
    if type(FrameObject) != dict:
        return "Only dictionary is acceptable"
    jk = 0
    for i in vals:
        if type(i) != list:
            return "Forbidden"
        elif jk == 1:
             return "Currently under development can't evaluate more than 1 column."
        jk += 1

    for k in FrameObject.keys():
            print(f"\t{k if k != None else ' '}", end = '\t')
    print()
    ip = 0
    for i in vals:
        pp = 0
        for kj in i:
            if ip == 0:
                print(f"{pp}\t{kj}\t")
            else:
                 print(f"{pp}\t\t{kj}\t")
        #print(f"{i}\n")
            pp += 1
        ip += 1
    return ""


if __name__ == "__main__":
    df = {
        "Hello": ["World", "Bye", "TC"]
    }
    print(create_dataframe(df))

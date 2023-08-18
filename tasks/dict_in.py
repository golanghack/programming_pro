def condense_csv(filename, id_name):
    list_names = []
    d = {}
    with open(filename, encoding='UTF-8') as f:
        text = csv.reader(f)
        for i in text:
            c1,c2,c3 = i
            if c1 not in d.values() and d:
                print(d)
                list_names.append(d)     
            d[id_name] = c1
            d[c2] = c3
        print(d,list_names)
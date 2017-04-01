def compiler(liste_val,str_obj):

    result = ""

    for idx, v in enumerate(liste_val):

        result = obj +  liste_val[idx]

    return  result


def loop_object(liste_val,str_obj):

    result = ""
    for idx, v in enumerate(liste_val):
        result += str_obj.replace("~",v) +'\n'
    return  result


def loop_values(liste_val,str_obj):

    lst_obj = list(str_obj)
    n=0
    for idx, c in enumerate(lst_obj):
        if c == '~':
            lst_obj[idx] = liste_val[n]
            n +=1
        if c == "\t":
            lst_obj[idx] = ''

    return  ''.join(lst_obj)

# @File    : newcolname.py


def Columnlabel(cols):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if cols <= 26:
        return letter_list[:cols]
    else:
        lis = letter_list
        k = 26
        for i in letter_list:
            for j in letter_list:
                if k < cols:
                    lis.append(i + j)
                    k += 1
                else:
                    return lis

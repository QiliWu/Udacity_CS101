def rotate(string,n):
    newlet=''
    for let in string:
        if let!=' ':
            newlet=newlet + shift_n_letters(let,n)
        else:
            newlet=newlet + let
    return newlet

def shift_n_letters(letter,n):
    s=ord(letter)+n
    if s<=ord('z') and s>=ord('a'):
        return chr(s)
    if s<ord('a'):
        return chr(ord('z')-(ord('a')-s-1))
    return chr(ord('a')+(s-ord('z')-1))

print shift_n_letters('s', 13)

print rotate('sarah',13)
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)

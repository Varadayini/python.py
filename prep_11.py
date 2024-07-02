def replace_char(input_str,chr1,chr2):
    res=''
    if input_str!=None:
        res=input_str.replace(chr1,'*').replace(chr2,chr1).replace('*',chr2)
        return res
    return 'Null'
input_str=input("enter the string:")    
chr1,chr2=map(str,input("enter the two char:").split())
print(replace_char(input_str,chr1,chr2))

    
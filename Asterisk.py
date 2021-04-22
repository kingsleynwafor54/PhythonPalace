def aFunc(fixedParam,*tupleParam):
    print("fixed=", fixedParam)
    print("tuple=", tupleParam)
    return fixedParam,tupleParam

print(aFunc((1,2,3,4),1,2,3,4,5,6,7,8,9))
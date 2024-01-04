def exception_test(val1, val2):

    value =0
 
    try:
        value = val1 + val2
    except:
        print("error")
        raise
    finally:
        print("end")
    
    return value


try:
    print(exception_test(100,"aaa"))
except:
    print("ERROR")

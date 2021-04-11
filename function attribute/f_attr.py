# In python you can access to  some variables in function even if the function doesn't return it
# We can set attributes in functions like what we do in classes
# These variables can be initiated inside and outside the function


def sample_func(x):
    if x % 2 == 0:
        sample_func.return_message = "Even Number"
    else:
        sample_func.return_message = "Odd Number"
    
    #attribute definition inside the function
    sample_func.greeding = "Welcome to the desert of real"
    return sample_func.return_message
    
    
if __name__ == "__main__":
    ret = sample_func(2)
    print(ret)
    
    # accessing function attribute outside the function
    print(sample_func.greeding)
    
    # attribute definition outside the function
    sample_func.whereami = "Earth"
    print(sample_func.whereami)




#digit checker
def passdigitchecker():
    digits = ("1", "2", "3","4", "5","6","7","8","9", "0")
    x = True
    while x ==True:
        password = str(input("please enter a password"))
        for char in password:
            if char in digits:
                print("your password is:", password)
                return
        if char not in digits:
            print("please make sure you have a digit in your password")
        
               
def passsymbolchecker():
    symbols = "!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`"
    x = True
    while x ==True:
        password = str(input("please enter a password"))
        for char in password:
            if char in digits:
                print("your password is:", password)
                return
        if char not in digits:
            print("please make sure you have a digit in your password")
               
        
passdigitchecker()
passsymbolchecker()
print("thanks for using the password checker")


        
     









    


    








  


def Account_type(type):
    if type=="saving":
        return("correct")
    else:
        return"invalid Account"
print(Account_type("saving"))
def language_in():
    if language=="hindi""english":
        return("correct language") 
    else:
        return("invalid language") 
print(language_in("hindi""english"))  
def enter_in(Atm_pin):
    i=0
    while i<4:
        if Atm_pin==8920:
            return("pin accepted")
        else:
            return("invalid pin")
        i+=1
print(enter_in(int(input("enter the pin"))))    
def balance_in(balance):
    if balance==8000:
        return("sufficient balance")
    else:
        return("unsufficient balance")
print(balance_in(int(input("enter the balance"))))

def receipt_req(receipt):
    if receipt=="yes":
        return("yes,receipt received")
    else:
        return("no,receipt recevived")
print(receipt_req(input("do you have receipt")))        
def exist_in(exist):
    if exist=="yes":
        return("existing process")
    else:
        return("exist")
print(exist_in(input("exist or not")))





from pathlib import Path
import json
import random
import string

class Bank:
    database = "data.json"
    data = [] #Yeh data json mr save hoga

    try:
        if Path(database).exists():
            print("File exists")
            with open(database) as fs:
                data = json.loads(fs.read())

        else:
            print("No such files exists...") 

    except Exception as err:
        print("Error ocurred!!")

    @classmethod
    def update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(cls.data))  

    @staticmethod
    def generateAcc():
        digits = random.choices(string.digits,k=4)
        alpha = random.choices(string.ascii_letters,k=4)
        id = digits+alpha
        random.shuffle(id)
        return "".join(id)
    
    def depositeMoney(self):
        AccountNo = input("Enter your account number : ")
        Pin = int(input("Enter your pin : "))

        user_data = [i for i in Bank.data if i['account_no']==AccountNo and i['pin']==Pin]
        if user_data == False:
            print("User not found")
        else:
            amount = int(input("Enter amount : "))
            if amount<=0:
                print("Invalid amount!!!")  
            elif amount>10000:      
                print("Invalid amount!!!")    
            else:
                user_data[0]['balance'] += amount
                print("Amount credited....")
                Bank.update()  
    def withdrawMoney(self):
        AccountNo = input("Enter your account number : ")
        Pin = int(input("Enter your pin : "))

        user_data = [i for i in Bank.data if i['account_no']==AccountNo and i['pin']==Pin]
        if user_data == False:
            print("User not found")
        else:
            amount = int(input("Enter amount : "))
            if amount<=0:
                print("Invalid amount!!!")  
            elif amount>10000:      
                print("Greater than 10000")    
            else:
                if user_data[0]['balance'] < amount:
                    print("Insufficiant funds...")
                else:
                    user_data[0]['balance'] -= amount
                    Bank.update()
                    print("Amount debited....")  
    def details(self):
        AccountNo = input("Enter your account number : ")
        Pin = int(input("Enter your pin : "))
        user_data = [i for i in Bank.data if i['account_no']==AccountNo and i['pin']==Pin]
        if user_data == False:
            print("User not found")
        else:
            for i in user_data[0]:
                print(i,user_data[0][i])    



    #Create user
    def CreateAccount(self):
        info = {
            'name' : input("Enter your name : "),
            'age' : int(input("Enter your age : ")),
            'phoneNo': int(input("Enter your contact no.. : ")),
            'email' : input("Enter your Email : "),
            'pin' : int(input("Enter your pin : ")),
            'account_no' : Bank.generateAcc(),
            'balance' : 0
        }
        if info['age'] > 18 and len(str(info['pin'])) ==4 and len(str(info['phoneNo'])) == 10:
            Bank.data.append(info)
            Bank.update()
            print("Data added in list..")
            print(Bank.data)
        else:
            print("Credentials are not valid!!")   

    def deleteAccount(self):
        accountno = input("Enter your account no. : ")
        pin = int(input("Enter your 4 digit pin : "))

        user_data = [i for i in Bank.data if i['account_no'] == accountno and i['pin'] == pin]
        if user_data == False:
            print("User not Found")
        else:
            print("Are you sure you want to delete your acccount? (Yes/No) : ")
            choice = input()

            if choice == 'Yes':
                ind = Bank.data.index(user_data[0])
                Bank.data.pop(ind)
                Bank.update()
                print("Account delete successfully")
            else:
                print("Operation Terminated")

    def updateDetails(self):
        AccountNo = input("Enter your account number : ")
        Pin = int(input("Enter your pin : "))
        user_data = [i for i in Bank.data if i['account_no']==AccountNo and i['pin']==Pin]
        if user_data == False:
            print("User not found")
        else:
            print("Aap Account number or balance update nahi kar sakte!!!")

            print("Enter your details to update or just press enter to skip them")

            new_data = {
                'name' : input("Enter your name : "),
                'phoneNo': (input("Enter your contact no.. : ")),
                'email' : input("Enter your Email : "),
                'pin' : (input("Enter your pin : ")),

            }     

            if new_data['name'] == "":
                new_data['name'] = user_data[0]['name']                
            if new_data['phoneNo'] == "":
                new_data['phoneNo'] = user_data[0]['phoneNo']   
            else:
                new_data['phoneNo']  = int(new_data['phoneNo'])                
            if new_data['email'] == "":
                new_data['email'] = user_data[0]['email']                
            if new_data['pin'] == "":
                new_data['pin'] = user_data[0]['pin'] 
            else:
                new_data['pin']  = int(new_data['pin'])   

            new_data['AccountNo'] = user_data[0]['account_no']
            new_data['balance'] = user_data[0]['balance']    

            user_data[0].update(new_data)
            Bank.update()  
            print("Details are updated('_')")              


obj = Bank()
print("Press 1 for Creating Account")
print("Press 2 for Depositing Money")
print("Press 3 for Withdrawing Money")
print("Press 4 for Account Details")
print("Press 5 for Updating Account Details")
print("Press 6 for Deleting Account")

choice = int(input("Enter your Choice : "))

if choice == 1:
    obj.CreateAccount()

elif choice == 2:
    obj.depositeMoney()

elif choice == 3:
    obj.withdrawMoney()

elif choice == 4:
    obj.details()

elif choice == 5:
    obj.updateDetails()

elif choice == 6:
    obj.deleteAccount()

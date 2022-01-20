
import json

# Create User
def create_user():
    # with open("information.json", "r") as f:
    #     obj = json.load(f)
    a = input("Enter your name :")
    b = input("Enter your email :")
    c = input("Enter your password :")
    # for s in obj:
    #     if s["Email"] == b:
    #         print("Already this mail exists, give another mail.")
    #         return
    # obj.append({"Name": a, "Email": b, "Password": c})

    # with open("information.json", "w") as f:
    #     json.dump(obj, f, indent=4)
    info=({"Name": a, "Email": b, "Password": c})
    with open(f'{a}.json',"a") as f:
        json.dump(info, f, indent=4)

# List Users
def show_user():
    with open("information.json", "r") as s:
        # print(s.read())
        for i in json.load(s):
            print("Name: {}\nEmail: {}\n\n".format(i['Name'], i['Email']))

# Update User
def updater_user(email):
    with open("information.json", 'r') as f:
        content = f.read()
    if content != "":
        jsonData = json.loads(content)
        for dic in jsonData:
            if email == dic["Email"]:
                name = input("Enter name:")
                pas = input("Enter password :")
                newDic = {"Name": name, "Email": dic["Email"], "Password": pas}
                jsonData.remove(dic)
                jsonData.append(newDic)
                with open("information.json", "w") as f:
                    json.dump(jsonData, f, indent=4)
                return
        print("there is no data with the given email")
        return
    else:
        print("json file is empty")

# Delete User
def deleteUser(email):
        with open("information.json", 'r') as f:
            jsonData = json.load(f)
        for dic in jsonData:
            if email == dic["Email"]:
                jsonData.remove(dic)
                print("data deleted")
                with open("information.json", "w") as f:
                    json.dump(jsonData, f, indent=4)
                return
        print("data does not exist")

print("Welcome to our database.....")
a = int(input("1) Create User\n2) Show All Users\n3) Update User\n4) Delete User\n :-"))
if a == 1:
    create_user()
elif a == 2:
    show_user()
elif a == 3:
    b = input("Enter mail for update:")
    updater_user(b)
elif a == 4:
    c = input("Enter email for deletion:")
    deleteUser(c)
else:
    print("thank you so much to visit our data base...")

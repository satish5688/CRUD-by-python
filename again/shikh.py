import json
def creat_user():
    a=input("Enter username :")
    b=input("Enter email address :")
    c=input("Enter password :")
    d=({"Name":a,"Email":b,"Password":c})
    with open(f'{a}.json',"w") as f:
        json.dump(d,f,indent=4)
# creat_user()

def delete_user(a):
    import os
    if os.path.exists(f'{a}.json'):
        os.remove(f'{a}.json')
        print("This user is removed")
    else:
        print("we don't have this data.")
# b=input("enter user name :")
# delete_user(b)


# def update_user(a):
#     with open(f'{a}.json',"w") as f:
#         a=input("Enter username :")
#         b=input("Enter email address :")
#         c=input("Enter password :")
#         d=({"Name":a,"Email":b,"Password":c})
#         f.write(f'{json.dump(d,f,indent=4)}')
# b=input("enter yourname :")       
# update_user(b)


def user_list():
    import os
    lis=os.listdir()
    user=list(lis)
    for s in user:
        print(s[:-5])
# user_list()













print("Welcome friends to our khel.")
a=int(input("1) Creat user 2) User list  \n3) Delete user\n:-"))
if a==1:
    creat_user()
elif a==2:
    user_list()
elif a==3:
    b=input("enter user name :")
    delete_user(b)

# Function created to check USERNAME:
def username(u):
    temp = []
    necs = ['@', '.']
    for i in u:
        temp.append(i)
    if temp[0].isalpha() == True:
        if necs[0] in temp and necs[1] in temp:
            if ' ' not in temp:
                if temp[(temp.index('@')) + 1] != necs[1]:
                    for i in range((temp.index('@')), len(temp)):
                        if necs[1] == temp[i]:
                            # print('Your username is in correct format')
                            file = open('Login_DB.txt','r')
                            for i in file:
                                if u not in i:
                                    continue
                                else:
                                    return ('Same username already exists, Please give different username')
                                    break

                            else:
                                return 'Pass'
                                break

                        else:
                            continue
                    else:
                        return ('. is not after @ in username, Please try again...')
                else:
                    return ('. is next to @ in username, Please try again...')
            else:
                return ('Space is not allowed in username. Please try again...')
        else:
            return ('@ or . is missing in username, Please try again...')
    else:
        return ('Username should start with alphabet, Please try again...')


# Function created to check PASSWORD:
def password(p):
    temp2 = []
    test_case_password = 'Pass'
    for i in p:
        temp2.append(i)
    if len(temp2) > 5 and len(temp2) < 16:

        for i in range(0, len(temp2)):
            if temp2[i].isdigit() == True:
                break
        else:
            test_case_password = 'Fail'
            return ('No numeric in password, Please try again...')

        for i in range(0, len(temp2)):
            if temp2[i].isupper() == True:
                break
        else:
            test_case_password = 'Fail'
            return ('No uppercase letter, Please try again...')

        for i in range(0, len(temp2)):
            if temp2[i].islower() == True:
                break
        else:
            test_case_password = 'Fail'
            return ('No lowercase letter, Please try again...')

        for i in range(0, len(temp2)):
            if temp2[i].isalnum() != True:
                if temp2[i] != ' ':
                    break

        else:
            test_case_password = 'Fail'
            return ('No special character, Please try again...')

        for i in range(0, len(temp2)):
            if temp2[i] != ' ':
                continue
            else:
                test_case_password = 'Fail'
                return ('space not allowed in password, Please try again...')
                break
    else:
        test_case_password = 'Fail'
        return ('Password length too short or too long, Please try again...')

    if test_case_password == 'Pass':
        # print('Your password is in correct format')
        return test_case_password



# Function created to add LOGIN DETAILS in text file:
def LoginDetails_Add_in_DB(x,a,b,y):
    file = open('Login_DB.txt', 'r+')
    file.readlines()
    # file.write('\n')
    file.write(x)
    file.write(',')
    file.write(a)
    file.write(',')
    file.write(b)
    file.write(',')
    file.write(y)
    file.write('\n')
    file.close()
    return ('Your Registration process completed.. Please Login now..')


# Function created for LOGIN:
def LoginDetails_check(x, y):
    file = open('Login_DB.txt', 'r+')
    for i in file:
        temp = i.split(',')
        if x == temp[0]:
            temp[-1] = temp[-1].replace('\n', '')
            if y == temp[-1]:
                return 'Pass'
                break

            else:
                return 'Fail'
                break

    else:
        return 'Account not exist..Please Register first..'


#Function created for Security Questions:
def Acc_Rec_Ques(x,y,z):
    file = open('Login_DB.txt', 'r')
    for i in file:
        temp1=i.split(',')
        if x == temp1[0]:
            if y == temp1[1] and z == temp1[2]:
                return 'Pass'
                break
            else:
                return 'Your answers for Security questions are Wrong..'
                break


#Function created to Get old Password during FORGET PASSWORD condition:
def Get_Old_PW(x):
    file = open('Login_DB.txt', 'r')
    for i in file:
        temp1 = i.split(',')
        if x == temp1[0]:
            temp1[-1] = temp1[-1].replace('\n', '')
            return (temp1[-1])
            break


#Function created to add New Password during FORGET PASSWORD condition:
def Add_New_PW(x,y,z):
    with open('Login_DB.txt','r+') as file:
        total_Datas = file.readlines()
        count = 0
        file.seek(0)
        for i in file:
            if x in i:
                r = total_Datas.index(i)
                count = count + 1
                break
        if count == 1:
            newpass = input('Enter new password: ')
            newpass_re=input('Re-Enter new password: ')
            if newpass==newpass_re:
                pwcheck = password(newpass)
                if pwcheck == 'Pass':
                    total_Datas[r] = (x + ',' + y + ',' + z + ',' + newpass + '\n')
                    file=open('Login_DB.txt','w+')
                    file.seek(0)
                    file.writelines(total_Datas)
                    file.close()
                    return ('Password successfully updated.. Login now..')
                else:
                    return (pwcheck)
            else:
                return ('Password mismatching.. Please enter password correctly..')




# PROJECT 1:
# REGISTRATION & LOGIN SYSTEM USING PYTHON, FILE HANDLING:


x = int(input('For Register press 1 / For Login press 2: '))

import os.path
if os.path.exists('Login_DB.txt'):
    pass
else:
    f = open('Login_DB.txt','x')
    f.close()

# Step 1: Registration
if x == 1:
    print('Create USERNAME & PASSWORD..')
    print('''Format for USERNAME: 1. Create USERNAME with '@' and '.' , but '.' should not be immediate next to '@'.
                     2. USERNAME should not start with special characters..''')
    user = input('Enter USERNAME: ')
    o1 = username(user)
    if o1 == 'Pass':
        print(user, 'is valid..')
        print('''Format for PASSWORD: 1. PASSWORD length should be >5 and <16..
                     2. PASSWORD should have Min. 1 special character, 1 digit, 1 Uppercase, 1 Lowercase characters atleast..''')
        passw = input('Enter PASSWORD: ')
        o2 = password(passw)
        if o2 == 'Pass':
            print(passw, 'is valid..')
            print('Please answer the below Security Question for SAFE ACCOUNT RECOVERY in future...')
            acc_rec_1=input('Enter your Favourite place (in lowercase): ')
            acc_rec_2=input('Enter your Favourite Color (in lowercase): ')
            if acc_rec_1.islower()==acc_rec_2.islower()==True:
                print(LoginDetails_Add_in_DB(user,acc_rec_1,acc_rec_2,passw))
            else:
                print('Security answers not in Lowercase.. Please Try again..')
        else:
            print(o2)
    else:
        print(o1)

# Step 2: Login
if x == 2:
    print('Enter your USERNAME & PASSWORD for LOGIN..')
    user = input('Enter USERNAME: ')
    passw = input('Enter PASSWORD: ')

    o3 = LoginDetails_check(user, passw)
    if o3 == 'Pass':
        print('LOGIN successful!!..You can continue..')
    elif o3 == 'Fail':
        print('PASSWORD is wrong..')
        pwcheck1=int(input('Press 1 for FORGET PASSWORD/Press 2 to Re-try LOGIN: '))
        if pwcheck1==1:
            print('Answer the security questions to access your account..')
            acc_rec_1 = input('Enter your Favourite place (in lowercase): ')
            acc_rec_2 = input('Enter your Favourite Color (in lowercase): ')
            op= Acc_Rec_Ques(user,acc_rec_1,acc_rec_2)
            if op=='Pass':
                print('GREAT... Now you can access your account..')
                a = int(input('Press 1 to get OLD PASSWORD / Press 2 to add NEW PASSWORD: '))
                if a == 1:
                    print('Your OLD PASSWORD is', Get_Old_PW(user))
                if a == 2:
                    print(Add_New_PW(user,acc_rec_1,acc_rec_2))
            else:
                print(op)
        else:
            print('Please go for LOGIN page..')
    else:
        print(o3)


# End of the Program..

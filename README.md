# PROJECT-1
REGISTRATION AND LOGIN SYSTEM USING PYTHON, FILE HANDLING.

PROBLEM: To create Registration and Login system using Python, file handling..
Note:- This task has to be accomplished using Python alone. No web.


STEP 1: REGISTRATION PROCESS:


Given conditions to create Username:
1. Email/username should have "@" and followed by ".".
2. It should not be like this 
       eg:- @gmail.com
3. There should not be any "." immediate next to "@".
4. It should not start with special characters and numbers.

Solution:
# Function created for Username checking:
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


Given conditions to create Password:

1. password (5 < password length > 16)
2. Must have minimum one special character, one digit, one uppercase, one lowercase character.

Solution:
# Function created for Password checking:
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




STEP 2: STORING THE VALIDATED DATA IN TXT FILE:

Once the username and password are validated, store that data in a text file.

Solution:

# Function created to add login details in text file:
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


STEP 3: LOGIN PROCESS:

When the user chooses to Login, check whether his/her credentials exist in the file or not based on the user input.

Solution: 
# Function created for Login:
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

If it doesn’t exist then ask them to go for Registration (or)
If they have chosen forget password you should be able to retrieve their original password based on their username provided in the user input
or else you can ask them to provide a new password (only if their username matches with the data exists in the file)

Solution: 

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


If nothing matches in your file you should ask them to Registration (Since they don't have an account)


import firebase_admin
from firebase_admin import db, credentials
from tkinter import *
from cryptography.fernet import *


cred_obj = firebase_admin.credentials.Certificate("C:/Users/LAKSHYA KUMAR/PycharmProjects/pythonProject/theOPkey.json")
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://medicinator-76e53-default-rtdb.firebaseio.com'})
ref = db.reference("/")


def encryptWithFernet(data):
    fernetKey = ref.get()["FERNET KEY"]["Key"]
    toEncrypt = bytes(data, 'utf-8')
    token = Fernet(fernetKey).encrypt(toEncrypt)
    encryptedText = token.decode('utf-8')
    return encryptedText


def decryptWithFernet(toDecrypt):
    fernetKey = ref.get()["FERNET KEY"]["Key"]
    bytesDecrypted = Fernet(fernetKey).decrypt(toDecrypt)
    decryptedText = bytesDecrypted.decode('utf-8')
    return decryptedText


def isLoggedIn():
    return True


def startLoginMethod():
    def loginToAccount(USERNAME, PASSWORD):
        my_tkn = USERNAME + PASSWORD
        encryptedAccountsDB = list(dict(ref.get()).keys())
        encryptedAccountsDB.pop(0)
        AccountsDB = []

        for token in encryptedAccountsDB:
            tkn = decryptWithFernet(token)
            AccountsDB.append(tkn)

        if my_tkn in AccountsDB:
            mainApplicationMethod()
        else:
            print("There has been an error")

    def openAccCreationWindow(idk):
        accountPage = Tk()
        headingTextBox2 = Label(accountPage, text="Create a new account", font=("Arial", 45))
        headingTextBox2.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 60))

        loginTextBox2 = Label(accountPage, text="Username : ", font=("Arial", 20))
        loginTextBox2.grid(row=1, column=0, )
        loginEntrybox2 = Entry(accountPage, width=30)
        loginEntrybox2.grid(row=1, column=1)

        passwordextBox2 = Label(accountPage, text="Password : ", font=("Arial", 20))
        passwordextBox2.grid(row=2, column=0, pady=(0, 20))
        passwordEntrybox2 = Entry(accountPage, width=30)
        passwordEntrybox2.grid(row=2, column=1, pady=(0, 20))

        createAccountButton = Button(accountPage, text="Create",
                                     command=lambda: createAccountFunction(loginEntrybox2.get(),
                                                                           passwordEntrybox2.get()), font=("Arial", 15))
        createAccountButton.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        def createAccountFunction(USERNAME, PASSWORD):
            my_tkn = USERNAME + PASSWORD
            tokenStr = encryptWithFernet(my_tkn)
            ref.child(tokenStr).push(USERNAME)
            print("Created Account" + tokenStr)
            accountPage.destroy()

    basicFrame = Tk()
    headingTextBox = Label(basicFrame, text="Login to your account", font=("Arial", 45))
    headingTextBox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 60))

    loginTextBox = Label(basicFrame, text="Username : ", font=("Arial", 20))
    loginTextBox.grid(row=1, column=0)
    loginEntrybox = Entry(basicFrame, width=30)
    loginEntrybox.grid(row=1, column=1)

    passwordextBox = Label(basicFrame, text="Password : ", font=("Arial", 20))
    passwordextBox.grid(row=2, column=0, pady=(0, 20))
    passwordEntrybox = Entry(basicFrame, width=30)
    passwordEntrybox.grid(row=2, column=1, pady=(0, 20))

    loginButton = Button(basicFrame, text="Login",
                         command=lambda: loginToAccount(loginEntrybox.get(), passwordEntrybox.get()),
                         font=("Arial", 15))
    loginButton.grid(row=3, column=0, columnspan=2)

    createAccountButton = Button(basicFrame, text="Create a new account", command=lambda: openAccCreationWindow("text"),
                                 font=("Arial", 15))
    createAccountButton.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    basicFrame.mainloop()


def mainApplicationMethod():
    main = Tk()
    main.geometry("100x100")
    something = Label(main, text="yay")
    something.grid(row=0, column=0)
    main.mainloop()


if not isLoggedIn():
    startLoginMethod()
else:
    mainApplicationMethod()

# Add Error box in line 46

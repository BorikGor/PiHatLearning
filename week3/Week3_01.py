'''
This program will be training in Object-orienting programming.
Part 1: Portable credit card reader:
'''
class CardReader:
    MerchantAccount = None
    PIN = None

    def SetMerchantAccount(self):
        for cnt in range(3):
            user_input = input("Whats your credit card number?\r\n")
            if user_input.isdigit():
                self.MerchantAccount = user_input
                break
            else:
                input("Nah, mate, you need to give me your card number in digits, not words.\r\npress Enter to continue")
        if self.MerchantAccount is not None:
            print("Your Account has been initialised to:\r\n", self.MerchantAccount)
            input("\r\npress Enter to continue")
        else:
            input("Your account still does not have a credit card number.\r\npress Enter to continue")
    
    
    def Payment(self):
        import getpass
        _success = False
        payment = input("Enter the Total amount to pay:\r\n")
        input("Swipe your card now and press Enter to continue")
        for cnt in range(3):
            PIN = getpass.getpass(prompt = "Enter your 4 digits PIN:\r\n")
            if PIN.isdigit():
                if PIN == "1234":
                    break
                else:
                    print("Wrong PIN!\r\n",PIN)
            else:
                print("PIN code should be composed of 4 digints, no other chars")
        if PIN != "1234":
            input("Sorry, your PIN is wrong, the transaction will be canceled.\r\npress Enter to continue")
        else:
            input("PIN Accepted\r\npress Enter to continue")
            _success = True
        if _success:
            print(f"Payment to "+ self.MerchantAccount +" accepted!\r\npress Enter to continue")
            input()
        else:
            print("Payment Failed.\r\npress Enter to continue")
            input()

    def StartMenu(self):
        while(True):
            from os import system
            system("clear||cls")
            user_choice = input("What do you want to do today?\r\n1) Set merchant account\r\n2) Customer payment\r\n0) Exit\r\n")
            if user_choice == "1":
                self.SetMerchantAccount()
            elif user_choice == "2":
                self.Payment()
            elif user_choice == "0":
                break
            elif user_choice in "Hello!hello!":
                input("Well, hello there!\r\nSo nice to be conversing with such a nice person like yourself!\r\npress Enter to continue")
            else:
                input("Well, that was unexpected. Now I don\'t know what to do...\r\nPlease try again.\r\npress Enter to continue")



Anton = CardReader()
# Anton.SetMerchantAccount(None)
# Anton.Payment(None)
Anton.StartMenu()

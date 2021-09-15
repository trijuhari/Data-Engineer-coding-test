class Contact:
    def __init__(self, firstname, lastname, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone

    def get_firstname(self):
        return (self.firstname)

    def get_lastname(self):
        return (self.lastname)

    def get_phone(self):
        return (self.phone)

    def get_fullname(self):
        return (self.firstname + " " + self.lastname)

    def get_info(self):
        return(self.get_fullname() + "-" + self.get_phone())


class Phonebook:
    def __init__(self):
        self.internal_list = []
        self.unique = []# list member variable, unique to each instantiated class

    def append(self,contact):
        isnumberexists =  self.is_exists_phone(contact.get_phone())
        if isnumberexists != True:
            self.internal_list.append(contact.get_phone())
            self.unique.append(contact.get_info())
            print(f"{contact.get_fullname()} - {contact.get_phone()} : insert success")
        else:
            print(f"{contact.get_fullname()} - {contact.get_phone()} : duplicate phone number")

    def is_exists_phone(self, phone):
        if phone in self.internal_list:
            return True
        else:
            return False

    def getList(self):
        print("Phone book:")
        for i,data in enumerate(self.unique,1):
            print(f" {i}.{data}")





def soal():
    string = "Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001"
    print(f"Input: \n{string}   ")
    print("Output: \n==== Output START ==== \nLog: ")

    # extract string which have  multiple delimeter
    split_string = string.split(';')
    split_list = []
    for string_new in split_string:
        split_list.append(string_new.split(','))
    p = Phonebook()
    for data in split_list:
        c =Contact(data[0], data[1], data[2])
        p.append(c)



    p.getList()
    print("=== Output END ===")

if __name__ == "__main__":
    soal()


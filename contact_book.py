class Contact:
    megaList = []
    with open('contactBook.txt', 'r') as cb:
        for i in cb:
            contact = i.split(';')
            address = contact[-1]
            printableAddress = address.strip('\n')
            printableAddress = address.replace(address, printableAddress)
            contact[-1] = printableAddress
            megaList.append(contact)
    def saveContact(self):
        with open('contactBook.txt', 'w') as contactBook:
            for contact in Contact.megaList:
                for details in contact:
                    if details == contact[-1]:
                        contactBook.write(details + '\n')
                    else:
                        contactBook.write(details + ';')
    def newContact(self):
        self.name = input('Enter Name: ')
        self.phoneNo = int(input('Enter Phone Number: '))
        self.email = input('Enter email: ')
        self.address = input('Enter address: ')
        new_contact = [self.name,self.phoneNo,self.email,self.address]
        with open('contactBook.txt', 'a') as cb:
            for detail in new_contact:
                if detail == new_contact[-1]:
                    cb.write(f'{detail}\n')
                else:
                    cb.write(f'{detail};')
        print('Contact has been created\n')
    def seeAllContact(self):
        print(f'Name            Phone Number')
        for contact in Contact.megaList:
            print(f'{contact[0]}            {contact[1]}')
        print()
        return

    def searchContact(self):
        searchItem = input('\nEnter name/number to search: ')
        found = False
        for indivContact in Contact.megaList:
            if searchItem in indivContact[0] or searchItem in indivContact[1]:
                print(f'{indivContact[0]}           {indivContact[1]}           {indivContact[2]}           {indivContact[3]}')
                found = True
        print()
        if found == False:
            print('Not found')
        return
    def updateContact(self):
        searchItem = input('\nEnter name to update: ')
        Found = False
        contactFound = ''
        for indivContact in Contact.megaList:
            if searchItem == indivContact[0]:
                Found = True
                contactFound = indivContact
                break
        if Found == True:
            print('''Enter serial number you want to change:
    1. Name                 3. Email
    2. Phone Number         4.Address''')
            updateChoice = input('>>> ')
            if updateChoice == '1':
                newName = input('Enter new name: ')
                contactFound[0] = newName
                print('\nChange has been saved')
            elif updateChoice == '2':
                newNumber = input('Enter new Number: ')
                contactFound[1] = newNumber
                print('\nChange has been saved')
            elif updateChoice == '3':
                newEmail = input('Enter new Email: ')
                contactFound[2] = newEmail
                print('\nChange has been saved')
            elif updateChoice == '4':
                newAddress = input('Enter new Address: ')
                contactFound[-1] = newAddress
                print('\nChange has been saved\n')
            else:
                print('Invalid input')
                return
            indivContactIndexNo = Contact.megaList.index(indivContact)
            Contact.megaList[indivContactIndexNo] = contactFound
            self.saveContact()
            return
        else:
            print('Contact not found')
    def deleteContact(self):
        contactName = input('Enter name: ')
        for contact in Contact.megaList:
            if contactName == contact[0]:
                Contact.megaList.pop(Contact.megaList.index(contact))
                self.saveContact()
                print('Contact has been removed\n')
                return
        print('Contact not found\n')
        return


def mainInterface():
    print('''Enter the respective number:
    1. Create New Contact           4. Update any contact
    2. See All Contacts             5. Delete a contact
    3. Search Contact''')
    firstChoice = input('>>> ')
    user = Contact()
    if firstChoice == '1':
        user.newContact()
        mainInterface()
    elif firstChoice == '2':
        user.seeAllContact()
        mainInterface()
    elif firstChoice == '3':
        user.searchContact()
        mainInterface()
    elif firstChoice == '4':
        user.updateContact()
        mainInterface()
    elif firstChoice == '5':
        user.deleteContact()
        mainInterface()
    else:
        return
mainInterface()

import pyperclip
class contact:
    '''
	creates new instance of the contact class.
	'''
    
    contact_list = [] # Saving our contacts()

    def __init__(self, first_name, last_name, phone_number, email): # creating new instances of the Contact class.
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        '''
        saves contacts.
        '''
        contact.contact_list.append(self) # adds new contacts in the contacts[]

    def delete_contact(self):
        '''
        deletes contacts.
        '''
        contact.contact_list.remove(self) # deletes  contacts.

    @classmethod 
    def find_by_number(cls, number):
        '''
        Finds and returns a similar contact number.
       
        '''
        for contact in cls.contact_list: # Loops in the contacts.
            if contact.phone_number == number: # passing an argument.
                return contact

    @classmethod
    def contact_exists(cls, number):
        '''
        checks if a contact exists.
       
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True 

        return False 

    @classmethod
    def display_contacts(cls):
        '''
        Displays the contacts.
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        '''
        copies contacts to clipboard.
        '''
        found_contact = contact.find_by_number(number)
        pyperclip.copy(found_contact.email) 


    @classmethod
    def paste_email(cls, number):
        '''
        paste contacts to clipboard.
        '''
        found_contact = contact.find_by_number(number)
        pyperclip.paste(found_contact.email) 
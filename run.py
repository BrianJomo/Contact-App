#!/usr/bin/env python3.9

from contact import contact

def create_contact(first_name, last_name, phone_number, email):
    '''
    create a new contact.
    '''
    new_contact = contact(first_name, last_name, phone_number, email)
    return new_contact

def save_contacts(contact):
    '''
    save contacts.
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    delete a contact.
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    finds  contacts.
    '''
    return contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    checks if a contact exists.
    '''
    return contact.contact_exists(number)

def display_contacts():
    '''
    display all the saved contacts.
    '''
    return contact.display_contacts()

def check_copy_email(number):
    '''
    copies returned contacts to clipboard.
    '''
    contact.copy_email(number)

def check_paste_email(number):
    '''
    paste returned contacts to clipboard.
    '''
    contact.paste_email(number)    

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()


                    save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                    print ('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_contact(search_number)
                            print(f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_contact.phone_number}")
                            print(f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
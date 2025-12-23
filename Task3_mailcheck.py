email =(input("Enter mail to check:")) 
flag=0
    # Check if exactly one '@' is present
if email.count('@') == 1:
         
    # Split the email into local part and domain part
         local_part, domain_part = email.split('@')

    # Check if local and domain parts are not empty
         if not local_part or not domain_part:     
            flag=0
         elif '.' not in domain_part:
             flag=0
         elif domain_part.startswith('.') or domain_part.endswith('.'):
            flag=0
         else:
               flag=1
else:
        flag=0
if flag==1:
        print(email,"valid",sep=" ")
else:
        print(email,"invalid",sep=" ")


import smtplib, imapclient, pyzmail

#eng
#keywords = ["fact": fact(), "weather": weather(), "wordchain": wordchain()]

going = True
password = input("Please input the password: ")

imapObj = imapclient.IMAPClient("imap-mail.outlook.com", ssl = True)
imapObj.login("boredatwork@outlook.hu",password)
imapObj.select_folder("INBOX", readonly = False)

smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587) #SMTP connection, .connect() is automatically called
smtpObj.ehlo() #showing our hand for a handshake - if the server is a cool dude and shakes back then we're good
smtpObj.starttls() #start tls encryption
smtpObj.login("boredatwork@outlook.hu",password)

while going:
    IDs = imapObj.search("UNSEEN")
    rawmsgs = imapObj.fetch(IDs,['BODY[]'])

    for ID in IDs:
        email = pyzmail.PyzMessage.factory(rawmsgs[ID][b'BODY[]'])
        new_recipient, new_sender = email.get_addresses("from")[0][1], email.get_addresses("to")[0][1]
        subject, message = "HOLA", "WHATSUPPPP"
        body = "Subject: {0}\n\n{1}".format(subject, message)
        smtpObj.sendmail(new_sender, new_recipient, body) #double linebreak bc...???
        print("finished")
        #if email.text_part != None:
        #    print(email.text_part.get_payload().decode(email.text_part.charset))

    #    if email.html_part != None:
    #        print(email.html_part.get_payload().decode(email.html_part.charset))
smtpObj.quit()
print("HEfinished")

import requests # http_requests
from bs4 import BeautifulSoup#web_scrapping
import smtplib # send the mail
# email body
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
#system date time manipulation 
import datetime
import getpass # to hide the password typed in terminal

now = datetime.datetime.now()

# email content placeholder

content = ''

# extracting

def extract_news(url):
    """[this function extracts the first 30 posts or titles from the website]"""

    print("extracring hackerNews new stories please be patient...😴")
    cnt = ''
    cnt += ('<b> HackerNews Top Stories <b>\n' + '<br>' + '•'*50 + '<br>') 
    response = requests.get(url)
    fun_content = response.content  
    soup = BeautifulSoup(fun_content , 'html.parser') # creating a soup 
    '''
    the conditions are find in the website the tags <td> and the attributes we check are the class- title and also where yaling
    is one enumerate goves us the count of all the things we find from scraping the 'i' will counatin the number of values ie. enumerate
    values and tag will contain the html we scraped  
    '''
    for i,tag in enumerate(soup.find_all('td',attrs= {'class':'title','yalign':''})):

        '''
        here str(i+1) is done because when we print this the first element will be 0 to make it one we use str(i+1)
        the if statements check when tag.text not equal to "More" (more is in the webesite) add values to cnt if not give nothing

        '''
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + "<br>") if tag.text !='More' else '')

    return cnt 
try:
    cnt = extract_news ('https://news.ycombinator.com')
    content += cnt
    content += ('<br>--------------------------------------<br>')
    content += ('<br><br> End of message 🦗')


    # sending the mail

    print("Composing email... 📝")

    # updating your email id
    #important parameters

    SERVER = 'smtp.gmail.com' # your smtp server
    PORT  = 587 # your port number
    FROM  = input("enter the FROM Email adress --> [without@gmal.com] 😁 :  ") + "@gmail.com"
    TO = input("enter the TO Email adress --> [without@gmal.com] 😁 :  ") + "@gmail.com" # could be [list of emails]
    print("[🪶 PASSWORD YOU ENTER WILL BE HIDDEN 🪶]")
    PASS = getpass.getpass("enter password for {} --> ".format(FROM)) # password

    msg = MIMEMultipart()
    # [dynamic printing because when we send mail having same subject it turns into a convo and not a new mail]
    msg['Subject'] = "✨Top News Stories In HackerNews [Automated Email]✨" + '' + str(now.day) + '-' + str(now.month) + '-' +str(now.year)
    msg[FROM] = FROM
    msg[TO] = TO

    msg.attach(MIMEText(content, 'html')) # since we used html text instead of normal text | remeber <b> and <br>



    print('Initialisng Server... 😴')

    server = smtplib.SMTP(SERVER,PORT)
    # server = smtplib.SMTP SSL('smtp.gmail.com' , 465)
    server.set_debuglevel(0) # 0- no , 1 error is shown in screen
    server.ehlo()
    server.starttls()

    server.login(FROM,PASS)
    server.sendmail(FROM,TO , msg.as_string())
    print('Email Sent ✔️✨')
    server.quit()

except smtplib.SMTPAuthenticationError:

    print(" This didnt work, please try the following ")
    print('''1. checking your internet connectivity
             2. checking if you had eneabled sign in from less secure apps
             3. if the password/mail id entered is correct
    ''')
except smtplib.SMTPConnectError:

    print(" This didnt work, please try the following ")
    print('''

             1. checking your internet connectivity
             2. checking if you had eneabled sign in from less secure apps
             3. if the password/mail id entered is correct
    ''')
except requests.exceptions.ConnectionError:
    print('*'*66)
    print('*'*66)
    print('*'*24 +" you are offline! " + '*'*24 )
    print('*'*66)
    print('*'*66)
except TypeError:
    print('*'*66)
    print('*'*66)
    print('*'*24 +" that did not work " + '*'*24 )
    print('*'*66)
    print('*'*66)
except KeyboardInterrupt:
    
    print(" exiting... ")


    



    
    



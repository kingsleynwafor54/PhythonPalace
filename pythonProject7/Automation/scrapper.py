import requests  #http requests
from bs4 import BeautifulSoup #web scrapping
import smtplib #send the mail
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now =datetime.datetime.now()
#email content placeholder

content=''

#extracting Hacker News Stories



def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt+= ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*5+'</br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt+=((str(i+1)+'::'+tag.text+"\n"+'<br>')if tag.text!='More' else '')
        return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
print(cnt)
content +=cnt
content +=('<br>-------<br>')
content +=('<br><br>End of Message')

print("printing your email ...")
SERVER = 'smtp.gmail.com'
PORT = 587 # your port number
FROM = 'kingsleynwafor54@gmail.com'
TO = 'nwaforkingsley369@gmailcom'
PASS ='09020076648kk' # your email id's password
# fb = open(file_name, 'rb')
#Create a text/plain message
#msg=MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition','attachment',filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]'+''+str(now.day)+ '-'+str(now.str)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html'))

print('Initiating Server')

server =smtplib.SMTP(SERVER, PORT)
#server =smtplib.SMTP_SSL('smtp.gmail.com',465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM,PASS)
server.sendmail(FROM, TO,msg.as_string())

print('Email Send...')

server.quit()

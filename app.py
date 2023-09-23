from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        #Create API Class Object
        self.apio = API()

        # Create database object
        self.dbo = Database()


        # Load Login GUI
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='black')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5,10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_button = Button(self.root, text='Login', width=20, height=2, command=self.perform_login)
        login_button.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member ?')
        label3.pack(pady=(10, 10))

        redirect_button = Button(self.root, text='Register Now', width=10, height=1, command=self.register_gui)
        redirect_button.pack(pady=(10, 10))


    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_button = Button(self.root, text='Register', width=20, height=2, command=self.perform_registration)
        register_button.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member ?')
        label3.pack(pady=(10, 10))

        redirect_button = Button(self.root, text='Login Now', width=10, height=1, command=self.login_gui)
        redirect_button.pack(pady=(10, 10))


    def clear(self):
        # Need to clear existing GUI here
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #Fatch Data From GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful! You can login now')

        else:
            messagebox.showerror('Error', 'Email Already Exist')

    def perform_login(self):
        #Fatch Data From GUI

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login successfully')
            self.home_gui()
        else:
            messagebox.showerror('Error','Email/Password Incorrect')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))

        ner_button = Button(self.root, text='Name Entity Recognition', width=30, height=4,
                                  command=self.ner_gui)
        ner_button.pack(pady=(10, 10))

        emotion_button = Button(self.root, text='Emotion Prediction', width=30, height=4,
                                  command=self.emotion_gui)
        emotion_button.pack(pady=(10, 10))

        logout_button = Button(self.root, text='Logout', width=20, height=2, command=self.login_gui)
        logout_button.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 10))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='black', fg='white')
        heading2.pack(pady=(30, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=30)
        self.sentiment_input.pack(pady=(10, 10), ipady=4)

        sentiment_button = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='black', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))


        go_back_button = Button(self.root, text='Go Back', width=10, height=1, command=self.home_gui)
        go_back_button.pack(pady=(20, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + '->' + str(result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = txt

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 10))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='NER Analysis', bg='black', fg='white')
        heading2.pack(pady=(30, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=30)
        self.ner_input.pack(pady=(10, 10), ipady=4)

        ner_button = Button(self.root, text='Analyze NER', command=self.do_ner_analysis)
        ner_button.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='black', fg='white')
        self.ner_result.pack(pady=(10, 5))
        self.ner_result.configure(font=('verdana', 10))


        go_back_button = Button(self.root, text='Go Back', width=10, height=1, command=self.home_gui)
        go_back_button.pack(pady=(10, 10))

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)

        txt = ''
        for i in result['entities']:
            for j in i:
                txt = txt + j + '-->' + str(i[j]) + '\n'
            txt += '\n'
        self.ner_result['text'] = txt

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 10))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='black', fg='white')
        heading2.pack(pady=(30, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=30)
        self.emotion_input.pack(pady=(10, 10), ipady=4)

        emotion_button = Button(self.root, text='Analyze Emotion', command=self.do_emotion_analysis)
        emotion_button.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='black', fg='white')
        self.emotion_result.pack(pady=(10, 5))
        self.emotion_result.configure(font=('verdana', 10))


        go_back_button = Button(self.root, text='Go Back', width=10, height=1, command=self.home_gui)
        go_back_button.pack(pady=(10, 10))

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)

        txt = ''
        for i in result['emotion']:
            txt = txt + i + '-->' + str(result['emotion'][i]) + '\n'
        self.emotion_result['text'] = txt

nlp = NLPApp()

import speech_recognition as s
import pyttsx3  # for text-to-speech conversion.
# ListTrainer is used to train the ChatBot.
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import spacy
# nlp = spacy.load(r'C:\Users\LENOVO\anaconda3\envs\virtual36\Lib\site-packages\en_core_web_sm\en_core_web_sm-2.3.1')
spacy.load('en')
''' Bot text-to-speech conversion Starts Here...'''
# creating object(named engine) of ttsx3 engine Class
engine = pyttsx3.init()

# init. voices variable to get the voices.
voices = engine.getProperty('voices')
# now setting the voice.
# index 1 = female voice , index 0 = male voice.
engine.setProperty('voice', voices[1].id)
''' Bot text-to-speech conversion Ends Here.'''

''' Bot speech-to-text conversion starts here.'''

# defining a function for speech recognition.


def take_query():
    # now we'll create object of speech_recognition class.
    speech = s.Recognizer()
    # Now we'll set time for hearing.
    # 1 sec is maximum time in which user can speak.New speech will be taken after this 1 sec.
    speech.pause_threshold = 1
    print('R.A.N.A is Listening....Try to speak.')

    # Now we'll create object of our Microphone Class. Through which we'll send our audio.
    # and for that we'll use with keyword which helps in closing the object of microphone class.
    with s.Microphone() as mic:
        try:
            audio = speech.listen(mic)
            # now we have to convert this audio into text.
            # we have use eng-indian language as the speaking language
            # so we have set it for converting.
            query = speech.recognize_google(audio, language='eng-in')
            # this query will be passed in askbot function.

            # we'll delete if anything is present on the questionField.
            # from 0th to END position,it'll delete everything
            questionField.delete(0, END)
            # we'll also insert the query in the questionField.
            # at 0th position query will be inserted.
            questionField.insert(0, query)
            askbot()  # here we are calling the askbot function.
        except Exception as e:
            print(e)
            # tinkter.messagebox.showerror('Error', 'Voice not recognized.')
# Now we have to call take_query() function. so we will call it jjust above the root.mainloop() line.


''' Bot speech-to-text conversion ends here.'''

''' Bot Training Part Starts Here'''
# Now we will create object(name = bot) of the ChatBot class.ChatBot('Bot Name')
bot = ChatBot('RANA')
# Now we will require conversation in a form of list.

# convo = ['Hello',
#          'Hi There',
#          'What is your name',
#          'My Name is RANA',
#          'How are you. ?',
#          'I am Fucked up these days.',
#          'Are you intelligent',
#          "Yes I'm intelligent"]
# Now we will train our bot using ListTrainer Class.
# trainer is the object created for the ListTrainer.
trainer = ListTrainer(bot)  # bot was the object of our ChatBot
# we will train our bot on the basis of the convo list.
# trainer.train(convo)
# we will train our bot using data of corpus-chatterbot data files.
import os
# os.listdir provide all the folder availabe in your os

# we are using loop here because we have so many files for training. so one by one bot will be trained by each file.
# for files in os.listdir(r'D:/chatbot__1_/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english'):
#     # we are opening files one by one using files loop.
#     data = open(r'D:/chatbot__1_/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
#     # now we are training our bot with this data. and it'll be also stored in db.sqlite3 file.
#     trainer.train(data)
    
def askbot():
    # first we will access the text written by the user on the entry field
    query = questionField.get()
    # getting response from the bot for our query
    answer = bot.get_response(query)

    # Now we will add our convo with bot in the textarea.
    textArea.insert(END, 'You: '+query+'\n\n')
    # only string can be concatnated with another string, that's why we converted answer into a string.
    textArea.insert(END, 'R.A.N.A: '+str(answer)+'\n\n')
    # now we will use say feature so that bot can speak out the answer.
    engine.say(answer)
    engine.runAndWait()  # engine will run and wait.

    # Now delete everything from the questionField so that next query can be asked.
    questionField.delete(0, END)

    # Our scrollbar should go down accordingly with our conversation goeson.
    textArea.yview(END)  # yview is y-axis view and we set it at END.


''' Bot Training Part Ends Here.'''
''' GUI Part Starts Here....'''
# now we are creating an object(name = root) of the Tk(tkinter) class
root = Tk()

# to manage the height and width of the window, we will use geometry function -> geometry('width * height + distance from x-axis + distance from y-axis')
root.geometry('500x570+650+230')

# to fix the size of windows (to switch off the maximize button)
# we are passing false value for width and height so that there will be no change in width and height
root.resizable(0, 0)

# to give the title to the titlebar
root.title('Chat Bot ~ Created With ❤ By Aman')

# to change the background color of the window.
root.config(background='gray10')

# to add the logo image
# so for this first we will create an object of the image and for this we will use PhotoImage class. PhotoImage(pass the location of the image)
logo = PhotoImage(file='bot_1.png')

# now to place the image on the lable , we will use lable class. Label(location where the image will be placed , image = object of the image)
# we are passing background(bg) color so that it can match with the bg color of window.
logo_label = Label(root, image=logo, bg='gray10')
logo_label.pack(pady=5)  # pady(padding along y-axis) # pack() is a method to place something and is generally used when we don't have any complex thing to place. pack(side = LEFT,RIGHT,TOP,BOTTOM. By default TOP) is a method
# to hold the main window

# Now to add the text area
# first we will create a frame using Frame() class wich will be inside our root window
center_frame = Frame(root, bg='gray13')
center_frame.pack()  # this frame is packed just after the logo image. if we placed this above logo image (line 23) then it will packed above the logo image

# Now we will add ScrollBar which will be inside center_frame.
scrollBar = Scrollbar(center_frame)
# fill is use to fill the scrollbar in whole axis, otherwise it'll be of small size by default.
scrollBar.pack(side=RIGHT, fill=Y)

# Now we will create a text area. which will be inside center_frame
textArea = Text(center_frame, font=('FangSong', 14), width=50, height=17.5,
                yscrollcommand=scrollBar.set, fg='SlateGray1', bg='gray20')
# yscrollcommand is use to bind the scrollbar with the text area
textArea.pack(side=LEFT, fill=BOTH)

# Now we will create Entry field where we will type our chats
questionField = Entry(root, font=('Prestige Elite Std',
                                  14), fg='SlateGray1', bg='gray15')
questionField.pack(fill=X, pady=10)

# Now we will add button. and will add image on the button.
askImage = PhotoImage(file='ask_1.png')
askButton = Button(root, image=askImage, bg='gray10', activebackground='gray10',
                   bd=0, cursor='hand2', command=askbot)  # bd = border of the button
# activebackground is the color of button after the click
# cursor = 'hand2' will change the cursor to hand symbol on hovering over the button.

# we will use command method to attach a command with the ask button
# so that when we will ask any ques. the bot will answer it.
askButton.pack()


def enter_function(event):
    askButton.invoke()


# whenever we'll press enterkey this enter_function will be called. and this function will invoke the askButton.
# To bind the ask button with Enter key. so that on pressing Enter key the button will work.
root.bind('<Return>', enter_function)  # Enter is represented like Return.

# we'll also use loop for take_query() because if not then it will for only one time.
# but it has to run after every voice message.so that user can ask next query.
def repeat():
    while True:
        take_query()

'''
# take_query() 
# as of now every function run on the main thread which leads to slower down of the program
# so we'll run take_query() function on different thread.
# So for doing this we'll import threading and then pass a target as repeat() which is calling take_query() funct.
''' 
import threading
variable_thread = threading.Thread(target=repeat)
variable_thread.start()

root.mainloop()

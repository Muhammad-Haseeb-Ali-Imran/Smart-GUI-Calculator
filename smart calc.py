import tkinter
from tkinter import messagebox
import speech_recognition as speech# for speech recognition
wn=tkinter.Tk()
wn.title('GUI-Calculator')
wn.geometry('670x650')
inp=''
history=[]
wn.config(bg='grey')  # Dark Orchid
def cal():
    global inp
    try:
        ans=str(round(eval(inp),6))
        text.delete(0,'end')
        text.insert(0,ans)
        inp=ans
        history.append(ans)
    except:
        text.delete(0,'end')
        text.insert(0,'Error')
def clearr():
    global inp
    inp=''
    text.delete(0,'end')
def back():
    global inp
    inp=inp[:-1]
    text.delete(0,'end')
    text.insert(0,inp)
def hist():
    messagebox.showinfo("History", '\n'.join(history))
    '''
    global history
    try:
        text.delete(0,'end')
        text.insert(0,','.join(history))
    except:
        text.delete(0,'end')
        text.insert(0,'Error')
    '''
def inputt(txt):
    global inp
    inp+=str(txt)
    text.delete(0,"end")
    text.insert(0,inp)
def speech_recog():
    global inp
    instance=speech.Recognizer()
    with speech.Microphone() as source:
        instance.adjust_for_ambient_noise(source) # do not recognize background noise 
        messagebox.showinfo("Speech Recognition", "Listening... Please speak now.")
        data=instance.listen(source) # listen() is a method of Recognizer that records audio from an audio source.
    try:
        recognized_text=instance.recognize_google(data).lower()
        replacement={'plus': '+','minus': '-','times': '*','multiplied by': '*','multiply by': '*','x': '*','divided by': '/','divide by': '/','over': '/',
            'open bracket': '(','close bracket': ')','open parenthesis': '(','close parenthesis': ')','point': '.','dot': '.','sqrt': '**0.5'}
        for word,symbol in replacement.items():
            recognized_text=recognized_text.replace(word,symbol)
        recognized_text=recognized_text.replace(' ', '')
        inputt(recognized_text)
    except:
        messagebox.showerror("Speech Recognition", "Could not understand properly")
#styles = ['flat', 'raised', 'sunken', 'groove', 'ridge']
buttonback=tkinter.Button(text='⌫',command=lambda:back(),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=500,y=360)
buttonsqrt=tkinter.Button(text='√',command=lambda:inputt('**0.5'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=500,y=280)
button7=tkinter.Button(text='7',command=lambda:inputt('7'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=100,y=200)
button4=tkinter.Button(text='4',command=lambda:inputt('4'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=100,y=280)
button1=tkinter.Button(text='1',command=lambda:inputt('1'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=100,y=360)
button0=tkinter.Button(text='0',command=lambda:inputt('0'),height=2,width=5,font=('Arial',14),bd=5,relief='groove').place(x=100,y=440)
button8=tkinter.Button(text='8',command=lambda:inputt('8'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=200,y=200)
button5=tkinter.Button(text='5',command=lambda:inputt('5'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=200,y=280)
button2=tkinter.Button(text='2',command=lambda:inputt('2'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=200,y=360)
button9=tkinter.Button(text='9',command=lambda:inputt('9'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=300,y=200)
button6=tkinter.Button(text='6',command=lambda:inputt('6'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=300,y=280)
button3=tkinter.Button(text='3',command=lambda:inputt('3'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=300,y=360)
point=tkinter.Button(text='.',command=lambda:inputt('.'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=200,y=440)
clear=tkinter.Button(text='clear',command=lambda:clearr(),height=2,width=5,font=('Arial', 14),bd=5,relief='groove',bg='yellow').place(x=300,y=440)
divide=tkinter.Button(text='/',command=lambda:inputt('/'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=400,y=200)
multiply=tkinter.Button(text='*',command=lambda:inputt('*'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=400,y=280)
add=tkinter.Button(text='+',command=lambda:inputt('+'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=400,y=360)
sub=tkinter.Button(text='-',command=lambda:inputt('-'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=400,y=440)
bracket1=tkinter.Button(text='(',command=lambda:inputt('('),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=100,y=520)
bracket2=tkinter.Button(text=')',command=lambda:inputt(')'),height=2,width=5,font=('Arial', 14),bd=5,relief='groove').place(x=200,y=520)
equalto=tkinter.Button(text='=',command=lambda:cal(),height=2,width=15,font=('Arial', 14),bd=5,relief='groove').place(x=300,y=520)
his=tkinter.Button(text='History',command=lambda:hist(),height=2,width=5,font=('Arial', 14),bg='orange',bd=5,relief='groove').place(x=500,y=440)
speechrecognize=tkinter.Button(text='🎤', command=lambda:speech_recog(),height=2,width=5,font=('Aerial',13),bd=5,relief='groove').place(x=500,y=200)
text=tkinter.Entry(wn,width=30,font=('Arial',20),bd=20,relief='ridge')
text.place(x=100,y=80)


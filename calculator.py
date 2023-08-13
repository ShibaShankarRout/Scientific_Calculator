from tkinter import *

import math 

from pygame import mixer
 
#import speech_recognition

mixer.init()

def click(value):
	ex=entryField.get()#789 ex[0:len(ex)-1]
	answer=''


	try:


		if value=='C':
			ex=ex[0:len(ex)-1]#78
			entryField.delete(0,END)
			entryField.insert(0,ex)
			return

		elif value=='CE':
			entryField.delete(0,END)

		elif value=='√':
			answer=math.sqrt(eval(ex))

			

		elif value=='π':
			answer=math.pi

			

		elif value=='cos0':
			answer=math.cos(math.radians(eval(ex)))


		elif value=='tan0':
			answer=math.tan(math.radians(eval(ex)))

		elif value=='sin0':
			answer=math.sin(math.radians(eval(ex)))

		elif value=='2π':
			answer=2*math.pi

		elif value=='cosh':
			answer=math.cosh(eval(ex))

		elif value=='tanh':
			answer=math.tanh(eval(ex))

		elif value=='sinh':
			answer=math.sinh(eval(ex))

		elif value==chr(8731):
			answer=eval(ex)**(1/3)

		elif value=='x\u02b8':
			entryField.insert(END,'**')
			return

		elif value=='x\u00B3':
			answer=eval(ex) ** 3

		elif value=='x\u00B2':
			answer=eval(ex) ** 2

		elif value=='ln':
			answer=math.log2(eval(ex))

		elif value=='deg':
			answer=math.degrees(eval(ex))

		elif value=="rad":
			answer=math.radians(eval(ex))

		elif value=='e':
			answer=math.e

		elif value=='log₁₀':
			answer=math.log10(eval(ex)) 

		elif value=='x!':
			answer=math.factorial(eval(ex))

		elif value==chr(247):
			entryField.insert(END,"/")
			return

		elif value=='=':
			answer=eval(ex)

		else:

			entryField.insert(END,value)
			return


		entryField.delete(0,END)
		entryField.insert(0,answer)

	except SyntaxError:
		pass


def audio():
	mixer.music.load('music.mp3')
	mixer.music.play()

#	sr=speech_recognition.Recognizer()
#	with speech_recognition.Microphone()as m:
#		try:
#			sr.adjust_for_ambient_noise(m,duration=0.2)
#			voice=sr.listen(m)
#			text=sr.recognize_google(voice)
#			print(text)
#		except:
#			pass
root=Tk()
root.title('SMART CALCULATOR')
root.config(bg='gray')
root.geometry('530x400+100+100')


logoImage=PhotoImage(file='logo.png')
logoLabel=Label(root,image=logoImage,bg='cyan')
logoLabel.grid(row=0,column=1)


entryField=Entry(root,font=('arial',20,'bold'),bg='lightskyblue',fg='magenta',bd=15,relief=SUNKEN,width=20,command=audio())
entryField.grid(row=0,column=1,columnspan=14)


#micImage=PhotoImage(file="microph.png")
#micButton=Button(root,image=micImage,bd=0,bg='blue',activebackground='green',command=audio)
#micButton.grid(row=0,column=7)


button_text_list=["C","CE","√","+","π","cos0","tan0","sin0",
				  "1","2","3","-","2π","cosh","tanh","sinh",
				  "4","5","6","*",chr(8731),"x\u02b8","x\u00B3","x\u00B2",
				  "7","8","9",chr(247),"ln","deg","rad","e",
				  "0",".","%","=","log₁₀","(",")","x!"]

rowvalue=1
columnvalue=0
for i in button_text_list:

		button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='blue',fg='magenta',font=('arial,19,bold'),activebackground='yellow',command=lambda button=i:click(button))
		button.grid(row=rowvalue,column=columnvalue,pady=1)
		columnvalue+=1
		if columnvalue>7:
			rowvalue+=1
			columnvalue=0


root.mainloop()
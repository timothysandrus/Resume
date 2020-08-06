# This program implements the GUI for the software.
# card.py and Database.sql are required for this program to function properly.
# Written by Jesus Aguayo
# Final edit was made on May 4, 2020

import tkinter as tk		# Use for Python 3
from tkinter import ttk		# Use for Python 3
#import Tkinter as tk		# Use for Python 2
#import ttk					# Use for Python 2
import time
import card

LARGE_FONT = ("Verdana", 20)
LARGER_FONT = ("Verdana", 28)

currentNum = ""
currentClass = ""
currentInstructor = ""
currentTutor = ""
currentRating = ""
signIn = "Null"

# This class sets the properties of each page.
class CardReaderGUI(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.wm_title(self, "Card Reader")
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		self.frames = {}
		
		for F in (StartPage, ClassPage, InstructorPage, TutorPage, RatePage, SignInPage, SignOutPage, GetTAPage):
			
			frame = F(container, self)
			
			self.frames[F] = frame
			
			frame.grid(row = 0, column = 0, sticky = "nsew")
			
		self.show_frame(StartPage)

	# This function changes what page is  shown.
	def show_frame(self, cont, text = ""):

		global signIn
		global currentTutor
		
		frame = self.frames[cont]
		frame.tkraise()
		frame.postupdate()

		if (cont == SignInPage or cont == SignOutPage or cont == GetTAPage):

			self.after(3000, self.show_frame, StartPage)

		if (cont == StartPage):

			if (signIn == "In"):

				currentClass = text

				result = card.getcardnum(int(currentNum))[0][0]
				print(result)
				card.studentSignInLog(result, currentClass)

				print(currentClass)

			elif (signIn == "Out"):

				currentRating = text

				result = card.getcardnum(int(currentNum))[0][0]

				card.studentSignOutLog(result, int(currentTutor), currentRating)

				print(currentRating)

		if (cont == RatePage):

			currentTutor = text[0]
			print(currentTutor)

# This class waits for the user to scan their card. It is the Start Page.
class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		self.controller = controller
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Please Sign In/Out", font = LARGER_FONT)
		label.place(relx = .5, rely = .5, anchor = "center")

		self.box = ttk.Entry(self)
		self.box.bind('<Return>', self.getText)
		self.box.place(x = 10000, y = 10000)
		self.box.focus_set()

	# This function obtains the user's card number, and takes the user to the appropriate page.
	def getText(self, event):

		global currentNum
		global TANum

		userInput = event.widget.get()
		currentNum = userInput
		event.widget.delete(0, 'end')

		result = card.scan(int(userInput))

		if (result == "TA Sign Out"):

			self.controller.show_frame(SignOutPage)

		elif (result == "Student Sign Out"):

			self.controller.show_frame(TutorPage)

		elif (result == "TA Sign In"):

			self.controller.show_frame(SignInPage)

		elif (result == "Student Sign In"):

			self.controller.show_frame(ClassPage)

		elif (result == "Get TA"):

			self.controller.show_frame(GetTAPage)

	# This function is needed to refocus on the entry box.
	def postupdate(self):

		self.box.focus()

# This page is displayed when a TA signs in.
class SignInPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "You have signed in", font = LARGER_FONT)
		label.place(relx = .5, rely = .5, anchor = "center")

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		pass

# This page asks the user to have a TA sign in first.
class GetTAPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Please have a TA sign in first", font = LARGER_FONT)
		label.place(relx = .5, rely = .5, anchor = "center")

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		pass

# This page is displayed when a TA signs out.
class SignOutPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "You have signed out", font = LARGER_FONT)
		label.place(relx = .5, rely = .5, anchor = "center")

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		pass

# This class obtains a list of classes from card, and displays them. It is the Class Page.
class ClassPage(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Select Your Class", font = LARGE_FONT)
		label.pack(padx = 10, pady = 10)

		classes = card.getClasses()

		style = ttk.Style()
		style.configure('W.TButton', font = ('helvetica', 24))

		for i in classes:

			button1 = ttk.Button(self, text = i, style = 'W.TButton', command = lambda x = i: controller.show_frame(StartPage, x))
			button1.pack(fill = 'both', expand = 1)

		button2 = ttk.Button(self, text = "Other", style = 'W.TButton', command = lambda: controller.show_frame(StartPage, "Other"))
		button2.pack(fill = 'both', expand = 1)

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		global signIn

		signIn = "In"

# This class obtains a list of instructors from card2, and displays them. It is the Instructor Page.
class InstructorPage(tk.Frame):

	def __init__(self, parent, controller):
	
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Select Your Instructor", font = LARGE_FONT)
		label.pack(padx = 10, pady = 10)

		instructors = card.getteachers()

		style = ttk.Style()
		style.configure('W.TButton', font = ('helvetica', 24))

		for j in instructors:
		
			button1 = ttk.Button(self, text = j, style = 'W.TButton', command = lambda x = j: controller.show_frame(StartPage, x))
			button1.pack(fill = 'both', expand = 1)
		other = ttk.Button(self, text = "Other", style = 'W.TButton', command = lambda: controller.show_frame(StartPage, "Other"))
		other.pack(fill = 'both', expand = 1)

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		global signIn

		signIn = "In"

# This class obtains a list of tutors from card2, and displays them. It is the Tutor Page.
class TutorPage(tk.Frame):
	
	def __init__(self, parent, controller):

		self.controller = controller
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Select Your Tutor", font = LARGE_FONT)
		label.pack(padx = 10, pady = 10)

		tutors = card.getTAs()

		style = ttk.Style()
		style.configure('W.TButton', font = ('helvetica', 24))

		for k in tutors:
		
			button1 = ttk.Button(self, text = k, style = 'W.TButton', command = lambda x = k: controller.show_frame(RatePage, x))
			button1.pack(fill = 'both', expand = 1)

	# This function updates the TA list every time TutorPage is raised.
	def postupdate(self):

		global signIn

		tutors = card.getTAs()

		style = ttk.Style()
		style.configure('W.TButton', font = ('helvetica', 24))

		for widget in self.winfo_children():

			widget.destroy()

		label = ttk.Label(self, text = "Select Your Tutor", font = LARGE_FONT)
		label.pack(padx = 10, pady = 10)

		signIn = "Out"

		for k in tutors:

			button1 = ttk.Button(self, text = k, style = 'W.TButton', command = lambda x = k: self.controller.show_frame(RatePage, x))
			button1.pack(fill = 'both', expand = 1)


# This class prompts the user to rate their experience. It is the Rate Page.
class RatePage(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text = "Rate Your Experience", font = LARGE_FONT)
		label.pack(pady = 10, padx = 10)

		style = ttk.Style()
		style.configure('W.TButton', font = ('helvetica', 24))

		button1 = ttk.Button(self, text = "Good", style = 'W.TButton', command = lambda: controller.show_frame(StartPage, "Good"))
		button1.pack(fill = 'both', expand = 1)
		button2 = ttk.Button(self, text = "Bad", style = 'W.TButton', command = lambda: controller.show_frame(StartPage, "Bad"))
		button2.pack(fill = 'both', expand = 1)

	# This function does nothing, but is needed for window management.
	def postupdate(self):

		global signIn

		signIn = "Out"

# Creation of the main class.
app = CardReaderGUI()

# This allows the user to press the <Escape> key to exit the program.
app.bind("<Escape>", lambda e: e.widget.quit())

# Setting display properties.
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.overrideredirect(1)
app.geometry("%dx%d+0+0" % (w, h))
app.update()

# Main loop function provided by Tkinter.
app.mainloop()
import tkinter as tk


app = tk.Tk()
app.title("Login")
app.geometry("300x400")

def login():
	name = input_name.get()
	key = input_password.get()
	if not name or not key:
			app_title.config(text="name or key invalid")	


app_title = tk.Label(app,text="Login")
app_title.pack()

input_name = tk.Entry(app,width=30)
input_name.pack(pady=5)

input_password = tk.Entry(app,width=30,show="*")
input_password.pack(pady=6)

btn_login = tk.Button(app,text="login",fg="white",bg="blue",width=20,command=login)
btn_login.pack(pady=9)

app.mainloop()

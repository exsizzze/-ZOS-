_h='Введите номер функции'
_g='Импорт/Экспорт данных'
_f='Проверка сложности пароля'
_e='password_too_short'
_d='decryption_success'
_c='encryption_success'
_b='encryption_key'
_a='qr_code_saved'
_Z='data_exported'
_Y='data_imported'
_X='note_edited'
_W='note_deleted'
_V='note_added'
_U='requirements_not_met'
_T='password_strength'
_S='action_logged'
_R='import_export'
_Q='manage_notes'
_P='decrypt_text'
_O='encrypt_text'
_N='generate_qr'
_M='check_password'
_L='create_password'
_K='password_menu'
_J='random_string'
_I='video_download'
_H='password'
_G='choose_function'
_F='video_downloaded'
_E='notes_view'
_D='exit'
_C='y'
_B=True
_A='invalid_choice'
import os,json,random,string,time,qrcode
from cryptography.fernet import Fernet
from rich.console import Console
from rich.prompt import Prompt
upper=string.ascii_uppercase
lower=string.ascii_lowercase
digits=string.digits
symbols=string.punctuation
all_characters=lower+upper+digits+symbols
log_file='activity_log.txt'
console=Console()
language={'welcome':'Добро пожаловать в помощник...',_G:'Выберите функцию:',_H:'Пароли',_I:'Загрузка видео',_J:'Генерация случайной строки',_D:'Выход',_K:'Меню паролей',_L:'Создание пароля',_M:_f,_N:'Генерация QR-кода',_O:'Шифрование текста',_P:'Дешифрование текста',_Q:'Управление заметками',_R:_g,'edit_note':'Редактировать заметку',_A:'Неверный выбор.',_S:'Действие зафиксировано.',_T:'Сила пароля: {}',_U:'Требования не выполнены:',_V:'Заметка добавлена.',_E:'Ваши заметки:',_W:'Заметка удалена.',_X:'Заметка изменена.',_Y:'Данные импортированы.',_Z:'Данные экспортированы.',_F:'Видео загружено.',_a:'QR-код сохранен как {}.',_b:'Ключ шифрования сгенерирован.',_c:'Текст зашифрован.',_d:'Текст расшифрован.',_e:'Пароль слишком короткий.','check_password_strength':_f,'password_strength_requirements':'Пароль должен содержать минимум 8 символов, заглавные и строчные буквы, цифры и специальные символы.'}
def log_action(action):
	with open(log_file,'a')as A:A.write(f"{time.ctime()}: {action}\n")
	console.print(language[_S])
def show_menu():console.print('\n'+language[_G]);console.print('1. '+language[_H]);console.print('2. '+language[_I]);console.print('3. '+language[_J]);console.print('4. '+language[_N]);console.print('5. '+language[_O]);console.print('6. '+language[_P]);console.print('7. '+language[_Q]);console.print('8. '+language[_R]);console.print('9. '+language[_D])
def password_menu():console.print('\n'+language[_K]);console.print('1. '+language[_L]);console.print('2. '+language[_M]);console.print('3. '+language[_D])
def generate_password(length,count,use_upper=_B,use_lower=_B,use_digits=_B,use_symbols=_B):
	A=''
	if use_upper:A+=upper
	if use_lower:A+=lower
	if use_digits:A+=digits
	if use_symbols:A+=symbols
	if not A:console.print(language[_A]);return[]
	B=[]
	for D in range(count):C=''.join(random.sample(A,length));B.append(C)
	return B
def save_to_file(name,data):
	with open(name,'w')as A:json.dump(data,A)
	console.print(f"{language[_Z]} {name}")
def load_from_file(name):
	A=name
	if os.path.exists(A):
		with open(A,'r')as B:C=json.load(B)
		console.print(f"{language[_Y]} {A}");return C
	else:console.print(language[_A]);return
def generate_qr_code(data,filename):B=filename;A=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4);A.add_data(data);A.make(fit=_B);C=A.make_image(fill_color='black',back_color='white');C.save(B);D=os.path.abspath(B);console.print(language[_a].format(D))
def encrypt_text(text,key):A=Fernet(key);B=A.encrypt(text.encode());return B
def decrypt_text(encrypted_text,key):A=Fernet(key);B=A.decrypt(encrypted_text).decode();return B
def generate_key():A=Fernet.generate_key();console.print(language[_b]);return A
def check_password_strength(password):
	C=password;A=0;B=[]
	if len(C)>=8:A+=1
	else:B.append(language[_e])
	if any(A.isupper()for A in C):A+=1
	else:B.append('должен содержать хотя бы одну заглавную букву.')
	if any(A.islower()for A in C):A+=1
	else:B.append('должен содержать хотя бы одну строчную букву.')
	if any(A.isdigit()for A in C):A+=1
	else:B.append('должен содержать хотя бы одну цифру.')
	if any(A in symbols for A in C):A+=1
	else:B.append('должен содержать хотя бы один специальный символ.')
	D=['Слабый(1/5)','Средний(2/5)','Сильный(3/5)','Очень сильный(4/5)','Чрезвычайно сильный(5/5)'][A-1];return D,B
def manage_notes():
	A=[]
	while _B:
		console.print('\nУправление заметками');console.print('1. Добавить заметку');console.print('2. Просмотреть заметки');console.print('3. Удалить заметку');console.print('4. Редактировать заметку');console.print('5. Вернуться в главное меню');B=int(Prompt.ask('Выберите действие'))
		if B==1:D=Prompt.ask('Введите текст заметки');A.append(D);console.print(language[_V]);log_action(f"Добавлена заметка: {D}")
		elif B==2:
			console.print(language[_E])
			for(F,D)in enumerate(A):console.print(f"{F+1}. {D}")
		elif B==3:
			console.print(language[_E]);C=int(Prompt.ask('Введите номер заметки для удаления'))-1
			if 0<=C<len(A):G=A.pop(C);console.print(language[_W]);log_action(f"Удалена заметка: {G}")
			else:console.print(language[_A])
		elif B==4:
			console.print(language[_E]);C=int(Prompt.ask('Введите номер заметки для редактирования'))-1
			if 0<=C<len(A):E=Prompt.ask('Введите новый текст заметки');A[C]=E;console.print(language[_X]);log_action(f"Изменена заметка: {E}")
			else:console.print(language[_A])
		elif B==5:break
		else:console.print(language[_A])
while _B:
	show_menu();func=int(Prompt.ask(_h))
	if func==1:
		while _B:
			password_menu();vp=int(Prompt.ask(_h))
			if vp==1:
				length=int(Prompt.ask('Введите длину пароля'));count=int(Prompt.ask('Сколько паролей вы хотите сгенерировать? '));use_upper=Prompt.ask('Использовать заглавные буквы? (y/n)',default=_C).lower()==_C;use_lower=Prompt.ask('Использовать строчные буквы? (y/n)',default=_C).lower()==_C;use_digits=Prompt.ask('Использовать цифры? (y/n)',default=_C).lower()==_C;use_symbols=Prompt.ask('Использовать специальные символы? (y/n)',default=_C).lower()==_C;passwords=generate_password(length,count,use_upper,use_lower,use_digits,use_symbols);console.print('Сгенерированные пароли:')
				for pwd in passwords:console.print(pwd)
				save_option=int(Prompt.ask('Хотите ли вы сохранить пароли в файл? 1. Да 2. Нет: '))
				if save_option==1:filename=Prompt.ask('Введите название файла для сохранения');save_to_file(filename+'.json',passwords)
				log_action(f"Сгенерированы {count} паролей длиной {length}.")
			elif vp==2:
				password=Prompt.ask('Введите пароль для проверки');strength_rating,requirements=check_password_strength(password);console.print(language[_T].format(strength_rating))
				if requirements:
					console.print(language[_U])
					for req in requirements:console.print('-',req)
				log_action(f"Проверка пароля: {password}. Рейтинг: {strength_rating}.")
			elif vp==3:break
			else:console.print(language[_A])
	elif func==2:
		console.print('Выберите откуда вы хотите загрузить видеоролик:');console.print('1. YouTube');console.print('2. RuTube');video_source=int(Prompt.ask('Введите номер источника'))
		if video_source==1:console.print(language[_F]);log_action('Загрузка видео с YouTube.')
		elif video_source==2:console.print(language[_F]);log_action('Загрузка видео из RuTube.')
		else:console.print(language[_A])
	elif func==3:length=int(Prompt.ask('Введите длину случайной строки'));random_string=''.join(random.choice(lower+upper+digits)for A in range(length));console.print(f"Сгенерированная строка: {random_string}");log_action(f"Сгенерирована случайная строка длиной {length}.")
	elif func==4:data=Prompt.ask('Введите данные для QR-кода');filename=Prompt.ask('Введите имя файла для сохранения QR-кода (например, qr_code.png)');generate_qr_code(data,filename)
	elif func==5:text=Prompt.ask('Введите текст для шифрования');key=generate_key();encrypted_text=encrypt_text(text,key);console.print(language[_c]);console.print(f"Зашифрованный текст: {encrypted_text}")
	elif func==6:
		encrypted_text=Prompt.ask('Введите зашифрованный текст');key=Prompt.ask('Введите ключ для расшифрования')
		try:decrypted_text=decrypt_text(encrypted_text.encode(),key.encode());console.print(language[_d]);console.print(f"Расшифрованный текст: {decrypted_text}")
		except Exception as e:console.print('Ошибка расшифрования:',e)
	elif func==7:manage_notes()
	elif func==8:console.print(_g)
	elif func==9:console.print(language[_D]);break
	else:console.print(language[_A])
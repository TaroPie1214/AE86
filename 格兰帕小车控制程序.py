import tkinter as tk
 
master = tk.Tk()
 
master.title('格兰帕控制程序')

master.geometry('500x600')
def stright():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('2')

def left():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('1')

def right():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('3')

def bleft():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('4')

def bstright():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('5')
        
def bright():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('6')

def nbleft():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('7')

def stop():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('8')

def nbright():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('9')

def soundon():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('10')

def soundoff():
    f_path=r'E:\XunLei\666.txt'
 
    with open(f_path,'w') as f:
        f.write('11')


 
b1 = tk.Button(master, text="Left", command=left)
b1.pack()

b2 = tk.Button(master, text="Stright", command=stright)
b2.pack()

b3 = tk.Button(master, text="Right", command=right)
b3.pack()

b4 = tk.Button(master, text="B-Left", command=bleft)
b4.pack()

b5 = tk.Button(master, text="B-Stright", command=bstright)
b5.pack()

b6 = tk.Button(master, text="B-Right", command=bright)
b6.pack()

b7 = tk.Button(master, text="NB-Left", command=nbleft)
b7.pack()

b8 = tk.Button(master, text="Stop", command=stop)
b8.pack()

b9 = tk.Button(master, text="NB-Right", command=nbright)
b9.pack()

b10 = tk.Button(master, text="Sound-on", command=soundon)
b10.pack()

b11 = tk.Button(master, text="Sound-off", command=soundoff)
b11.pack()

master.mainloop()
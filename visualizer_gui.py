import tkinter as tk
import numpy as np
import time

class App(tk.Tk):

    def __init__(self):
        # initialize tk
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.flag = 0
        self.values = {1:"bubble",2:"selection",3:"insertion"}
        self.data = []
        self.colors = []
        # declare widgets
        self.top_frame = tk.Frame(self,width=200,height=10)
        label = tk.Label(self.top_frame,text="Select a sorting algorithm",font=("Ubuntu",20))
        self.methods_frame = tk.Frame(self,width=200)
        bubble = tk.Button(self.methods_frame,text="Bubble Sort",activebackground="green",font=("Ubuntu",15),bd=2,relief="raised",command=self.bubble)
        selection = tk.Button(self.methods_frame,text="Selection Sort",activebackground="green",font=("Ubuntu",15),bd=2,relief="raised",command=self.selection)
        insertion = tk.Button(self.methods_frame,text="Insertion Sort",activebackground="green",font=("Ubuntu",15),bd=2,relief="raised",command=self.insertion)
        self.canvas = tk.Canvas(self,width=1000,height=600,bg="white")
        self.options_frame = tk.Frame(self,width=700)
        self.max = tk.Scale(self.options_frame,from_=10,to=500,orient="horizontal",label="max element : ",font=("Ubuntu",10),sliderlength=50,length=150)
        self.num = tk.Scale(self.options_frame,from_=5,to=100,orient="horizontal",label="No. of elements : ",font=("Ubuntu",10),sliderlength=50,length=150)
        generate = tk.Button(self.options_frame,text="Generate Numbers",activebackground="green",font=("Ubuntu",10),bd=2,relief="raised",command=self.generate)
        self.start = tk.Button(self,text="Start",activebackground="green",font=("Ubuntu",20),bd=2,relief="raised",width=30,command=self.start_sort)
        self.clear = tk.Button(self,text="Clear",activebackground="green",font=("Ubuntu",20),bd=2,relief="raised",width=30,command=self.clear_all)

        # grid structure
        self.top_frame.grid(row=0,column=1,padx=2,pady=2,sticky="w")
        self.methods_frame.grid(row=1,column=1,padx=2,pady=2,sticky="w")
        label.pack(side="left")
        bubble.grid(row=0,column=0,padx=2,pady=2)
        selection.grid(row=0,column=1,padx=2,pady=2)
        insertion.grid(row=0,column=2,padx=2,pady=2)
        self.canvas.grid(row=3,columnspan=2,padx=2,pady=2)
        self.options_frame.grid(row=0,column=0,padx=2,pady=2,rowspan=2,sticky="w")
        self.max.grid(row=0,column=1,sticky="w",padx=2,pady=2)
        self.num.grid(row=0,column=0,sticky="w",padx=2,pady=2)
        generate.grid(row=1,padx=2,pady=2,columnspan=2)
        self.start.grid(row=2,column=0,padx=2,pady=2)
        self.clear.grid(row=2,column=1,padx=2,pady=2)

    def bubble(self):
        self.flag = 1
    
    def selection(self):
        self.flag = 2

    def insertion(self):
        self.flag = 3
    
    def generate(self):
        self.data = []
        self.canvas.delete("all")
        max = self.max.get()
        num = self.num.get()
        self.data = np.random.randint(max,size=num)
        self.colors = ["red" for i in range(num)]
        self.Draw(self.colors)
        
    def clear_all(self):
        self.flag=0
        self.num.set(5)
        self.max.set(10)
        self.data = []
        self.canvas.delete("all")

    def start_sort(self):
        flag = self.flag
        if flag==0:
            return
        elif flag==1:
            self.bubblesort()
        elif flag==2:
            self.selectionsort()
        else:
            self.insertionsort()
        self.Draw(["green" for i in range(len(self.data))])
    
    def Draw(self,colors):
        self.canvas.delete("all")
        c_height = 600
        c_width = 1000
        temp = self.data*(501 // np.max(self.data))
        x_width = c_width / (2*len(self.data))
        val = 0
        offset = x_width / 2
        for i,height in enumerate(self.data):
            x1 = val * x_width + offset
            y1 = c_height - temp[i]
            x2 = (val+1)*x_width + offset
            y2 = c_height
            self.canvas.create_rectangle(x1,y1,x2,y2,fill=colors[i])
            self.canvas.create_text(x1+2,y1,anchor='sw',text=str(height))
            val += 2
        self.update_idletasks()

    def bubblesort(self):
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-1):
                self.Draw(["green" if k==j or k==j+1 else "red" for k in range(len(self.data))])
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]            
                time.sleep(0.5)
                self.Draw(["green" if k==j or k==j+1 else "red" for k in range(len(self.data))])

    def selectionsort(self):
        for i in range(len(self.data)):
            min = i
            for j in range(i+1,len(self.data)):
                if self.data[min] > self.data[j]:
                    min = j
            self.Draw(["green" if k==i or k==min else "red" for k in range(len(self.data))])
            self.data[i], self.data[min] = self.data[min], self.data[i]
            time.sleep(0.5)
            self.Draw(["green" if k==i or k==min else "red" for k in range(len(self.data))])
    
    def insertionsort(self):
        for i in range(len(self.data)):
            key = self.data[i]
            j = i-1
            while j>=0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                time.sleep(0.5)
                self.Draw(["green" if k==j or k==j+1 else "red" for k in range(len(self.data))])
                j -= 1
            self.data[j+1] = key   
            self.Draw(["green" if k==j or k==j+1 else "red" for k in range(len(self.data))])


app = App()
app.title("Sorting Visualizer")
app.mainloop()
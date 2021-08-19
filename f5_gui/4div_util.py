import tkinter


root = tkinter.Tk()
cv_width = 800
cv_height = 400

canvas = tkinter.Canvas(width=cv_width,height= cv_height)
canvas.pack()
text = tkinter.Label(text="Hello world")
text.pack()
button = tkinter.Button(text = "1.품목명별 정보 출력",width=20,height=1)
button.place(x=100,y=100)

root.mainloop()
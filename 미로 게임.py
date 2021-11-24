from tkinter import *
from tkinter import messagebox
import random
import time
a = time.time()
check = True

class Player():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="red")
        self.x, self.y = x, y
        self.nx, self.ny = x, y


    def move(self, direction):

        global check
        # 키보드에서 누른 키에 따라서 움직임
        # 키보드에서 누른 키에 따라서 움직임
        if direction == 'w' and check:
            self.nx, self.ny = self.x, self.y - 1
        elif direction == 'a' and check:
            self.nx, self.ny = self.x - 1, self.y
        elif direction == 's' and check:
            self.nx, self.ny = self.x, self.y + 1
        elif direction == 'd' and check:
            self.nx, self.ny = self.x + 1, self.y



        # 이동한 곳이 벽이 아닐 경우 이동시키며 x, y 갱신
        if not self.is_collide():
            self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
            self.x, self.y = self.nx, self.ny
        if map[self.y][self.x] == 2:
            check =True

        if map[self.y][self.x] == 3:
            check = False
            messagebox.showinfo(title="성공", message="미로 찾기에 성공하셨습니다")
            end = time.time()
            global a
            result = 0
            result=end-a
            sec=0
            min=0
            sec=result%60
            min=result/60
            messagebox.showinfo(message="%d분%d초 걸렸습니다." %(min,sec))

        if map[self.y][self.x] == 4:
            check = False
            root2 = Tk()
            root2.title("주사위 던지기 게임")
            root2.geometry("300x200")
            num = random.randint(1, 6)
            lbl = Label(root2, text="주사위를 굴리세요", font="Arial 20")
            lbl.pack()


            def rollclick():
                global check
                lbl["text"] = random.randint(1, 6)
                if lbl["text"] % 2 == 0:
                    messagebox.showinfo(message="다시 던지세요")
                    check = False
                else:
                    messagebox.showinfo(message="지나가도 좋습니다")
                    check = True


            num = random.randint(1, 6)
            roll = Button(root2, text="roll", command=rollclick)
            roll.pack()

        if map[self.y][self.x] == 5:
            root3 = Tk()
            check = False

            def enter():
                su = int(e.get())
                global check
                check = False

                if su<num:
                    check = False
                    text['text'] = "그 숫자보다 큽니다"
                elif su>num:
                    check = False
                    text['text'] = "그 숫자보다 작습니다"
                else:
                    check = True
                    messagebox.showinfo(title="성공", message="정답을 맞추셨습니다. 지나가셔도 좋습니다.")

            text = Label(root3, text ="1~10까지 숫자를 적어주세요")
            text.pack()

            e=Entry(root3)
            e.pack()

            num =random.randint(1,10)

            b1 = Button(root3, text="입력",command=enter)
            b1.pack()

            root3.mainloop()

        if map[self.y][self.x] == 6:
            check = False
            root4 = Tk()
            secret=''
            secretLen = 3
            secretList = random.sample(range(10), secretLen)

            for i in range(secretLen):
                secret += str(secretList[i])

            try1 = 0
            def enter():
                global check
                nonlocal try1

                guess = str(e.get())
                try1 += 1
                c=0
                strike=0
                ball=0

                for c in range(secretLen):
                    if secret[c] == guess[c]:
                        strike +=1
                    elif secret[c] in guess:
                        ball += 1
                if guess!= secret:
                    check = False
                    text['text'] = str(strike)+"strike"+str(ball)+"ball"
                elif guess == secret:
                    check = True
                    messagebox.showinfo(title="성공", message="%d번만에 정답을 맞추셨습니다. 지나가셔도 좋습니다." %try1)

            text = Label(root4, text ="3자리 숫자를 맞춰 보세요")
            text.pack()

            e=Entry(root4)
            e.pack()

            num =random.randint(1,10)

            b1 = Button(root4, text="입력",command=enter)
            b1.pack()

            root4.mainloop()

        if map[self.y][self.x] == 7:
            messagebox.showinfo(message="백의 자리 : 5")

        if map[self.y][self.x] == 8:
            check = False
            root5= Tk()
            num1="586"

            def enter():
                su = str(e.get())
                for s in range(3):
                    if su[s] == num1[s]:
                        c=True
                    else:
                        c=False
                if(c):
                    messagebox.showinfo(title="성공", message="정답을 맞추셨습니다. 지나가셔도 좋습니다.")
                else:
                    text['text'] = "틀렸습니다. 다시 입력하세요"

            text = Label(root5,text="비밀번호는? (힌트 : 같은 모양의 도형을 찾아보세요)")
            text.pack()

            e = Entry(root5)
            e.pack()


            b2 = Button(root5, text="입력", command=enter)
            b2.pack()

            root.mainloop()

        if map[self.y][self.x] == 9:
            messagebox.showinfo(message="십의 자리 : 8")

        if map[self.y][self.x] == 10:
            messagebox.showinfo(message="일의 자리 : 6")

    # 이동한 곳이 벽인지 아닌지 판별
    def is_collide(self):
        if map[self.ny][self.nx] == 1:
            return True
        else:
            return False


# 키리스너 이벤트
def keyEvent(event):
    player.move(repr(event.char).strip("'"))

root = Tk()
root.title("미로 찾기 게임")
root.resizable(False, False)

# 목숨 갯수 변수가 i이고 어떤 조건에 의해서 라이프 차감되면



# 창 너비, 높이, 위치 설정
width, height = 540, 540
x, y = (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2
root.geometry("%dx%d+%d+%d" % (width, height, x, y))


# canvas를 추가하고 키이벤트를 부착
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.bind("<Key>", keyEvent)
canvas.focus_set()
canvas.pack()

# 1 : 벽, 2 : 플레이어 시작 지점, 3 : 골인 지점
map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
    [1,2,0,1,0,1,1,0,1,1,0,0,1,0,0,0,1,3,],
    [1,0,0,1,0,0,5,1,1,0,1,0,1,1,1,0,0,0,],
    [1,1,6,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,],
    [1,0,0,1,0,1,0,1,0,0,1,1,8,0,0,1,0,0,],
    [0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,],
    [0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,],
    [0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,],
    [1,0,0,4,1,1,0,0,1,10,1,0,0,1,0,1,0,1],
    [0,0,1,0,1,0,0,1,1,1,4,0,1,1,6,1,0,0,],
    [1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,],
    [0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,],
    [1,1,1,5,1,0,0,0,1,0,0,1,1,0,0,1,0,0,],
    [0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,],
    [1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,4,0,],
    [1,7,0,0,0,1,1,0,6,1,1,9,1,1,0,0,0,1,],
    [1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,],
    [1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,]
]

# canvas에 맵을 그림
for y in range(len(map[0])):
    for x in range(len(map[y])):
        if map[y][x] == 1:
            canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="black")
        elif map[y][x] == 2:
            player = Player(canvas, x, y)
        elif map[y][x] == 3:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="blue")
        elif map[y][x] == 4:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="yellow")
        elif map[y][x] == 5:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="black")
        elif map[y][x] == 6:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="orange")
        elif map[y][x] == 7:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="red")
        elif map[y][x] == 8:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="green")
        elif map[y][x] == 9:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="pink")
        elif map[y][x] == 10:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="Brown")

root.mainloop()

import tkinter
from tkinter import messagebox
total_trades = 0
win_trade = 0
lose_trade = 0
FONT = ("Arial", 16, "bold")


window = tkinter.Tk()
window.title("Trades calculator")
window.minsize(500, 500)
window.maxsize(500, 500)

def winning_trade():
    global total_trades, win_trade
    total_trades += 1
    win_trade += 1
    trades_num_label.config(text=total_trades)
    win_num_label.config(text=win_trade)


def losing_trade():
    global total_trades, lose_trade
    total_trades += 1
    lose_trade += 1
    trades_num_label.config(text=total_trades)
    lose_num_label.config(text=lose_trade)


def calculate_ratio():
    winning_ratio = (win_trade * 100) / total_trades
    losing_ratio = (lose_trade * 100) / total_trades
    message = f"Total Trades = {total_trades}/100%\n" \
              f"Winning Trades = {win_trade}/{round(winning_ratio, 1)}%\n" \
              f"Losing Trades = {lose_trade}/{round(losing_ratio, 1)}%"
    messagebox.showinfo(title="Win/Lose Ratio", message=message)
    
trades_label = tkinter.Label(text="Trades", font=FONT, bg="#5d6c71")
trades_label.place(x=220, y=100)

trades_num_label = tkinter.Label(text=total_trades, font=FONT, bg="#25383e", fg="White")
trades_num_label.place(x=250, y=160)

win_button = tkinter.Button(text="Win Trade", bg="Green", command=winning_trade)
win_button.place(x=380, y=400)

win_num_label = tkinter.Label(text=win_trade, font=FONT, bg="#202b2f", fg="White")
win_num_label.place(x=400, y=360)

lose_button = tkinter.Button(text="Lose Trade", bg="Red", command=losing_trade)
lose_button.place(x=75, y=400)

lose_num_label = tkinter.Label(text=lose_trade, font=FONT, bg="#262f36", fg="White")
lose_num_label.place(x=100, y=360)

calculate = tkinter.Button(text="Calculate", command=calculate_ratio)
calculate.place(x=230, y=460)


window.mainloop()

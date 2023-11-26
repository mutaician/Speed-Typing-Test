import tkinter as tk
import random

words_to_type = []
with open("data.txt", "r") as f:
    for line in f:
        words_to_type.append(line.strip())

random_words = random.sample(words_to_type, 100)

time_to_type = 60

def update_time():
    global time_to_type
    if time_to_type > 0:
        time_to_type -= 1
        timer_label.config(text=f"{time_to_type}")
        root.after(1000, update_time)
    else:
        text_entry.config(state=tk.DISABLED)
        text_input = text_entry.get()
        timer_label.config(text=f"Time's up!\n Score: {check_words(text_input)}wpm")


def check_words(text: str):
    count = 0
    for word in text.split():
        if word in random_words:
            count += 1 
    # words = text.count(" ") + 1
    return count

def key_check(event):
    t_char = event.char
    text_content = text.get('1.0', 'end')
    index = text_entry.index(tk.INSERT)
    # if event.keysym == 'BackSpace':
    #     print('space')
    #     text.tag_add(f'char{index}', f'1.{index-1}', f'1.{index}')
    #     text.tag_config(f'char{index}', foreground='black')
    if t_char == text_content[index]:
        text.tag_add(f'char{index}', f'1.{index}', f'1.{index+1}')
        text.tag_config(f'char{index}', foreground='green')
    elif t_char!= text_content[index]:
        text.tag_add(f'char{index}', f'1.{index}', f'1.{index+1}')
        text.tag_config(f'char{index}', foreground='red')
    
def start_type():
    text_entry.config(state='normal')
    update_time()
    start_button.config(state=tk.DISABLED)
    text_entry.bind('<Key>', key_check)

root = tk.Tk()
root.title("Typing master")
root.geometry("900x700")
root.configure(background='aqua')

msg = random_words

text = tk.Text(root, width=60, height=13, wrap='word', padx=20, pady=20)
text.insert(tk.END, msg)
text.config(state=tk.DISABLED, font=("Courier New", 20), background='white')
text.pack()

text_entry = tk.Entry(root, width=50, justify='center', font=('Courier New', 15))
text_entry.config(state='disabled')
text_entry.focus_set()

text_entry.pack()

timer_label = tk.Label(root, text=f"{time_to_type}")
timer_label.config(font=("Arial", 27))
timer_label.pack()

start_button = tk.Button(root, text="Start", width=10, height=5, bg='green',bd=0,command=start_type)
start_button.configure(borderwidth=0, highlightthickness=0, highlightbackground='red', highlightcolor='red')
start_button.pack()


root.mainloop()
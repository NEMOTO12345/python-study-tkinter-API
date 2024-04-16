import requests
import json
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext
import re







root = tk.Tk()
root.title("本のAPIアプリ")
root.minsize(400,300)


u = tk.Label(text="本のISBNを入力")
u.pack()
entry1 = tk.Entry(width=40)
entry1.pack()


#画面上のテキストを設定1
static1 = tk.Label(text="内容")
static1.pack()

#セレクトボックス(コンボボックス)を作る
combo = ttk.Combobox(root, state='readonly')
# セレクトボックスの選択値を設定
combo["values"] = ("title", "authors", "publisher", "description")
# デフォルトの値をA(index=0)に設定　"タイトル", "著者", "出版社", "説明"
combo.current(0)
# コンボボックスの配置
combo.pack()

result = tkinter.scrolledtext.ScrolledText(width = 30,height=10)
def get_value(event):
    result.delete("1.0", tk.END)
    entry1_value = entry1.get()
    if entry1_value == '':
        result.insert(tk.END,'入力してください')
    else:
        i = re.search(r"^[0-9]{13}$",entry1_value)
        if i == None:
            result.insert(tk.END,'入力が間違っています。')
        else:
            combo_value = combo.get()
            res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{entry1_value}")
            temp = json.loads(res.text)
            books_data = temp["items"]
            for i in books_data:
                li = i
        #ならば辞書を一気に書き出そう
            for k,v in li.items():
                if (k == "volumeInfo"):
                    for k2, v2 in v.items():
                        if k2 == combo_value:
                            result.insert(tk.END,v2)
                    
                # if(k2 in [f"{combo_value}"]):
                #     result.insert(k2,v2)

# 9784295016052

    

#ボタン
btn = tk.Button(text="検索")
btn.bind("<1>", get_value)
btn.pack()



result.pack()

root.mainloop()
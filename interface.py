from tkinter import *
from backend import *

janela = Tk()
janela.title('Notícias')
janela['background'] = 'black'
janela['padx'] = 20
janela['pady'] = 20


main = Frame(janela)
buttons = Frame(janela)


subjectVar = StringVar()
subjectVar.set('')


l_title = Label(main, text='Agregador de Notícias')

l_subject = Label(main, text='Assunto')
e_subject = Entry(main, textvariable=subjectVar)

l_results = Label(main, text='Resultados da Pesquisa')
lb_news = Listbox(main)
lb_news.bind('<Double-1>', lambda event: newsDetails(lb_news))

e_subject.bind('<Return>', lambda event: searchNews(subjectVar, lb_news))




main['background'] = 'black'
buttons['background'] = 'black'

l_title['font'] = ('Roboto Slab', 20, 'bold')
l_title['bg'] = 'black'
l_title['fg'] = 'yellow'
l_subject['font'] = ('Roboto Slab', 10)
l_subject['bg'] = 'black'
l_subject['fg'] = 'yellow'
e_subject['font'] = ('Roboto Slab', 12)
e_subject['bg'] = 'black'
e_subject['fg'] = 'yellow'
e_subject['width'] = 100
l_results['font'] = ('Roboto Slab', 10)
l_results['bg'] = 'black'
l_results['fg'] = 'yellow'
lb_news['font'] = ('Roboto Slab', 12)
lb_news['bg'] = 'black'
lb_news['fg'] = 'grey99'
lb_news['width'] = 100




main.pack()
buttons.pack()

l_title.pack(pady=(5,10))
l_subject.pack(anchor=W, pady=(5,2))
e_subject.pack(pady=(5,10))
l_results.pack(anchor=W, pady=(5,2))
lb_news.pack(pady=(5,10))


janela.mainloop()
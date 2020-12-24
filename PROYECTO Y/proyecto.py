import tkinter#libreria para graficar
from tkinter import ttk#libreria para graficar lienzo

ventana=tkinter.Tk()#creacion de la ventana
ventana.geometry("1100x600")#tamaño de la ventana
ventana.title("polleria")#creacion de titulo de ventana


lamina=tkinter.Frame(ventana)#creacion de una lamina
lamina.pack(fill="both", expand=1)#empaquetado de la lamina

myCanvas=tkinter.Canvas(lamina)#creacion de un lienzo
myCanvas.pack(side="left", fill="both", expand=1)#empaquetado e lienzo
myCanvas.configure(bg="black")#color fondo negro

myScrollbar=ttk.Scrollbar(lamina, orient="vertical", command=myCanvas.yview)#creacion de la barra menu
myScrollbar.pack(side="right", fill="y")#empaquetado de la barra

myCanvas.configure(yscrollcommand=myScrollbar.set)#configuracion de barra de menu
myCanvas.bind( lambda e: myCanvas.configure(scrollregion= myCanvas.bbox('all')))#configuracion de barra de menu

segundaLamina=tkinter.Frame(myCanvas)#creacion de una lamina y agregado al lienzo


lamina=tkinter.Frame(segundaLamina )#creacion de una lamina y lo agrego a la segunda lamina
lamina.pack(fill="both", expand=1)#rellena toda la ventana 
lamina.config(bg="black")#ponieno color fondo negro
lamina.config(width="800", height="350")#tamaño a la lamina
lamina.config(cursor="hand2")#cursor en forma de mano


fuentePantallas=("Comic Sans MS", 30)#creacion de una variable para la letra y tamaño

titulo=tkinter.Label(lamina, text="BIENVENIDOS A LA POLLERIA 'POLLOS HERMANOS' ", font=fuentePantallas)#creacion de una etiqueta label 
titulo.grid(row=1, column=1, columnspan=4)#empaquetado de en orma de rejilla
titulo.config(bg="black", fg="white", width=45)#color tamaño fondo 

imagen=tkinter.PhotoImage(file="imagenPollo.gif")#creacion d euna var#iable imagen


imagenLabel=tkinter.Label(lamina, image=imagen)#creacion de una etiqueta label imagen
imagenLabel.config(width="200", height="450")# dando tamaño a la imagen
imagenLabel.grid(row=2, column=1, columnspan=4)#empaquetado y agreagdo a la lamina,dando posicion en la lamina

menuLabel=tkinter.Label(lamina, text="OFRECEMOS:", font=fuentePantallas)#creacion de etiqueta label ofrecemos
menuLabel.grid(row=3, column=1, columnspan=4)#empaquetado y agreagdo a la lamina,dando posicion en la lamina
menuLabel.config(fg="white", bg="black")#dando color a letra y fond
#===========================================================================
								#calculos
unPoBra=tkinter.IntVar()
medioPoBra=tkinter.IntVar()
cuartoPoBra=tkinter.IntVar()
octavoPoBra=tkinter.IntVar()

unPoBro=tkinter.IntVar()
medioPoBro=tkinter.IntVar()
cuartoPoBro=tkinter.IntVar()
octavoPoBro=tkinter.IntVar()

dosLiGa=tkinter.IntVar()
unLiMeGa=tkinter.IntVar()
unLiGa=tkinter.IntVar()
medioLiGa=tkinter.IntVar()

dosLiCh=tkinter.IntVar()
unLiCh=tkinter.IntVar()
medioLiCh=tkinter.IntVar()
vasoLiCh=tkinter.IntVar()

calGa=tkinter.IntVar()
calPo=tkinter.IntVar()

def opciones():

	opcionEscogida=""
	total=0

	if(unPoBra.get()==1):

		total=total+60
		opcionEscogida=opcionEscogida + "1 Pollo Brasa s/. 60.00\n"

	if(medioPoBra.get()==1):

		total=total+30
		opcionEscogida=opcionEscogida + "1/2 Pollo Brasa s/. 30.00\n"

	if(cuartoPoBra.get()==1):

		total=total+15
		opcionEscogida=opcionEscogida + "1/4 Pollo Brasa s/. 15.00\n"	

	if(octavoPoBra.get()==1):

		total=total+8
		opcionEscogida=opcionEscogida + "1/8 Pollo Brasa s/. 8.00\n"	

	if(unPoBro.get()==1):	

		total=total+100
		opcionEscogida=opcionEscogida + "1 pollo Broaster s/. 100.00\n"

	if(medioPoBro.get()==1):

		total=total+50
		opcionEscogida=opcionEscogida + "1/2 pollo Broaster s/. 50.00\n"

	if(cuartoPoBro.get()==1):

		total=total+25
		opcionEscogida=opcionEscogida + "1/4 pollo Broaster s/. 25.00\n"

	if(octavoPoBro.get()==1):

		total=total+13
		opcionEscogida=opcionEscogida + "1/8 pollo Broaster s/. 13.00\n"

	if(dosLiGa.get()==1):

		total=total+10
		opcionEscogida=opcionEscogida + "2 Litros de Gaseosa s/. 10.00\n"

	if(unLiMeGa.get()==1):

		total=total+8
		opcionEscogida=opcionEscogida + "1 Litro 1/2 de Gaseosa s/. 8.00\n"	

	if(unLiGa.get()==1):

		total=total+5
		opcionEscogida=opcionEscogida + "1 Litro de Gaseosa s/. 5.00\n"	

	if(medioLiGa.get()==1):	

		total=total+3
		opcionEscogida=opcionEscogida + "1/2 Litro de Gaseosa s/. 3.00\n"	

	if(dosLiCh.get()==1):	

		total=total+8
		opcionEscogida=opcionEscogida + "2 Litros de Chicha s/. 8.00\n"

	if(unLiCh.get()==1):

		total=total+4
		opcionEscogida=opcionEscogida + "1 Litro de Chicha s/. 4.00\n"	

	if(medioLiCh.get()==1):	

		total=total+2
		opcionEscogida=opcionEscogida + "1/2 Litro de Chicha s/. 2.00\n"

	if(vasoLiCh.get()==1):	

		total=total+1
		opcionEscogida=opcionEscogida + "1 Vaso de Chicha s/. 1.00\n"

	if(calGa.get()==1):	

		total=total+10
		opcionEscogida=opcionEscogida + "1 Caldo de Gallina s/. 10.00\n"

	if(calPo.get()==1):	

		total=total+7
		opcionEscogida=opcionEscogida + "1 Caldo de Pollo s/. 7.00\n"



	menuElegido.config(text=opcionEscogida, fg="white", bg="black")

	precioTotal.config(text=total, fg="white", bg="black")

#===========================================================================
									#BRASA
brasaLabel=tkinter.Label(lamina, text="BRASA", font=fuentePantallas)
brasaLabel.grid(row=4, column=1, columnspan=2)
brasaLabel.config(fg="white", bg="black")

unPolloBrasa=tkinter.Checkbutton(lamina ,text="1 Pollo s/. 60.00", variable=unPoBra, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unPolloBrasa.grid(row=5, column=1, columnspan=2)
unPolloBrasa.config(fg="green", bg="black")

medioPolloBrasa=tkinter.Checkbutton(lamina, text="1/2 Pollo s/. 30.00", variable=medioPoBra,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
medioPolloBrasa.grid(row=6, column=1, columnspan=2)
medioPolloBrasa.config(fg="green", bg="black")

cuartoPolloBrasa=tkinter.Checkbutton(lamina, text="1/4 Pollo s/. 15.00", variable=cuartoPoBra,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
cuartoPolloBrasa.grid(row=7, column=1, columnspan=2)
cuartoPolloBrasa.config(fg="green", bg="black")

octavoPolloBrasa=tkinter.Checkbutton(lamina, text="1/8 Pollo s/. 8.00", variable=octavoPoBra,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
octavoPolloBrasa.grid(row=8, column=1, columnspan=2)
octavoPolloBrasa.config(fg="green", bg="black")
#===========================================================================
									#BROASTER
broasterLabel=tkinter.Label(lamina, text="BROASTER", font=fuentePantallas)
broasterLabel.grid(row=4, column=3, columnspan=2)
broasterLabel.config(fg="white", bg="black")

unPolloBroaster=tkinter.Checkbutton(lamina, text="1 Pollo s/. 100.00", variable=unPoBro, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unPolloBroaster.grid(row=5, column=3, columnspan=2)
unPolloBroaster.config(fg="red", bg="black")

medioPolloBroaster=tkinter.Checkbutton(lamina, text="1/2 Pollo s/. 50.00", variable=medioPoBro, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
medioPolloBroaster.grid(row=6, column=3, columnspan=2)
medioPolloBroaster.config(fg="red", bg="black")

cuartoPolloBroaster=tkinter.Checkbutton(lamina, text="1/4 Pollo s/. 25.00", variable=cuartoPoBro, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
cuartoPolloBroaster.grid(row=7, column=3, columnspan=2)
cuartoPolloBroaster.config(fg="red", bg="black")

octavoPolloBroaster=tkinter.Checkbutton(lamina, text="1/8 Pollo s/. 13.00", variable=octavoPoBro, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
octavoPolloBroaster.grid(row=8, column=3, columnspan=2)
octavoPolloBroaster.config(fg="red", bg="black")

#===========================================================================
									#BEBIDAS
bebidasLabel=tkinter.Label(lamina, text="BEBIDAS", font=fuentePantallas)
bebidasLabel.grid(row=10, column=2, columnspan=2)
bebidasLabel.config(fg="white", bg="black")

gaseosasLabel=tkinter.Label(lamina, text="GASEOSAS", font=fuentePantallas)
gaseosasLabel.grid(row=12, column=1, columnspan=2)
gaseosasLabel.config(fg="white", bg="black")

dosLitros=tkinter.Checkbutton(lamina, text="2 Litros s/. 10.00", variable=dosLiGa,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
dosLitros.grid(row=13, column=1, columnspan=2)
dosLitros.config(fg="blue", bg="black")

unLitroMedio=tkinter.Checkbutton(lamina, text="1 Litro 1/2  s/. 8.00", variable=unLiMeGa,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unLitroMedio.grid(row=14, column=1, columnspan=2)
unLitroMedio.config(fg="blue", bg="black")

unLitro=tkinter.Checkbutton(lamina, text="1 Litro s/. 5.00", variable=unLiGa, onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unLitro.grid(row=15, column=1, columnspan=2)
unLitro.config(fg="blue", bg="black")

medioLitro=tkinter.Checkbutton(lamina, text="1/2 Litro s/. 3.00", variable=medioLiGa,onvalue=1, offvalue=0, command=opciones,font=fuentePantallas)
medioLitro.grid(row=16, column=1, columnspan=2)
medioLitro.config(fg="blue", bg="black")

#---------------------------------------------------------------------------------------
									#REFRESCOS

chichaLabel=tkinter.Label(lamina, text="CHICHA MORADA", font=fuentePantallas)
chichaLabel.grid(row=12, column=3, columnspan=2)
chichaLabel.config(fg="white", bg="black")

dosLitrosChicha=tkinter.Checkbutton(lamina, text="2 Litros s/. 8.00",  variable=dosLiCh, onvalue=1, offvalue=0, command=opciones,font=fuentePantallas)
dosLitrosChicha.grid(row=13, column=3, columnspan=2)
dosLitrosChicha.config(fg="purple", bg="black")

unLitroChicha=tkinter.Checkbutton(lamina, text="1 Litro s/. 4.00", variable=unLiCh,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unLitroChicha.grid(row=14, column=3, columnspan=2)
unLitroChicha.config(fg="purple", bg="black")

medioLitroChicha=tkinter.Checkbutton(lamina, text="1/2 Litro s/. 2.00", variable=medioLiCh,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
medioLitroChicha.grid(row=15, column=3, columnspan=2)
medioLitroChicha.config(fg="purple", bg="black")

unVasoChicha=tkinter.Checkbutton(lamina, text="1 Vaso s/. 1.00", variable=vasoLiCh,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
unVasoChicha.grid(row=16, column=3, columnspan=2)
unVasoChicha.config(fg="purple", bg="black")

#-------------------------------------------------------------------------------------
										#OTROS
otrosLabel=tkinter.Label(lamina, text="OTROS", font=fuentePantallas)
otrosLabel.grid(row=18, column=1, columnspan=2)
otrosLabel.config(fg="white", bg="black")

caldoGallina=tkinter.Checkbutton(lamina, text="Caldo de Gallina s/. 10.00", variable=calGa,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
caldoGallina.grid(row=20, column=1, columnspan=2)
caldoGallina.config(fg="yellow", bg="black")

caldoPollo=tkinter.Checkbutton(lamina, text="Caldo de Pollo s/. 7.00", variable=calPo,onvalue=1, offvalue=0, command=opciones, font=fuentePantallas)
caldoPollo.grid(row=21, column=1, columnspan=2)
caldoPollo.config(fg="yellow", bg="black")

#=======================================================================

pedido=tkinter.Label(lamina, text="SU PEDIDO:",font=fuentePantallas)
pedido.grid(row=22, column=1, columnspan=2)
pedido.config(fg="white", bg="black")

menuElegido=tkinter.Label(lamina, font=fuentePantallas)
menuElegido.grid(row=24, column=0, columnspan=3, rowspan=4)

TotalLabel=tkinter.Label(lamina, text="TOTAL S/. ",font=fuentePantallas)
TotalLabel.grid(row=30, column=3, columnspan=2)
TotalLabel.config(fg="white", bg="black")

precioTotal=tkinter.Label(lamina, font=fuentePantallas)
precioTotal.grid(row=30, column=4, columnspan=2)

#=======================================================================

myCanvas.create_window((0,0), window=segundaLamina, anchor="nw")

ventana.mainloop()#sirve para que mi ventana este abierta
#padding is between layout and object, spacing is between objects.
#padding can take 1, 2, or 4 args. with 2, its side topbottom, 4 its left up right bottom
from kivy.config import Config

Config.set('graphics', 'resizable', False)

import mysql.connector

sql=mysql.connector.connect(host='localhost',user='root',passwd='password')
cursor=sql.cursor()

sql.autocommit = True

cursor.execute('CREATE DATABASE IF NOT EXISTS PRACTICE')
cursor.execute('USE PRACTICE')

def tablecreator():
    cursor.execute('CREATE TABLE IF NOT EXISTS CUSTOMERS (username varchar(255), password varchar(255), customerID smallint UNSIGNED PRIMARY KEY AUTO_INCREMENT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS cpu(Name varchar(255), Type varchar(20) not null default "cpu", cpuID smallint unsigned not null primary key auto_increment, socket varchar(10) not null, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS cpucooler(Name varchar(255), Type varchar(20) not null default "cpucooler", coolerID smallint unsigned not null primary key auto_increment, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS storage(Name varchar(255), Type varchar(20) not null default "storage", storageID smallint unsigned not null primary key auto_increment, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS peripheral(Name varchar(255), Type varchar(20) not null default "peripheral", peripheralID smallint unsigned not null primary key auto_increment, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ram(Name varchar(255), Type varchar(20) not null default "ram", ramID smallint unsigned not null primary key auto_increment, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS gpu(Name varchar(255), Type varchar(20) not null default "gpu", gpuID smallint unsigned not null primary key auto_increment, gpulength smallint unsigned, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS psu(Name varchar(255), Type varchar(20) not null default "psu", psuID smallint unsigned not null primary key auto_increment, wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS pccase(Name varchar(255), Type varchar(20) not null default "pccase", caseID smallint unsigned not null primary key auto_increment, caselength smallint unsigned, casetype varchar(20), cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS mobo(Name varchar(255), Type varchar(20) not null default "mobo", moboID smallint unsigned not null primary key auto_increment, mobotype varchar(20), mobosocket varchar(20), wattage smallint unsigned, cost int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS orders(Name varchar(255), producttype varchar(20), productID smallint unsigned, quantity smallint unsigned, cost int unsigned, currentuserID int unsigned)')
    cursor.execute('CREATE TABLE IF NOT EXISTS customerdetails (customerID smallint unsigned primary key, phno varchar(255), address varchar(255), emailid varchar(50))')
    cursor.execute('CREATE TABLE IF NOT EXISTS cart (Name varchar(255), producttype varchar(20), productID smallint unsigned, quantity smallint unsigned, cost int unsigned, currentuserID int unsigned)')
    partinserter()

def partinserter():
    cursor.execute('INSERT INTO gpu(Name,gpuLength,Wattage,cost) values("Zotac GeForce GTX 1050 Ti OC Edition 4GB PCI Express Graphics Card",28,75,11000)')
    cursor.execute('INSERT INTO gpu(Name,gpuLength,Wattage,cost) values("GALAX GeForce GTX 1650 EX 1-Click OC 4GB GDDR5",20,75,12000)')
    cursor.execute('INSERT INTO gpu(Name,gpuLength,Wattage,cost) values("ZOTAC Gaming GeForce GTX 1660Ti Twin Fan 6GB GDDR6",17.3,130,23000)')
    cursor.execute('INSERT INTO gpu(Name,gpuLength,Wattage,cost) values("ZOTAC Gaming GeForce RTX 2060 Mini 6GB GDDR6",21,160,30000)')
    cursor.execute('INSERT INTO gpu(Name,gpuLength,Wattage,cost) values("GIGABYTE GeForce RTX 2070 DirectX 12 8GB 256-Bit GDDR6",26,200,45000)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("Gigabyte GA-A320M-H","ATX","AM4",50,4200)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("ASRock B450M-HDV","MATX","AM4",50,7500)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("ASRock B450M Steel legend","MATX","AM4",50,12000)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("ASUS Prime H310-CS 2.0","MATX","LGA1151",50,5200)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("ASUS ROG Strix B-365","ATX","LGA1155",50,13000)')
    cursor.execute('INSERT INTO mobo(Name,mobotype,mobosocket,wattage,cost) values("ASUS ROG Maximus XI Extreme Z390","EATX","LGA1151",50,40000)')
    cursor.execute('INSERT INTO ram(name,wattage,cost) values("HyperX Fury 4GB 2400MHz DDR4",1,2300)')
    cursor.execute('INSERT INTO ram(name,wattage,cost) values("Corsair Vengeance LPX 8GB DDR4",1,3500)')
    cursor.execute('INSERT INTO ram(name,wattage,cost) values("G.SKILL FBA4719692004970 Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 ",1,10000)')
    cursor.execute('INSERT INTO ram(name,wattage,cost) values("Corsair 16 GB Vengeance LPX DDR4 3000MHz C16 XMP 2.0 Desktop Memory - Black",1,6000)')
    cursor.execute('INSERT INTO ram(name,wattage,cost) values("TEAMGROUP T-Force Delta RGB DDR4 16GB (2x8GB) 3200MHz",2,9800)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("BBC 8865",50,"MIDTOWER",2100)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("Ant Esports ICE-400TG",43,"MIDTOWER",4500)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("Antec NX 310",53,"MIDTOWER",3600)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("Corsair Carbide SPEC-06 ",46,"MIDTOWER",8500)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("NZXT H510i",42,"MIDTOWER",10500)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("Corsair Graphite 780T CC-9011063-WW",60,"FULLTOWER",16500)')
    cursor.execute('INSERT INTO pccase(Name,caselength,casetype,cost) values("iBall Baby 342",50,"MINITOWER",3200)')
    cursor.execute('INSERT INTO cpu(Name,Socket,Wattage,cost) values("AMD Athlon 3000 Dual Core","AM4",35,4500)')
    cursor.execute('INSERT INTO cpu(Name,Socket,Wattage,cost) values("AMD Ryzen 5 3500 Octa Core","AM4",65,11000)')
    cursor.execute('INSERT INTO cpu(Name,Socket,Wattage,cost) values("AMD Ryzen 7 2700 Octa Core","AM4",65,17500)')
    cursor.execute('INSERT INTO cpu(Name,Socket,Wattage,cost) values("Intel Core i5 9400F Hexa Core","LGA1151",65,13500)')
    cursor.execute('INSERT INTO cpu(Name,Socket,Wattage,cost) values("Intel Core i7 9700K Octa Core","LGA1151",95,32500)')
    cursor.execute('INSERT INTO cpucooler(Name, Wattage, Cost) values("Lamao Bro Test", 50, 5000)')
    cursor.execute('INSERT INTO storage(Name, Wattage, Cost) values("Lamao Bro Test", 50, 5000)')
    cursor.execute('INSERT INTO psu(Name, Wattage, Cost) values("Corsair MX500", 500, 5000)')

tablecreator()

from kivy.core.window import Window
Window.size = (450,520)

from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
#to connect widgets in kv file to py
# username = ObjectProperty(None) is a way to connect username from kv file to property
# you can use self.username then to refer to username in the class

LabelBase.register(name='OpenSans', fn_regular='OpenSans-Light.ttf', fn_bold='OpenSans-SemiBold.ttf')

class MyTable(MDDataTable):
    pass

class LoginScreen(Screen):

    def upderrordispl1(self):
        self.ids.errordispl.text = ''

    def upderrordispl2(self):
        self.ids.errordispl.text = '[color=fb403b]Wrong Credentials[/color]'
        self.ids.uname.text = ''
        self.ids.passw.text = ''

    def createaccount(self):
        uname = self.ids.uname.text
        passw = self.ids.passw.text
        cursor.execute('SELECT * FROM customers where username="'+uname+'"')
        a = tuple(cursor)
        if len(a) == 0:
            if len(passw) >= 8:
                cursor.execute('INSERT INTO customers (username, password) values(%s,%s)',(uname,passw))
                self.ids.errordispl.text = '[color=000000]Login now.[/color]'
            if len(passw) < 8:
                self.ids.errordispl.text = '[color=fb403b]Your password is too short[/color]'
        else:
            self.ids.errordispl.text = '[color=fb403b]User already exists[/color]'

    def logincheck(self):
        uname = self.ids.uname.text
        passw = self.ids.passw.text
        cursor.execute('SELECT * FROM customers where username = "'+uname+'"')
        a = tuple(cursor)
        if len(a) == 0:
            self.upderrordispl2()
        for i in a:
            if passw in i:
                self.upderrordispl1()
                cursor.execute('SELECT customerID from customers where username = "'+uname+'"')
                for i in tuple(cursor):
                    for j in i:
                        global curruser
                        curruser = j
                print(curruser)
                self.ids.uname.text = ''
                self.ids.passw.text = ''
                self.ids.errordispl.theme_text_color = 'Primary'
                app.root.current = 'main'
            else:
                self.upderrordispl2()

class MainScreen(Screen):
    def clearcart(self):
        cursor.execute(f'DELETE FROM cart where currentuserID={curruser}')

class Add(Screen):
    pass


class AdminScreen(Screen):
    pass

class BudgetScreen(Screen):
    def setbudgetandchangescreen(self):
        global budget
        try:
            budget = int(self.ids.budget.text)
        except ValueError:
            budget = None

class InstructionScreen(Screen):
    pass

class GuidedCaseScreen(Screen):
    column_data = []
    row_data = []
    inp = None

    def create_lists(self):
        self.column_data = [
            ("Name", dp(30)),
            ("Type", dp(30)),
            ("Case ID", dp(30)),
            ("Case Length", dp(30)),
            ("Case Type", dp(30)),
            ("Cost", dp(30)),
        ]
        cursor.execute('SELECT * FROM pccase')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.casein.text)
            cursor.execute(f'SELECT * FROM pccase where caseID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global casename, caseID, caselength, casetype, casecost
                for i in res:
                    casename = str(i[0])
                    caseID = int(i[2])
                    caselength = int(i[3])
                    casetype = str(i[4])
                    casecost = int(i[5])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (casename,"pccase",caseID, 1, casecost, curruser))
                    app.root.current = 'gmobo'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"pccase"))
        sql.commit()

class GuidedMotherboardScreen(Screen):

    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(30)),
            ("Type", dp(30)),
            ("Mobo ID", dp(30)),
            ("Mobo Type", dp(30)),
            ("Mobo Socket", dp(30)),
            ("Wattage", dp(30)),
            ("Cost", dp(30)),
        ]
        cursor.execute('SELECT * FROM mobo')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.moboselect.text)
            cursor.execute(f'SELECT * FROM mobo where moboID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global moboname, moboID, mobotype, mobosocket, mobocost, mobowatt
                for i in res:
                    moboname = str(i[0])
                    moboID = int(i[2])
                    mobotype = str(i[3])
                    mobosocket = str(i[4])
                    mobowatt = int(i[5])
                    mobocost = int(i[6])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (moboname,"mobo",moboID, 1, mobocost, curruser))
                    app.root.current = 'gcpu'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"mobo"))

class GuidedCpuScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(30)),
            ("Type", dp(30)),
            ("CPU ID", dp(30)),
            ("CPU Socket", dp(30)),
            ("CPU Wattage", dp(30)),
            ("Cost", dp(30))
        ]
        cursor.execute('SELECT * FROM cpu')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.cpuselect.text)
            cursor.execute(f'SELECT * FROM cpu where cpuID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global cpuname, cpuID, cpusocket, cpucost, cpuwatt
                for i in res:
                    cpuname = str(i[0])
                    cpuID = int(i[2])
                    cpusocket = str(i[3])
                    cpuwatt = int(i[4])
                    cpucost = int(i[5])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (cpuname,"cpu",cpuID, 1, cpucost, curruser))
                    app.root.current = 'ggpu'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"cpu"))

class GuidedGpuScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(50)),
            ("Type", dp(30)),
            ("GPU ID", dp(30)),
            ("GPU Length", dp(30)),
            ("GPU Wattage", dp(30)),
            ("Cost", dp(30))
        ]
        cursor.execute('SELECT * FROM gpu')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.gpuselect.text)
            cursor.execute(f'SELECT * FROM gpu where gpuID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global gpuname, gpuID, gpulength, gpucost, gpuwatt
                for i in res:
                    gpuname = str(i[0])
                    gpuID = int(i[2])
                    gpulength = int(i[3])
                    gpuwatt = int(i[4])
                    gpucost = int(i[5])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (gpuname,"gpu",gpuID, 1, gpucost, curruser))
                    app.root.current = 'gram'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"gpu"))

class GuidedRamScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("RAM ID", dp(20)),
            ("Ram Wattage", dp(20)),
            ("Cost", dp(20))
        ]
        cursor.execute('SELECT * FROM ram')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.ramselect.text)
            cursor.execute(f'SELECT * FROM ram where ramID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global ramname, ramID, ramcost, ramwatt
                for i in res:
                    ramname = str(i[0])
                    ramID = int(i[2])
                    ramwatt = int(i[3])
                    ramcost = int(i[4])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (ramname,"ram",ramID, 1, ramcost, curruser))
                    app.root.current = 'gcooler'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"ram"))

class GuidedCoolerScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("Cooler ID", dp(20)),
            ("Cooler Wattage", dp(20)),
            ("Cost", dp(20))
        ]
        cursor.execute('SELECT * FROM cpucooler')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.coolerselect.text)
            cursor.execute(f'SELECT * FROM cpucooler where coolerID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global coolername, coolerID, coolercost, coolerwatt
                for i in res:
                    coolername = str(i[0])
                    coolerID = int(i[2])
                    coolerwatt = int(i[3])
                    coolercost = int(i[4])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (coolername,"cpucooler",coolerID, 1, coolercost, curruser))
                    app.root.current = 'gstorage'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"cpucooler"))

class GuidedStorageScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("Storage ID", dp(20)),
            ("Storage Wattage", dp(20)),
            ("Cost", dp(20))
        ]
        cursor.execute('SELECT * FROM storage')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.storageselect.text)
            cursor.execute(f'SELECT * FROM storage where storageID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global storagename, storageID, storagecost, storagewatt
                for i in res:
                    storagename = str(i[0])
                    storageID = int(i[2])
                    storagewatt = int(i[3])
                    storagecost = int(i[4])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (storagename,"storage",storageID, 1, storagecost, curruser))
                    app.root.current = 'gpsu'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"storage"))

class GuidedPSUScreen(Screen):
    column_data = []
    row_data = []

    def create_lists(self):
        self.column_data = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("PSU ID", dp(20)),
            ("PSU Wattage", dp(20)),
            ("Cost", dp(20))
        ]
        cursor.execute('SELECT * FROM psu')
        for i in cursor:
            self.row_data.append(i)

    def storeparts(self):
        try:
            inp = int(self.ids.psuselect.text)
            cursor.execute(f'SELECT * FROM psu where psuID={inp}')
            res = tuple(cursor)
            if len(res) == 0:
                pass
            else:
                global psuname, psuID, psucost, psuwatt
                for i in res:
                    psuname = str(i[0])
                    psuID = int(i[2])
                    psuwatt = int(i[3])
                    psucost = int(i[4])
                    cursor.execute('INSERT INTO cart values (%s, %s, %s, %s, %s, %s)', (psuname,"psu",psuID, 1, psucost, curruser))
                    app.root.current = 'compatible'
        except ValueError:
            self.ids.errorcase.text = '[color=fb403b]You need to enter an ID in digits.[/color]'

    def delparts(self):
        cursor.execute('DELETE FROM cart where currentuserID=%s and producttype =%s',(curruser,"psu"))

class CompatibilityChecker(Screen):

    def check(self):
        if casetype == 'FULLTOWER':
            pass
        elif casetype == 'MIDTOWER':
            if mobotype == 'EATX':
                self.ids.label1.text = "[color=fb403b]Your Motherboard and Case aren't compatible.[/color]"
        elif casetype == 'MINITOWER':
            if mobotype == 'EATX' or mobotype == 'ATX':
                self.ids.label1.text = "[color=fb403b]Your Motherboard and Case aren't compatible.[/color]"
        if cpusocket != mobosocket:
            self.ids.label2.text = "[color=fb403b]Your Motherboard and CPU aren't compatible.[/color]"
        if caselength < gpulength:
            self.ids.label3.text = "[color=fb403b]Your GPU and Case aren't compatible.[/color]"
        if (cpuwatt+storagewatt+gpuwatt+coolerwatt+mobowatt+ramwatt) > psuwatt:
            self.ids.label4.text = "[color=fb403b]Your PSU's wattage is too low. [/color]"
        if self.ids.label1.text == '' and self.ids.label2.text == '' and self.ids.label3.text == '' and self.ids.label4.text =='':
            self.ids.label1.text = '[b]All your parts are compatible, good job![/b]'

    def emptycart(self):
        cursor.execute('TRUNCATE table cart')
        app.root.current = 'main'

class YourAccount(Screen):
    def customerdetails(self):
        self.ids.customererror.text = ''
        j=curruser
        cursor.execute(f'DELETE FROM customerdetails WHERE customerID={j}')
        a,b,c = self.ids.customerphone.text, self.ids.customeremail.text, self.ids.customeraddress.text
        a_low = a.lower()
        if a == '' or b == '' or c == '':
            self.ids.customererror.text = '[color=fb403b]Fill in all the information.[/color]'
            return
        elif a_low.islower():
            self.ids.customererror.text = '[color=fb403b]Your number is supposed to have digits in it g[/color]'
            return
        cursor.execute('INSERT INTO customerdetails values(%s,%s,%s,%s)',(j,a,c,b))

    def carttoorders(self):
        cursor.execute(f'INSERT INTO orders SELECT * FROM cart WHERE currentuserID={curruser}')
        self.ids.successlabel.text = '[color=000000]Your parts have been ordered. :)[/color]'
        cursor.execute(f'DELETE FROM cart WHERE currentuserID={curruser}')

    column_data_cart, column_data_orders = [], []
    row_data_cart, row_data_orders = [], []

    def create_lists_cart(self):
        self.column_data_cart = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("Product ID", dp(20)),
            ("Quantity", dp(20)),
            ("Cost", dp(20)),
            ("User ID", dp(20))
        ]
        cursor.execute(f'SELECT * FROM cart where currentuserID={curruser}')
        for i in cursor:
            self.row_data_cart.append(i)
            self.row_data_cart = list(dict.fromkeys(self.row_data_cart))

    def create_lists_orders(self):
        self.column_data_orders = [
            ("Name", dp(50)),
            ("Type", dp(20)),
            ("Product ID", dp(20)),
            ("Quantity", dp(20)),
            ("Cost", dp(20)),
            ('User ID', dp(20))
        ]
        cursor.execute(f'SELECT * FROM orders where currentuserID={curruser}')
        for i in cursor:
            self.row_data_orders.append(i)
            self.row_data_orders = list(dict.fromkeys(self.row_data_orders))      #to fix duplicates appearing in the kivy table which dont exist in the mysql table
            print(self.row_data_orders)

    def customeriddisplay(self):
        self.ids.id.text = f'[color=000000]Your Customer ID is {curruser}. \nThank you for buying parts from us! :)[/color]'

class DemoApp(MDApp):

    data_table_one = None
    data_table_two = None
    data_table_three = None
    data_table_four = None
    data_table_five = None
    data_table_six = None
    data_table_seven = None
    data_table_eight = None
    data_table_cart = None
    data_table_orders = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "800"
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = "Light"

    def on_start(self):

        self.root.ids.gcase.create_lists()
        self.root.ids.gmobo.create_lists()
        self.root.ids.gcpu.create_lists()
        self.root.ids.ggpu.create_lists()
        self.root.ids.gram.create_lists()
        self.root.ids.gcooler.create_lists()
        self.root.ids.gstorage.create_lists()
        self.root.ids.gpsu.create_lists()

        if not self.data_table_one:
            self.create_data_table_one()

        if not self.data_table_two:
            self.create_data_table_two()

        if not self.data_table_three:
            self.create_data_table_three()

        if not self.data_table_four:
            self.create_data_table_four()

        if not self.data_table_five:
            self.create_data_table_five()

        if not self.data_table_six:
            self.create_data_table_six()

        if not self.data_table_seven:
            self.create_data_table_seven()

        if not self.data_table_eight:
            self.create_data_table_eight()

    def cartandorders(self):
        data_table_cart = None
        data_table_orders = None
        self.root.ids.youraccount.create_lists_cart()
        self.root.ids.youraccount.create_lists_orders()

        if not self.data_table_cart:
            self.create_data_table_cart()
        if not self.data_table_orders:
            self.create_data_table_orders()

    def orders(self):
        data_table_orders = None
        self.root.ids.youraccount.create_lists_orders()

        #if not self.data_table_orders:
        self.create_data_table_orders()


    def create_data_table_cart(self):

        self.data_table_cart = MyTable(
            column_data=self.root.ids.youraccount.column_data_cart,
            row_data=self.root.ids.youraccount.row_data_cart
            )

    def create_data_table_orders(self):

        self.data_table_orders = MyTable(
            column_data=self.root.ids.youraccount.column_data_orders,
            row_data=self.root.ids.youraccount.row_data_orders
            )

    def create_data_table_one(self):

        self.data_table_one = MyTable(
            column_data=self.root.ids.gcase.column_data,
            row_data=self.root.ids.gcase.row_data
            )

    def create_data_table_two(self):

        self.data_table_two = MyTable(
            column_data=self.root.ids.gmobo.column_data,
            row_data=self.root.ids.gmobo.row_data
            )

    def create_data_table_three(self):

        self.data_table_three = MyTable(
            column_data = self.root.ids.gcpu.column_data,
            row_data = self.root.ids.gcpu.row_data
            )

    def create_data_table_four(self):

        self.data_table_four = MyTable(
            column_data = self.root.ids.ggpu.column_data,
            row_data = self.root.ids.ggpu.row_data
            )

    def create_data_table_five(self):

        self.data_table_five = MyTable(
            column_data = self.root.ids.gram.column_data,
            row_data = self.root.ids.gram.row_data
            )

    def create_data_table_six(self):

        self.data_table_six = MyTable(
            column_data = self.root.ids.gcooler.column_data,
            row_data = self.root.ids.gcooler.row_data
            )

    def create_data_table_seven(self):

        self.data_table_seven = MyTable(
            column_data = self.root.ids.gstorage.column_data,
            row_data = self.root.ids.gstorage.row_data
            )

    def create_data_table_eight(self):

        self.data_table_eight = MyTable(
            column_data = self.root.ids.gpsu.column_data,
            row_data = self.root.ids.gpsu.row_data
            )


    def originalsize(self):
        Window.size = (450, 520)

    def windowsize(self):
        Window.size = (1000,800)

    def emptycart(self):
        cursor.execute('TRUNCATE table cart')


if __name__ == '__main__':
    app = DemoApp()
    app.run()

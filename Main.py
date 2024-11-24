{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs26 \cf0 class Car:\
    def __init__(self, brand, color, year):\
        self.brand = brand\
        self.color = color\
        self.year = year\
\
    def details(self):\
        print(f"This is a \{self.color\} \{self.brand\} from \{self.year\}.")\
\
    def owner(self,name):\
        self.name=name\
        print(f"The \{self.brand\} belongs to \{self.name\}")\
\
\
# Create objects (instances) of the Car class\
car1 = Car("Toyota", "red", 2020)\
car2 = Car("Honda", "blue", 2018)\
\
# Access methods and display details\
car1.details()\
car1.owner("Mr.X")\
\
car2.details()  \
car2.owner("Mr.Y")\
}
import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt

from math import atan, pi,sqrt
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "matplotlib example"
        self.col1='r'
        self.col2='orange'
        self.col3='pink'
        self.initInterface()
        self.initWidgets()
    
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300,100,1000,200)
        self.show()
        
    def initWidgets(self):
        btn=QPushButton('Rysuj',self)
        btncol=QPushButton('Kolor AB',self)
        btncol2=QPushButton('Kolor CD',self)
        kasuj=QPushButton('Kasuj',self)
        XLabel=QLabel('xa',self)
        YLabel=QLabel('ya',self)
        Xblabel=QLabel('xb',self)
        Yblabel=QLabel('yb',self)
        Xclabel=QLabel('xc',self)
        Yclabel=QLabel('yc',self)
        Xdlabel=QLabel('xd',self)
        Ydlabel=QLabel('yd',self)
        Xplabel=QLabel('Xp',self)
        Yplabel=QLabel('Yp',self)
        K1a=QLabel('Kąt ostry',self)
        K2a=QLabel('Kąt rozwarty',self)
        D=QLabel('Kąt między prostymi w gradach:',self)
        M1a=QLabel('Punkt P względem AB po:',self)
        M2a=QLabel('Punkt P względem CD po:',self)
        A1a=QLabel('Azymut odcinka AB',self)
        A2a=QLabel('Azymut odcinka CD:',self)
        self.XbEdit=QLineEdit()
        self.YbEdit=QLineEdit()
        self.XcEdit=QLineEdit()
        self.YcEdit=QLineEdit()
        self.XdEdit=QLineEdit()
        self.YdEdit=QLineEdit()
        self.XbEdit=QLineEdit()
        self.YbEdit=QLineEdit()
        self.xEdit=QLineEdit()
        self.yEdit=QLineEdit()
        self.Xpp=QLineEdit()
        self.Ypp=QLineEdit()
        self.W=QLineEdit()
        self.K1=QLineEdit()
        self.K2=QLineEdit()
        self.M1=QLineEdit()
        self.M2=QLineEdit()
        self.A1=QLineEdit()
        self.A2=QLineEdit()
        resultLabel=QLabel('',self)
        
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        
        grid=QGridLayout()
        grid.addWidget(XLabel,2,0)
        grid.addWidget(self.xEdit,2,1)
        grid.addWidget(YLabel,3,0)
        grid.addWidget(self.yEdit,3,1)
        grid.addWidget(btn,11,0,1,2)
        grid.addWidget(self.canvas,1,2,-1,-1)
        grid.addWidget(resultLabel, 5, 0)
        grid.addWidget(Xblabel,4,0)
        grid.addWidget(self.XbEdit,4,1)
        grid.addWidget(Yblabel,5,0)
        grid.addWidget(self.YbEdit,5,1) 
        grid.addWidget(Xclabel,6,0)
        grid.addWidget(self.XcEdit,6,1)
        grid.addWidget(Yclabel,7,0)
        grid.addWidget(self.YcEdit,7,1)
        grid.addWidget(Xdlabel,8,0)
        grid.addWidget(self.XdEdit,8,1)
        grid.addWidget(Ydlabel,9,0)
        grid.addWidget(self.YdEdit,9,1)
        grid.addWidget(btncol,10,0,1,1)
        grid.addWidget(btncol2,10,1,1,1)
        grid.addWidget(Xplabel,13,0)
        grid.addWidget(self.Xpp,13,1)
        grid.addWidget(Yplabel,14,0)
        grid.addWidget(self.Ypp,14,1)
        grid.addWidget(self.W,15,0,1,2)
        grid.addWidget(D,16,0,1,2)
        grid.addWidget(K1a,17,0)
        grid.addWidget(self.K1,17,1)
        grid.addWidget(K2a,18,0)
        grid.addWidget(self.K2,18,1)
        grid.addWidget(M1a,19,0)
        grid.addWidget(self.M1,19,1)
        grid.addWidget(M2a,20,0)
        grid.addWidget(self.M2,20,1)
        grid.addWidget(A1a,21,0)
        grid.addWidget(self.A1,21,1)
        grid.addWidget(A2a,22,0)
        grid.addWidget(self.A2,22,1)
        grid.addWidget(kasuj,23,0,1,1)
        self.setLayout(grid)
       
        btncol.clicked.connect(self.color)
        kasuj.clicked.connect(self.kas)
        btncol2.clicked.connect(self.color2)
        btn.clicked.connect(self.oblicz)
        self.kas()
    def kontrola(self,e):
        if e.text().lstrip('-').replace('.','',1).isdigit():
            return float(e.text())
        else:
            e.setFocus()
            return None
            
    def color(self):
            kolor= QColorDialog.getColor()
            if kolor.isValid():
                print('color AB', kolor.name())
                self.col1 = kolor.name()
                self.doit()

    def color2(self):
            kolor2= QColorDialog.getColor()
            if kolor2.isValid():
                print('color CD', kolor2.name())
                self.col2 = kolor2.name()
                self.doit()
    
        
    def kat(self):
        
        xa=self.kontrola(self.xEdit)
        ya=self.kontrola(self.yEdit)
        xb=self.kontrola(self.XbEdit)
        yb=self.kontrola(self.YbEdit)
        xc=self.kontrola(self.XcEdit)
        yc=self.kontrola(self.YcEdit)
        xd=self.kontrola(self.XdEdit)
        yd=self.kontrola(self.YdEdit)
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]:
            
            xa=float(self.xEdit.text())
            ya=float(self.yEdit.text())
            xb=float(self.XbEdit.text())
            yb=float(self.YbEdit.text())
            
            xc=float(self.XcEdit.text())
            yc=float(self.YcEdit.text())
            xd=float(self.XdEdit.text())
            yd=float(self.YdEdit.text())
            
            if (xb-xa)==0 and (xd-xc)==0:
                    self.K2.setText('brak przecięcia')
                    self.K1.setText('brak przecięcia')
            elif (xb-xa)==0 and xc==0:
                    fi=atan(yd/xd)*200/pi
            elif (xb-xa)==0 and xd==0:
                    fi=atan(yc/xc)*200/pi
            elif (xd-xc)==0 and xa==0:
                    fi=atan(yb/xb)*200/pi
            elif (xd-xc)==0 and xb==0:
                    fi=atan(ya/xa)*200/pi
            else:    
                    a1=(yb-ya)/(xb-xa)
                    a2=(yd-yc)/(xd-xc)
                    fi=atan(abs((a1-a2)/(1+a1*a2)))*200/pi
            fi=round(fi,4)
            fir=200-fi
            fir=round(fir,4)
            if fi>100:
                    self.K2.setText(str(fi))
                    self.K1.setText(str(fir))
            else:
                    self.K1.setText(str(fi))
                    self.K2.setText(str(fir))
                    
    
        
    def oblicz(self):
        self.doit()
        self.kat()
        self.azymut()
    
    def azymut(self):
        xa=float(self.xEdit.text())
        ya=float(self.yEdit.text())
        xb=float(self.XbEdit.text())
        yb=float(self.YbEdit.text())
       
        xc=float(self.XcEdit.text())
        yc=float(self.YcEdit.text())
        xd=float(self.XdEdit.text())
        yd=float(self.YdEdit.text()) 
        
        dyAB=yb-ya
        dxAB=xb-xa
        dyCD=yd-yc
        dxCD=xd-xc
        if dyAB==0:
                az=100
                az=round(az,4)
                self.A1.setText(str(az))
        elif dyAB>0 and dxAB>0:
                az=atan(dxAB/dyAB)*200/pi
               
                az=round(az,4)
                self.A1.setText(str(az))
        elif dyAB<0 and dxAB>0:
                az=atan(dxAB/dyAB)*200/pi+200
              
                az=round(az,4)
                self.A1.setText(str(az))
        elif dxAB<0 and dyAB<0:
                az=atan(dxAB/dyAB)*200/pi+200
            
                az=round(az,4)
                self.A1.setText(str(az))
        elif dyAB>0 and dxAB<0:
                az=atan(dxAB/dyAB)*200/pi+400
             
                az=round(az,4)
                self.A1.setText(str(az))
     
            
            
        if dyCD==0:
            az1=100
            az1=round(az1)
            
        elif dyCD>0 and dxCD>0:
            az1=atan(dxCD/dyCD)*200/pi
        elif dyCD<0 and dxCD>0:
            az1=atan(dxCD/dyCD)*200/pi+200
        elif dxCD<0 and dyCD<0:
            az1=atan(dxCD/dyCD)*200/pi+200
        elif dyCD>0 and dxCD<0:
            az1=atan(dxCD/dyCD)*200/pi+400
        elif dxCD==0:
            az1=0
        az1=round(az1)
        self.A2.setText(str(az1))
        if dxCD==0:
            self.A2.setText('0')
    def doit(self):
        xa=self.kontrola(self.xEdit)
        ya=self.kontrola(self.yEdit)
        xb=self.kontrola(self.XbEdit)
        yb=self.kontrola(self.YbEdit)
        xc=self.kontrola(self.XcEdit)
        yc=self.kontrola(self.YcEdit)
        xd=self.kontrola(self.XdEdit)
        yd=self.kontrola(self.YdEdit)
        
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]:
            
            xa=float(self.xEdit.text())
            ya=float(self.yEdit.text())
            xb=float(self.XbEdit.text())
            yb=float(self.YbEdit.text())
            dx1=[xa,xb]
            dy1=[ya,yb]
            xc=float(self.XcEdit.text())
            yc=float(self.YcEdit.text())
            xd=float(self.XdEdit.text())
            yd=float(self.YdEdit.text())
            dx2=[xc,xd]
            dy2=[yc,yd]
            
            #obliczanie kąta między prostymi
            
            #gdzie znajduje sie punkt P
            delta_Xac = xc - xa
            delta_Yac = yc -ya
            delta_Ycd = yd-yc
            delta_Xcd = xd-xc
            delta_Xab = xb-xa
            delta_Yab = yb-ya
        
            licznik1 = delta_Xac*delta_Ycd-delta_Yac*delta_Xcd
            licznik2 = delta_Xac*delta_Yab-delta_Yac*delta_Xab
            mianownik = delta_Xab*delta_Ycd-delta_Yab*delta_Xcd
          
            if mianownik==0:
                self.W.setText('Punkt nie istnieje')
                self.figure.clear()
                ax=self.figure.add_subplot(111)
                ax.plot(dx1,dy1,color=self.col1)
                ax=self.figure.add_subplot(111)
                ax.plot(dx2,dy2,color=self.col2)
                ax=self.figure.add_subplot(111)
                ax.plot([xa,xb,xc,xd], [ya,yb,yc,yd], 'ro')
                self.K2.setText('brak')
                self.K1.setText('brak')
                self.Xpp.setText('brak')
                self.Ypp.setText('brak')
                self.M1.setText('brak')
                self.M2.setText('brak')
                A='A'
                B='B'
                C='C'
                D='D'
           
                ax.text(xa,ya,A)
                ax.text(xb,yb,B)
                ax.text(xc,yc,C)
                ax.text(xd,yd,D)
                self.canvas.draw()
            elif mianownik != 0:
                t1 = (licznik1)/(mianownik)
                t2 = (licznik2)/(mianownik)
                xpa = xa+t1*delta_Xab
                ypa = ya+t1*delta_Yab
                
                if (0 <= t1 <= 1) and (0 <= t2 <= 1):
                    self.W.setText('Na przecięciu ')
                elif (0 <= t1 <= 1) and ((t2 < 0) or (t2 > 1)):
                    self.W.setText('Na odcinku AB')
                elif (0 <= t2 <= 1) and ((t1 < 0) or (t1 > 1)):
                    self.W.setText('Na odcinku CD')
                else:
                    self.W.setText('Na przedłużeniu obu')
                    
            
            xp=round(xpa,5)
            yp=round(ypa,5)
            xp=float(xp)
            yp=float(yp)
            
            #po której stronie od odcników znajduje się punkt P
            dxAB=xb-xa
            dyAP=yp-ya
            dxAP=xp-xa
            dyAB=yb-ya
            
            
            k=dxAB*dyAP-dxAP*dyAB
            
            if k==0:
                self.M1.setText('współliniowe')
            elif k>0:
                self.M1.setText('prawej stronie')
            else:
                 self.M1.setText('lewej stronie')
                 
            dxCD=xd-xc
            dyCP=yp-yc
            dxCP=xp-xc
            dyCD=yd-yc
    
            kb=dxCD*dyCP-dxCP*dyCD
            if kb==0:
                self.M2.setText('współliniowe')
            elif kb>0:
                self.M2.setText('prawej stronie')
            else:
                self.M2.setText('lewej stronie')
            
            

            
           
            #szukanie bliższego punktu odcinka do punktu P
            if sqrt((xp-xa)*(xp-xa)+(yp-ya)*(yp-ya))>sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)):
                dxpa=[xp,xb]
                dypa=[yp,yb]
            else:
                dxpa=[xp,xa]
                dypa=[yp,ya]
            
            if sqrt((xp-xc)*(xp-xc)+(yp-yc)*(yp-yc))>sqrt((xb-xd)*(xb-xd)+(yb-yd)*(yb-yd)):
                dxpa2=[xp,xd]
                dypa2=[yp,yd]
            else:
                dxpa2=[xp,xc]
                dypa2=[yp,yc]
           
            ax=self.figure.add_subplot(111)
            self.Xpp.setText(str(xp))
            self.Ypp.setText(str(yp))
            
            self.figure.clear()
            ax=self.figure.add_subplot(111)
            ax.plot(dx1,dy1,color=self.col1)
            ax=self.figure.add_subplot(111)
            ax.plot(dx2,dy2,color=self.col2)
            ax=self.figure.add_subplot(111)
            ax.plot([xa,xb,xc,xd,xp], [ya,yb,yc,yd,yp], 'ro')
            ax.plot(dxpa,dypa,linestyle=':')
            ax=self.figure.add_subplot(111)
            ax.plot(dxpa2,dypa2,linestyle=':')
            A='A'
            B='B'
            C='C'
            D='D'
            P='P'
            ax.text(xa,ya,A)
            ax.text(xb,yb,B)
            ax.text(xc,yc,C)
            ax.text(xd,yd,D)
            ax.text(xp,yp,P)
            self.canvas.draw()
            
            
            
            plik=open('Wyniki.txt','w')
            plik.write('\n|{:^20}|{:^20}|{:^20}|'.format('Nazwa punktu','WspX','wspY'))
            plik.write('\n|{:^20}|{:^20.3f}|{:^20.3f}|'.format(A,xa,ya))
            plik.write('\n|{:^20}|{:^20.3f}|{:^20.3f}|'.format(B,xb,yb))
            plik.write('\n|{:^20}|{:^20.3f}|{:^20.3f}|'.format(C,xc,yc))
            plik.write('\n|{:^20}|{:^20.3f}|{:^20.3f}|'.format(D,xd,yd))
            plik.write('\n|{:^20}|{:^20.3f}|{:^20.3f}|'.format(P,xp,yp))
            
            plik.close()
    def kas(self):
        self.XbEdit.clear()
        
        self.YbEdit.clear()
        self.XcEdit.clear()
        self.YcEdit.clear()
        self.XdEdit.clear()
        self.YdEdit.clear()
        self.XbEdit.clear()
        self.YbEdit.clear()
        self.xEdit.clear()
        self.yEdit.clear()
        self.Xpp.clear()
        self.Ypp.clear()
        self.W.clear()
        self.K1.clear()
        self.K2.clear()
        self.M1.clear()
        self.M2.clear()
        self.A1.clear()
        self.A2.clear()
        
        
                  
def main():
    app=QApplication(sys.argv)
    window=AppWindow()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main()
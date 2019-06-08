from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty #polaczenie kv z aplikacja
from kivy.garden.mapview import MapMarker, MarkerMapLayer
import gpxpy
from zks import vin , dod
import math
import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt 
class AddLocationForm(BoxLayout):

    my_map = ObjectProperty()
    lhmax = ObjectProperty()
    lhmin = ObjectProperty()
    lnachmax = ObjectProperty()
    lnachmin = ObjectProperty()
    ldh = ObjectProperty()
    plots=ObjectProperty()
    lvmax=ObjectProperty()
    lvmin=ObjectProperty()
    lvave=ObjectProperty()
    lczash=ObjectProperty()
    lczasm=ObjectProperty()
    lczass=ObjectProperty()
    ldyst = ObjectProperty()
    def __init__(self, **kwargs):
        super(AddLocationForm, self).__init__(**kwargs)
        self.fig = plt.figure()
        self.cnv = FigureCanvasKivyAgg(self.fig)
        self.plots.add_widget(self.cnv)
    def draw_marker(self):
        
        
        data_lay=MarkerMapLayer()
        self.my_map.add_layer(data_lay)
        for i in range(len(self.lati)):
            
            marker = MapMarker(lat = self.lati[i], lon = self.loni[i], source="dot.png")
            self.my_map.add_marker(marker, layer=data_lay)
        
        self.my_map.set_zoom_at(10, self.lati[1], self.loni[1], scale=None)
        self.my_map.center_on(self.lati[1], self.loni[1])
        
    
    def wczytaj(self):
        lat = []
        lon = []
        el = []
        dates = []
        gpx_file = open("2012.gpx",'r')
        gpx = gpxpy.parse(gpx_file)
        gpx_file.close()
        for track in gpx.tracks:
            for seg in track.segments:
                for point in seg.points:
                    lon.append(point.longitude)
                    lat.append(point.latitude)
                        
                    vfb=getattr(point, 'elevation')
                    if vfb == None:
                        pass
                    else:
                        el.append(point.elevation)
                    
                    hsv=getattr(point, 'time')
                    if hsv == None:
                        pass
                    else:
                       hsv=getattr(point, 'time')
                       hsv=str(hsv)
                       dates.append(hsv)
        
        lat = lat[0::6]
        lon = lon[0::6]
        el = el[0::6]
        dates = dates[0::6]
        self.lati=lat
        self.loni=lon
        dh = [0]

        dist = [0]
       
        for i in range(len(lat)):
            if i == 0:
                pass
            else:
                aa = i-1
                bb = i

                d=vin(lat[aa],lon[aa],lat[bb],lon[bb])
                dhcz = el[bb]-el[aa]
                D=math.sqrt(d**2+dhcz**2)
                dh.append(dhcz)
                dist.append(D)
                
        n=[]

        for a in range(len(lat)):
            if i==0:
                pass
            else:
                if dist[a]==0:
                    nach=0
                else:

                    nach=(dh[a]/dist[a])
                    n.append(nach)
        

        h=[]
        minute=[]
        sec=[]
        tpart=[]
        if len(dates) > 1: 
            ki=[]
            wi=[]
            for e in dates:
                e=str(e)
                aq=e.split("+")
                del aq[-1]
                yy=aq[0]
                ki.append(yy)
            for f in ki:
                f=str(f)
                ass=f.split(" ")
                ssa=ass[1]
                wi.append(ssa)
            for g in wi:    
                g=str(g)
                qq=g.split(":")
                go=qq[0]
                m=qq[1]
                s=qq[2]
                h.append(go)
                minute.append(m)
                sec.append(s)
            czasyyy=[]
            if len(dates) > 1:               
               
               
               for i in range(len(h)):
                   czasyyy.append(float(h[i])+float(minute[i])/60+float(sec[i])/3600)
               for i in range(len(h)):
                   if i == 0:
                       pass
                   else:
                       aaa = i-1
                       bbb = i
                       dtime = czasyyy[bbb]-czasyyy[aaa]
                       tpart.append(dtime)
            vparty=[]
            
            if len(tpart) > 1:
                
               del dist[0]
               predkosc=zip(dist,tpart)
               for i,j in predkosc:
                   vvv=i/j
                   vparty.append(vvv)
               vparty = [i/1000 for i in vparty] #przeliczanie na km/h
               Vmax=max(vparty) 
               Vmin=min(vparty)
               abba=[i/1000 for i in dist] #przeliczanie na km
               Vave=sum(abba)/sum(tpart)
               self.lvmax.text=str("%.3f" % Vmax)    
               self.lvmin.text=str("%.3f" % Vmin)
               self.lvave.text=str("%.3f" % Vave)
               #rozdzielanie godziny na oczekiwane wartosci
               timeee=math.floor(sum(tpart))
               minuty=math.floor((sum(tpart)-timeee)*60)
               sekundy=math.floor(((sum(tpart)-timeee)*60-minuty)*60)
               self.lczash.text=str(timeee)
               self.lczasm.text=str(minuty)
               self.lczass.text=str(sekundy)
               dist.insert(0,0)
               czasyyy.insert(0,0)
               vparty.insert(0,0)


        
                 
        hmax=max(el)
        hmin=min(el)

        #profil
        self.ax1=self.fig.add_subplot(111)
        self.ax1.set_xlabel('Dystans [km]')
        self.ax1.set_ylabel('Wysokosc m.n.p.m')
        plt.title('Profil wysokosciowy')

        self.ax1.plot(dod(dist),el)
        self.cnv.draw()
        
        #nachylenia w procentach
        f=max(n)*100
        ff=min(n)*100
        self.draw_route(lat, lon)
        self.lhmax.text=str("%.2f" % hmax)
        self.lhmin.text=str("%.2f" % hmin)
        self.lnachmax.text=str("%.2f" %f)
        self.lnachmin.text=str("%.2f" %ff)
        self.ldyst.text=str("%.2f" % sum(dist))
        self.ldh.text=str("%.2f" % sum(dh))


    def draw_route(self,lat, lon):
        data_layer = MarkerMapLayer()
    
        for point in zip(lat,lon):
            
            self.mark_point(*point,layer=data_layer)

        
    def mark_point(self, lat, lon, layer=None):
        if lat!=None and lon!=None:
            self.my_map.add_marker

    def kas(self):
        self.lhmax.text="wczytaj dane"
        self.lhmin.text="wczytaj dane"
        self.lnachmax.text="wczytaj dane"
        self.lnachmin.text="wczytaj dane"
        self.ldh.text="wczytaj dane"
        self.lvmax.text="wczytaj dane"
        self.lvmin.text="wczytaj dane"
        self.lvave.text="wczytaj dane"
        self.ldyst.text="wczytaj dane"

class MapViewApp(App):
    def build(self):
            return AddLocationForm()
    #pass

if __name__ == '__main__':
    MapViewApp().run()
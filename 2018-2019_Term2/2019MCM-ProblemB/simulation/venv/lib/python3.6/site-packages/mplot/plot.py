'''
This is the plot library.
It is designed to look and feel as similar as possible to Maple's plotting style.
It was designed partially while working at the Institute for Sustainable Future, University of Technology Sydney
I am indebted to Dr Peter Rickwood for assistance in the creation of the library. 

As mentioned it works similar to Maple's approach.

you start by defining a basic element (think line, or histogram etc).
The following elements exist

pie
boxplot
histogram
chart
harea
varea
areabetween
area
hline
vline
line
text

you create a number of these elements - e.g.
p1 = line(x,y)
p2 = area(x,y)
then display these elements:
display([p1,p2],example)
This will then create a file called example.png which displays the data.

Simple :-)
'''


import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
#import pylab
import matplotlib.pyplot as pyplot
import datetime
import math
import numpy
#import matplotlib.mlab
#import scipy.stats
import copy
import os
from mplot import createdate as createdate
from mplot.color import *

BADLEGENDS = ['',None,'None']
BOXWIDTHPERCENT = 0.5
DEFAULTWIDTH = 0.5
LINEOFBESTFITSTYLE = '--'
LINEOFBESTFITLEG = 'Trend'
FONTSIZE = 16
AIREDUCTION = 0.2
BOXPLOTPERS = [0,25,50,75,100]
HISTOGRAMYLABEL = {True:'Density',False:'Count'} # if no Y axis given for a plot, normed value gives default Y axis label.

CATEGORYNAMES = ['chart','boxplot']
COLORASSUMPTION = {'line':'list',
                   'text':BLACK,
                   'area':'list',
                   'chart':'list',
                   'hchart':'list',
                   'histogram':'list',
                   'vline':BLACK,
                   'hline':BLACK,
                   'varea':'list',
                   'harea':'list',
                   'boxplot':'list'}
CATGAP = 0.1
INNERCATGAP = 0.05
DATETYPES = [type(datetime.date(2000,1,1)),type(datetime.datetime(2000,1,1))]

LINEOFBESTFITCOLOR = [BLACK,DARK_GREY,LIGHT_GREY,BLACK]

SPECIFICCOLORS = [BLUECOLORS,REDCOLORS,GREENCOLORS,ORANGECOLORS]

MEDIANLINECOLOR = BLACK
MEDIANLINESTYLE = '--'
MEDIANTHICKNESS = 2
MEDIANLEGEND = 'Median'
MEANLINECOLOR = BLACK
MEANLINESTYLE = '-'
MEANTHICKNESS = 2
MEANLEGEND = 'Mean'

SECOND_YLABEL = None
SECOND_YTICKS = None
SECOND_YSUBTICKS = 0
SECOND_YROTATION = 0
SECOND_YALIGN = 'left'
SECOND_YMINMAX = None
SECOND_YZERO = False
SECOND_YFONTSIZE = FONTSIZE




def getlength(x,y):
    if len(x)!=len(y):
        print('Length of x and y mismatched: ',len(x),len(y))
        raise Exception()
    return len(x)

    
def boundbyxaxis(obj):
    '''
    So this function essentially, assumes the area should be bounded by the x axis
    '''
    if obj.x == []:
        return obj
    newx = [obj.x[0]]
    newy = [0]
    for i in range(0,obj.lenny):
        newx.append(obj.x[i])
        newy.append(obj.y[i])
    for index in range(0,obj.lenny):
        i = obj.lenny-1-index
        newx.append(obj.x[i])
        newy.append(0)
    obj.x = newx
    obj.y = newy
    return obj

def updateis(ci,ai,colorlist):
    ci += 1
    if ci < len(colorlist):
        return ci,ai
    ci = 0
    ai = ai - AIREDUCTION
    if ai < 0:
        ai = 0
    return ci,ai






def makeboxplot(obj,ax):
    edgecolor = BLACK
    leg = obj.legend
    if obj.edgecolor != None:
        edgecolor = obj.edgecolor
    for i in range(0,obj.lenny):
        lowx = obj.xtrans(obj.xbars[i][0])
        highx = obj.xtrans(obj.xbars[i][1])
        lowy = obj.ytrans(obj.pers[25][i])
        highy = obj.ytrans(obj.pers[75][i])
        if i > 0:
            leg = None
        xi = obj.xtrans(obj.x[i])
        oi = obj.ytrans(obj.pers[0][i])
        iooi = obj.ytrans(obj.pers[100][i])
        ax.fill([lowx,lowx,highx,highx,lowx],[lowy,highy,highy,lowy,lowy],color = obj.color,alpha = obj.alpha,label = leg,edgecolor = edgecolor,hatch = obj.hatch,fill = obj.fill)
        ax.plot([xi,xi],[lowy,oi],'-',color = edgecolor,label =None)
        ax.plot([xi,xi],[highy,iooi],'-',color = edgecolor,label =None)                          
        for key in obj.pers.keys():
            ax.plot([lowx,highx],[obj.ytrans(obj.pers[key][i]),obj.ytrans(obj.pers[key][i])],'-',color = edgecolor,label = None)
        if obj.mean == True:
            ax.plot([lowx,highx],[obj.ytrans(obj.means[i]),obj.ytrans(obj.means[i])],obj.meanstyle,color = edgecolor,label = None)
        

 

def makepie(obj,ax):
    empty=[]    
    for i in range(0,obj.lenny):
        empty.append(' ')
    if obj.colors == None:
        realcolors = []
        for i in range(0,obj.lenny):
            realcolors.append(WHITE)
    else:
        realcolors = obj.colors    
    legend = []
    for leg in obj.legends:
        if leg in BADLEGENDS:
            legend.append(None)
        else:
            legend.append(leg)
    graph = ax.pie(obj.fractions,labels=empty,startangle=obj.rotation,colors=realcolors)
    if obj.hatch != None:
        patches = graph[0]
        for i in range(0,len(obj.hatch)):
            patches[i].set_hatch(obj.hatch[i])
    return legend    


def getxis(obj,i):
    xis = []
    for elem in obj.xs[i]:
        xis.append(obj.xtrans(elem))
    return xis

def getyis(obj,i):
    yis = []
    for elem in obj.ys[i]:
        yis.append(obj.ytrans(elem))
    return yis

def makechart(obj,ax):
    leg = obj.legend
    edgecolor = obj.color
    if obj.edgecolor != None:
        edgecolor = obj.edgecolor
    for i in range(0,obj.lenny):
        if i > 0:
            leg = None
        xis = getxis(obj,i)
        yis = getyis(obj,i)
        ax.fill(xis,yis,obj.color,alpha=obj.alpha,label = leg,edgecolor = edgecolor,hatch = obj.hatch,fill = obj.fill,linewidth = obj.thickness)


def getxs(obj):
    xs = []
    for elem in obj.x:
        xs.append(obj.xtrans(elem))
    return xs

def getys(obj):
    ys = []
    for elem in obj.y:
        ys.append(obj.ytrans(elem))
    return ys



def makearea(obj,ax):
    edgecolor = obj.color
    if obj.edgecolor!=None:
        edgecolor = obj.edgecolor
    xs = getxs(obj)
    ys = getys(obj)
    ax.fill(xs,ys,obj.color,alpha=obj.alpha,label = obj.legend,edgecolor=edgecolor,hatch=obj.hatch,fill = obj.fill,linewidth = obj.thickness)

def getlineofbestfit(xdata,ydata):
    sumxy = getsumxy(xdata,ydata)
    sumxx = getsumxy(xdata,xdata)
    sumx = sum(xdata)
    sumy = sum(ydata)
    n = float(len(xdata))
    slope = (sumxy - (sumx*sumy/n))/float(sumxx-(sumx*sumx/n))
    intercept = numpy.mean(ydata) - slope*numpy.mean(xdata)
    return slope,intercept

def getsumxy(xdata,ydata):
    sumxy = 0
    for i in range(0,len(xdata)):
        sumxy += xdata[i]*ydata[i]
    return sumxy


def converttofloat(elem):
    if type(elem) not in DATETYPES:
        return elem
    val = elem.year
    startofyear = datetime.datetime(val,1,1)
    endofyear = datetime.datetime(val+1,1,1)
    daysinyear = (endofyear - startofyear).days
    days = (elem-startofyear).days
    seconds = (elem - startofyear).seconds
    val += days/float(daysinyear)
    val += (1/float(daysinyear))*(seconds/float(60*60*24))
    return val

def convertthelist(thelist):
    if thelist == []:
        return
    if type(thelist[0]) not in DATETYPES:
        return thelist
    newlist = []
    for elem in thelist:
        newelem = converttofloat(elem)
        newlist.append(newelem)
    return newlist


def makeline(obj,ax):
    xs = getxs(obj)
    ys = getys(obj)
    ax.plot(xs,ys,obj.style,color=obj.color,label = obj.legend,alpha=obj.alpha,linewidth = obj.thickness,markersize = obj.markthickness,solid_capstyle="butt")
    if obj.lineofbestfit != True:
        return
    m,b = getlineofbestfit(convertthelist(obj.x),convertthelist(obj.y))
    tag = ''
    if obj.legend != None:
        tag = obj.legend+' '
    ax.plot([min(xs),max(xs)],[m*converttofloat(min(xs))+b,m*converttofloat(max(xs))+b],LINEOFBESTFITSTYLE,color=obj.color,label = tag+LINEOFBESTFITLEG)
        

def maketext(obj,ax):
    ax.text(obj.xtrans(obj.x),obj.ytrans(obj.y),obj.text,ha = obj.ha,va=obj.va,rotation = obj.rot,fontsize = obj.fsize,color = obj.color)

def getdist(obj):
    normdist = matplotlib.mlab.normpdf(obj.bins,obj.mean,obj.std)
    if obj.normed == True:
        return normdist
    countdist = []
    scalefactor = len(obj.data)*obj.stepsize
    for elem in normdist:
        countdist.append(elem*scalefactor)
    return countdist
    



def makehistogram(obj,ax):
    #ax.hist(obj.data,bins = obj.bins,normed=obj.normed,alpha = obj.alpha,facecolor=obj.color,label = obj.legend,hatch=obj.hatch,fill=obj.fill,edgecolor = obj.edgecolor,linewidth = obj.thickness)
    ax.hist(obj.data,bins = obj.bins,density=obj.normed,alpha = obj.alpha,facecolor=obj.color,label = obj.legend,hatch=obj.hatch,fill=obj.fill,edgecolor = obj.edgecolor,linewidth = obj.thickness)
    if obj.gaussfit != True:
        return
    dist = getdist(obj)
    ax.plot(obj.bins,dist,obj.gausscolor,alpha = obj.gaussalpha,label=obj.gausslegend)
        


def nextintbelow(mini):
    inty = int(mini)
    if inty < mini:
        return inty
    return inty -1

def loghistogram(data,offset = 0,legend = None,color = None,alpha = 0.5,numbins = 100,normed = True,secondaxis = False,gaussfit = False,gausscolor = None,gaussstyle = '-',gausslegend = None,fill = True,edgecolor = BLACK,thickness = 1,mean = True,median = True):
    newdata = []
    mini = min(data)
    if mini <= offset:
        offset = int(mini)+1
        print('warning, changing offset to: '+str(offset))
    for val in data:
        logval = math.log(val+offset)
        newdata.append(logval)
    return histogram(newdata,legend = legend,color = color,alpha = alpha,numbins = numbins,normed = normed,secondaxis = secondaxis,gaussfit = gaussfit,gausscolor = gausscolor,gaussstyle = gaussstyle,gausslegend = gausslegend,fill = fill,edgecolor = edgecolor,thickness = thickness,mean = mean,median = median)

def reverse(thelist):
    revlist = copy.deepcopy(thelist)
    revlist.reverse()
    return revlist
    
def convertforboxplotsilos(x,y,xbins):
    '''
    x,y are lists of floats
    xbins is a list of elements of the form (start,stop,label)
    converts the data into a bin list (the x in boxplot) which is a list of the labels
    and partitions the y data based on where the x datapoint exists in the bins. 
    bins are created to be [start,stop)
    '''
    labels = []
    for silo in xbins:
        labels.append(silo[2])
    if len(x)!=len(y):
        raise Exception()
    ys= []
    for silo in xbins:
        ys.append([])
    for i in range(0,len(x)):
        xpt = x[i]
        ypt = y[i]
        for j in range(0,len(xbins)):
            if xbins[j][0] <= xpt and xpt < xbins[j][1]:
                ys[j].append(ypt)
    return labels,ys




class pie():
    def __init__(self,fractions,legends,colors = True,alphas = None,hatch = None,rotation = 0):
        '''
        Note: colors is either True (I'll figure out the color based on the color list)
                               False (pie will be white)
                               list (the list of colors)
            Fractions are self evident the pieces of the pie e.g. 0.25, 0.3, 0.45
            legends is labels for the fractions e.g. ['cats','dogs','mice']
        '''
        self.name = 'pie'
        self.func = makepie
        self.fractions = fractions
        self.legends = legends
        self.colors = colors
        self.alphas = alphas
        self.hatch = hatch
        self.rotation = rotation
        self.lenny = getlength(fractions,legends)
        self.secondaxis = False




class boxplot():
    def __init__(self,x,y,legend = None,color = None,alpha = 0.5,hatch = None,secondaxis = False,edgecolor = None,mean = False,meanstyle = '--',width = None,fill = True,thickness = 1,markthickness = None):
        '''
        In this case X is a list ['Cat','Dog','Mouse']
        y is a series of values for the box plot [[cat_1,..,cat_n],[dog_1,...,dog_n],[mouse_1,..,mouse_n]]
        '''
        self.name = 'boxplot'
        self.func = makeboxplot
        self.rawx = x
        self.rawy = y
        self.x = None
        self.y = None
        self.pers = None
        self.means = None
        self.legend = legend
        self.color = color
        self.edgecolor = edgecolor
        self.alpha = alpha
        self.hatch = hatch
        self.mean = mean
        self.meanstyle = meanstyle
        self.width = width
        self.secondaxis = secondaxis
        self.lenny = getlength(x,y)
        self.fill = fill
        self.xbars = None
        self.minx = None
        self.maxx = None
        miny,maxy = findminymaxy(y)
        self.miny = miny
        self.maxy = maxy
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


class histogram():
    def __init__(self,data,legend = None,color = None,alpha = 0.5,numbins = 100,normed = True,hatch = None,secondaxis = False,gaussfit = False,gausscolor = None,gaussstyle = '-',gausslegend = None,gaussalpha = 1,fill = True,edgecolor = BLACK,thickness = 1,markthickness = None,mean = True,median = True):
        '''
        This is a straight forward histogram.
        data is the data e.g. [0,0.1,0.2]
        '''
        self.name = 'histogram'
        self.func = makehistogram
        self.data = data
        self.bins = None
        self.legend = legend
        if hatch != None and color == None:
            self.color = WHITE
            self.alpha = 1
            self.fill = False
        else:
            self.color = color
            self.alpha = alpha
            self.fill = fill    
        self.numbins = numbins
        self.stepsize = None
        self.normed = normed
        self.secondaxis = secondaxis
        self.hatch = hatch
        self.gaussfit = gaussfit
        self.gausscolor = gausscolor
        self.gaussstyle = gaussstyle
        self.gausslegend = gausslegend
        self.gaussalpha = gaussalpha
        self.mean = numpy.mean(data)
        self.median = numpy.median(data)
        self.std = numpy.std(data)
        self.mindata = min(data)
        self.maxdata = max(data)
        self.edgecolor = edgecolor
        self.minx = None
        self.maxx = None
        self.miny = 0
        self.maxy = None
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick

        self.makemean = mean
        self.makemedian = median
        self.xtrans = None
        self.ytrans = None
        

    
class chart():
    def __init__(self,cats,vals,legend = None,color = None, alpha = 1,filledge = None,hatch = None,secondaxis = False,stacked = False,edgecolor = None,fill = True,thickness = 1,markthickness = None):
        '''
        cats can be 0,1,2 or Cat, Dog, Rabbit
        '''
        self.name = 'chart'
        self.func = makechart
        self.rawx = cats
        self.x = None
        self.xs = None
        self.ys = None
        self.y = vals
        self.legend = legend
        self.color = color
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = stacked
        self.secondaxis = secondaxis
        self.edgecolor = edgecolor
        self.lenny = getlength(cats,vals)
        self.fill = True
        self.minx = None
        self.maxx = None
        self.miny = min(vals)
        self.maxy = max(vals)
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


class hchart():
    def __init__(self,cats,vals,legend = None,color = None, alpha = 1,filledge = None,hatch = None,secondaxis = False,stacked = False,edgecolor = None,fill = True,thickness = 1,markthickness = None):
        self.name = 'hchart'
        self.func = makechart
        self.x = vals
        self.xs = None
        self.ys = None
        self.y = None
        self.rawy = cats
        self.legend = legend
        self.color = color
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = stacked
        self.secondaxis = secondaxis
        self.edgecolor = edgecolor
        self.lenny = getlength(cats,vals)
        self.fill = True
        self.minx = min(vals)
        self.maxx = max(vals)
        self.miny = None
        self.maxy = None
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None




class harea():
    def __init__(self,y,legend = None,color = None, alpha = 0.25,filledge = None,hatch = None,secondaxis = False,stacked = True,byxaxis = True,edgecolor = None,fill = True,thickness = 1,markthickness = None):
        self.name = 'harea'
        self.func = makearea
        self.x = None
        self.y = recty(y)
        self.legend = legend
        self.color = color
        self.edgecolor = edgecolor
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = stacked
        self.byxaxis = byxaxis
        self.secondaxis = secondaxis
        self.lenny = len(self.y)
        if hatch !=None:
            self.fill = False
        else:
            self.fill = fill
        self.minx = None
        self.maxx = None
        self.miny = min(y)
        self.maxy = max(y)
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


class varea():
    def __init__(self,x,legend = None,color = None, alpha = 0.25,filledge = None,hatch = None,secondaxis = False,stacked = True,byxaxis = True,edgecolor = None,fill = True,thickness = 1):
        '''
        x is the only necessary input:
        format is of the form [lowerbound,upperbound] or (lowerbound,upperbound)
        '''
        self.name = 'varea'
        self.func = makearea
        self.x = rectx(x)
        self.y = None
        self.legend = legend
        self.color = color
        self.edgecolor = edgecolor
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = stacked
        self.byxaxis = byxaxis
        self.secondaxis = secondaxis
        self.lenny = len(self.x)
        if hatch !=None:
            self.fill = False
        else:
            self.fill = fill
        self.minx = min(x)
        self.maxx = max(x)
        self.miny = None
        self.maxy = None
        self.thickness = thickness
        self.xtrans = None
        self.ytrans = None




class areabetween():
    def __init__(self,x,yhigh,ylow,legend = None,color = None, alpha = 1,filledge = None,hatch = None,secondaxis = False,edgecolor = None,fill = True,thickness = 1):
        if len(x)!= len(yhigh) or len(x) != len(ylow):
            print('issue with data')
            raise Exception()
        newx = x + reverse(x) + [x[0]]
        newy = yhigh + reverse(ylow) + [yhigh[0]]
        self.name = 'areabetween'
        self.func = makearea
        self.x = newx
        self.y = newy
        self.legend = legend
        self.color = color
        self.edgecolor = edgecolor
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = False
        self.byxaxis = False
        self.secondaxis = secondaxis
        self.lenny = getlength(newx,newy)
        if hatch !=None:
            self.fill = False
        else:
            self.fill = fill
        self.minx = min(newx)
        self.maxx = max(newx)
        self.miny = min(newy)
        self.maxy = max(newy)
        self.thickness = thickness
        self.xtrans = None
        self.ytrans = None
        





class area():
    def __init__(self,x,y,legend = None,color = None, alpha = 1,filledge = None,hatch = None,secondaxis = False,stacked = True,byxaxis = True,edgecolor = None,fill = True,thickness = 1):
        self.name = 'area'
        self.func = makearea
        self.x = x
        self.y = y
        self.legend = legend
        self.color = color
        self.edgecolor = edgecolor
        self.alpha = alpha
        self.filledge = filledge
        self.hatch = hatch
        self.stacked = stacked
        self.byxaxis = byxaxis
        self.secondaxis = secondaxis
        self.lenny = getlength(x,y)
        if hatch !=None:
            self.fill = False
        else:
            self.fill = fill
        self.minx = min(x)
        self.maxx = max(x)
        self.miny = min(y)
        self.maxy = max(y)
        self.thickness = thickness
        self.xtrans = None
        self.ytrans = None





class hline():
    def __init__(self,y,legend = None,color = None, alpha = 1,style = '-',secondaxis = False,thickness = 1,markthickness = None):
        self.name = 'hline'
        self.func = makeline
        self.x = None
        self.y = [y,y]
        self.legend = legend
        self.color = color
        self.alpha = alpha
        self.style = style
        self.secondaxis = secondaxis
        self.lenny = 2
        self.minx = None
        self.maxx = None
        self.miny = y
        self.maxy = y
        self.lineofbestfit = False
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


class vline():
    def __init__(self,x,legend = None,color = None, alpha = 1,style = '-',secondaxis = False,thickness = 1,markthickness = None):
        self.name = 'vline'
        self.func = makeline
        self.x = [x,x]
        self.y = None
        self.legend = legend
        self.color = color
        self.alpha = alpha
        self.style = style
        self.secondaxis = secondaxis
        self.lenny = 2
        self.minx = x
        self.maxx = x
        self.miny = None
        self.maxy = None
        self.lineofbestfit = False
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


class line():
    def __init__(self,x,y,legend = None,color = None, alpha = 1,style = '-',secondaxis = False,lineofbestfit = False,thickness = 1,markthickness = None):
        self.name = 'line'
        self.func = makeline
        self.x = x
        self.y = y
        self.legend = legend
        self.color = color
        self.alpha = alpha
        self.style = style
        self.secondaxis = secondaxis
        self.lenny = getlength(x,y)
        self.minx = min(x)
        self.maxx = max(x)
        self.miny = min(y)
        self.maxy = max(y)
        self.lineofbestfit = lineofbestfit
        self.thickness = thickness
        mthick = thickness
        if markthickness != None:
            mthick = markthickness
        self.markthickness = mthick
        self.xtrans = None
        self.ytrans = None


        
class text():
    def __init__(self,x,y,text,secondaxis = False,fontsize = FONTSIZE,halign = 'center',valign = 'center',rotation = 0,color = 'k'):
        self.name = 'text'
        self.func = maketext
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.legend = None
        self.secondaxis = secondaxis
        self.lenny = 1
        self.ha = halign
        self.va = valign
        self.rot = rotation
        self.fsize = fontsize
        self.minx = x
        self.maxx = x
        self.miny = y
        self.maxy = y
        self.xtrans = None
        self.ytrans = None



class lineclass():
    def __init__(self,line,name):
        self.name = name
        self.line = line


def getline(col,fname,colname):
    f = open(fname,'r')
    header = f.readline()
    points = []
    i = -1
    for line in f:
        i +=1
        bits = line.strip().split(',')
        elem = bits[col].strip()
        if elem in ['','0']:
            continue
        points.append(bits[colname])
    f.close()
    return points

def readfile(fname,colname,colstart):
    f = open(fname,'r')
    header = f.readline()
    names = []
    for line in f:
        name = line.strip().split(',')[colname]
        names.append(name)
    f.close()
    hbits = header.strip().split(',')
    lines = []
    groups = []
    for i in range(colstart,len(hbits)):
        group = hbits[i]
        groups.append(group)
        line = getline(i,fname,colname)
        lines.append(lineclass(line,group))
    return lines,names,groups

def getallnames(linedata):
    names = {}
    for line in linedata:
        for node in line.line:
            names[node] = True
    return names.keys()

def getallgroups(linedata):
    groups = {}
    for line in linedata:
        group = line.name
        groups[group] = True
    return groups.keys()
        
def circleplot(data,additionalplots = [],names = 'ALL',groups = 'ALL'):
    '''
    if data = string --> assume data is a csv file with a table (first column is the names, first row is the groups)
    if data = list of line classes (then its already clean)

    names and groups are either 'ALL' or a sublist of allnames/allgroups
    
    '''
    if type(data) == type('string'):
        linedata,allnames,allgroups = readfile(data,0,1)
    elif type(data) == type(['l','i','s','t']):
        linedata = data
        allnames = getallnames(linedata)
        allgroups = getallgroups(linedata)
    else:
        raise Exception()
    ### TODO --> keep going, add in functionality so that plot can handle this graph.


    



def findminymaxy(ys):
    miny = None
    maxy = None
    for y in ys:
        ny = min(y)
        xy = max(y)
        if miny == None:
            miny = ny
        if maxy ==None:
            maxy = xy
        if ny < miny:
            miny = ny
        if xy > maxy:
            maxy = xy
    return miny,maxy
        



def getsecond(objects,second_ylabel,second_yticks,second_ysubticks,second_yrotation,second_yalign,second_yminmax,second_yzero,second_yfontsize):
    if second_ylabel != SECOND_YLABEL:
        return True
    if second_yticks != SECOND_YTICKS:
        return True
    if second_ysubticks != SECOND_YSUBTICKS:
        return True
    if second_yrotation != SECOND_YROTATION:
        return True
    if second_yalign != SECOND_YALIGN:
        return True
    if second_yminmax != SECOND_YMINMAX:
        return True
    if second_yzero != SECOND_YZERO:
        return True
    if second_yfontsize != SECOND_YFONTSIZE:
        return True
    for obj in objects:
        if obj.secondaxis == True:
            return True
    return False

def initplot(objects,fontsize,figsize,frame,second):
    ax2 = None
    matplotlib.rcParams.update({'font.size': fontsize})
    fig = pyplot.figure()
    fig.clf()
    fig.set_size_inches((figsize[0],figsize[1]))
    ax1=fig.add_subplot(111,frameon=frame)
    if not frame:
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
    else:
        ax1.yaxis.set_ticks_position('left')
        ax1.xaxis.set_ticks_position('bottom')
    if second:
        ax2=ax1.twinx()
    return fig,ax1,ax2



def makelegend(objects,legend):
    if legend != None:
        return True
    for obj in objects:
        if obj.legend in BADLEGENDS:
            continue
        return True
    return False

def sortlegends_string(handles,labels,legendorder):
    if legendorder == 'NORMAL':
        return handles,labels
    if legendorder == 'REVERSE':
        handles.reverse()
        labels.reverse()
        return handles,labels
    if legendorder != 'ALPHABETIC':
        raise Exception()
    randomorder = []
    for i in range(0,len(labels)):
        randomorder.append((labels[i],i))
    alphaorder = sorted(randomorder,key = lambda a:a[0])
    newhandles = []
    newlabels = []
    for pair in alphaorder:
        i = pair[1]
        newhandles.append(handles[i])
        newlabels.append(labels[i])
    return newhandles,newlabels




def sortlegends(handles,labels,legendorder,ncols,legenddirection):
    if type(legendorder) == type('string'):
        newhandles,newlabels = sortlegends_string(handles,labels,legendorder.upper())
    elif type(legendorder) in [type([0,1]),type((0,1))]:
        newhandles,newlabels = sortlengend_order(handles,labels,legendorder)
    else:
        raise Exception()
    if legenddirection == 'VERTICAL':
        return newhandles,newlabels
    if legenddirection != 'HORIZONTAL':
        raise Exception()
    num = len(newlabels)
    ls = []
    hs = []
    rows = int(num/ncols)+1
    for c in range(0,ncols):
        for r in range(0,rows):
            i = r*ncols + c
            if i >= num:
                continue
            ls.append(newlabels[i])
            hs.append(newhandles[i])
    return hs,ls


def sortlengend_order(handles,labels,legendorder):
    newhandles = []
    newlables = []
    for leg in legendorder:
        if leg not in labels:
            print('Warning issue with legendorder: '+str(leg) +' not in labels')
            continue
        i = labels.index(leg)
        newlabels.append(labels[i])
        newhandles.append(handles[i])
    return newhandles,newlabels


def saveplot(objects,fig,ax1,ax2,fname,rawext,lloc,lpos,ncols,legendorder,legenddirection,minmax,resolution,legend = None):
    rawext = rawext.replace('.','')
    ext = rawext    
    if ext == 'pdf2ps':
        ext = 'pdf'
    ax1.set_xlim(minmax[0][0],minmax[0][1])
    ax1.set_ylim(minmax[1][0],minmax[1][1])
    if ax2!=None:
        ax2.set_ylim(minmax[2][0],minmax[2][1])
    if makelegend(objects,legend):
        handles, labels = ax1.get_legend_handles_labels()
        if ax2!= None:
            htemp, ltemp = ax2.get_legend_handles_labels()
            handles+=htemp
            labels+=ltemp
        if legend != None:
            labels = legend
        handles,labels = sortlegends(handles,labels,legendorder,ncols,legenddirection.upper())
        lgd = ax1.legend(handles,labels,ncol=ncols,loc = lpos,bbox_to_anchor=lloc)
        pyplot.savefig(fname+'.'+ext,bbox_extra_artists=(lgd,), bbox_inches='tight',dpi = resolution)
    else:
        pyplot.savefig(fname+'.'+ext, bbox_inches='tight',dpi = resolution)
    pyplot.close(fig)
    pyplot.clf()
    if rawext == 'pdf2ps':
        os.system('pdf2ps '+fname+'.pdf '+fname+'.ps')

    
def getmaxlen(objects):
    maxy = 0
    for obj in objects:
        if obj.lenny > maxy:
            maxy = obj.lenny
    return maxy


def getname(obj,i):
    if obj.legend == None:
        return obj.name+'_'+str(i)
    return obj.legend

def writeheader(objects,f):
    for i in range(0,len(objects)):
        obj = objects[i]
        name = getname(obj,i)
        if i > 0:
            f.write(',')
        f.write(name+' x,'+name+' y')
    f.write('\n')

def writeoutsub(objects,col,f):
    for i in range(0,len(objects)):
        if i > 0:
            f.write(',')
        obj = objects[i]
        if obj.lenny <= col:
            f.write(',')
            continue
        f.write(str(obj.x)+','+str(obj.y))
    f.write('\n')
        
def writeout(objects,fname,write):
    if write != True:
        return
    f = open(fname+'.csv','w')
    maxlen = getmaxlen(objects)
    writeheader(objects,f)
    for i in range(0,maxlen):
        writeoutsub(objects,i,f)
    f.close()



def stackitup(overlay,obj):
    newy = []
    for i in range(0,obj.lenny):
        x = obj.x[i]
        if x not in overlay:
            overlay[x] = 0
        overlay[x] += obj.y[i]
        newy.append(overlay[x])
    obj.y = newy
    obj.miny = min(newy)
    obj.maxy = max(newy)
    return obj,overlay


def getstack(objects,name,specificstacked,stacked):
    if stacked in [True,False]:
        return stacked
    if specificstacked in [True,False]:
        return specificstacked
    for obj in objects:
        if obj.name!=name:
            continue
        if obj.stacked == True:
            return True
    return False


def getcategories(objects):
    cats = {'x':{},'y':{}}
    indexes = {'x':1,'y':1}
    for obj in objects:
        if obj.name not in ['chart','boxplot','hchart']:
            continue
        if obj.name == 'hchart':
            cat,i = getcategories_sub(obj,cats['y'],'rawy',indexes['y'])
            cats['y'] = cat
            indexes['y'] = i
        else:
            cat,i = getcategories_sub(obj,cats['x'],'rawx',indexes['x'])
            cats['x'] = cat
            indexes['x'] = i
    return cats

def getcategories_sub(obj,cat,att,i):
    newcats = getattr(obj,att)
    if newcats == []:
        return cat,i
    for nc in newcats:
        if nc in cat:
            continue
        cat[nc] = i
        i+=1
    return cat,i



def fixboxplots(objects,categories,width,mindiff,offsets):
    rawoffsets = getoffsetindexes(objects,'boxplot')
    for i in rawoffsets:
        sidealongboxplot(objects[i],offsets[i],width,categories)
    return objects

        
def sidealongboxplot(obj,offset,width,categories):
    newx = []
    newy = []
    per_0 = []
    pers = {}
    xbars = []
    for key in BOXPLOTPERS:
        pers[key] = []
    means = []
    for i in range(0,obj.lenny):
        x = categories[obj.rawx[i]]
        newx.append(x+offset+width/2.0)
        xbars.append((x+offset,x+offset+width))
        vals = obj.rawy[i]
        for key in BOXPLOTPERS:
            pers[key].append(numpy.percentile(vals,key))
        if obj.mean == True:
            means.append(numpy.mean(vals))
        newy.append(numpy.median(vals))
    obj.x = newx
    obj.y = newy
    obj.xbars = xbars
    obj.means = means
    obj.pers = pers
    obj.minx = min(newx)-width/2.0
    obj.maxx = max(newx)+width/2.0
    obj.miny = min(pers[0])
    obj.maxy = max(pers[100])


def fixhcharts(objects,categories,width,mindiff,offsets,stack):
    if stack:
        return fixhcharts_stacked(objects,categories,width,mindiff,offsets)
    return fixhcharts_sidebyside(objects,categories,width,mindiff,offsets)

def fixhcharts_sidebyside(objects,categories,width,mindiff,offsets):
    '''
    first up, need to get the number of things plotted side-by-side
    '''
    rawoffsets = getoffsetindexes(objects,'hchart')
    for i in rawoffsets:
        sidealonghchart(objects[i],offsets[i],width,categories)
    return objects

def sidealonghchart(obj,offset,width,categories):
    newx = []
    newy = []
    newxs = []
    newys = []
    for i in range(0,obj.lenny):
        y = categories[obj.rawy[i]]
        newy.append(y)
        newx.append(obj.x[i])
        newys.append([y+offset,y+offset,y+offset+width,y+offset+width,y+offset])        
        newxs.append([0,obj.x[i],obj.x[i],0,0])
    obj.xs = newxs
    obj.ys = newys
    obj.x = newx
    obj.y = newy
    obj.minx = min([0,min(newx)])
    obj.maxx = max([0,max(newx)])
    obj.miny = min(newy)-width/2.0
    obj.maxy = max(newy)+width/2.0
    


def stackhchartup(obj,overlay,width,categories,offset):
    newxs = []
    newys = []
    newx = []
    newy = []
    for i in range(0,obj.lenny):
        y = categories[obj.rawy[i]]
        if y not in overlay['neg']:
            overlay['neg'][y] = 0
            overlay['pos'][y] = 0
        key = 'pos'
        if obj.x[i] < 0:
            key = 'neg'
        overlay[key][y] += obj.x[i]
        newx.append(overlay[key][y])
        newxs.append([0,overlay[key][y],overlay[key][y],0,0])
        newy.append(y)
        newys.append([y+offset,y+offset,y+offset+width,y+offset+width,y+offset])                
    obj.xs = newxs
    obj.ys = newys
    obj.x = newx
    obj.y = newy
    obj.minx = min([0,min(newx)])
    obj.maxx = max([0,max(newx)])
    obj.miny = min(newy)-width/2.0
    obj.maxy = max(newy)+width/2.0
    return obj,overlay




def fixhcharts_stacked(objects,categories,width,mindiff,offsets):
    newobjects = []
    order = []
    stackedobjects = []
    offi = getoffsetindexes(objects,'hchart')
    if offi == []:
        return objects
    offset = offsets[min(offi)]
    overlay = {'neg':{},'pos':{}}
    for i in range(0,len(objects)):
        obj = objects[i]
        if obj.name != 'hchart':
            newobjects.append(obj)
            continue
        obj,overlay = stackhchartup(obj,overlay,width,categories,offset)
        order.append(i)
        stackedobjects.append(obj)
        newobjects.append(None)
    if order == []:
        return newobjects,categories,mindiff
    order.reverse()
    for i in range(0,len(order)):
        index = order[i]
        newobjects[index] = stackedobjects[i]
    return newobjects







def fixcharts(objects,categories,width,mindiff,offsets,stack):
    if stack:
        return fixcharts_stacked(objects,categories,width,mindiff,offsets)
    return fixcharts_sidebyside(objects,categories,width,mindiff,offsets)

    


def fixcharts_sidebyside(objects,categories,width,mindiff,offsets):
    '''
    first up, need to get the number of things plotted side-by-side
    '''
    rawoffsets = getoffsetindexes(objects,'chart')
    for i in rawoffsets:
        sidealongchart(objects[i],offsets[i],width,categories)
    return objects


def sidealongchart(obj,offset,width,categories):
    newx = []
    newy = []
    newxs = []
    newys = []
    for i in range(0,obj.lenny):
        x = categories[obj.rawx[i]]
        newx.append(x)
        newy.append(obj.y[i])
        newxs.append([x+offset,x+offset,x+offset+width,x+offset+width,x+offset])        
        newys.append([0,obj.y[i],obj.y[i],0,0])
    obj.xs = newxs
    obj.ys = newys
    obj.x = newx
    obj.y = newy
    obj.minx = min(newx)-width/2.0
    obj.maxx = max(newx)+width/2.0
    obj.miny = min([0,min(newy)])
    obj.maxy = max([0,max(newy)])
    

def getwidth(categories,num):
    mindiff = {}
    width = {}
    for key in categories:
        md,w = getwidth_sub(categories[key],num[key])
        mindiff[key] = md
        width[key] = w
    return mindiff,width
    
def getwidth_sub(categories,num):
    svals = sorted(categories.values())
    if len(svals) <=1:
        if num == 1:
            return 1,1 - CATGAP
        else:
            return 1,(1-CATGAP-INNERCATGAP)/float(num)
    mindiff = None
    for i in range(1,len(svals)):
        d = svals[i] - svals[i-1]
        if mindiff == None:
            mindiff = d
        elif d < mindiff:
            mindiff = d
    if num == 1:
        return mindiff,(1-CATGAP)*mindiff
    return mindiff,(1-CATGAP-INNERCATGAP)*mindiff/float(num)


def stackchartup(obj,overlay,width,categories,offset):
    newxs = []
    newys = []
    newx = []
    newy = []
    for i in range(0,obj.lenny):
        x = categories[obj.rawx[i]]
        if x not in overlay['neg']:
            overlay['neg'][x] = 0
            overlay['pos'][x] = 0
        key = 'pos'
        if obj.y[i] < 0:
            key = 'neg'
        overlay[key][x] += obj.y[i]
        newx.append(x)
        newy.append(overlay[key][x])
        newxs.append([x+offset,x+offset,x+offset+width,x+offset+width,x+offset])        
        newys.append([0,overlay[key][x],overlay[key][x],0,0])
    obj.xs = newxs
    obj.ys = newys
    obj.x = newx
    obj.y = newy
    obj.minx = min(newx)-width/2.0
    obj.maxx = max(newx)+width/2.0
    obj.miny = min([0,min(newy)])
    obj.maxy = max([0,max(newy)])
    return obj,overlay



def fixcharts_stacked(objects,categories,width,mindiff,offsets):
    newobjects = []
    order = []
    stackedobjects = []
    offi = getoffsetindexes(objects,'chart')
    if offi == []:
        return objects
    offset = offsets[min(offi)]
    overlay = {'neg':{},'pos':{}}
    for i in range(0,len(objects)):
        obj = objects[i]
        if obj.name != 'chart':
            newobjects.append(obj)
            continue
        obj,overlay = stackchartup(obj,overlay,width,categories,offset)
        order.append(i)
        stackedobjects.append(obj)
        newobjects.append(None)
    if order == []:
        return newobjects,categories,mindiff
    order.reverse()
    for i in range(0,len(order)):
        index = order[i]
        newobjects[index] = stackedobjects[i]
    return newobjects

    

def fixareas(objects,areastacked,stacked):
    '''
    Basically, I want to add in data to the areas, to account for:
    1) bounded by x axis
    2) stacked.
    '''
    stack = getstack(objects,'area',areastacked,stacked)    
    newobjects = []
    order = []
    stackedobjects = []
    overlay = {}
    for i in range(0,len(objects)):
        obj = objects[i]
        if obj.name not in ['area']:
            newobjects.append(obj)
            continue
        if obj.byxaxis and stack == False:        
            obj = boundbyxaxis(obj)
            newobjects.append(obj)
            continue
        if stack == False:
            newobjects.append(obj)
            continue
        obj,overlay = stackitup(overlay,obj)
        if obj.byxaxis:
            obj = boundbyxaxis(obj)
        order.append(i)
        stackedobjects.append(obj)
        newobjects.append(None)
    if order == []:
        return newobjects
    order.reverse()
    for i in range(0,len(order)):
        index = order[i]
        newobjects[index] = stackedobjects[i]
    return newobjects
        
def fixhistogramfit(objects):
    newobjects = []
    for obj in objects:
        if obj.name != 'histogram':
            newobjects.append(obj)
            continue
        if obj.gausscolor == None and obj.gaussfit == True:
            obj.gausscolor = obj.color
        newobjects.append(obj)        
        if obj.makemean == True:
            meany = vline(obj.mean,color = MEANLINECOLOR,style = MEANLINESTYLE,thickness = MEANTHICKNESS,legend = MEANLEGEND)
            newobjects.append(meany)
        if obj.makemedian == True:
            mediany = vline(obj.median,color = MEDIANLINECOLOR,style = MEDIANLINESTYLE,thickness = MEDIANTHICKNESS,legend = MEDIANLEGEND)
            newobjects.append(mediany)
    return newobjects
    
def fixcolor(objects,colorlist):
    ci = 0
    ai = 1
    for obj in objects:
        if obj.color == None:
            if COLORASSUMPTION[obj.name] != 'list':
                obj.color = COLORASSUMPTION[obj.name]
            else:
                obj.color = colorlist[ci]
                if obj.alpha == 1:
                    obj.alpha = ai         
                ci,ai = updateis(ci,ai,colorlist)
    return objects

def getrelivanti(objects,name):
    reli = []
    for i in range(0,len(objects)):
        if objects[i].name != name:
            continue
        reli.append(i)
    return reli

def getmaxdata(obj):
    return obj.maxdata

def getmindata(obj):
    return obj.mindata

def getnumbins(obj):
    return obj.numbins    

def getnormed(obj):
    return obj.normed

def getsecondaxis(obj):
    return obj.secondaxis

def getattributes(objects,func,reli = None):
    if reli == None:
        reli = range(0,len(objects))
    thelist = []
    for i in reli:
        val = func(objects[i])
        thelist.append(val)
    return thelist



def getbins_sub(minx,maxx,stepsize):
    if stepsize == 0:
        print('warning issues with histogram')
        return (minx,)
    val = minx
    bins = []
    while True:
        bins.append(val)
        val += stepsize
        if val > maxx:
            bins.append(val)
            break
    return tuple(bins)


def getnorm(objects,reli):
    norms = getattributes(objects,getnormed,reli)
    norm = False
    if True in norms:
        norm = True
    return norm

def fixylabels(objects,reli,norm,ylabel,second_ylabel):
    axes = getattributes(objects,getsecondaxis,reli)
    if False in axes and ylabel == None:
        ylabel = HISTOGRAMYLABEL[norm]
    if True in axes and second_ylabel == None:
        second_ylabel = HISTOGRAMYLABEL[norm]
    return ylabel,second_ylabel


def getbins(objects,ylabel,second_ylabel,xminmax):
    reli = getrelivanti(objects,'histogram')
    if reli == []:
        return objects,ylabel,second_ylabel
    norm = getnorm(objects,reli)
    ylabel,second_ylabel = fixylabels(objects,reli,norm,ylabel,second_ylabel)
    maxx = max(getattributes(objects,getmaxdata,reli))
    minx = min(getattributes(objects,getmindata,reli))
    if xminmax != None:
        minx = xminmax[0]
        maxx = xminmax[1]
    numbins = max(getattributes(objects,getnumbins,reli))
    stepsize = (maxx - minx)/float(numbins)
    bins = getbins_sub(minx,maxx,stepsize)
    for i in reli:
        objects[i].bins = bins
        objects[i].stepsize = stepsize
        objects[i].minx = minx
        objects[i].maxx = maxx
        #vals,meh,ign = pylab.hist(objects[i].data,bins,normed = norm)
        vals,meh,ign = pylab.hist(objects[i].data,bins,density = norm)
        objects[i].maxy = max(vals)
        objects[i].normed = norm
    return objects,ylabel,second_ylabel

def maketitle(title):
    if title in [None,'']:
        return
    pyplot.title(title)


def getfontsizes(xfontsize,yfontsize,second_yfontsize,axisfontsize):
    if axisfontsize != None:
        return axisfontsize,axisfontsize,axisfontsize
    return xfontsize,yfontsize,second_yfontsize


def makeaxis(ax1,ax2,objects,cats,mindiff,xlabel,xticks,xsubticks,xrotation,xalign,xminmax,xzero,rawxfontsize,ylabel,yticks,ysubticks,yrotation,yalign,yminmax,yzero,rawyfontsize,second_ylabel,second_yticks,second_ysubticks,second_yrotation,second_yalign,second_yminmax,second_yzero,rawsecond_yfontsize,axisfontsize,xlog,xlogbase,xlog0,ylog,ylogbase,ylog0,second_ylog,second_ybase,second_ylog0):
    xfontsize,yfontsize,second_yfontsize = getfontsizes(rawxfontsize,rawyfontsize,rawsecond_yfontsize,axisfontsize)
    trans = {}
    minx,maxx,xlocs,xvals,xtrans = makeaxis_sub(ax1,'x',objects,xlabel,xticks,xsubticks,xrotation,xalign,xminmax,xzero,xfontsize,xlog,xlogbase,xlog0,categories = cats['x'],mindiff = mindiff['x'])
    miny,maxy,ylocs,yvals,ytrans = makeaxis_sub(ax1,'y',objects,ylabel,yticks,ysubticks,yrotation,yalign,yminmax,yzero,yfontsize,ylog,ylogbase,ylog0,categories = cats['y'],mindiff = mindiff['y'])
    trans['x'] = xtrans
    trans['y'] = ytrans
    ax1.axis([minx,maxx,miny,maxy])
    minsy = None
    maxsy = None
    ylocss = None
    yvalss = None
    if ax2 != None:
        minsy,maxsy,ylocss,yvalss,secondytrans = makeaxis_sub(ax2,'sy',objects,second_ylabel,second_yticks,second_ysubticks,second_yrotation,second_yalign,second_yminmax,second_yzero,second_yfontsize,second_ylog,second_ybase,second_ylog0)
        ax2.axis([minx,maxx,minsy,maxsy])
        trans['sy'] = secondytrans
    return ((minx,maxx),(miny,maxy),(minsy,maxsy)),((xlocs,xvals),(ylocs,yvals),(ylocss,yvalss)),trans


def getminmax(objects,xory):
    vals = []
    for obj in objects:
        if xory == 'x' and obj.minx!=None:
            vals.append(obj.minx)
            vals.append(obj.maxx)
        elif xory == 'y' and not obj.secondaxis and obj.miny!=None:
            vals.append(obj.miny)
            vals.append(obj.maxy)
        elif xory == 'sy' and obj.secondaxis and obj.miny!=None:
            vals.append(obj.miny)
            vals.append(obj.maxy)
    if vals == []:
        return 0,1,type(1.0)
    maxval = max(vals)
    minval = min(vals)
    return minval,maxval,type(minval)
            



def getlocs(mini,maxi,tp,subticks,log,logbase,log0):
    if tp in DATETYPES:
        return createdateticks(mini,maxi,step = None,subticks = subticks)
    return createvalticks(mini,maxi,subticks = subticks,log = log,logbase=logbase,log0 = log0)

    

def getdiffval(diff,vmax):
    if diff == 0 :
        if vmax >0:
            difflog = math.log10(vmax)
            difforder = int(math.floor(difflog))
            diffmag = pow(10,difforder)
        else:
            diffmag = 1
        diffval = 1
    else:
        difflog = math.log10(diff)
        difforder = int(math.floor(difflog))
        diffmag = pow(10,difforder)
        diffval = diff/float(diffmag)
    return diffval,diffmag


def getrealstep(step,diffval,diffmag):
    if step != None:
        return step
    if diffval < 2.5:
        diffstep = 0.25
    elif diffval < 5:
        diffstep = 0.5
    elif diffval < 7.5:
        diffstep = 1
    elif diffval < 10:
        diffstep = 2
    else:
        raise Exception()
    return diffstep*diffmag

def getround(order):
    def getround_sub(val):
        if val > 10 or val == int(val):
            return str(int(round(val,order)))
        return str(round(val,order))
    return getround_sub

def makeint(val):
    return str(int(val))




def getyearmonth(targetyear,targetmonth):
    ty = targetyear
    tm = targetmonth
    while tm > 12:
        tm = tm - 12
        ty += 1
    return int(ty),int(tm)        


def makedatetime(seconds = 0,days = 0,months = 0,step = 0):
    def makedatetime_seconds(dt):
        return dt + datetime.timedelta(seconds = seconds)
    def makedatetime_days(dt,locs,vals):
        newdt = dt + datetime.timedelta(days = days)
        if step == 0:
            return newdt,locs,vals
        tmp = dt + datetime.timedelta(days = step)
        while tmp < newdt:
            locs.append(tmp)
            vals.append('')
            tmp += datetime.timedelta(days = step)
        return newdt,locs,vals
    def addmonths(dt,locs,vals):
        d = dt
        targetyear = dt.year
        targetmonth = dt.month + months
        targetyear,targetmonth = getyearmonth(targetyear,targetmonth)
        newdt = datetime.datetime(targetyear,targetmonth,1)
        if step == 0:
            return newdt,locs,vals    
        ty = dt.year
        tm = dt.month + step
        ty,tm = getyearmonth(ty,tm)
        tmp = datetime.datetime(ty,tm,1)
        while tmp < newdt:
            locs.append(tmp)
            vals.append('')
            ty = tmp.year
            tm = tmp.month + step
            ty,tm = getyearmonth(ty,tm)
            tmp = datetime.datetime(ty,tm,1)
        return newdt,locs,vals
    if seconds != 0:
        return makedatetime_seconds
    if days != 0:
        return makedatetime_days
    if months != 0:
        return addmonths
    
    

def getfunc(step,log):
    if log == False:
        return defaultgetfunc(step)
    def applyfunc(val):
        if val <= 0:
            return '0'
        order = 1-int(math.log10(val))
        if val > 10 or val == int(val):
            return str(int(round(val,order)))
        return str(round(val,order))
    return applyfunc

def defaultgetfunc(step):
    if step >=5:
        return makeint
    if step >=1:
        return getround(1)
    string = str(step)
    string = string.replace('0.','')
    order = len(string)
    return getround(order)
    

def getvallocsvals(ymin,ymax,num,step,subticks,func,invlogfunc):
    locs = [num]
    vals = [func(invlogfunc(num))]
    while num < ymax:
        for i in range(0,subticks):
            locs.append(num+(i+1)*(step)/float(1+subticks))
            vals.append('')
        num = num + step
        locs.append(num)
        vals.append(func(invlogfunc(num)))
    if len(locs)==1:
        locs = [num - step,num,num+step]
        vals = [func(invlogfunc(num - step)),func(invlogfunc(num)),func(invlogfunc(num+step))]
    return locs,vals


def getlogfunc(log,base,translate):
    def returnx(x):
        return x
    if log == False:
        return returnx,returnx
    def logfunc(x):
        return math.log(x+translate)/float(math.log(base))
    def invlogfunc(y):
        return pow(base,y) - translate
    return logfunc,invlogfunc
                                 



def getdefaulttranslateto(vmin,vmax,log,logbase):
    if vmin > 0:
        return vmin
    if vmax - vmin > 1:
        return 1
    if vmin == vmax and vmin < 0:
        return -vmin
    if vmin == vmax and vmin == 0:
        return 1
    if vmax - vmin > 0:
        return pow(logbase,math.floor((math.log(vmax-vmin))/float(math.log(logbase))))
    print('What is this: ',vmin,vmax)
    raise Exception()


def gettranslate(vmin,vmax,log,logbase,rawtranslateto):
    if log == False:
        return 0
    defaulttranslateto = getdefaulttranslateto(vmin,vmax,log,logbase)
    if rawtranslateto == None or rawtranslateto <= 0:
        translateto = defaulttranslateto
    else:
        translateto = rawtranslateto
    return translateto - vmin
    
def createvalticks(vmin,vmax,subticks  = 0,log = False,logbase = 10,log0 = None):
    if vmin == None or vmax == None:
        return [0,1], ['0','1']
    translate = gettranslate(vmin,vmax,log,logbase,log0)
    logfunc,invlogfunc = getlogfunc(log,logbase,translate)
    diff = logfunc(vmax) - logfunc(vmin)
    diffval,diffmag = getdiffval(diff,logfunc(vmax))
    realstep = getrealstep(None,diffval,diffmag)
    func = getfunc(realstep,log)
    num = int(math.floor(logfunc(vmin)/realstep))*realstep
    locs,vals = getvallocsvals(logfunc(vmin),logfunc(vmax),num,realstep,subticks,func,invlogfunc)
    return locs,vals,logfunc   
   




def getdatestep(diffdays,diffseconds,minval,maxval,subticks):
    if diffdays == 0:
        return getdateseconds(diffseconds,minval,subticks)
    return getdatedays(diffdays,minval,maxval,subticks)


def makesecond(dt):
    return str(dt.second)

def makeminute(dt):
    return str(dt.minute)

def makehour(dt):
    return str(dt.hour)

def makefulldate(dt):
    return str(dt.day)+'/'+str(dt.month)+'/'+str(dt.year)

def makemonthyear(dt):
    return str(dt.month)+'/'+str(dt.year)

def makeyear(dt):
    return str(dt.year)


def getdateseconds(diffseconds,minval,subticks):
    if diffseconds < 60: #Minute
        seconds = 5
        valfunc = makesecond
        mysub = 1
    elif diffseconds < 2*60:
        seconds = 20
        valfunc = makesecond
        mysub = 5
    elif diffseconds < 5*60:
        seconds = 60
        valfunc = makeminute
        mysub = 15
    elif diffseconds < 10*60:
        seconds = 2*60
        valfunc = makeminute
        mysub = 30
    elif diffseconds < 60*60: #hour
        seconds = 5*60
        valfunc = makeminute
        mysub = 60
    elif diffseconds < 2*60*60:
        seconds = 20*60
        valfunc = makeminute
        mysub = 5*60
    elif diffseconds < 5*60*60:
        seconds = 60*60
        valfunc = makehour
        mysub = 15*60
    elif diffseconds < 10*60*60:
        seconds = 2*60*60
        valfunc = makehour
        mysub = 30*60
    else:
        seconds = 4*60*60
        valfunc = makehour
        mysub = 60*60
    stepfunc = makedatetime(seconds = seconds)
    if subticks == None:
        substepfunc = makedatetime(seconds = mysub)
    else:
        substepfunc = makedatetime(seconds = seconds/float(subticks))
    firstval = getfirstvalseconds(minval,seconds)
    return stepfunc,firstval,valfunc,substepfunc

def getfirstvalseconds(minval,seconds):
    offset = minval.seconds % seconds
    if offset == 0:
        return minval
    return minval + datetime.timedelta(seconds = seconds - offset)

def getfirstvaldays(minval,days,months):
    if months == 0: # days scale
        if minval.hour == 0:
            return datetime.datetime(minval.year,minval.month,minval.day)
        else:
            return datetime.datetime(minval.year,minval.month,minval.day+1)
    if months % 12 == 0: # years scale
        if minval.month ==1:
            return datetime.datetime(minval.year,1,1)
        else:
            return datetime.datetime(minval.year+1,1,1)
    # months scale
    offset = minval.month % months
    if minval.day <=10 and months ==1:
        return datetime.datetime(minval.year,minval.month,1)
    if minval.day <= 10 and offset == 1:
        return datetime.datetime(minval.year,minval.month,1)
    addmonths = months - offset -1
    targetyear = minval.year
    targetmonth = minval.month + addmonths
    while targetmonth > 12:
        targetmonth = targetmonth - 12
        targetyear += 1
    return datetime.datetime(targetyear,targetmonth,1)    
    
    


def getdatedays(diffdays,minval,maxval,subticks):
    if diffdays <= 5:
        days = 1
        months = 0  
        valfunc = makefulldate
        step = 0
    elif diffdays <= 10:
        days = 2
        months = 0    
        valfunc = makefulldate
        step = 1
    elif diffdays <= 31:
        days = 7
        months = 0
        valfunc = makefulldate
        step = 1
    elif diffdays < 93:
        days = 28
        months = 0
        valfunc = makefulldate
        step = 7
    elif diffdays < 183:
        days = 0
        months = 1
        valfunc = makemonthyear
        step = 0
    elif diffdays <365:
        days = 0
        months = 2
        valfunc = makemonthyear
        step = 1
    elif diffdays < 3*365+1:
        days = 0
        months = 6
        valfunc = makemonthyear
        step = 2 
    elif diffdays < 5*365+1:
        days = 0
        months = 12
        valfunc = makeyear
        step = 3
    else:
        years = diffdays/365.25
        diffval,diffmag = getdiffval(years,maxval)
        yearstep = max(1,int(math.floor(getrealstep(None,diffval,diffmag))))
        days = 0
        months = 12*yearstep
        valfunc = makeyear
        step = 0
        if subticks!=0:
            step = yearstep*12/subticks
    stepfunc = makedatetime(days = days, months = months,step = step)
    firstval = getfirstvaldays(minval,days,months)
    return stepfunc,firstval,valfunc



def timebetween(later,earlier):
    diff = later-earlier
    val = diff.seconds
    days = diff.days
    val += days * 24*60*60
    return float(val)

    
def enddateclose(maxdate,enddate,stepfunc):
    nextbit,meh,meh = stepfunc(enddate,[],[])
    gap = timebetween(enddate,maxdate)
    width = timebetween(nextbit,enddate)
    return gap/width < 0.25
        

    

def createdateticks(mindate,maxdate,step = None,subticks = 0):
    if mindate == None or maxdate == None:
        return [datetime.datetime(2012,l,1),datetime.datetime(2013,1,1)],['2012','2013']
    diffdays = (maxdate - mindate).days
    diffseconds = (maxdate - mindate).seconds
    stepfunc,firstval,valfunc = getdatestep(diffdays,diffseconds,mindate,maxdate,subticks) 
    locs = []
    vals = []
    if mindate < firstval:
        locs.append(mindate)
        vals.append('')
    locs.append(firstval)
    vals.append(valfunc(firstval))
    num,locs,vals = stepfunc(firstval,locs,vals) 
    locs.append(num)
    vals.append(valfunc(num))
    while num < maxdate:    
        num,locs,vals = stepfunc(num,locs,vals)
        locs.append(num)
        vals.append(valfunc(num))
    return locs,vals,donothings


def checkifmixed(objects):
    names = []
    for obj in objects:
        if obj.name in CATEGORYNAMES:
            names.append(True)
        else:
            names.append(False)
    if len(list(set(names))) < 2:
        return False
    return True

def adjustforcategories(objects,locs,vals,categories,mindiff):
    if categories == {}:
        return locs,vals
    mixed = checkifmixed(objects)
    newvals = []
    newlocs = []
    mini = min(categories.values()) - mindiff/2.0
    maxi = max(categories.values()) + mindiff/2.0
    newlocs.append(mini)
    newvals.append('')
    for key in categories.keys():
        newlocs.append(categories[key])
        newvals.append(str(key))
    newlocs.append(maxi)
    newvals.append('')
    if not mixed:
        return newlocs,newvals
    for i in range(0,len(locs)):
        loc = locs[i]
        val = vals[i]
        if loc in newlocs:
            i = newlocs.index(loc)
            newvals[i] = val
        else:
            newlocs.append(loc)
            newvals.append(val)
    return newlocs,newvals    


def addone(mini,tp):
    if tp == type(datetime.datetime(2000,1,1)):
        return mini + datetime.timedelta(1)
    if tp == type(datetime.date(2000,1,1)):
        val = datetime.datetime(mini.year,mini.month,mini.day)+datetime.timedelta(1)
        return val.date()
    return mini + 1
              

def identity(element):
    return element

    


def makeaxis_sub(ax,xory,objects,label,ticks,subticks,rotation,align,minmax,zero,fontsize,log,logbase,log0,categories = {},mindiff = 1):
    if minmax == None:
        mini,maxi,tp = getminmax(objects,xory)
    else:
        mini = minmax[0]
        maxi = minmax[1]
        tp = type(mini)
    if tp in DATETYPES:
        func = identity
    else:
        func = float
    if zero == True:
        mini = 0
    if mini == maxi:
        maxi = addone(mini,tp)    
    if ticks == None:
        locs,vals,logfunc = getlocs(mini,maxi,tp,subticks,log,logbase,log0)
        locs,vals = adjustforcategories(objects,locs,vals,categories,mindiff)
    else:
        locs = ticks[0]
        vals = ticks[1]
        logfunc = donothing
    if 'x' in xory:
        ax.set_xticks(locs)
        ax.set_xticklabels(vals,rotation = rotation,ha = align,fontsize = fontsize)
        if label !=None:
            ax.set_xlabel(label)
    if 'y' in xory:
        ax.set_yticks(locs)
        ax.set_yticklabels(vals,rotation = rotation,ha = align,fontsize = fontsize)
        if label !=None:
            ax.set_ylabel(label)
    if minmax != None:
        return func(mini),func(maxi),locs,vals,logfunc
    if len(locs) > 1:
        return func(min(locs)),func(max(locs)),locs,vals,logfunc
    return func(mini),func(maxi),locs,vals,logfunc

def updatehvlines(minmax,objects):
    for obj in objects:
        if obj.name == 'hline':
            obj.x = minmax[0]
        if obj.name == 'vline' and obj.secondaxis == False:
            obj.y = minmax[1]
        if obj.name == 'vline' and obj.secondaxis == True:
            obj.y = minmax[2]
    return objects


def rectx(pair):
    xs = []
    for i in [0,0,1,1,0]:
        xs.append(pair[i])
    return xs

def recty(pair):
    ys = []
    for i in [0,1,1,0,0]:
        ys.append(pair[i])
    return ys

def updatehvareas(minmax,objects):
    for obj in objects:
        if obj.name == 'harea':
            obj.x = rectx(minmax[0])
        if obj.name == 'varea' and obj.secondaxis == False:
            obj.y = recty(minmax[1])
        if obj.name == 'varea' and obj.secondaxis == True:
            obj.y = recty(minmax[2])
    return objects


def donothing(x):
    return x

def makegridlines_sub(gridlinestyle,key,default):
    if key not in gridlinestyle:
        return default
    return gridlinestyle[key]


def makegridlines(ax,gridlines,xgridlines,ygridlines,ticks,minmax,gridlinestyle):
    if gridlines == False and xgridlines == False and ygridlines == False:
        return
    xlocs,xvals = ticks[0]
    subticks = makegridlines_sub(gridlinestyle,'subticks',False)
    color = makegridlines_sub(gridlinestyle,'color',BLACK)
    style = makegridlines_sub(gridlinestyle,'style','--')
    alpha = makegridlines_sub(gridlinestyle,'alpha',0.3)
    if gridlines == True or xgridlines == True:
        for i in range(0,len(xlocs)):
            if xvals[i]!='' or subticks == True:
                ax.plot([xlocs[i],xlocs[i]],minmax[1],style,color=color,label = None,alpha=alpha)
    if gridlines == True or ygridlines == True:
        ylocs,yvals = ticks[1]
        for i in range(0,len(ylocs)):
            if yvals[i]!='' or subticks == True:
                ax.plot(minmax[0],[ylocs[i],ylocs[i]],style,color=color,label = None,alpha=alpha)
    




def handlechartboxplotoverlap(objects,chartstacked,stacked):
    cats = getcategories(objects)
    stackcharts = getstack(objects,'chart',chartstacked,stacked)
    stackhcharts = getstack(objects,'hchart',chartstacked,stacked)
    boxplotindexes = getoffsetindexes(objects,'boxplot')
    numbps = len(boxplotindexes)
    chartindexes = getoffsetindexes(objects,'chart')
    hchartindexes = getoffsetindexes(objects,'hchart')
    numcharts = len(chartindexes)
    numhcharts = len(hchartindexes)
    if numcharts > 0 and stackcharts:
        numcharts = 1
        chartindexes = [min(chartindexes)]
    if numhcharts > 0 and stackcharts:
        numhcharts = 1
        hchartindexes = [min(hchartindexes)]
    num={}
    num['x'] = max((1,numbps+numcharts))
    num['y'] = max(1,numhcharts)
    mindiff,width = getwidth(cats,num)
    offsets = {}
    offsets['x'] = getoffset(mindiff['x'],width['x'],boxplotindexes+chartindexes,num['x'])
    offsets['y'] = getoffset(mindiff['y'],width['y'],hchartindexes,num['y'])
    return objects,cats,stackcharts,stackhcharts,width,mindiff,offsets

    
def getoffsetindexes(objects,name):
    offsets = []
    for i in range(0,len(objects)):
        if objects[i].name == name:
            offsets.append(i)
    return offsets

def getoffset(mindiff,width,offsetindex,num):
    if offsetindex == []:
        return {} 
    if num == 1:
        return {offsetindex[0]:-(1-CATGAP)*mindiff/2.0}
    innergap = INNERCATGAP/(num-1)
    offsets = {}
    for i in range(0,num):
        index = offsetindex[i]
        offsets[index] = (i)*(innergap+width) - (1-CATGAP)*mindiff/2.0
    return offsets


    
def makepiename(objects,rawfname,i):
    if len(objects) == 1:
        return rawfname
    num = 0
    for j in range(0,len(objects)):
        obj = objects[j]
        if obj.name != 'pie':
            continue
        num += 1
        if j == i:
            break
    return rawfname + '_PIE_'+str(num)



def addpiecolor(colorlist,obj):
    doalphas = False
    if obj.alphas == None:
        doalphas = True
    if obj.colors == True:
        ci = 0
        ai = 1
        obj.colors = []
        if doalphas:
            obj.alphas = []
        for i in range(0,obj.lenny):
            obj.colors.append(colorlist[ci])
            if doalphas:
                obj.alphas.append(ai)
            ci,ai = updateis(ci,ai,colorlist)
    elif obj.colors in [False,None]:
        obj.colors = []
        if doalphas:
            obj.alphas = []
        for i in range(0,obj.lenny):
            obj.colors.append(WHITE)
            if doalphas:
                obj.alphas.append(1)
    
            
    


def makepiecharts(objects,rawfname,write,fontsize,rawfigsize,frame,ext,lloc,lpos,ncols,resolution,colorlist,title,legendorder,legenddirection):
    newobjects = []
    ave = (rawfigsize[0]+rawfigsize[1])/2.0
    figsize = (ave,ave)
    for i in range(0,len(objects)):
        obj = objects[i]
        if obj.name != 'pie':
            newobjects.append(obj)
            continue
        fname = makepiename(objects,rawfname,i)
        addpiecolor(colorlist,obj)
        fig,ax1,ax2 = initplot([obj],fontsize,figsize,frame)
        maketitle(title)
        legend = makepie(obj,ax1)
        saveplot(objects,fig,ax1,ax2,fname,ext,lloc,lpos,ncols,legendorder,legenddirection,resolution,legend = legend)
    return newobjects

def getval(string):
    if '/' in string:
        return createdate.convertdatetime(string)
    if string.count('-') > 1:
        return createdate.convertdatetime(string)
    return float(string)

def readdata(pathtofile,header = True):
    f = open(pathtofile,'r')
    hline = f.readline()
    hbits = hline.strip().split(',')
    lenny = len(hbits)
    data = {}
    if header:
        hnames = hbits
    else:
        hnames = range(0,lenny)
    for name in hnames:
        data[name] = []
    if not header:
        for i in range(0,lenny):
            data[i].append(getval(hbits[i]))
    for line in f:
        bits = line.strip().split(',')
        for i in range(0,lenny):
            data[hnames[i]].append(getval(bits[i])) 
    return data
    
        

def hideaxes(ax1,ax2,xaxisdisplay,yaxisdisplay,second_yaxisdisplay):
    ax1.get_yaxis().set_visible(yaxisdisplay)
    if second_yaxisdisplay == False and ax2!=None:
        ax2.get_yaxis().set_visible(False)
    if yaxisdisplay == False:
        ax1.get_xaxis().set_visible(False)
        if ax2!=None:
            ax2.get_xaxis().set_visible(False)
    

def fixscale(objects,trans):
    for obj in objects:
        fixscale_sub(obj,trans)
    return objects

        
def fixscale_sub(obj,trans):
    if obj.name in ['pie']:
        return
    obj.xtrans = trans['x']
    if obj.secondaxis == True:
        obj.ytrans = trans['sy']
    else:
        obj.ytrans = trans['y']

def display(rawobjects,fname,write = False,fontsize = FONTSIZE,figsize = (8,6),frame = True,ext = 'png',lloc = (0.5,-0.1),lpos = 'upper center',
            ncols = 3,gridlines=False,xgridlines = False,ygridlines = False,gridlinestyle = {'style' :'--','color': BLACK,'subticks' : False,'alpha' : 0.3},resolution = 300,colorlist = COLORLIST,title = None,
            xlabel = None,xticks = None,xsubticks = 0,xrotation = 0,xalign = 'center',xminmax = None,xzero = False,xfontsize = FONTSIZE,xaxisdisplay = True,
            ylabel = None,yticks = None,ysubticks = 0,yrotation = 0,yalign = 'right',yminmax = None,yzero = False, yfontsize = FONTSIZE,yaxisdisplay = True,
            second_ylabel = SECOND_YLABEL,second_yticks = SECOND_YTICKS,second_ysubticks = SECOND_YSUBTICKS,second_yrotation = SECOND_YROTATION,
            second_yalign = SECOND_YALIGN,second_yminmax = SECOND_YMINMAX,second_yzero = SECOND_YZERO,second_yfontsize = SECOND_YFONTSIZE,second_yaxisdisplay = True,
            axisfontsize = None,areastacked = True,chartstacked = False,stacked = None,legendorder = 'normal',legenddirection = 'horizontal',lowmemory=False,
            xlog=False,xlogbase=10,xlog0 = None,ylog=False,ylogbase=10,ylog0 = None,second_ylog=False,second_ybase=10,second_ylog0 = None):

    ### will eventually need the chart, boxplot and piecharts...
    '''
    ext is one of: 'png' 'eps' 'pdf' 'pdf2ps'
    legendorder is either: 'reverse' 'normal' 'alphabetic' (reverse, reverses the order, normal does nothing, alphabetic orders alphabetically)
    or : legendorder is a list e.g. ['leg 1','leg 2'...] of the desired order
    legenddirection = 'horizontal' or 'vertical'
    '''
    if lowmemory == True:
        objects = rawobjects
    else:
        objects = copy.deepcopy(rawobjects)
    objects = makepiecharts(objects,fname,write,fontsize,figsize,frame,ext,lloc,lpos,ncols,resolution,colorlist,title,legendorder,legenddirection)
    if objects == []:
        return
    writeout(objects,fname,write)        
    objects = fixcolor(objects,colorlist)    
    objects = fixhistogramfit(objects)
    objects = fixareas(objects,areastacked,stacked)
    objects,cats,stackcharts,stackhcharts,width,mindiff,offsets = handlechartboxplotoverlap(objects,chartstacked,stacked)
    objects = fixcharts(objects,cats['x'],width['x'],mindiff['x'],offsets['x'],stackcharts)
    objects = fixhcharts(objects,cats['y'],width['y'],mindiff['y'],offsets['y'],stackhcharts)
    objects = fixboxplots(objects,cats['x'],width['x'],mindiff['x'],offsets['x'])
    objects,ylabel,second_ylabel = getbins(objects,ylabel,second_ylabel,xminmax)
    second = getsecond(objects,second_ylabel,second_yticks,second_ysubticks,second_yrotation,second_yalign,second_yminmax,second_yzero,second_yfontsize)
    fig,ax1,ax2 = initplot(objects,fontsize,figsize,frame,second)
    minmax,ticks,trans = makeaxis(ax1,ax2,objects,cats,mindiff,xlabel,xticks,xsubticks,xrotation,xalign,xminmax,xzero,xfontsize,ylabel,yticks,ysubticks,yrotation,yalign,yminmax,yzero,yfontsize,second_ylabel,second_yticks,second_ysubticks,second_yrotation,second_yalign,second_yminmax,second_yzero,second_yfontsize,axisfontsize,xlog,xlogbase,xlog0,ylog,ylogbase,ylog0,second_ylog,second_ybase,second_ylog0)
    objects = updatehvlines(minmax,objects)
    objects = updatehvareas(minmax,objects)
    makegridlines(ax1,gridlines,xgridlines,ygridlines,ticks,minmax,gridlinestyle)
    objects = fixscale(objects,trans)
    for obj in objects:
        if obj.secondaxis:
            obj.func(obj,ax2)
        else:
            obj.func(obj,ax1)
    maketitle(title)
    hideaxes(ax1,ax2,xaxisdisplay,yaxisdisplay,second_yaxisdisplay)
    saveplot(objects,fig,ax1,ax2,fname,ext,lloc,lpos,ncols,legendorder,legenddirection,minmax,resolution)
    

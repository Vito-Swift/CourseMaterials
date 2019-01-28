'''
This is a simplistic list of various colors that I have found useful. 
There is also a couple of simple functions to convert color formats etc.
In addition there are a bunch of heatmaps that can be used. (for styling purposes)

these colors only work for the plot library.
To make them work in google earth, need to add in the alpha.
To do this call hextocolor(hexidecimal,alpha=1)
e.g. hextocolor(BLUE,0.5) makes a blue color with 50% transparency.
'''

ONETHIRD = 1.0/3.0
TWOTHIRD = 2.0/3.0
HALF = 1/2.0


### Colors: alphabetically arranged:
ALICE_BLUE = '#F0F8FF'
AMBER = '#FFBF00'
ANTIQUE_RUBY = '#841B2D'
AQUA = '#00FFFF'
AQUARMARINE = '#7FFFD4'
BLACK = '#000000'
BLUE = '#1C38FF'
BLUE_PURPLE = '#A7A7FF'
BROWN = '#A62A2A'
BURLYWOOD = '#DEB887'
CADET_BLUE = '#5F9EA0'
CHOCOLATE = '#7B3F00'
CYAN = '#66D5F7'
DARK_BLUE = '#000094'
DARK_CYAN = '#008B8B'
DARK_BROWN = '#654321'
DARK_GREY = '#696969'
DARK_KHAKI = '#BDB76B'
DARK_OLIVE_GREEN = '#556B2F'
DARK_ORANGE = '#F47A00'
DARK_PURPLE = '#330066'
DARK_RED = '#840000'
DARK_SEA_GREEN = '#8FBC8F'
DARK_SLATE_BLUE = '#483D8B'
DARK_VIOLET = '#9400D3'
DEEP_PINK = '#FF1493'   
DODGER_BLUE = '#1E90FF'
EGYPTIAN_BLUE = '#1034A6'
EXCEL_BLUE = '#1D73AA'
EXCEL_GREEN = '#8CBC4F'
EXCEL_LIGHT_GREEN = '#C4D69C'
EXCEL_RED = '#C44441'
FOREST_GREEN = '#228B22'
GREEN = '#0BC905'
GREEN_YELLOW = '#ADFF2F'
GREY = '#808080'
GREY_BLUE = '#B9CDE5'
HOT_PINK = '#FF69B4'
INDIAN_RED = '#CD5C5C'
LAWN_GREEN = '#7CFC00'  
LIGHT_BLUE = '#66C0F7'
LIGHT_BROWN = '#FF7D00'
LIGHT_GREEN = '#90EE90'  
LIGHT_GREY = '#D3D3D3'
LIGHT_PURPLE = '#E5CCFF'
LIGHTER_GREY = '#C8C8C8'
LILAC = '#B666D2'
MEDIUM_GREY = '#949391'
MEDIUM_SEA_GREEN = '#3CB371' 
MIDNIGHT_BLUE = '#003366' 
MILD_GREY = '#C4C4C4'
MILD_PINK = '#F3C3E2'
MUTED_GREEN = '#BBD18F'
ORANGE = '#FACE21'
PALE_GREEN = '#8FBC8F'    
PALE_VIOLET_RED = '#DB7093'
PINK = '#FFCBDB'
PURPLE = '#7F00FF'
RED = '#FF0000'
RED_RUBY = '#9B111E'
ROSY_BROWN = '#BC8F8F'
ROYAL_BLUE = '#4169E1'
SEA_GREEN = '#238E68' 
SIENNA = '#A0522D'
SPEERMINT = '#B6F0D6'
TAN = '#D2B48C'
TOMATO = '#FF6347'
VERY_LIGHT_GREY = '#E6E6E6'
VIOLENT_RED = '#F43E71'
VIOLET = '#C653FF'
WASABI = '#78933C'
WHITE = '#FFFFFF'
YELLOW = '#FFFF00'




COLORLIST = [BLUE,
             RED,
             FOREST_GREEN,
             ORANGE,
             CADET_BLUE,
             DARK_RED,
             LAWN_GREEN,
             BROWN,
             DARK_SLATE_BLUE,
             DEEP_PINK,
             DARK_OLIVE_GREEN,
             TAN,
             MIDNIGHT_BLUE,
             VIOLENT_RED,
             MEDIUM_SEA_GREEN,
             BURLYWOOD,
             ALICE_BLUE,
             TOMATO,
             SEA_GREEN,
             SIENNA,
             DODGER_BLUE,
             PALE_VIOLET_RED,
             GREEN_YELLOW,
             DARK_ORANGE,
             AQUARMARINE,
             INDIAN_RED,
             PALE_GREEN,
             ROSY_BROWN,
             DARK_CYAN,
             HOT_PINK,
             DARK_SEA_GREEN,
             CHOCOLATE,
             AQUA,
             DARK_VIOLET,
             LIGHT_GREEN,
             DARK_KHAKI,
             AMBER,
             ANTIQUE_RUBY,
             EGYPTIAN_BLUE,
             BLACK,
             BLUE_PURPLE,
             CYAN,
             DARK_BLUE,
             DARK_BROWN,
             DARK_GREY,
             DARK_PURPLE,
             EXCEL_BLUE,
             EXCEL_GREEN,
             EXCEL_LIGHT_GREEN,
             EXCEL_RED,
             GREEN,
             GREY,
             GREY_BLUE,
             LIGHT_BLUE,
             LIGHT_BROWN,
             LIGHT_GREY,
             LIGHT_PURPLE,
             LIGHTER_GREY,
             LILAC,
             MEDIUM_GREY,
             MILD_GREY,
             MILD_PINK,
             MUTED_GREEN,
             PINK,
             PURPLE,
             RED_RUBY,
             ROYAL_BLUE,
             SPEERMINT,
             VERY_LIGHT_GREY,
             WASABI,
             WHITE,
             YELLOW]
                                

EXCELCOLORLIST = [EXCEL_BLUE,
                  EXCEL_RED,
                  EXCEL_GREEN,
                  MUTED_GREEN,
                  MILD_GREY,
                  GREY_BLUE,
                  BLUE_PURPLE,
                  MILD_PINK,
                  SPEERMINT]

BLUECOLORS = [BLUE,
             CADET_BLUE,
             DARK_SLATE_BLUE,
             MIDNIGHT_BLUE,
             ALICE_BLUE,
             DODGER_BLUE,
             AQUARMARINE,
             DARK_CYAN,
             AQUA,
             DARK_KHAKI,
             EGYPTIAN_BLUE]


REDCOLORS = [RED,
             DARK_RED,
             DEEP_PINK,
             VIOLENT_RED,
             TOMATO,
             PALE_VIOLET_RED,
             INDIAN_RED,
             HOT_PINK,
             DARK_VIOLET,
             ANTIQUE_RUBY]


GREENCOLORS = [FOREST_GREEN,
             LAWN_GREEN,
             DARK_OLIVE_GREEN,
             MEDIUM_SEA_GREEN,
             SEA_GREEN,
             GREEN_YELLOW,
             PALE_GREEN,
             DARK_SEA_GREEN,
             LIGHT_GREEN]


ORANGECOLORS = [ORANGE,
             BROWN,
             TAN,
             BURLYWOOD,
             SIENNA,
             DARK_ORANGE,
             ROSY_BROWN,
             CHOCOLATE,
             DARK_KHAKI,
             AMBER]


SPECIFICCOLORS = [BLUECOLORS,REDCOLORS,GREENCOLORS,ORANGECOLORS]


HEXI = {0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'}




def converttohex(r,g,b):
    '''
    for plotter
    '''
    Rq,Rr = divmod(r,16)
    Gq,Gr = divmod(g,16)
    Bq,Br = divmod(b,16)
    return '#'+HEXI[Rq]+HEXI[Rr]+HEXI[Gq]+HEXI[Gr]+HEXI[Bq]+HEXI[Br]


def rgbtocolor(r,g,b,alpha = 1):
    '''
    for makekml
    '''
    Rq,Rr = divmod(r,16)
    Gq,Gr = divmod(g,16)
    Bq,Br = divmod(b,16)
    a = int(round(alpha*255,0))
    aq,ar = divmod(a,16)
    return '#' +HEXI[aq]+HEXI[ar]+HEXI[Bq]+HEXI[Br]+HEXI[Gq]+HEXI[Gr]+HEXI[Rq]+HEXI[Rr]


def hextocolor(hexidecimal,alpha=1):
    string = hexidecimal
    if '#' not in string:
        string = '#'+string
    Rq = string[1]
    Rr = string[2]
    Gq = string[3]
    Gr = string[4]
    Bq = string[5]
    Br = string[6]
    a = int(round(alpha*255,0))
    aq,ar = divmod(a,16)
    return '#' +HEXI[aq]+HEXI[ar]+Bq+Br+Gq+Gr+Rq+Rr



def hextorgb(hexidecimal):
    string = hexidecimal
    if '#' not in string:
        string = '#'+string
    r = int(string[1:3],16)
    g = int(string[3:5],16)
    b = int(string[5:7],16)
    return (r,g,b)
       



def blueredheatmap(val,rgbonly = False):
    if val >= 0 and val <= ONETHIRD:
        r = 0
        g = int((255/ONETHIRD)*val)
        b = 255        
    elif val > ONETHIRD and val <= TWOTHIRD:
        r = int((255/ONETHIRD)*(val - ONETHIRD))
        g = 255
        b = int((-255/ONETHIRD)*(val - TWOTHIRD))
    elif val > TWOTHIRD and val <= 1:
        r = 255
        g = int((-255/ONETHIRD)*(val-1))
        b = 0
    else:
        raise Exception(val)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)

def redgreenheatmap(val,rgbonly = False):
    b = 0
    if val >=0 and val <= HALF:
        r = 255
        g = int(255*val*2)
    elif val > HALF and val <=1:
        r = int(255 - (255*2*(val-HALF)))
        g = 255
    else:
        raise Exception()
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)

def darkredgreenheatmap(val,splitpoint = ONETHIRD,rgbonly = False):
    if val > splitpoint:
        newval = (val - splitpoint)/float(1-splitpoint)
        return redgreenheatmap(newval,alpha = alpha,rgbonly = rgbonly)
    red = (255,0,0)
    darkred = (51,0,0)
    newval = (val)/float(splitpoint)
    r,g,b = heatmaprange(newval,darkred,red)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)


def grayscaleheatmap(val,rgbonly = False):
    white = (255,255,255)
    black = (0,0,0)
    r,g,b = heatmaprange(val,white,black)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)

def lightgrayscaleheatmap(val,rgbonly = False):
    black = (75,75,75)
    white = (255,255,255)
    r,g,b = heatmaprange(val,white,black)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)


def brownheatmap(val, rgbonly = False):
    dark = (51,25,0)
    light = (255,125,0)
    r,g,b = heatmaprange(val,dark,light)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)


def purpleheatmap(val, rgbonly = False):
    lightpurple = (229,204,255)
    mediumpurple = (127,0,255)
    darkpurple = (51,0,102)
    if val <0.5:
        r,g,b = heatmaprange(val*2,darkpurple,mediumpurple)
    elif val == 0.5:
        r,g,b = mediumpurple
    elif val > 0.5:
        r,g,b = heatmaprange(val*2-1,mediumpurple,lightpurple)
    else:
        raise Exception()
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)


def greenheatmap(val, rgbonly = False):
    lightgreen = (226,250,226)
    mediumgreen = (40,215,40)
    darkgreen = (5,29,5)
    if val <0.5:
        r,g,b = heatmaprange(val*2,darkgreen,mediumgreen)
    elif val == 0.5:
        r,g,b = mediumgreen
    elif val > 0.5:
        r,g,b = heatmaprange(val*2-1,mediumgreen,lightgreen)
    else:
        raise Exception()
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)


def redheatmap(val,rgbonly = False):
    lightred = (250,226,226)
    mediumred = (215,40,40)
    darkred = (29,5,5)
    if val <0.5:
        r,g,b = heatmaprange(val*2,darkred,mediumred)
    elif val == 0.5:
        r,g,b = mediumred
    elif val > 0.5:
        r,g,b = heatmaprange(val*2-1,mediumred,lightred)
    else:
        raise Exception()
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)

def blueheatmap(val,rgbonly = False):
    lightblue = (226,226,250)
    mediumblue = (40,40,215)
    darkblue = (5,5,29)
    if val <0.5:
        r,g,b = heatmaprange(val*2,darkblue,mediumblue)
    elif val == 0.5:
        r,g,b = mediumblue
    elif val > 0.5:
        r,g,b = heatmaprange(val*2-1,mediumblue,lightblue)
    else:
        raise Exception()
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)






def yellowredheatmap(val,rgbonly = False):
    lightyellow = (255,255,145)
    red = (255,50,20)
    r,g,b = heatmaprange(val,lightyellow,red)
    if rgbonly:
        return r,g,b
    return converttohex(r,g,b)




def heatmaprange(val,low,high):
    vals = []
    for i in range(0,3):
        vals.append(int(low[i] + val*(high[i] - low[i])))
    return tuple(vals)



def fraction(val,mini,maxi):
    if mini == maxi:
        return None
    val = (1.0/(maxi-mini))*(val-mini)
    if val < 0:
        print('warning value too low')
        return 0
    if val > 1:
        print('warning value too high')
        return 1
    return val




    

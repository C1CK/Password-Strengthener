import Dependencies.pyperclip as pyperclip

elements={"h":"hydrogen",
	"he":"helium",
	"li":"lithium",
	"be":"beryllium",
	"b":"boron",
	"c":"carbon",
	"n":"nitrogen",
	"o":"oxygen",
	"f":"fluorine",
	"ne":"neon",
	"na":"sodium",
	"mg":"magnesium",
	"al":"aluminum",
	"si":"silicon",
	"p":"phosphorus",
	"s":"sulfur",
	"cl":"chlorine",
	"ar":"argon",
	"k":"potassium",
	"ca":"calcium",
	"sc":"scandium",
	"ti":"titanium",
	"v":"vanadium",
	"cr":"chromium",
	"mn":"manganese",
	"fe":"iron",
	"co":"cobalt",
	"ni":"nickel",
	"cu":"copper",
	"zn":"zinc",
	"ga":"gallium",
	"ge":"germanium",
	"as":"arsenic",
	"se":"selenium",
	"br":"bromine",
	"kr":"krypton",
	"rb":"rubidium",
	"sr":"strontium",
	"y":"yttrium",
	"zr":"zirconium",
	"nb":"niobium",
	"mo":"molybdenum",
	"tc":"technetium",
	"ru":"ruthenium",
	"rh":"rhodium",
	"pd":"palladium",
	"ag":"silver",
	"cd":"cadmium",
	"in":"indium",
	"sn":"tin",
	"sb":"antimony",
	"te":"tellurium",
	"i":"iodine",
	"xe":"xenon",
	"cs":"cesium",
	"ba":"barium",
	"la":"lanthanum",
	"ce":"cerium",
	"pr":"praseodymium",
	"nd":"neodymium",
	"pm":"promethium",
	"sm":"samarium",
	"eu":"europium",
	"gd":"gadolinium",
	"tb":"terbium",
	"dy":"dysprosium",
	"ho":"holmium",
	"er":"erbium",
	"tm":"thulium",
	"yb":"ytterbium",
	"lu":"lutetium",
	"hf":"hafnium",
	"ta":"tantalum",
	"w":"tungsten",
	"re":"rhenium",
	"os":"osmium",
	"ir":"iridium",
	"pt":"platinum",
	"au":"gold",
	"hg":"mercury",
	"tl":"thallium",
	"pb":"lead",
	"bi":"bismuth",
	"po":"polonium",
	"at":"astatine",
	"rn":"radon",
	"fr":"francium",
	"ra":"radium",
	"ac":"actinium",
	"th":"thorium",
	"pa":"protactinium",
	"u":"uranium",
	"np":"neptunium",
	"pu":"plutonium",
	"am":"americium",
	"cm":"curium",
	"bk":"berkelium",
	"cf":"californium",
	"es":"einsteinium",
	"fm":"fermium",
	"md":"mendelevium",
	"no":"nobelium",
	"lr":"lawrencium",
	"rf":"rutherfordium",
	"db":"dubnium",
	"sg":"seaborgium",
	"bh":"bohrium",
	"hs":"hassium",
	"mt":"meitnerium",
	"ds":"darmstadtium",
	"rg":"roentgenium",
	"cn":"copernicium",
	"fl":"flerovium",}

def char_rep(start):
    end = ""
    count = 0
    incomplete = True
    lchar = False
    while incomplete == True:
        print(count)
        cchar = start[count]
        if lchar != True:
            nchar = start[count+1]
        if cchar+nchar in elements:
            end += elements[cchar+nchar]
            count += 2
        elif cchar in elements:
            end += elements[cchar]
            count+=1
        else:
            end += cchar
            count += 1
        if count == len(start)-1:
            lchar = True
        elif count >= len(start):
            incomplete = False
    return(end)
            
while True:
    inp = input("Enter Password To Lengthen: ")
    if inp == "":
        print(pyperclip.paste())
        inp = pyperclip.paste()
    output = (char_rep(inp))
    print(output)
    pyperclip.copy(output)
    













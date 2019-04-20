invalid_edi = """ISA*00*          *00*          *ZZ*Mycorp         *ZZ*ACMECOR00216271*190418*1657*^*00501*191300001*0*P*:~
GS*BE*Mycorp*ACMECOR00216271*20190418*1657*191300001*X*005010X220A1~
ST*834*191300001*005010X220A1~
BGN*00*Mycorp*20190418*1657****RX~
REF*38*1234~
DTP*382*D8*20190131~
QTY*DT*1~
QTY*ET*1~
QTY*TO*2~
N1*P5*Mycorp*FI*12-3456789~
N1*IN*Acmecor*FI*13-5581829~
INS*Y*18*001*XN*A***FT*N~
INS*Y*18*001*XN*A***FT*N~
REF*0F*213548281~
DTP*336*D8*20181201~
NM1*IL*1*Doe*John****34*213548281~
PER*IP**HP*243754848~
N3*123 Sesame Street~
N4*Cullman*AL*35212~
DMG*D8*19910101*M*M~
ICM*2*1234*20181201~
HD*001**VIS**ESP~
DTP*348*D8*20190501~
REF*1L*021627100010006~
HD*001**DEN**ESP~
DTP*348*D8*20190301~
REF*1L*021627100010004~
HD*001**STD**IND~
DTP*348*D8*20190501~
REF*1L*021627100010009~
HD*001**LTD**IND~
DTP*348*D8*20190401~
REF*1L*021627100010008~
INS*N*01*001*XN*A***FT*N~
REF*0F*213548281~
DTP*336*D8*20181201~
NM1*IL*1*Doe*Jane****34*382743626~
PER*IP**HP*2053338181~
N3*123 Sesame Street~
N4*Cullman*AL*35212~
DMG*D8*19931221*F*M~
HD*001**DEN**ESP~
DTP*348*D8*20190301~
REF*1L*021627100010004~
HD*001**VIS**ESP~
DTP*348*D8*20190501~
REF*1L*021627100010006~
SE*45*191300001~
GE*1*191300001~
IEA*1*191300001~
"""

generator_input_valid_edi = [
    ("ISA", ["00", "          ", "00", "          ", "ZZ", "Mycorp         ", "ZZ", "ACMECOR00216271", "190418", "1657", "^", "00501", "191300001", "0", "P", ":"]),
    ("GS", ["BE", "Mycorp", "ACMECOR00216271", "20190418", "1657", "191300001", "X", "005010X220A1"]),
    ("ST", ["834", "191300001", "005010X220A1"]),
    ("BGN", ["00", "Mycorp", "20190418", "1657", "", "", "", "RX"]),
    ("REF", ["38", "1234"]),
    ("DTP", ["382", "D8", "20190131"]),
    ("QTY", ["DT", "1"]),
    ("QTY", ["ET", "1"]),
    ("QTY", ["TO", "2"]),
    ("N1", ["P5", "Mycorp", "FI", "12-3456789"]),
    ("N1", ["IN", "Acmecor", "FI", "13-5581829"]),
    ("INS", ["Y", "18", "001", "XN", "A", "", "", "FT", "N"]),
    ("REF", ["0F", "213548281"]),
    ("DTP", ["336", "D8", "20181201"]),
    ("NM1", ["IL", "1", "Doe", "John", "", "", "", "34", "213548281"]),
    ("PER", ["IP", "", "HP", "243754848"]),
    ("N3", ["123 Sesame Street"]),
    ("N4", ["Cullman", "AL", "35212"]),
    ("DMG", ["D8", "19910101", "M", "M"]),
    ("ICM", ["2", "1234", "20181201"]),
    ("HD", ["001", "", "VIS", "", "ESP"]),
    ("DTP", ["348", "D8", "20190501"]),
    ("REF", ["1L", "021627100010006"]),
    ("HD", ["001", "", "DEN", "", "ESP"]),
    ("DTP", ["348", "D8", "20190301"]),
    ("REF", ["1L", "021627100010004"]),
    ("HD", ["001", "", "STD", "", "IND"]),
    ("DTP", ["348", "D8", "20190501"]),
    ("REF", ["1L", "021627100010009"]),
    ("HD", ["001", "", "LTD", "", "IND"]),
    ("DTP", ["348", "D8", "20190401"]),
    ("REF", ["1L", "021627100010008"]),
    ("INS", ["N", "01", "001", "XN", "A", "", "", "FT", "N"]),
    ("REF", ["0F", "213548281"]),
    ("DTP", ["336", "D8", "20181201"]),
    ("NM1", ["IL", "1", "Doe", "Jane", "", "", "", "34", "382743626"]),
    ("PER", ["IP", "", "HP", "2053338181"]),
    ("N3", ["123 Sesame Street"]),
    ("N4", ["Cullman", "AL", "35212"]),
    ("DMG", ["D8", "19931221", "F", "M"]),
    ("HD", ["001", "", "DEN", "", "ESP"]),
    ("DTP", ["348", "D8", "20190301"]),
    ("REF", ["1L", "021627100010004"]),
    ("HD", ["001", "", "VIS", "", "ESP"]),
    ("DTP", ["348", "D8", "20190501"]),
    ("REF", ["1L", "021627100010006"]),
    ("SE", ["45", "191300001"]),
    ("GE", ["1", "191300001"]),
    ("IEA", ["1", "191300001"])
]

valid_edi = """ISA*00*          *00*          *ZZ*Mycorp         *ZZ*ACMECOR00216271*190418*1657*^*00501*191300001*0*P*:~
GS*BE*Mycorp*ACMECOR00216271*20190418*1657*191300001*X*005010X220A1~
ST*834*191300001*005010X220A1~
BGN*00*Mycorp*20190418*1657****RX~
REF*38*1234~
DTP*382*D8*20190131~
QTY*DT*1~
QTY*ET*1~
QTY*TO*2~
N1*P5*Mycorp*FI*12-3456789~
N1*IN*Acmecor*FI*13-5581829~
INS*Y*18*001*XN*A***FT*N~
REF*0F*213548281~
DTP*336*D8*20181201~
NM1*IL*1*Doe*John****34*213548281~
PER*IP**HP*243754848~
N3*123 Sesame Street~
N4*Cullman*AL*35212~
DMG*D8*19910101*M*M~
ICM*2*1234*20181201~
HD*001**VIS**ESP~
DTP*348*D8*20190501~
REF*1L*021627100010006~
HD*001**DEN**ESP~
DTP*348*D8*20190301~
REF*1L*021627100010004~
HD*001**STD**IND~
DTP*348*D8*20190501~
REF*1L*021627100010009~
HD*001**LTD**IND~
DTP*348*D8*20190401~
REF*1L*021627100010008~
INS*N*01*001*XN*A***FT*N~
REF*0F*213548281~
DTP*336*D8*20181201~
NM1*IL*1*Doe*Jane****34*382743626~
PER*IP**HP*2053338181~
N3*123 Sesame Street~
N4*Cullman*AL*35212~
DMG*D8*19931221*F*M~
HD*001**DEN**ESP~
DTP*348*D8*20190301~
REF*1L*021627100010004~
HD*001**VIS**ESP~
DTP*348*D8*20190501~
REF*1L*021627100010006~
SE*45*191300001~
GE*1*191300001~
IEA*1*191300001~
"""

generator_input_basic = [
    ("ISA", ["00", "          ", "00", "          ", "ZZ"]),
    ("GS", ["BE", "          ", "00", "          ", "ZZ"]),
    ("ST", ["00", "          ", "00", "          ", "ZZ"]),
    ("SE", ["00", "          ", "00", "          ", "ZZ"]),
    ("GE", ["00", "          ", "00", "          ", "ZZ"]),
    ("IEA", ["00", "          ", "00", "          ", "ZZ"]),
]

generator_output_basic = """ISA*00*          *00*          *ZZ~
GS*BE*          *00*          *ZZ~
ST*00*          *00*          *ZZ~
SE*00*          *00*          *ZZ~
GE*00*          *00*          *ZZ~
IEA*00*          *00*          *ZZ~
"""

generator_output_basic_custom_separators = """ISA@00@          @00@          @ZZ#
GS@BE@          @00@          @ZZ#
ST@00@          @00@          @ZZ#
SE@00@          @00@          @ZZ#
GE@00@          @00@          @ZZ#
IEA@00@          @00@          @ZZ#
"""

generator_input_empty_elements = [
    ("ISA", ["00", "          ", "00", "          ", "ZZ"]),
    ("GS", ["BE", "", "", "", ""]),
    ("ST", ["00", "          ", "00", "          ", "ZZ"]),
    ("SE", ["00", "          ", "00", "          ", "ZZ"]),
    ("GE", ["00", "          ", "00", "          ", "ZZ"]),
    ("IEA", ["00", "          ", "00", "          ", "ZZ"]),
]

generator_output_empty_elements = """ISA*00*          *00*          *ZZ~
GS*BE~
ST*00*          *00*          *ZZ~
SE*00*          *00*          *ZZ~
GE*00*          *00*          *ZZ~
IEA*00*          *00*          *ZZ~
"""

generator_input_no_elements = [
    ("ISA", ["00", "          ", "00", "          ", "ZZ"]),
    ("GS", ["BE", "          ", "00", "          ", "ZZ"]),
    ("ST", ["00", "          ", "00", "          ", "ZZ"]),
    ("SE", None),
    ("GE", []),
    ("IEA", ["00", "          ", "00", "          ", "ZZ"]),
]

generator_output_no_elements = """ISA*00*          *00*          *ZZ~
GS*BE*          *00*          *ZZ~
ST*00*          *00*          *ZZ~
IEA*00*          *00*          *ZZ~
"""

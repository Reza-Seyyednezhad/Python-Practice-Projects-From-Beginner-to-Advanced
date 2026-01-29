import os
os.system("cls")
class Length_Unit_Class:
    def __init__(self, value:float):
        self.value = value

    def meter_to_meter(self):
        return f"{self.value} m"
    
    def meter_to_foot(self):
        return f"{self.value * 3.2808399} ft"
    
    def meter_to_inch(self):
        return f"{self.value * 39.37007874} inch"
    
    def meter_to_yard(self):
        return f"{self.value * 1.0936133} yard"
    
    def meter_to_mile(self):
        return f"{self.value * 0.00062137} mile"
    
    def foot_to_foot(self):
        return f"{self.value} ft"
    
    def foot_to_meter(self):
        return f"{self.value * 0.3048} m"
    
    def foot_to_inch(self):
        return f"{self.value * 12} inch"
    
    def foot_to_yard(self):
        return f"{self.value * 0.333333} yard"
    
    def foot_to_mile(self):
        return f"{self.value * 0.00018939} mile"
    
    def inch_to_inch(self):
        return f"{self.value} inch"
    
    def inch_to_meter(self):
        return f"{self.value * 0.0254} m"
    
    def inch_to_foot(self):
        return f"{self.value * 0.0833333} foot"
    
    def inch_to_yard(self):
        return f"{self.value * 0.02777778} yard"
    
    def inch_to_mile(self):
        return f"{self.value * 0.00001578} mile"
    
    def yard_to_yard(self):
        return f"{self.value} yard"
    
    def yard_to_meter(self):
        return f"{self.value * 0.9144} m"
    
    def yard_to_inch(self):
        return f"{self.value * 36} inch"
    
    def yard_to_foot(self):
        return f"{self.value * 3} foot"
    
    def yard_to_mile(self):
        return f"{self.value * 0.00056818} mile"
    
    def mile_to_mile(self):
        return f"{self.value} mile"
    
    def mile_to_meter(self):
        return f"{self.value * 1609.344} m"
    
    def mile_to_inch(self):
        return f"{self.value * 63360} inch"
    
    def mile_to_foot(self):
        return f"{self.value * 5280} ft"
    
    def mile_to_yard(self):
        return f"{self.value * 1760} yard"

# test1 = Length_Unit_Class(7)

# print(test1.meter_to_meter()) => 7 m
# print(test1.meter_to_inch()) => 275.59055118 inch
# print(test1.meter_to_foot()) => 22.9658793 ft
# print(test1.meter_to_mile()) => 0.00434959 mile
# print(test1.meter_to_yard()) => 7.6552931 yard

# print(test1.inch_to_inch()) => 7 inch
# print(test1.inch_to_meter()) => 0.17779999999999999 m
# print(test1.inch_to_foot()) => 0.5833330999999999 foot
# print(test1.inch_to_mile()) => 0.00011046000000000001 mile
# print(test1.inch_to_yard()) => 0.19444445999999999 yard

# print(test1.foot_to_foot()) => 7 ft
# print(test1.foot_to_meter()) => 2.1336 m
# print(test1.foot_to_inch()) => 84 inch
# print(test1.foot_to_mile()) => 0.00132573 mile
# print(test1.foot_to_yard()) => 2.333331 yard

# print(test1.mile_to_mile()) => 7 mile
# print(test1.mile_to_meter()) => 11265.408 m
# print(test1.mile_to_inch()) => 443520 inch
# print(test1.mile_to_foot()) => 36960 ft
# print(test1.mile_to_yard()) => 12320 yard 

# print(test1.yard_to_yard()) => 7 yard
# print(test1.yard_to_meter()) => 6.4008 m
# print(test1.yard_to_inch()) => 252 inch
# print(test1.yard_to_foot()) => 21 foot
# print(test1.yard_to_mile()) => 0.003977260000000001 mile

class Weight_Unit_Class:
    def __init__(self, value:float):
        self.value = value
    
    def gram_to_gram(self):
        return f"{self.value} gr"
    
    def gram_to_ton(self):
        return f"{self.value * 0.000001} ton"
    
    def gram_to_Ib(self):
        return f"{self.value * 0.00220462} Ib"
    
    def gram_to_slug(self):
        return f"{self.value * 0.00006852} slug"
    
    def ton_to_ton(self):
        return f"{self.value} ton"
    
    def ton_to_gram(self):
        return f"{self.value * 1000000} gram"
    
    def ton_to_Ib(self):
        return f"{self.value * 2204.62262185} Ib"
    
    def ton_to_slug(self):
        return f"{self.value * 68.52176556} slug"
    
    def Ib_to_Ib(self):
        return f"{self.value} Ib"
    
    def Ib_to_gram(self):
        return f"{self.value * 453.59237} gram"
    
    def Ib_to_ton(self):
        return f"{self.value * 0.00045359} ton"
    
    def Ib_to_slug(self):
        return f"{self.value * 0.03108095} slug"
    
    def slug_to_slug(self):
        return f"{self.value} slug"
    
    def slug_to_gram(self):
        return f"{self.value * 14593.903} gram"
    
    def slug_to_ton(self):
        return f"{self.value * 0.0145939} ton"
    
    def slug_to_Ib(self):
        return f"{self.value * 32.17404869} Ib"

# test2 = Weight_Unit_Class(7)

# print(test2.gram_to_gram()) => 7 gr
# print(test2.gram_to_ton()) => 7e-06 ton
# print(test2.gram_to_Ib()) => 0.01543234 Ib
# print(test2.gram_to_slug()) => 0.00047964000000000004 slug

# print(test2.ton_to_ton()) => 7 ton
# print(test2.ton_to_gram()) => 7000000 gram
# print(test2.ton_to_Ib()) => 15432.358352950001 Ib  
# print(test2.ton_to_slug()) => 479.65235892000004 slug

# print(test2.Ib_to_Ib()) => 7 Ib
# print(test2.Ib_to_gram()) => 3175.1465900000003 gram
# print(test2.Ib_to_ton()) => 0.00317513 ton
# print(test2.Ib_to_slug()) => 0.21756665 slug  

# print(test2.slug_to_slug()) => 7 slug
# print(test2.slug_to_gram()) => 102157.321 gram
# print(test2.slug_to_ton()) => 0.1021573 ton
# print(test2.slug_to_Ib()) => 225.21834083 Ib

class Pressure_Unit_Class:
    def __init__(self, value:float):
        self.value = value

    def pascal_to_pascal(self):
        return f"{self.value} pascal"
    
    def pascal_to_bar(self):
        return f"{self.value * 0.00001} bar"
    
    def pascal_to_psi(self):
        return f"{self.value * 0.00014504} psi"
    
    def pascal_to_torr(self):
        return f"{self.value * 0.00750062} torr"
    
    def pascal_to_atm(self):
        return f"{self.value * 0.00000987} atm"
    
    def pascal_to_mmHg(self):
        return f"{self.value * 0.00750062} mmHg"
    
    
    def bar_to_bar(self):
        return f"{self.value} bar"
    
    def bar_to_pascal(self):
        return f"{self.value * 100000} pascal"
    
    def bar_to_psi(self):
        return f"{self.value * 14.50377377} psi"
    
    def bar_to_torr(self):
        return f"{self.value * 750.0616827} torr"
    
    def bar_to_atm(self):
        return f"{self.value * 0.98692327} atm"
    
    def bar_to_mmHg(self):
        return f"{self.value * 750.06157585} mmHg"
    
    
    def psi_to_psi(self):
        return f"{self.value} psi"
    
    def psi_to_pascal(self):
        return f"{self.value * 6894.7572931} pascal"
    
    def psi_to_bar(self):
        return f"{self.value * 0.06894757} bar"
    
    def psi_to_torr(self):
        return f"{self.value * 51.71493257} torr"
    
    def psi_to_atm(self):
        return f"{self.value * 0.06804596} atm"
    
    def psi_to_mmHg(self):
        return f"{self.value * 51.7149252} mmHg"
    
    
    def torr_to_torr(self):
        return f"{self.value} torr"
    
    def torr_to_pascal(self):
        return f"{self.value * 133.32236842} pascal"
    
    def torr_to_bar(self):
        return f"{self.value * 0.00133322} bar"
    
    def torr_to_psi(self):
        return f"{self.value * 0.01933677} psi"
    
    def torr_to_atm(self):
        return f"{self.value * 0.00131579} atm"
    
    def torr_to_mmHg(self):
        return f"{self.value * 0.99999986} mmHg"
    
    
    def atm_to_atm(self):
        return f"{self.value} atm"
    
    def atm_to_pascal(self):
        return f"{self.value * 101325} pascal"
    
    def atm_to_bar(self):
        return f"{self.value * 1.01325} bar"
    
    def atm_to_psi(self):
        return f"{self.value * 14.69594878} psi"
    
    def atm_to_torr(self):
        return f"{self.value * 760} torr"
    
    def atm_to_mmHg(self):
        return f"{self.value * 759.99989173} mmHg"
    
    
    def mmHg_to_mmHg(self):
        return f"{self.value} mmHg"
    
    def mmHg_to_pascal(self):
        return f"{self.value * 133.32238742} pascal"
    
    def mmHg_to_bar(self):
        return f"{self.value * 0.00133322} bar"
    
    def mmHg_to_psi(self):
        return f"{self.value * 0.01933678} psi"
    
    def mmHg_to_torr(self):
        return f"{self.value * 1.00000014} torr"
    
    def mmHg_to_atm(self):
        return f"{self.value * 0.00131579} atm"
    
# test3 = Pressure_Unit_Class(7)

# print(test3.pascal_to_pascal()) => 7 pascal
# print(test3.pascal_to_bar()) => 7.000000000000001e-05 bar
# print(test3.pascal_to_psi()) => 0.0010152800000000001 psi
# print(test3.pascal_to_torr()) => 0.052504340000000004 torr
# print(test3.pascal_to_atm()) => 6.909e-05 atm
# print(test3.pascal_to_mmHg()) => 0.052504340000000004 mmHg

# print(test3.bar_to_bar()) => 7 bar
# print(test3.bar_to_pascal()) => 700000 pascal
# print(test3.bar_to_psi()) => 101.52641639000001 psi
# print(test3.bar_to_torr()) => 5250.4317789 torr
# print(test3.bar_to_atm()) => 6.90846289 atm
# print(test3.bar_to_mmHg()) => 5250.431030950001 mmHg

# print(test3.psi_to_psi()) => 7 psi
# print(test3.psi_to_pascal()) => 48263.3010517 pascal
# print(test3.psi_to_bar()) => 0.48263299 bar
# print(test3.psi_to_torr()) => 362.00452799000004 torr
# print(test3.psi_to_atm()) => 0.47632172 atm
# print(test3.psi_to_mmHg()) => 362.00447640000004 mmHg
    
# print(test3.torr_to_torr()) => 7 torr
# print(test3.torr_to_pascal()) => 933.25657894 pascal
# print(test3.torr_to_bar()) => 0.00933254 bar     
# print(test3.torr_to_psi()) => 0.13535739 psi     
# print(test3.torr_to_atm()) => 0.00921053 atm     
# print(test3.torr_to_mmHg()) => 6.99999902 mmHg

# print(test3.atm_to_atm()) => 7 atm
# print(test3.atm_to_pascal()) => 709275 pascal
# print(test3.atm_to_bar()) => 7.09275 bar
# print(test3.atm_to_psi()) => 102.87164146 psi
# print(test3.atm_to_torr()) => 5320 torr
# print(test3.atm_to_mmHg()) => 5319.99924211 mmHg

# print(test3.mmHg_to_mmHg()) => 7 mmHg
# print(test3.mmHg_to_pascal()) => 933.2567119400001 pascal
# print(test3.mmHg_to_bar()) => 0.00933254 bar
# print(test3.mmHg_to_psi()) => 0.13535746 psi
# print(test3.mmHg_to_torr()) => 7.00000098 torr
# print(test3.mmHg_to_atm()) => 0.00921053 atm


class Volume_Unit_Class:
    def __init__(self, value:float):
        self.value = value
        
    def liter_to_liter(self):
        return f"{self.value} liter"
    
    def liter_to_m3(self):
        return f"{self.value * 0.001} m3"
    
    def liter_to_cc(self):
        return f"{self.value * 1000} cc"
    
    def liter_to_ft3(self):
        return f"{self.value * 0.03531467} ft3"
    
    def liter_to_usGal(self):
        return f"{self.value * 0.26417205} US Gal"
    
    def liter_to_ukGal(self):
        return f"{self.value * 0.21996925} UK Gal"
    
    
    def m3_to_m3(self):
        return f"{self.value} m3"
    
    def m3_to_liter(self):
        return f"{self.value * 1000} liter"
    
    def m3_to_cc(self):
        return f"{self.value * 1000000} cc"
    
    def m3_to_ft3(self):
        return f"{self.value * 35.31466672} ft3"
    
    def m3_to_usGal(self):
        return f"{self.value * 264.17205236} US Gal"
    
    def m3_to_ukGal(self):
        return f"{self.value * 219.9692483} UK Gal"
    
    
    def cc_to_cc(self):
        return f"{self.value} cc"
    
    def cc_to_liter(self):
        return f"{self.value * 0.001} liter"
    
    def cc_to_m3(self):
        return f"{self.value * 0.000001} m3"
    
    def cc_to_ft3(self):
        return f"{self.value * 0.00003531} ft3"
    
    def cc_to_usGal(self):
        return f"{self.value * 0.00026417} US Gal"
    
    def cc_to_ukGal(self):
        return f"{self.value * 0.00021997} UK Gal"
    
    
    def ft3_to_ft3(self):
        return f"{self.value} ft3"
    
    def ft3_to_liter(self):
        return f"{self.value * 28.31684659} liter"
    
    def ft3_to_m3(self):
        return f"{self.value * 0.02831685} m3"
    
    def ft3_to_cc(self):
        return f"{self.value * 28316.846592} cc"
    
    def ft3_to_usGal(self):
        return f"{self.value * 7.48051948} US Gal"
    
    def ft3_to_ukGal(self):
        return f"{self.value * 6.22883546} UK Gal"
    

    def usGal_to_usGal(self):
        return f"{self.value} US Gal"
    
    def usGal_to_liter(self):
        return f"{self.value * 3.78541178} liter"
    
    def usGal_to_m3(self):
        return f"{self.value * 0.00378541} m3"
    
    def usGal_to_cc(self):
        return f"{self.value * 3785.411784} cc"
    
    def usGal_to_ft3(self):
        return f"{self.value * 0.13368056} ft3"
    
    def usGal_to_ukGal(self):
        return f"{self.value * 0.83267418} UK Gal"
    
    
    def ukGal_to_ukGal(self):
        return f"{self.value} UK Gal"

    def ukGal_to_liter(self):
        return f"{self.value * 4.54609} liter"
    
    def ukGal_to_m3(self):
        return f"{self.value * 0.00454609} m3"
    
    def ukGal_to_cc(self):
        return f"{self.value * 4546.09} cc"
    
    def ukGal_to_ft3(self):
        return f"{self.value * 0.16054365} ft3"
    
    def ukGal_to_usGal(self):
        return f"{self.value * 1.20094993} US Gal"
    

# test4 = Volume_Unit_Class(7)

# print(test4.liter_to_liter()) => 7 liter
# print(test4.liter_to_m3()) => 0.007 m3
# print(test4.liter_to_cc()) => 7000 cc
# print(test4.liter_to_ft3()) => 0.24720269 ft3
# print(test4.liter_to_usGal()) => 1.84920435 US Gal
# print(test4.liter_to_ukGal()) => 1.53978475 UK Gal

# print(test4.m3_to_m3()) => 7 m3
# print(test4.m3_to_liter()) => 7000 liter
# print(test4.m3_to_cc()) => 7000000 cc
# print(test4.m3_to_ft3()) => 247.20266704 ft3
# print(test4.m3_to_usGal()) => 1849.2043665200001 US Gal
# print(test4.m3_to_ukGal()) => 1539.7847381000001 UK Gal

# print(test4.cc_to_cc()) => 7 cc
# print(test4.cc_to_liter()) => 0.007 liter
# print(test4.cc_to_m3()) => 7e-06 m3
# print(test4.cc_to_ft3()) => 0.00024717 ft3
# print(test4.cc_to_usGal()) => 0.00184919 US Gal
# print(test4.cc_to_ukGal()) => 0.00153979 UK Gal

# print(test4.ft3_to_ft3()) => 7 ft3
# print(test4.ft3_to_liter()) => 198.21792613 liter
# print(test4.ft3_to_m3()) => 0.19821795 m3
# print(test4.ft3_to_cc()) => 198217.92614400003 cc
# print(test4.ft3_to_usGal()) => 52.36363636 US Gal
# print(test4.ft3_to_ukGal()) => 43.60184822 UK Gal

# print(test4.usGal_to_usGal()) => 7 US Gal
# print(test4.usGal_to_liter()) => 26.49788246 liter
# print(test4.usGal_to_m3()) => 0.02649787 m3
# print(test4.usGal_to_cc()) => 26497.882488 cc
# print(test4.usGal_to_ft3()) => 0.9357639200000001 ft3
# print(test4.usGal_to_ukGal()) => 5.828719260000001 UK Gal

# print(test4.ukGal_to_ukGal()) => 7 UK Gal
# print(test4.ukGal_to_liter()) => 31.822630000000004 liter
# print(test4.ukGal_to_m3()) => 0.03182263 m3
# print(test4.ukGal_to_cc()) => 31822.63 cc
# print(test4.ukGal_to_ft3()) => 1.1238055500000002 ft3
# print(test4.ukGal_to_usGal()) => 8.40664951 US Gal


class Temperature_Unit_Class:
    def __init__(self, value:float):
        self.value = value
    
    def celsius_to_celsius(self):
        return f"{self.value} C"
    
    def celsius_to_kelvin(self):
        return f"{self.value + 273.15} K"
    
    def celsius_to_fahrenheit(self):
        return f"{(self.value * 1.8) + 32} F"
    
    
    def kelvin_to_kelvin(self):
        return f"{self.value} K"
    
    def kelvin_to_celsius(self):
        return f"{self.value - 273.15} C"
    
    def kelvin_to_fahrenheit(self):
        return f"{(self.value * (9/5)) - 459.67} F"
    
    
    def fahrenheit_to_fahrenheit(self):
        return f"{self.value} F"
    
    def fahrenheit_to_celsius(self):
        return f"{(self.value - 32) / 1.8} C"
    
    def fahrenheit_to_kelvin(self):
        return f"{(self.value + 459.67) * (5/9)} K"

# test5 = Temperature_Unit_Class(7)

# print(test5.celsius_to_celsius()) => 7 C
# print(test5.celsius_to_kelvin()) => 280.15 K
# print(test5.celsius_to_fahrenheit()) => 44.6 F

# print(test5.kelvin_to_kelvin()) => 7 K
# print(test5.kelvin_to_celsius()) => -266.15 C
# print(test5.kelvin_to_fahrenheit()) => -447.07 F

# print(test5.fahrenheit_to_fahrenheit()) => 7 F
# print(test5.fahrenheit_to_celsius()) => -13.88888888888889 C
# print(test5.fahrenheit_to_kelvin()) => 259.2611111111111 K


class Area_Unit_Class:
    def __init__(self, value:float):
        self.value = value
    
    def m2_to_m2(self):
        return f"{self.value} m2"
    
    def m2_to_ft2(self):
        return f"{self.value * 10.76391042} ft2"
    
    def m2_to_inch2(self):
        return f"{self.value * 1550.00310001} inch2"
    
    def m2_to_mile2(self):
        return f"{self.value * 0.000000386102159} mile2"
    
    
    def ft2_to_ft2(self):
        return f"{self.value} ft2"
    
    def ft2_to_m2(self):
        return f"{self.value * 0.09290304} m2"
    
    def ft2_to_inch2(self):
        return f"{self.value * 144} inch2"
    
    def ft2_to_mile2(self):
        return f"{self.value * 0.0000000358700643} mile2"
    
    
    def inch2_to_inch2(self):
        return f"{self.value} inch2"
    
    def inch2_to_m2(self):
        return f"{self.value * 0.00064516} m2"
    
    def inch2_to_ft2(self):
        return f"{self.value * 0.00694444} ft2"
    
    def inch2_to_mile2(self):
        return f"{self.value * 0.000000000249097669} mile2"
    
    
    def mile2_to_mile2(self):
        return f"{self.value} mile2"
    
    def mile2_to_m2(self):
        return f"{self.value * 2589988.110336} m2"
    
    def mile2_to_ft2(self):
        return f"{self.value * 27878400} ft2"
    
    def mile2_to_inch2(self):
        return f"{self.value * 4014489600} inch2"

# test5 = Area_Unit_Class(7)

# print(test5.m2_to_m2()) => 7 m2
# print(test5.m2_to_inch2()) => 10850.02170007 inch2
# print(test5.m2_to_ft2()) => 75.34737294 ft2
# print(test5.m2_to_mile2()) => 2.702715113e-06 mile2
    
# print(test5.ft2_to_ft2()) => 7 ft2
# print(test5.ft2_to_m2()) => 0.65032128 m2
# print(test5.ft2_to_inch2()) => 1008 inch2
# print(test5.ft2_to_mile2()) => 2.510904501e-07 mile2
    
# print(test5.inch2_to_inch2()) => 7 inch2
# print(test5.inch2_to_m2()) => 0.00451612 m2
# print(test5.inch2_to_ft2()) => 0.04861108 ft2
# print(test5.inch2_to_mile2()) => 1.7436836830000002e-09 mile2

# print(test5.mile2_to_mile2()) => 7 mile2
# print(test5.mile2_to_m2()) => 18129916.772352003 m2
# print(test5.mile2_to_inch2()) => 28101427200 inch2
# print(test5.mile2_to_ft2()) => 195148800 ft2


class Time_Unit_Class:
    def __init__(self, value:float):
        self.value = value
        
    def second_to_second(self):
        return f"{self.value} second"
    
    def second_to_minute(self):
        return f"{self.value * 0.01666667} minute"
    
    def second_to_hour(self):
        return f"{self.value * 0.00027778} hour"
    
    def second_to_day(self):
        return f"{self.value * 0.00001157} day"
    
    def second_to_week(self):
        return f"{self.value * 0.00000165} week"
    
    def second_to_month(self):
        return f"{self.value * 3.80257054e-7} month"
    
    def second_to_year(self):
        return f"{self.value * 3.16880878e-8} year"
    
    
    
    def minute_to_minute(self):
        return f"{self.value} minute"
    
    def minute_to_second(self):
        return f"{self.value * 60} second"
    
    def minute_to_hour(self):
        return f"{self.value * 0.01666667} hour"
    
    def minute_to_day(self):
        return f"{self.value * 0.00069444} day"
    
    def minute_to_week(self):
        return f"{self.value * 0.00009921} week"
    
    def minute_to_month(self):
        return f"{self.value * 0.00002282} month"
    
    def minute_to_year(self):
        return f"{self.value * 0.0000019} year"
    
    
    
    def hour_to_hour(self):
        return f"{self.value} hour"
    
    def hour_to_second(self):
        return f"{self.value * 3600} second"
    
    def hour_to_minute(self):
        return f"{self.value * 60} minute"
    
    def hour_to_day(self):
        return f"{self.value * 0.04166667} day"
    
    def hour_to_week(self):
        return f"{self.value * 0.00595238} week"
    
    def hour_to_month(self):
        return f"{self.value * 0.00136893} month"
    
    def hour_to_year(self):
        return f"{self.value * 0.00011408} year"
    
    
    
    def day_to_day(self):
        return f"{self.value} day"
    
    def day_to_second(self):
        return f"{self.value * 86400} second"
    
    def day_to_minute(self):
        return f"{self.value * 1440} minute"
    
    def day_to_hour(self):
        return f"{self.value * 24} hour"
    
    def day_to_week(self):
        return f"{self.value * 0.14285714} week"
    
    def day_to_month(self):
        return f"{self.value * 0.03285421} month"
    
    def day_to_year(self):
        return f"{self.value * 0.00273785} year"
    
    
    
    def week_to_week(self):
        return f"{self.value} week"
    
    def week_to_second(self):
        return f"{self.value * 604800} second"
    
    def week_to_minute(self):
        return f"{self.value * 10080} minute"
    
    def week_to_hour(self):
        return f"{self.value * 168} hour"
    
    def week_to_day(self):
        return f"{self.value * 7} day"
    
    def week_to_month(self):
        return f"{self.value * 0.22997947} month"
    
    def week_to_year(self):
        return f"{self.value * 0.01916496} year"
    
    
    
    def month_to_month(self):
        return f"{self.value} month"
    
    def month_to_second(self):
        return f"{self.value * 2629800} second"
    
    def month_to_minute(self):
        return f"{self.value * 43830} minute"
    
    def month_to_hour(self):
        return f"{self.value * 730.5} hour"
    
    def month_to_day(self):
        return f"{self.value * 30.4375} day"
    
    def month_to_week(self):
        return f"{self.value * 4.34821429} week"
    
    def month_to_year(self):
        return f"{self.value * 0.08333333} year"
    
    
    
    def year_to_year(self):
        return f"{self.value} year"
    
    def year_to_second(self):
        return f"{self.value * 31557600} second"
    
    def year_to_minute(self):
        return f"{self.value * 525960} minute"
    
    def year_to_hour(self):
        return f"{self.value * 8766} hour"
    
    def year_to_day(self):
        return f"{self.value * 365.25} day"
    
    def year_to_week(self):
        return f"{self.value * 52.1785} week"
    
    def year_to_month(self):
        return f"{self.value * 12} month"


# test6 = Time_Unit_Class(7)

# print(test6.second_to_second()) => 7 second
# print(test6.second_to_minute()) => 0.11666669000000002 minute
# print(test6.second_to_hour()) => 0.0019444599999999999 hour
# print(test6.second_to_day()) => 8.099e-05 day
# print(test6.second_to_week()) => 1.1550000000000001e-05 week
# print(test6.second_to_month()) => 2.661799378e-06 month
# print(test6.second_to_year()) => 2.2181661459999998e-07 year

# print(test6.minute_to_minute()) => 7 minute
# print(test6.minute_to_second()) => 420 second
# print(test6.minute_to_hour()) => 0.11666669000000002 hour
# print(test6.minute_to_day()) => 0.00486108 day
# print(test6.minute_to_week()) => 0.00069447 week
# print(test6.minute_to_month()) => 0.00015973999999999999 month
# print(test6.minute_to_year()) => 1.33e-05 year

# print(test6.hour_to_hour()) => 7 hour
# print(test6.hour_to_second()) => 25200 second
# print(test6.hour_to_minute()) => 420 minute
# print(test6.hour_to_day()) => 0.29166669 day
# print(test6.hour_to_week()) => 0.04166666 week
# print(test6.hour_to_month()) => 0.009582509999999999 month
# print(test6.hour_to_year()) => 0.00079856 year

# print(test6.day_to_day()) => 7 day
# print(test6.day_to_second()) => 604800 second
# print(test6.day_to_minute()) => 10080 minute
# print(test6.day_to_hour()) => 168 hour
# print(test6.day_to_week()) => 0.9999999799999999 week
# print(test6.day_to_month()) => 0.22997947000000002 month
# print(test6.day_to_year()) => 0.01916495 year

# print(test6.week_to_week()) => 7 week
# print(test6.week_to_second()) => 4233600 second
# print(test6.week_to_minute()) => 70560 minute
# print(test6.week_to_hour()) => 1176 hour
# print(test6.week_to_day()) => 49 day
# print(test6.week_to_month()) => 1.60985629 month
# print(test6.week_to_year()) => 0.13415472 year

# print(test6.month_to_month()) => 7 month
# print(test6.month_to_second()) => 18408600 second
# print(test6.month_to_minute()) => 306810 minute
# print(test6.month_to_hour()) => 5113.5 hour
# print(test6.month_to_day()) => 213.0625 day
# print(test6.month_to_week()) => 30.437500029999995 week
# print(test6.month_to_year()) => 0.58333331 year

# print(test6.year_to_year()) => 7 year
# print(test6.year_to_second()) => 220903200 second
# print(test6.year_to_minute()) => 3681720 minute
# print(test6.year_to_hour()) => 61362 hour
# print(test6.year_to_day()) => 2556.25 day
# print(test6.year_to_week()) => 365.25 week
# print(test6.year_to_month()) => 84 month



# Create User Interface

def user_input():
    user_input_unit_name_to_convert = int(input(f"Which UNIT do you want to CONVERT: \n1. Length \n2. Weight \n3. Pressure \n4. Volume \n5. Temperature \n6. Area \n7. Time \n Please Enter NUMBER (1 to 7): "))
    os.system("cls")
    if user_input_unit_name_to_convert == 1:
        user_input_length_unit = int(input("Length Unit Converter \n1. meter to meter \n2. meter to inch \n3. meter to foot \n4. meter to mile \n5. meter to yard \n\n6. inch to inch \n7. inch to meter \n8. inch to foot \n9. inch to mile \n10. inch to yard \n\n11. foot to foot \n12. foot to meter \n13. foot to inch \n14. foot to mile \n15. foot to yard \n\n16. mile to mile \n17. mile to meter \n18. mile to inch \n19. mile to foot \n20. mile to yard \n\n21. yard to yard \n22. yard to meter \n23. yard to inch \n24. yard to foot \n25. yard to mile \n\nWhich one of these length unit converter do you need (Enter a number from 1 to 25): "))
        user_input_length_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Length_Unit_Converter = Length_Unit_Class(user_input_length_value)
        if user_input_length_unit == 1:
            print(f"{user_input_length_value} meter = {Length_Unit_Converter.meter_to_meter()}")
        elif user_input_length_unit == 2:
            print(f"{user_input_length_value} meter = {Length_Unit_Converter.meter_to_inch()}")
        elif user_input_length_unit == 3:
            print(f"{user_input_length_value} meter = {Length_Unit_Converter.meter_to_foot()}")
        elif user_input_length_unit == 4:
            print(f"{user_input_length_value} meter = {Length_Unit_Converter.meter_to_mile()}")
        elif user_input_length_unit == 5:
            print(f"{user_input_length_value} meter = {Length_Unit_Converter.meter_to_yard()}")
            
        elif user_input_length_unit == 6:
            print(f"{user_input_length_value} inch = {Length_Unit_Converter.inch_to_inch()}")
        elif user_input_length_unit == 7:
            print(f"{user_input_length_value} inch = {Length_Unit_Converter.inch_to_meter()}")
        elif user_input_length_unit == 8:
            print(f"{user_input_length_value} inch = {Length_Unit_Converter.inch_to_foot()}")
        elif user_input_length_unit == 9:
            print(f"{user_input_length_value} inch = {Length_Unit_Converter.inch_to_mile()}")
        elif user_input_length_unit == 10:
            print(f"{user_input_length_value} inch = {Length_Unit_Converter.inch_to_yard()}")
            
        elif user_input_length_unit == 11:
            print(f"{user_input_length_value} foot = {Length_Unit_Converter.foot_to_foot()}")
        elif user_input_length_unit == 12:
            print(f"{user_input_length_value} foot = {Length_Unit_Converter.foot_to_meter()}")
        elif user_input_length_unit == 13:
            print(f"{user_input_length_value} foot = {Length_Unit_Converter.foot_to_inch()}")
        elif user_input_length_unit == 14:
            print(f"{user_input_length_value} foot = {Length_Unit_Converter.foot_to_mile()}")
        elif user_input_length_unit == 15:
            print(f"{user_input_length_value} foot = {Length_Unit_Converter.foot_to_yard()}")
        
        elif user_input_length_unit == 16:
            print(f"{user_input_length_value} mile = {Length_Unit_Converter.mile_to_mile()}")
        elif user_input_length_unit == 17:
            print(f"{user_input_length_value} mile = {Length_Unit_Converter.mile_to_meter()}")
        elif user_input_length_unit == 18:
            print(f"{user_input_length_value} mile = {Length_Unit_Converter.mile_to_inch()}")
        elif user_input_length_unit == 19:
            print(f"{user_input_length_value} mile = {Length_Unit_Converter.mile_to_foot()}")
        elif user_input_length_unit == 20:
            print(f"{user_input_length_value} mile = {Length_Unit_Converter.mile_to_yard()}")
        
        elif user_input_length_unit == 21:
            print(f"{user_input_length_value} yard = {Length_Unit_Converter.yard_to_yard()}")
        elif user_input_length_unit == 22:
            print(f"{user_input_length_value} yard = {Length_Unit_Converter.yard_to_meter()}")
        elif user_input_length_unit == 23:
            print(f"{user_input_length_value} yard = {Length_Unit_Converter.yard_to_inch()}")
        elif user_input_length_unit == 24:
            print(f"{user_input_length_value} yard = {Length_Unit_Converter.yard_to_foot()}")
        elif user_input_length_unit == 25:
            print(f"{user_input_length_value} yard = {Length_Unit_Converter.yard_to_mile()}")
        
        else:
            print("Enter Right NUMBER from 1 to 25, PLEASE...")
            
    elif user_input_unit_name_to_convert == 2:
        user_input_weight_unit = int(input(f"Weight Unit Converter \n1. gram to gram \n2. gram to ton \n3. gram to Ib \n4. gram to slug \n\n5. ton to ton \n6. ton to gram \n7. ton to Ib \n8. ton to slug \n\n9. Ib to Ib \n10. Ib to gram \n11. Ib to ton \n12. Ib to slug \n\n13. slug to slug \n14. slug to gram \n15. slug to ton \n16. slug to Ib \n\nWhich one of these weight unit converter do you need (Enter a number from 1 to 16): "))
        user_input_weight_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Weight_Unit_Converter = Weight_Unit_Class(user_input_weight_unit)
        if user_input_weight_unit == 1:
            print(f"{user_input_weight_value} gram = {Weight_Unit_Converter.gram_to_gram()}")
        elif user_input_weight_unit == 2:
            print(f"{user_input_weight_value} gram = {Weight_Unit_Converter.gram_to_ton()}")
        elif user_input_weight_unit == 3:
            print(f"{user_input_weight_value} gram = {Weight_Unit_Converter.gram_to_Ib()}")
        elif user_input_weight_unit == 4:
            print(f"{user_input_weight_value} gram = {Weight_Unit_Converter.gram_to_slug()}")
        
        elif user_input_weight_unit == 5:
            print(f"{user_input_weight_value} ton = {Weight_Unit_Converter.ton_to_ton()}")
        elif user_input_weight_unit == 6:
            print(f"{user_input_weight_value} ton = {Weight_Unit_Converter.ton_to_gram()}")
        elif user_input_weight_unit == 7:
            print(f"{user_input_weight_value} ton = {Weight_Unit_Converter.ton_to_Ib()}")
        elif user_input_weight_unit == 8:
            print(f"{user_input_weight_value} ton = {Weight_Unit_Converter.ton_to_slug()}")
        
        elif user_input_weight_unit == 9:
            print(f"{user_input_weight_value} Ib = {Weight_Unit_Converter.Ib_to_Ib()}")
        elif user_input_weight_unit == 10:
            print(f"{user_input_weight_value} Ib = {Weight_Unit_Converter.Ib_to_gram()}")
        elif user_input_weight_unit == 11:
            print(f"{user_input_weight_value} Ib = {Weight_Unit_Converter.Ib_to_ton()}")
        elif user_input_weight_unit == 12:
            print(f"{user_input_weight_value} Ib = {Weight_Unit_Converter.Ib_to_slug()}")
        
        elif user_input_weight_unit == 13:
            print(f"{user_input_weight_value} slug = {Weight_Unit_Converter.slug_to_slug()}")
        elif user_input_weight_unit == 14:
            print(f"{user_input_weight_value} slug = {Weight_Unit_Converter.slug_to_gram()}")
        elif user_input_weight_unit == 15:
            print(f"{user_input_weight_value} slug = {Weight_Unit_Converter.slug_to_ton()}")
        elif user_input_weight_unit == 16:
            print(f"{user_input_weight_value} slug = {Weight_Unit_Converter.slug_to_Ib()}")

    elif user_input_unit_name_to_convert == 3:
        user_input_pressure_unit = int(input(f"Pressure Unit Converter \n1. pascal to pascal \n2. pascal to bar \n3. pascal to psi \n4. pascal to torr \n5. pascal to atm \n6. pascal to mmHg \n\n7. bar to bar \n8. bar to pascal \n9. bar to psi \n10. bar to torr \n11. bar to atm \n12. bar to mmHg \n\n13. psi to psi \n14. psi to pascal \n15. psi to bar \n16. psi to torr \n17. psi to atm \n18. psi to mmHg \n\n19. torr to torr \n20. torr to pascal \n21. torr to bar \n22. torr to psi \n23. torr to atm \n24. torr to mmHg \n\n25. atm to atm \n26. atm to pascal \n27. atm to bar \n28. atm to psi \n29. atm to torr \n30. atm to mmHg \n\n31. mmHg to mmHg \n32. mmHg to pascal \n33. mmHg to bar \n34. mmHg to psi \n35. mmHg to torr \n36. mmHg to atm \n\nWhich one of these pressure unit converter do you need (Enter a number from 1 to 36): "))
        user_input_pressure_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Pressure_Unit_Converter = Pressure_Unit_Class(user_input_pressure_value)
        if user_input_pressure_unit == 1:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_pascal()}")
        elif user_input_pressure_unit == 2:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_bar()}")
        elif user_input_pressure_unit == 3:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_psi()}")
        elif user_input_pressure_unit == 4:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_torr()}")
        elif user_input_pressure_unit == 5:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_atm()}")
        elif user_input_pressure_unit == 6:
            print(f"{user_input_pressure_value} pascal = {Pressure_Unit_Converter.pascal_to_mmHg()}")
        
        elif user_input_pressure_unit == 7:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_bar()}")
        elif user_input_pressure_unit == 8:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_pascal()}")
        elif user_input_pressure_unit == 9:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_psi()}")
        elif user_input_pressure_unit == 10:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_torr()}")
        elif user_input_pressure_unit == 11:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_atm()}")
        elif user_input_pressure_unit == 12:
            print(f"{user_input_pressure_value} bar = {Pressure_Unit_Converter.bar_to_mmHg()}")
        
        elif user_input_pressure_unit == 13:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_psi()}")
        elif user_input_pressure_unit == 14:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_pascal()}")
        elif user_input_pressure_unit == 15:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_bar()}")
        elif user_input_pressure_unit == 16:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_torr()}")
        elif user_input_pressure_unit == 17:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_atm()}")
        elif user_input_pressure_unit == 18:
            print(f"{user_input_pressure_value} psi = {Pressure_Unit_Converter.psi_to_mmHg()}")
        
        elif user_input_pressure_unit == 19:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_torr()}")
        elif user_input_pressure_unit == 20:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_pascal()}")
        elif user_input_pressure_unit == 21:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_bar()}")
        elif user_input_pressure_unit == 22:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_psi()}")
        elif user_input_pressure_unit == 23:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_atm()}")
        elif user_input_pressure_unit == 24:
            print(f"{user_input_pressure_value} torr = {Pressure_Unit_Converter.torr_to_mmHg()}")
        
        elif user_input_pressure_unit == 25:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_atm()}")
        elif user_input_pressure_unit == 26:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_pascal()}")
        elif user_input_pressure_unit == 27:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_bar()}")
        elif user_input_pressure_unit == 28:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_psi()}")
        elif user_input_pressure_unit == 29:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_torr()}")
        elif user_input_pressure_unit == 30:
            print(f"{user_input_pressure_value} atm = {Pressure_Unit_Converter.atm_to_mmHg()}")
        
        elif user_input_pressure_unit == 31:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_mmHg()}")
        elif user_input_pressure_unit == 32:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_pascal()}")
        elif user_input_pressure_unit == 33:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_bar()}")
        elif user_input_pressure_unit == 34:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_psi()}")
        elif user_input_pressure_unit == 35:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_torr()}")
        elif user_input_pressure_unit == 36:
            print(f"{user_input_pressure_value} mmHg = {Pressure_Unit_Converter.mmHg_to_atm()}")
        
        else:
            print("Enter Right NUMBER from 1 to 36, PLEASE...")
        
    elif user_input_unit_name_to_convert == 4:
        user_input_volume_unit = int(input(f"Volume Unit Converter \n1. liter to liter \n2. liter to m3 \n3. liter to cc \n4. liter to ft3 \n5. liter to US Gal \n6. liter to UK Gal \n\n7. m3 to m3 \n8. m3 to liter \n9. m3 to cc \n10. m3 to ft3 \n11. m3 to US Gal \n12. m3 to UK Gal \n\n13. cc to cc \n14. cc to liter \n15. cc to m3 \n16. cc to ft3 \n17. cc to US Gal \n18. cc to UK Gal \n\n19. ft3 to ft3 \n20. ft3 to liter \n21. ft3 to m3 \n22. ft3 to cc \n23. ft3 to US Gal \n24. ft3 to UK Gal \n\n25. US Gal to US Gal \n26. US Gal to liter \n27. US Gal to m3 \n28. US Gal to cc \n29. US Gal to ft3 \n30. US Gal to UK Gal \n\n31. UK Gal to UK Gal \n32. UK Gal to liter \n33. UK Gal to m3 \n34. UK Gal to cc \n35. UK Gal to ft3 \n36. UK Gal to US Gal \n\nWhich one of these Volume unit converter do you need (Enter a number from 1 to 36): "))
        user_input_volume_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Volume_Unit_Converter = Volume_Unit_Class(user_input_volume_value)
        if user_input_volume_unit == 1:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_liter()}")
        elif user_input_volume_unit == 2:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_m3()}")
        elif user_input_volume_unit == 3:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_cc()}")
        elif user_input_volume_unit == 4:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_ft3()}")
        elif user_input_volume_unit == 5:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_usGal()}")
        elif user_input_volume_unit == 6:
            print(f"{user_input_volume_value} liter = {Volume_Unit_Converter.liter_to_ukGal()}")
        
        elif user_input_volume_unit == 7:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_m3()}")
        elif user_input_volume_unit == 8:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_liter()}")
        elif user_input_volume_unit == 9:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_cc()}")
        elif user_input_volume_unit == 10:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_ft3()}")
        elif user_input_volume_unit == 11:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_usGal()}")
        elif user_input_volume_unit == 12:
            print(f"{user_input_volume_value} m3 = {Volume_Unit_Converter.m3_to_ukGal()}")
        
        elif user_input_volume_unit == 13:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_cc()}")
        elif user_input_volume_unit == 14:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_liter()}")
        elif user_input_volume_unit == 15:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_m3()}")
        elif user_input_volume_unit == 16:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_ft3()}")
        elif user_input_volume_unit == 17:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_usGal()}")
        elif user_input_volume_unit == 18:
            print(f"{user_input_volume_value} cc = {Volume_Unit_Converter.cc_to_ukGal()}")
        
        elif user_input_volume_unit == 19:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_ft3()}")
        elif user_input_volume_unit == 20:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_liter()}")
        elif user_input_volume_unit == 21:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_m3()}")
        elif user_input_volume_unit == 22:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_cc()}")
        elif user_input_volume_unit == 23:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_usGal()}")
        elif user_input_volume_unit == 24:
            print(f"{user_input_volume_value} ft3 = {Volume_Unit_Converter.ft3_to_ukGal()}")
        
        elif user_input_volume_unit == 25:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_usGal()}")
        elif user_input_volume_unit == 26:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_liter()}")
        elif user_input_volume_unit == 27:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_m3()}")
        elif user_input_volume_unit == 28:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_cc()}")
        elif user_input_volume_unit == 29:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_ft3()}")
        elif user_input_volume_unit == 30:
            print(f"{user_input_volume_value} US Gal = {Volume_Unit_Converter.usGal_to_ukGal()}")
        
        elif user_input_volume_unit == 31:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_ukGal()}")
        elif user_input_volume_unit == 32:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_liter()}")
        elif user_input_volume_unit == 33:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_m3()}")
        elif user_input_volume_unit == 34:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_cc()}")
        elif user_input_volume_unit == 35:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_ft3()}")
        elif user_input_volume_unit == 36:
            print(f"{user_input_volume_value} UK Gal = {Volume_Unit_Converter.ukGal_to_usGal()}")
        
        else:
            print("Enter Right NUMBER from 1 to 36, PLEASE...")
            
    elif user_input_unit_name_to_convert == 5:
        user_input_temperature_unit = int(input(f"Temperature Unit Converter \n1. celsius to celsius \n2. celsius to kelvin \n3. celsius to fahrenheit \n\n4. kelvin to kelvin \n5. kelvin to celsius \n6. kelvin to fahrenheit \n\n7. fahrenheit to fahrenheit \n8. fahrenheit to celsius \n9. fahrenheit to kelvin \n\nWhich one of these Temperature unit converter do you need (Enter a number from 1 to 9): "))
        user_input_temperature_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Temperature_Unit_Converter = Temperature_Unit_Class(user_input_temperature_value)
        if user_input_temperature_unit == 1:
            print(f"{user_input_temperature_value} celsius = {Temperature_Unit_Converter.celsius_to_celsius()}")
        elif user_input_temperature_unit == 2:
            print(f"{user_input_temperature_value} celsius = {Temperature_Unit_Converter.celsius_to_kelvin()}")
        elif user_input_temperature_unit == 3:
            print(f"{user_input_temperature_value} celsius = {Temperature_Unit_Converter.celsius_to_fahrenheit()}")   
        
        elif user_input_temperature_unit == 4:
            print(f"{user_input_temperature_value} kelvin = {Temperature_Unit_Converter.kelvin_to_kelvin()}")   
        elif user_input_temperature_unit == 5:
            print(f"{user_input_temperature_value} kelvin = {Temperature_Unit_Converter.kelvin_to_celsius()}")   
        elif user_input_temperature_unit == 6:
            print(f"{user_input_temperature_value} kelvin = {Temperature_Unit_Converter.kelvin_to_fahrenheit()}")   
        
        elif user_input_temperature_unit == 7:
            print(f"{user_input_temperature_value} fahrenheit = {Temperature_Unit_Converter.fahrenheit_to_fahrenheit()}")   
        elif user_input_temperature_unit == 8:
            print(f"{user_input_temperature_value} fahrenheit = {Temperature_Unit_Converter.fahrenheit_to_celsius()}")   
        elif user_input_temperature_unit == 9:
            print(f"{user_input_temperature_value} fahrenheit = {Temperature_Unit_Converter.fahrenheit_to_kelvin()}")   
        
        else:
            print("Enter Right NUMBER from 1 to 9, PLEASE...")
        
        
    elif user_input_unit_name_to_convert == 6:
        user_input_area_unit = int(input(f"Area Unit Converter \n1. m2 to m2 \n2. m2 to ft2 \n3. m2 to inch2 \n4. m2 to mile2 \n\n5. ft2 to ft2 \n6. ft2 to m2 \n7. ft2 to inch2 \n8. ft2 to mile2 \n\n9. inch2 to inch2 \n10. inch2 to m2 \n11. inch2 to ft2 \n12. inch2 to mile2 \n\n13. mile2 to mile2 \n14. mile2 to m2 \n15. mile2 to ft2 \n16. mile2 to inch2 \n\nWhich one of these Area unit converter do you need (Enter a number from 1 to 16): "))
        user_input_area_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Area_Unit_Converter = Area_Unit_Class(user_input_area_value)
        if user_input_area_unit == 1:
            print(f"{user_input_area_value} m2 = {Area_Unit_Converter.m2_to_m2()}")   
        elif user_input_area_unit == 2:
            print(f"{user_input_area_value} m2 = {Area_Unit_Converter.m2_to_ft2()}")   
        elif user_input_area_unit == 3:
            print(f"{user_input_area_value} m2 = {Area_Unit_Converter.m2_to_inch2()}")   
        elif user_input_area_unit == 4:
            print(f"{user_input_area_value} m2 = {Area_Unit_Converter.m2_to_mile2()}")   
        
        elif user_input_area_unit == 5:
            print(f"{user_input_area_value} ft2 = {Area_Unit_Converter.ft2_to_ft2()}")   
        elif user_input_area_unit == 6:
            print(f"{user_input_area_value} ft2 = {Area_Unit_Converter.ft2_to_m2()}")   
        elif user_input_area_unit == 7:
            print(f"{user_input_area_value} ft2 = {Area_Unit_Converter.ft2_to_inch2()}")   
        elif user_input_area_unit == 8:
            print(f"{user_input_area_value} ft2 = {Area_Unit_Converter.ft2_to_mile2()}")   
        
        elif user_input_area_unit == 9:
            print(f"{user_input_area_value} inch2 = {Area_Unit_Converter.inch2_to_inch2()}")   
        elif user_input_area_unit == 10:
            print(f"{user_input_area_value} inch2 = {Area_Unit_Converter.inch2_to_m2()}")   
        elif user_input_area_unit == 11:
            print(f"{user_input_area_value} inch2 = {Area_Unit_Converter.inch2_to_ft2()}")   
        elif user_input_area_unit == 12:
            print(f"{user_input_area_value} inch2 = {Area_Unit_Converter.inch2_to_mile2()}")   
        
        elif user_input_area_unit == 13:
            print(f"{user_input_area_value} mile2 = {Area_Unit_Converter.mile2_to_mile2()}")   
        elif user_input_area_unit == 14:
            print(f"{user_input_area_value} mile2 = {Area_Unit_Converter.mile2_to_m2()}")   
        elif user_input_area_unit == 15:
            print(f"{user_input_area_value} mile2 = {Area_Unit_Converter.mile2_to_ft2()}")   
        elif user_input_area_unit == 16:
            print(f"{user_input_area_value} mile2 = {Area_Unit_Converter.mile2_to_inch2()}")   
        
        else:
            print("Enter Right NUMBER from 1 to 16, PLEASE...")
        
    elif user_input_unit_name_to_convert == 7:
        user_input_time_unit = int(input("Time Unit Converter \n1. second to second \n2. second to minute \n3. second to hour \n4. second to day \n5. second to week \n6. second to month \n7. second to year \n\n8. minute to minute \n9. minute to second \n10. minute to hour \n11. minute to day \n12. minute to week \n13. minute to month \n14. minute to year \n\n15. hour to hour \n16. hour to second \n17. hour to minute \n18. hour to day \n19. hour to week \n20. hour to month \n21. hour to year \n\n22. day to day \n23. day to second \n24. day to minute \n25. day to hour \n26. day to week \n27. day to month \n28. day to year \n\n29. week to week \n30. week to second \n31. week to minute \n32. week to hour \n33. week to day \n34. week to month \n35. week to year \n\n36. month to month \n37. month to second \n38. month to minute \n39. month to hour \n40. month to day \n41. month to week \n42. month to year \n\n43. year to year \n44. year to second \n45. year to minute \n46. year to hour \n47. year to day \n48. year to week \n49. year to month \n\nWhich one of these Time unit converter do you need (Enter a number from 1 to 25): "))
        user_input_time_value = float(input("Enter numerical value to Convert: "))
        os.system("cls")
        Time_Unit_Converter = Time_Unit_Class(user_input_time_value)
        if user_input_time_unit == 1:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_second()}")   
        elif user_input_time_unit == 2:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_minute()}")   
        elif user_input_time_unit == 3:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_hour()}")   
        elif user_input_time_unit == 4:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_day()}")   
        elif user_input_time_unit == 5:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_week()}")   
        elif user_input_time_unit == 6:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_month()}")   
        elif user_input_time_unit == 7:
            print(f"{user_input_time_unit} second = {Time_Unit_Converter.second_to_year()}")   
        
        elif user_input_time_unit == 8:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_minute()}")   
        elif user_input_time_unit == 9:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_second()}")   
        elif user_input_time_unit == 10:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_hour()}")   
        elif user_input_time_unit == 11:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_day()}")   
        elif user_input_time_unit == 12:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_week()}")   
        elif user_input_time_unit == 13:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_month()}")   
        elif user_input_time_unit == 14:
            print(f"{user_input_time_unit} minute = {Time_Unit_Converter.minute_to_year()}")   
        
        elif user_input_time_unit == 15:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_hour()}")   
        elif user_input_time_unit == 16:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_second()}")   
        elif user_input_time_unit == 17:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_minute()}")   
        elif user_input_time_unit == 18:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_day()}")   
        elif user_input_time_unit == 19:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_week()}")   
        elif user_input_time_unit == 20:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_month()}")   
        elif user_input_time_unit == 21:
            print(f"{user_input_time_unit} hour = {Time_Unit_Converter.hour_to_year()}")   
        
        elif user_input_time_unit == 22:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_day()}")   
        elif user_input_time_unit == 23:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_second()}")   
        elif user_input_time_unit == 24:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_minute()}")   
        elif user_input_time_unit == 25:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_hour()}")   
        elif user_input_time_unit == 26:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_week()}")   
        elif user_input_time_unit == 27:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_month()}")   
        elif user_input_time_unit == 28:
            print(f"{user_input_time_unit} day = {Time_Unit_Converter.day_to_year()}")   
        
        elif user_input_time_unit == 29:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_week()}")   
        elif user_input_time_unit == 30:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_second()}")   
        elif user_input_time_unit == 31:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_minute()}")   
        elif user_input_time_unit == 32:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_hour()}")   
        elif user_input_time_unit == 33:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_day()}")   
        elif user_input_time_unit == 34:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_month()}")   
        elif user_input_time_unit == 35:
            print(f"{user_input_time_unit} week = {Time_Unit_Converter.week_to_year()}")   
        
        elif user_input_time_unit == 36:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_month()}")   
        elif user_input_time_unit == 37:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_second()}")   
        elif user_input_time_unit == 38:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_minute()}")   
        elif user_input_time_unit == 39:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_hour()}")   
        elif user_input_time_unit == 40:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_day()}")   
        elif user_input_time_unit == 41:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_week()}")   
        elif user_input_time_unit == 42:
            print(f"{user_input_time_unit} month = {Time_Unit_Converter.month_to_year()}")   
        
        elif user_input_time_unit == 43:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_year()}")   
        elif user_input_time_unit == 44:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_second()}")   
        elif user_input_time_unit == 45:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_minute()}")   
        elif user_input_time_unit == 46:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_hour()}")   
        elif user_input_time_unit == 47:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_day()}")   
        elif user_input_time_unit == 48:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_week()}")   
        elif user_input_time_unit == 49:
            print(f"{user_input_time_unit} year = {Time_Unit_Converter.year_to_month()}")   
        
        else:
            print("Enter Right NUMBER from 1 to 49, PLEASE...")
                
    else:
        print("Enter Right NUMBER from 1 to 7, PLEASE...")
    
    user_continue_app_input = int(input(f"\nDo you want Continue or Not? 1) Yes 2) No : "))
    if user_continue_app_input == 1:
        user_input()
    


user_input()
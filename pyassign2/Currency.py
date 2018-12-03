#!/usr/bin/env python3

"""Currency.py: Currency exchange calculator.

__author__ = "ZhuQi"
__pkuid__  = "1800011808"
__email__  = "1800011808@pku.edu.cn"
"""

from urllib.request import urlopen


Clist=[
    'AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG',
    'AZN','BAM','BBD','BDT','BGN','BHD','BIF','BMD','BND',
    'BOB','BRL','BSD','BTC','BTN','BWP','BYR','BZD','CAD',
    'CDF','CHF','CLF','CLP','CNY','COP','CRC','CUC','CUP',
    'CVE','CZK','DJF','DKK','DOP','DZD','EEK','EGP','ERN',
    'ETB','EUR','FJD','FKP','GBP','GEL','GGP','GHS','GIP',
    'GMD','GNF','GTQ','GYD','HKD','HNL','HRK','HTG','HUF',
    'IDR','ILS','IMP','INR','IQD','IRR','ISK','JEP','JMD',
    'JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD',
    'KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL',
    'LYD','MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRO',
    'MTL','MUR','MVR','MWK','MXN','MYR','MZN','NAD','NGN',
    'NIO','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP',
    'PKR','PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR',
    'SBD','SCR','SDG','SEK','SGD','SHP','SLL','SOS','SRD',
    'STD','SVC','SYP','SZL','THB','TJS','TMT','TND','TOP',
    'TRY','TTD','TWD','TZS','UAH','UGX','USD','UYU','UZS',
    'VEF','VND','VUV','WST','XAF','XAG','XAU','XCD','XDR',
    'XOF','XPD','XPF','XPT','YER','ZAR','ZMK','ZMW','ZWL'
    ]

CAlist=[
    'United Arab Emirates Dirham','Afghan Afghani','Albanian Lek','Armenian Dram',
    'Netherlands Antillean Guilder','Angolan Kwanza','Argentine Peso','Australian Dollar',
    'Aruban Florin','Azerbaijani Manat','Bosnia-Herzegovina Convertible Mark','Barbadian Dollar',
    'Bangladeshi Taka','Bulgarian Lev','Bahraini Dinar','Burundian Franc','Bermudan Dollar',
    'Brunei Dollar','Bolivian Boliviano','Brazilian Real','Bahamian Dollar','Bitcoin',
    'Bhutanese Ngultrum','Botswanan Pula','Belarusian Ruble','Belize Dollar','Canadian Dollar',
    'Congolese Franc','Swiss Franc','Chilean Unidad de Fomento','Chilean Peso','Chinese Yuan',
    'Colombian Peso','Costa Rican Colón','Cuban Convertible Peso','Cuban Peso','Cape Verdean Escudo',
    'Czech Republic Koruna','Djiboutian Franc','Danish Krone','Dominican Peso','Algerian Dinar',
    'Estonian Kroon','Egyptian Pound','Eritrean Nakfa','Ethiopian Birr','Euro','Fijian Dollar',
    'Falkland Islands Pound','British Pound Sterling','Georgian Lari','Guernsey Pound',
    'Ghanaian Cedi','Gibraltar Pound','Gambian Dalasi','Guinean Franc','Guatemalan Quetzal',
    'Guyanaese Dollar','Hong Kong Dollar','Honduran Lempira','Croatian Kuna','Haitian Gourde',
    'Hungarian Forint','Indonesian Rupiah','Israeli New Sheqel','Manx pound','Indian Rupee',
    'Iraqi Dinar','Iranian Rial','Icelandic Króna','Jersey Pound','Jamaican Dollar',
    'Jordanian Dinar','Japanese Yen','Kenyan Shilling','Kyrgystani Som','Cambodian Riel',
    'Comorian Franc','North Korean Won','South Korean Won','Kuwaiti Dinar','Cayman Islands Dollar',
    'Kazakhstani Tenge','Laotian Kip','Lebanese Pound','Sri Lankan Rupee','Liberian Dollar',
    'Lesotho Loti','Lithuanian Litas','Latvian Lats','Libyan Dinar','Moroccan Dirham',
    'Moldovan Leu','Malagasy Ariary','Macedonian Denar','Myanma Kyat','Mongolian Tugrik',
    'Macanese Pataca','Mauritanian Ouguiya','Maltese Lira','Mauritian Rupee','Maldivian Rufiyaa',
    'Malawian Kwacha','Mexican Peso','Malaysian Ringgit','Mozambican Metical','Namibian Dollar',
    'Nigerian Naira','Nicaraguan Córdoba','Norwegian Krone','Nepalese Rupee','New Zealand Dollar',
    'Omani Rial','Panamanian Balboa','Peruvian Nuevo Sol','Papua New Guinean Kina',
    'Philippine Peso','Pakistani Rupee','Polish Złoty','Paraguayan Guarani','Qatari Rial',
    'Romanian Leu','Serbian Dinar','Russian Ruble','Rwandan Franc','Saudi Riyal','Solomon Islands Dollar',
    'Seychellois Rupee','Sudanese Pound','Swedish Krona','Singapore Dollar','Saint Helena Pound',
    'Sierra Leonean Leone','Somali Shilling','Surinamese Dollar','São Tomé and Príncipe Dobra',
    'Salvadoran Colón','Syrian Pound','Swazi Lilangeni','Thai Baht','Tajikistani Somoni',
    'Turkmenistani Manat','Tunisian Dinar',"Tongan Pa'anga",'Turkish Lira','Trinidad and Tobago Dollar',
    'New Taiwan Dollar','Tanzanian Shilling','Ukrainian Hryvnia','Ugandan Shilling',
    'United States Dollar','Uruguayan Peso','Uzbekistan Som','Venezuelan Bolívar Fuerte',
    'Vietnamese Dong','Vanuatu Vatu','Samoan Tala','CFA Franc (BEAC)','Troy Ounce of Silver',
    'Troy Ounce of Gold','East Caribbean Dollar','Special Drawing Rights','CFA Franc (BCEAO)',
    'Troy Ounce of Palladium','CFP Franc','Troy Ounce of Platinum','Yemeni Rial','South African Rand',
    'Zambian Kwacha (pre-2013)','Zambian Kwacha','Zimbabwean Dollar',
    ]


def test(func,expt):
    """
    Function 'test' is responsible for testing a function name 'func', whose estimated output is 'expt'
    """
    assert(func==expt)


def inputnprocess():
    """
    Function 'inputnprocess' is responsible for getting information from the user and judge whether it's legal or not.
        'legal': 'Currency From' and 'Current To' should in the 'Clist' and 'Amount of Current From' should only contain numbers and one '.'.
    Returning 'Current From', 'Current To' and 'Amount From', in type 'list'.
    """
    AfrT = 0
    Ndot = 0
    while 1:
        Cfr = input('Please input the currency you wish to exchange from in the 3-characters form:  ').upper()
        if Cfr not in Clist:
            print('Wrong input!')
            continue
        Cto = input('Please input the currency you wish to exchange to in the 3-characters form:  ').upper()
        if Cto not in Clist:
            print('Wrong input!')
            continue
        Afr = input('Please input the amount you wish to exchange:  ')
        for i in range(len(Afr)):
            if (ord(Afr[i:i + 1]) > 57 or ord(Afr[i:i + 1]) < 48) and ord(Afr[i:i + 1]) != 46:
                print('Wrong input!')
                AfrT = AfrT+1
                break
            if ord(Afr[i:i + 1]) == 46:
                Ndot = Ndot + 1
        if Ndot >= 2:
            print('Wrong input!')
            AfrT = AfrT + 1
        break
    if AfrT == 0:
        return Cfr,Cto,Afr
    else:
        inputnprocess()


def exchange(Cfr, Cto, Afr):
    """
    Function 'exchange' is responsible for communicating with the server and grab the result from it.
    Returning the raw result in type string.
    """
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + Cfr + '&to=' + Cto + '&amt=' + Afr)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def check(inp):
    li = inp.split('"')
    if 'true' in inp:
        return inp
    else:
        return 'error'


def convert(inp):
    """
    Function 'convert' is responsible for turning the raw returned data to 'Amount To'.
    Returning 'Amount To' in type 'string'
    """
    if inp == 'error':
        inputnprocess()
    else:
        li = inp.split('"')
        raw = str(li[7])
        Ato = ''
        for i in range(len(raw)):
            if ord(raw[i:i + 1]) == 46 or 48 <= ord(raw[i:i + 1]) <= 57:
                Ato = Ato + raw[i:i + 1]
        return Ato


def main():
    """
    Function 'Main' is responsible for interacting with user.
    """
    print('Welcome to the currency converter!')
    while 1:
        print()
        print('If you want to use the currency convert function, please input "exch".')
        print('If you want to know the abbreviation of currencies, please input "abbr".')
        print('If you want to test this converter, please input "test".')
        print('If you want to exit, please input "exit".')
        print()
        inp = input().lower()
        if inp == 'exit':
            break
        elif inp == 'abbr':
            for i in range(len(Clist)):
                print(Clist[i],CAlist[i])
        elif inp == 'test':
            test(convert('"from" : "3 United States Dollars", "to" : "20.5563 Chinese Yuan", "success" : true, "error" : ""'),'20.5563')
            test(exchange('USD', 'USD', '1'),'{ "from" : "1 United States Dollar", "to" : "1 United States Dollar", "success" : true, "error" : "" }')
            test(check('"from" : "3 United States Dollars", "to" : "20.5563 Chinese Yuan", "success" : true, "error" : ""'),'"from" : "3 United States Dollars", "to" : "20.5563 Chinese Yuan", "success" : true, "error" : ""')
            test(check(' "from" : "", "to" : "", "success" : false, "error" : "Quote for currency EEK not present." '),'error')
            print('All test passed!')
        elif inp == 'exch':
            x, y, z = inputnprocess()
            string = exchange(x, y, z)
            string1 = check(string)
            stringli = string.split('"')
            if string1 == 'error':
                print()
                print('Error!')
                print(stringli[13])
            else:
                result = convert(string1)
                print(result)
                print('Done!')
        else:
            print('Wrong input!')


if __name__=='__main__':
    main()
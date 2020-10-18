import MySQLdb
import json
import datetime
from nested_lookup import nested_lookup
import collections
import yaml
global reqq
import xlrd

def Mulesoft():

    ##################### Declarations ############################

    global suc, success, msg, mydb, cursor
    yml = []
    cnt1 = 0
    event = []
    lijs = []
    flag = 'event'
    cnt = 0
    lis = []
    lis1 = []
    ob = []
    ob1 = []
    li = []
    li1 = []
    li2 = []

    ##################### Yaml file loading ############################

    with open('gidp.yml') as file:
        cfg = yaml.full_load(file)
        yml.append(cfg)
        first = [sub['Mulesoft']['RequestField'] for sub in yml]
        second = [sub['Mulesoft']['ResponseField'] for sub in yml]
        cols = [sub['Mulesoft']['Columns'] for sub in yml]

    ##################### Database Connections ############################

    try:
        mydb = MySQLdb.connect(user=cfg['mysql']['user'], password=cfg['mysql']['password'], host=cfg['mysql']['host'],
                               database=cfg['mysql']['database'])
        cursor = mydb.cursor()
    except:

        print("Wrong database details. Please check the username and password")

    now = datetime.datetime.now()
    filename = 'GIDP/InputFiles/Req-Res.log'

    with open(filename) as f:
        content = f.readlines()

    ################  Extraction of json content from logs ####################

    for con in content:
        if flag == 'json' and not con.startswith('[' + str(now.year)):
            js.append(con)
        if flag == 'json' and con.startswith('[' + str(now.year)):
            jsjoin = ''.join(js)
            lijs.append(jsjoin)
            flag = 'eve'
        if 'event:' in con and (flag == 'eve' or flag == 'event'):
            flag = 'event'
            cont = con.split("event:", 1)[1]
            chk = cont.split(' ', 1)
            event.append(cont)
            if '{' not in chk[1]:
                cnt1 = cnt1 + 1
            else:
                flag = 'json'
                js = []
                js.append(chk[1])

    pairs = collections.defaultdict(list)
    req = [y for x, y in enumerate(lijs) if x % 2 == 0]
    resp = [y for x, y in enumerate(lijs) if x % 2 != 0]

    ############# Extracting columns from and inserting  to database #################

    for sec in second:
        for each in resp:
            each = json.loads(each)
            lis1.append(each)
            obj = json.dumps(each, indent=1)
            ob1.append(obj)
            suc = (nested_lookup(sec[0], each))
            success = (nested_lookup(sec[1], each))
            msg = (nested_lookup(sec[2], each))
            res1 = []
            if msg == res1:
                msg.insert(0, '-')
            if suc == res1:
                suc.insert(0, '-')
            if success == res1:
                success.insert(0, '-')
            li.append(success[0])
            li1.append(suc[0])
            li2.append(msg[0])

    for each in req:
        each = json.loads(each)
        obj1 = json.dumps(each, indent=1)
        ob.append(obj1)

    for fir, col in zip(first, cols):
        for each, a, b, c, d, e in zip(req, li1, li, li2, ob, ob1):
            each = json.loads(each)
            lis.append(each)
            cors = (nested_lookup(fir[0], each))
            pid = (nested_lookup(fir[1], each))
            ens = (nested_lookup(fir[2], each))
            sns = (nested_lookup(fir[3], each))
            clid = (nested_lookup(fir[4], each))
            date = (nested_lookup(fir[5], each))
            res1 = []
            if cors == res1:
                cors.insert(0, '-')
            if pid == res1:
                pid.insert(0, '-')
            if sns == res1:
                sns.insert(0, '-')
            if ens == res1:
                ens.insert(0, '-')
            if date == res1:
                date.insert(0, '-')
            if clid == res1:
                clid.insert(0, '-')

            cu = """INSERT INTO"""+ cfg['Tablenames']['Mulesoft'] + """(""" + col[0] + """,""" + col[1] + """,""" + col[2] + """,""" + col[3] + """,""" +  col[4] + """)VALUES(%s,%s,%s,%s,%s)"""
            da = (cors[0], ens[0], date[0], str(d), str(e),)
            cursor.execute(cu, da)
            mydb.commit()



def Salesforce():


    ##################### Declarations ############################

    global mydb, cursor
    cnt = 0
    lis = []
    cid = []
    date = []
    id = []

    ################  Extraction of json content from file ####################

    book = xlrd.open_workbook("GIDP/InputFiles/transaction log export.xlsx")
    sheet = book.sheet_by_index(0)

    for cell1 in sheet.col(0):
        new = cell1.value
        cid.append(new)
    for cell in sheet.col(1):
        res = cell.value
        lis.append(res)
    for cell2 in sheet.col(2):
        da = cell2.value
        date.append(da)
    for cell3 in sheet.col(3):
        da1 = cell3.value
        id.append(da1)

    ##################### Yaml file loading ############################

    with open('gidp.yml') as file:
        cfg = yaml.full_load(file)
        yml = []
        yml.append(cfg)
        first = [sub['sfdc']['Fields'] for sub in yml]
        cols = [sub['sfdc']['Columns'] for sub in yml]
        print(first)


    ##################### Database Connections ############################

    try:
        mydb = MySQLdb.connect(user=cfg['mysql']['user'], password=cfg['mysql']['password'],
                               host=cfg['mysql']['host'], database=cfg['mysql']['database'])
        cursor = mydb.cursor()
    except:
        print("Wrong database details. Please check the username and password")



    ############# Extracting columns from and inserting  to database #################

    for col in cols:
        for (a, each, c, d) in zip(cid, lis, date, id):
            res = json.loads(each)
            for e in first:
                if "ExtractPolicyRelationshipTypes" in res:
                    cors = (nested_lookup(e[0], res))
                    pid = (nested_lookup(e[1], res))
                    sns = (nested_lookup(e[2], res))
                    ens = (nested_lookup(e[3], res))
                    msg = (nested_lookup(e[4], res))
                    clid = (nested_lookup(e[5], res))
                    success = (nested_lookup(e[6], res))
                    obj = json.dumps(res, indent=1)
                    print(obj)
                    res1 = []
                    if cors == res1:
                        cors.insert(0, '-')
                    if pid == res1:
                        pid.insert(0, '-')
                    if sns == res1:
                        sns.insert(0, '-')
                    if ens == res1:
                        ens.insert(0, '-')
                    if msg == res1:
                        msg.insert(0, '-')
                    if clid == res1:
                        clid.insert(0, '-')
                    if success == res1:
                        success.insert(0, '-')
                    if obj == res1:
                        obj.insert(0, '-')

                    cu = """INSERT INTO""" + cfg['Tablenames']['Salesforce'] +"""(""" + col[0] + """,""" + col[1] + """,""" + col[2] + """,""" + col[3] + """)VALUES(%s,%s,%s,%s)"""
                    print(cu)
                    da = (cors[0], ens[0], c, obj,)
                    cursor.execute(cu, da)
                    mydb.commit()
                    print("bye1")


                else:
                    cors = (nested_lookup(e[0], res))
                    pid = (nested_lookup(e[1], res))
                    sns = (nested_lookup(e[2], res))
                    ens = (nested_lookup(e[3], res))
                    msg = (nested_lookup(e[4], res))
                    clid = (nested_lookup(e[5], res))
                    success = (nested_lookup(e[6], res))
                    obj = json.dumps(res, indent=1)

                    res1 = []
                    if cors == res1:
                        cors.insert(0, '-')
                    if pid == res1:
                        pid.insert(0, '-')
                    if sns == res1:
                        sns.insert(0, '-')
                    if ens == res1:
                        ens.insert(0, '-')
                    if msg == res1:
                        msg.insert(0, '-')
                    if clid == res1:
                        clid.insert(0, '-')
                    if success == res1:
                        success.insert(0, '-')
                    if obj == res1:
                        obj.insert(0, '-')

                    cu = """INSERT INTO """ + cfg['Tablenames']['Salesforce'] +"""(""" + col[0] + """,""" + col[1] + """,""" + col[2] + """,""" + col[3] + """)VALUES(%s,%s,%s,%s)"""
                    da = (cors[0], ens[0], c, obj,)
                    cursor.execute(cu, da)
                    mydb.commit()













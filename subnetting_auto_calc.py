#!/usr/bin/env python3

def ip2lst(ip_address_with_CIDR):
    b = ip_address_with_CIDR.split(".")
    c = ip_address_with_CIDR.split("/")
    d = b[3].split("/")
    ip = [b[0], b[1], b[2], d[0]]
    cidr = [c[1]]
    return ip, cidr

def smask(cidr):
    smdict1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    smdict0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f = int(cidr[0])
    g = 32 - f
    df = smdict1[:f]
    hg = smdict0[:g]
    bsm = df + hg
    return bsm

def spb2d(bin_lst):
    a = str(bin_lst)
    b1 = a[1]+a[4]+a[7]+a[10]+a[13]+a[16]+a[19]+a[22]
    b2 = a[25]+a[28]+a[31]+a[34]+a[37]+a[40]+a[43]+a[46]
    b3 = a[49]+a[52]+a[55]+a[58]+a[61]+a[64]+a[67]+a[70]
    b4 = a[73]+a[76]+a[79]+a[82]+a[85]+a[88]+a[91]+a[94]
    bmas = b1+b2+b3+b4
    return bmas

def b2d(op):
    # op = input("enter the binary value: ")
    op_lst = []
    for b in op:
        op_lst.append(b)
        b = int(b)
    hgf = len(op_lst)
    if hgf < 8:
        print("you entered less than 8 bit")
    else:
        a = [int(op_lst[0]), int(op_lst[1]), int(op_lst[2]), int(op_lst[3]), int(op_lst[4]), int(op_lst[5]),
             int(op_lst[6]),
             int(op_lst[7])]
        xc = len(op_lst)
        if xc == 8:

            mp_lst = [128, 64, 32, 16, 8, 4, 2, 1]
            sc = []
            if a[0] == 1:
                sc.append(mp_lst[0])
            if a[1] == 1:
                sc.append(mp_lst[1])
            if a[2] == 1:
                sc.append(mp_lst[2])
            if a[3] == 1:
                sc.append(mp_lst[3])
            if a[4] == 1:
                sc.append(mp_lst[4])
            if a[5] == 1:
                sc.append(mp_lst[5])
            if a[6] == 1:
                sc.append(mp_lst[6])
            if a[7] == 1:
                sc.append(mp_lst[7])
            ds = sum(sc)
            return ds
        else:
            print("you entered more than 8 bit")

def classckc(ip):
    a = ip
    b = a.split("/")
    d = b[0]
    c = d.split(".")
    e = int(c[0])
    if e in range(1,126):
        return "A"
    if e in range(128,191):
        return "B"
    if e in range(192,223):
        return "C"
    if e in range(224,239):
        return "D"
    if e in range(240,254):
        return "E"

def ccksubnet(clss, binary_value):
    if clss == "A":
        ds = binary_value[8:32]
        fg = []
        for gh in ds:
            fg.append(gh)
        fg1 = fg.count("1")
        fg2sm = 2 ** fg1
        fgk = fg.count("0")
        fgk1 = 2 ** fgk - 2
        host = fgk1
        subnet = fg2sm
        return subnet, host

    if clss == "B":
        gg11 = binary_value[16:32]
        fg11 = []
        for gh11 in gg11:
            fg11.append(gh11)
        fg12 = fg11.count("1")
        fg2sm11 = 2**fg12
        fgk = fg11.count("0")
        fgk12 = 2**fgk -2
        host = fgk12
        subnet = fg2sm11
        return subnet, host

    if clss == "C":
        yh55 = binary_value[24:32]
        fg55 = []
        for gh5 in yh55:
            fg55.append(gh5)
        fg155 = fg55.count("1")
        fg2sm55 = 2 ** fg155
        fgk44 = fg55.count("0")
        fgk144 = 2 ** fgk44 - 2
        host = fgk144
        subnet = fg2sm55
        return subnet, host

def d2b32(ip2):
    ip = ip2.split("/")
    ip = str(ip)
    ip1 = ip.split(".")
    sd1 = int(ip1[0])
    sd2 = int(ip1[1])
    sd3 = int(ip1[2])
    sd4 = int(ip1[3])
    print(f'{sd1:08b}', f'{sd2:08b}', f'{sd3:08b}', f'{sd4:08b}')

def onetwo(a):
    b = a.split("///")
    c = b[1]
    ip = str(c)
    ip1 = ip.split(".")
    sd1 = int(ip1[0])
    sd2 = int(ip1[1])
    sd3 = int(ip1[2])
    sd4 = int(ip1[3])
    ggh = f'{sd1:08b}', f'{sd2:08b}', f'{sd3:08b}', f'{sd4:08b}'
    hj = []
    for dc in ggh[0]:
        hj.append(dc)
    for dc in ggh[1]:
        hj.append(dc)
    for dc in ggh[2]:
        hj.append(dc)
    for dc in ggh[3]:
        hj.append(dc)
    return hj

def netid(a, clss):
    b = a.split("/")
    c = b[0]
    ip = str(c)
    ip1 = ip.split(".")
    sd1 = int(ip1[0])
    sd2 = int(ip1[1])
    sd3 = int(ip1[2])
    sd4 = int(ip1[3])
    ggh = f'{sd1:08b}', f'{sd2:08b}', f'{sd3:08b}', f'{sd4:08b}'
    hj = []
    for dc in ggh[0]:
        hj.append(dc)
    for dc in ggh[1]:
        hj.append(dc)
    for dc in ggh[2]:
        hj.append(dc)
    for dc in ggh[3]:
        hj.append(dc)
    one = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
    zero = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    if clss == "A":
        hj1 = hj[0:8]
        hj2 = hj1+zero
        hj3 = hj1+one
        bcast = hj3[0:32]
        nwid = hj2[0:32]
        return nwid,bcast
    if clss == "B":
        hj1 = hj[0:16]
        hj2 = hj1 + zero
        hj3 = hj1 + one
        bcast = hj3[0:32]
        nwid = hj2[0:32]
        return nwid, bcast
    if clss == "C":
        hj1 = hj[0:24]
        hj2 = hj1 + zero
        hj3 = hj1 + one
        bcast = hj3[0:32]
        nwid = hj2[0:32]
        return nwid,bcast


print('CIDR notation eg: 192.168.42.129/24\n\t\t\t(or)\nSM notation eg: 192.168.42.129///255.255.255.255\n')
io = str(input('IP address : '))
lenght = len(io)
if lenght <= 18:
    print("IP address :",io)
    a = ip2lst(io)
    b = smask(a[1])
    c = spb2d(b)
    f = classckc(io)
    i = ccksubnet(f, c)
    a55 = netid(io, f)
    nid = "network ID :{0}.{1}.{2}.{3}".format(b2d(a55[0][:8]), b2d(a55[0][8:16]), b2d(a55[0][16:24]),
                                               b2d(a55[0][24:32]))
    bid = "broadcast ID :{0}.{1}.{2}.{3}".format(b2d(a55[1][:8]), b2d(a55[1][8:16]), b2d(a55[1][16:24]),
                                                 b2d(a55[1][24:32]))
    g = "class {0}".format(f)
    d = "subnet mask: {}.{}.{}.{}".format(b2d(c[:8]), b2d(c[8:16]), b2d(c[16:24]), b2d(c[24:32]))
    # e = "binary value is: {}  {}  {}  {}".format(c[:8],c[8:16],c[16:24],c[24:32])
    calc = "total subnet is: {0}\nhost in a subnet: {1}".format(i[0], i[1])
    print(g)
    print(d)
    print(nid)
    print(bid)
    print(calc)

if lenght > 20:
    lll = io.split("///")
    print("IP address: ",lll[0])
    print("subnet mask :",lll[1])
    aaa = classckc(io)
    aa1 = "class {0}".format(aaa)
    a22 = onetwo(io)
    a44 = ccksubnet(aaa, a22)
    a55 = netid(io, aaa)
    nid = "network ID :{0}.{1}.{2}.{3}".format(b2d(a55[0][:8]), b2d(a55[0][8:16]), b2d(a55[0][16:24]), b2d(a55[0][24:32]))
    bid = "broadcast ID :{0}.{1}.{2}.{3}".format(b2d(a55[1][:8]), b2d(a55[1][8:16]), b2d(a55[1][16:24]), b2d(a55[1][24:32]))
    calc1 = "total subnet is: {0}\nhost in a subnet: {1}".format(a44[0], a44[1])
    print(aa1)
    print(nid)
    print(bid)
    print(calc1)

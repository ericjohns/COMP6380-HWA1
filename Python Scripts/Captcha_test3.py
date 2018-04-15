from PIL import Image, ImageChops
import pandas as pd
import numpy as np 
import operator
import csv
from random import shuffle
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import time
import warnings
import array

warnings.filterwarnings("ignore")

point_table = ([0] + ([255] * 255))

def compare(a, b):
    #a = a.convert('1')
    #a = ImageChops.invert(a)
    #b = b.convert('1')
    #b = ImageChops.invert(b)
    diff = ImageChops.darker(a, b)
    #diff = diff.convert('L')
    new = ImageChops.invert(diff)
    #new = diff.point(point_table)
    #new = diff.convert('RGB')
    #new.paste(b, mask=diff)
    #new = ImageChops.invert(diff)
    return diff

    
a0 = Image.open('captchadata/a0.jpg')
a0 = a0.convert('1')
A0 = list(a0.getdata())
a1 = Image.open('captchadata/a1.jpg')
a1 = a1.convert('1')
A1 = list(a1.getdata())
a2 = Image.open('captchadata/a2.jpg')
a2 = a2.convert('1')
A2 = list(a2.getdata())
a3 = Image.open('captchadata/a3.jpg')
a3 = a3.convert('1')
A3 = list(a3.getdata())
a4 = Image.open('captchadata/a4.jpg')
a4 = a4.convert('1')
A4 = list(a4.getdata())
a5 = Image.open('captchadata/a5.jpg')
a5 = a5.convert('1')
A5 = list(a5.getdata())
a6 = Image.open('captchadata/a6.jpg')
a6 = a6.convert('1')
A6 = list(a6.getdata())
a7 = Image.open('captchadata/a7.jpg')
a7 = a7.convert('1')
A7 = list(a7.getdata())
result1 =  compare(a0, a1)
AR1 = list(result1.getdata())
result2 =  compare(a2, a3)
AR2 = list(result2.getdata())
result3 =  compare(a4, a5)
AR3 = list(result3.getdata())
result4 =  compare(a6, a7)
AR4 = list(result4.getdata())
result7 =  compare(result1, result2)
result8 =  compare(result3, result4)
result_A =  compare(result7, result8)
#result_A.save('Result_A.png')
result_A=result_A.getdata()

b0 = Image.open('captchadata/b0.jpg')
b0 = b0.convert('1')
B0 = list(b0.getdata())
b1 = Image.open('captchadata/b1.jpg')
b1 = b1.convert('1')
B1 = list(b1.getdata())
b2 = Image.open('captchadata/b2.jpg')
b2 = b2.convert('1')
B2 = list(b2.getdata())
b3 = Image.open('captchadata/b3.jpg')
b3 = b3.convert('1')
B3 = list(b3.getdata())
b4 = Image.open('captchadata/b4.jpg')
b4 = b4.convert('1')
B4 = list(b4.getdata())
b5 = Image.open('captchadata/b5.jpg')
b5 = b5.convert('1')
B5 = list(b5.getdata())
b6 = Image.open('captchadata/b6.jpg')
b6 = b6.convert('1')
B6 = list(b6.getdata())
b7 = Image.open('captchadata/b7.jpg')
b7 = b7.convert('1')
B7 = list(b7.getdata())
b8 = Image.open('captchadata/b8.jpg')
b8 = b8.convert('1')
B8 = list(b8.getdata())
b9 = Image.open('captchadata/b9.jpg')
b9 = b9.convert('1')
B9 = list(b9.getdata())
b10 = Image.open('captchadata/b10.jpg')
b10 = b10.convert('1')
B10 = list(b10.getdata())
b11 = Image.open('captchadata/b11.jpg')
b11 = b11.convert('1')
B11 = list(b11.getdata())
result1 =  compare(b0, b1)
BR1 = list(result1.getdata())
result2 =  compare(b2, b3)
BR2 = list(result2.getdata())
result3 =  compare(b4, b5)
BR3 = list(result3.getdata())
result4 =  compare(b6, b7)
BR4 = list(result4.getdata())
result5 =  compare(b8, b9)
BR5 = list(result5.getdata())
result6 =  compare(b10, b11)
BR6 = list(result6.getdata())
result7 =  compare(result1, result2)
result8 =  compare(result3, result4)
result9 =  compare(result5, result6)
result10 =  compare(result7, result8)
result11 =  compare(result8, result9)
result_B =  compare(result10, result11)
#result_B.save('Result_B.png')
result_B=result_B.getdata()

   
c0 = Image.open('captchadata/c0.jpg')
c0 = c0.convert('1')
C0 = list(c0.getdata())
c1 = Image.open('captchadata/c1.jpg')
c1 = c1.convert('1')
C1 = list(c1.getdata())
c2 = Image.open('captchadata/c2.jpg')
c2 = c2.convert('1')
C2 = list(c2.getdata())
c3 = Image.open('captchadata/c3.jpg')
c3 = c3.convert('1')
C3 = list(c3.getdata())
c4 = Image.open('captchadata/c4.jpg')
c4 = c4.convert('1')
C4 = list(c4.getdata())
c5 = Image.open('captchadata/c5.jpg')
c5 = c5.convert('1')
C5 = list(c5.getdata())
c6 = Image.open('captchadata/c6.jpg')
c6 = c6.convert('1')
C6 = list(c6.getdata())
result1 =  compare(c0, c1)
CR1 = list(result1.getdata())
result2 =  compare(c2, c3)
CR2 = list(result2.getdata())
result3 =  compare(c4, c5)
CR3 = list(result3.getdata())
result4 =  compare(c5, c6)
CR4 = list(result4.getdata())
result7 =  compare(result1, result2)
result8 =  compare(result3, result4)
result_A =  compare(result7, result8)
#result_A.save('Result_A.png')
result_A=result_A.getdata()

   
d0 = Image.open('captchadata/d0.jpg')
d0 = d0.convert('1')
D0 = list(d0.getdata())
d1 = Image.open('captchadata/d1.jpg')
d1 = d1.convert('1')
D1 = list(d1.getdata())
d2 = Image.open('captchadata/d2.jpg')
d2 = d2.convert('1')
D2 = list(d2.getdata())
d3 = Image.open('captchadata/d3.jpg')
d3 = d3.convert('1')
D3 = list(d3.getdata())
result1 =  compare(d0, d1)
DR1 = list(result1.getdata())
result2 =  compare(d2, d3)
DR2 = list(result2.getdata())
result7 =  compare(result1, result2)
result8 =  compare(result3, result4)
result_A =  compare(result7, result8)
#result_A.save('Result_A.png')
result_A=result_A.getdata()

e0 = Image.open('captchadata/e0.jpg')
e0 = b0.convert('1')
E0 = list(e0.getdata())
e1 = Image.open('captchadata/e1.jpg')
e1 = b1.convert('1')
E1 = list(e1.getdata())
e2 = Image.open('captchadata/e2.jpg')
e2 = b2.convert('1')
E2 = list(e2.getdata())
e3 = Image.open('captchadata/e3.jpg')
e3 = b3.convert('1')
E3 = list(e3.getdata())
e4 = Image.open('captchadata/e4.jpg')
e4 = b4.convert('1')
E4 = list(e4.getdata())
e5 = Image.open('captchadata/e5.jpg')
e5 = b5.convert('1')
E5 = list(e5.getdata())
e6 = Image.open('captchadata/e6.jpg')
e6 = b6.convert('1')
E6 = list(e6.getdata())
e7 = Image.open('captchadata/e7.jpg')
e7 = b7.convert('1')
E7 = list(e7.getdata())
e8 = Image.open('captchadata/e8.jpg')
e8 = b8.convert('1')
E8 = list(e8.getdata())
e9 = Image.open('captchadata/e9.jpg')
e9 = b9.convert('1')
E9 = list(e9.getdata())
result1 =  compare(e0, e1)
ER1 = list(result1.getdata())
result2 =  compare(b2, e3)
ER2 = list(result2.getdata())
result3 =  compare(e4, e5)
ER3 = list(result3.getdata())
result4 =  compare(e6, e7)
ER4 = list(result4.getdata())

f0 = Image.open('captchadata/f0.jpg')
f0 = b0.convert('1')
F0 = list(f0.getdata())
f1 = Image.open('captchadata/f1.jpg')
f1 = b1.convert('1')
F1 = list(f1.getdata())
f2 = Image.open('captchadata/f2.jpg')
f2 = b2.convert('1')
F2 = list(f2.getdata())
f3 = Image.open('captchadata/f3.jpg')
f3 = b3.convert('1')
F3 = list(f3.getdata())
f4 = Image.open('captchadata/f4.jpg')
f4 = b4.convert('1')
F4 = list(f4.getdata())
result1 =  compare(f0, f1)
FR1 = list(result1.getdata())
result2 =  compare(f2, f3)
FR2 = list(result2.getdata())
result3 =  compare(e3, e4)
FR3 = list(result3.getdata())

f0 = Image.open('captchadata/g0.jpg')
f0 = b0.convert('1')
G0 = list(f0.getdata())
f1 = Image.open('captchadata/g1.jpg')
f1 = b1.convert('1')
G1 = list(f1.getdata())
f2 = Image.open('captchadata/g2.jpg')
f2 = b2.convert('1')
G2 = list(f2.getdata())
f3 = Image.open('captchadata/g3.jpg')
f3 = b3.convert('1')
G3 = list(f3.getdata())
f4 = Image.open('captchadata/g4.jpg')
f4 = b4.convert('1')
G4 = list(f4.getdata())
result1 =  compare(f0, f1)
GR1 = list(result1.getdata())
result2 =  compare(f2, f3)
GR2 = list(result2.getdata())
result3 =  compare(e3, e4)
GR3 = list(result3.getdata())

b0 = Image.open('captchadata/h0.jpg')
b0 = b0.convert('1')
H0 = list(b0.getdata())
b1 = Image.open('captchadata/h1.jpg')
b1 = b1.convert('1')
H1 = list(b1.getdata())
b2 = Image.open('captchadata/h2.jpg')
b2 = b2.convert('1')
H2 = list(b2.getdata())
b3 = Image.open('captchadata/h3.jpg')
b3 = b3.convert('1')
H3 = list(b3.getdata())
b4 = Image.open('captchadata/h4.jpg')
b4 = b4.convert('1')
H4 = list(b4.getdata())
b5 = Image.open('captchadata/h5.jpg')
b5 = b5.convert('1')
H5 = list(b5.getdata())
b6 = Image.open('captchadata/h6.jpg')
b6 = b6.convert('1')
H6 = list(b6.getdata())
b7 = Image.open('captchadata/h7.jpg')
b7 = b7.convert('1')
H7 = list(b7.getdata())
b8 = Image.open('captchadata/h8.jpg')
b8 = b8.convert('1')
H8 = list(b8.getdata())
b9 = Image.open('captchadata/h9.jpg')
b9 = b9.convert('1')
H9 = list(b9.getdata())
b10 = Image.open('captchadata/h10.jpg')
b10 = b10.convert('1')
H10 = list(b10.getdata())
b11 = Image.open('captchadata/h11.jpg')
b11 = b11.convert('1')
H11 = list(b11.getdata())
b12 = Image.open('captchadata/h12.jpg')
b12 = b12.convert('1')
H12 = list(b12.getdata())
b13 = Image.open('captchadata/h13.jpg')
b13 = b13.convert('1')
H13 = list(b13.getdata())
result1 =  compare(b0, b1)
HR1 = list(result1.getdata())
result2 =  compare(b2, b3)
HR2 = list(result2.getdata())
result3 =  compare(b4, b5)
HR3 = list(result3.getdata())
result4 =  compare(b6, b7)
HR4 = list(result4.getdata())
result5 =  compare(b8, b9)
HR5 = list(result5.getdata())
result6 =  compare(b10, b11)
HR6 = list(result6.getdata())
result7 =  compare(b12, b13)
HR7 = list(result7.getdata())

b0 = Image.open('captchadata/i0.jpg')
b0 = b0.convert('1')
I0 = list(b0.getdata())
b1 = Image.open('captchadata/i1.jpg')
b1 = b1.convert('1')
I1 = list(b1.getdata())
b2 = Image.open('captchadata/i2.jpg')
b2 = b2.convert('1')
I2 = list(b2.getdata())
b3 = Image.open('captchadata/i3.jpg')
b3 = b3.convert('1')
I3 = list(b3.getdata())
b4 = Image.open('captchadata/i4.jpg')
b4 = b4.convert('1')
I4 = list(b4.getdata())
b5 = Image.open('captchadata/i5.jpg')
b5 = b5.convert('1')
I5 = list(b5.getdata())
result1 =  compare(b0, b1)
IR1 = list(result1.getdata())
result2 =  compare(b2, b3)
IR2 = list(result2.getdata())
result3 =  compare(b4, b5)
IR3 = list(result3.getdata())

b0 = Image.open('captchadata/j0.jpg')
b0 = b0.convert('1')
J0 = list(b0.getdata())
b1 = Image.open('captchadata/j1.jpg')
b1 = b1.convert('1')
J1 = list(b1.getdata())
b2 = Image.open('captchadata/j2.jpg')
b2 = b2.convert('1')
J2 = list(b2.getdata())
b3 = Image.open('captchadata/j3.jpg')
b3 = b3.convert('1')
J3 = list(b3.getdata())
b4 = Image.open('captchadata/j4.jpg')
b4 = b4.convert('1')
J4 = list(b4.getdata())
b5 = Image.open('captchadata/j5.jpg')
b5 = b5.convert('1')
J5 = list(b5.getdata())
b6 = Image.open('captchadata/j6.jpg')
b6 = b6.convert('1')
J6 = list(b6.getdata())
b7 = Image.open('captchadata/j7.jpg')
b7 = b7.convert('1')
J7 = list(b7.getdata())
b8 = Image.open('captchadata/j8.jpg')
b8 = b8.convert('1')
J8 = list(b8.getdata())
b9 = Image.open('captchadata/j9.jpg')
b9 = b9.convert('1')
J9 = list(b9.getdata())
b10 = Image.open('captchadata/j10.jpg')
b10 = b10.convert('1')
J10 = list(b10.getdata())
b11 = Image.open('captchadata/j11.jpg')
b11 = b11.convert('1')
J11 = list(b11.getdata())
b12 = Image.open('captchadata/j12.jpg')
b12 = b12.convert('1')
J12 = list(b12.getdata())
result1 =  compare(b0, b1)
JR1 = list(result1.getdata())
result2 =  compare(b2, b3)
JR2 = list(result2.getdata())
result3 =  compare(b4, b5)
JR3 = list(result3.getdata())
result4 =  compare(b6, b7)
JR4 = list(result4.getdata())
result5 =  compare(b8, b9)
JR5 = list(result5.getdata())
result6 =  compare(b10, b11)
JR6 = list(result6.getdata())
result7 =  compare(b11, b12)
JR7 = list(result7.getdata())

b0 = Image.open('captchadata/k0.jpg')
b0 = b0.convert('1')
K0 = list(b0.getdata())
b1 = Image.open('captchadata/k1.jpg')
b1 = b1.convert('1')
K1 = list(b1.getdata())
b2 = Image.open('captchadata/k2.jpg')
b2 = b2.convert('1')
K2 = list(b2.getdata())
b3 = Image.open('captchadata/k3.jpg')
b3 = b3.convert('1')
K3 = list(b3.getdata())
b4 = Image.open('captchadata/k4.jpg')
b4 = b4.convert('1')
K4 = list(b4.getdata())
b5 = Image.open('captchadata/k5.jpg')
b5 = b5.convert('1')
K5 = list(b5.getdata())
b6 = Image.open('captchadata/k6.jpg')
b6 = b6.convert('1')
K6 = list(b6.getdata())
b7 = Image.open('captchadata/k7.jpg')
b7 = b7.convert('1')
K7 = list(b7.getdata())
b8 = Image.open('captchadata/k8.jpg')
b8 = b8.convert('1')
K8 = list(b8.getdata())
b9 = Image.open('captchadata/k9.jpg')
b9 = b9.convert('1')
K9 = list(b9.getdata())
b10 = Image.open('captchadata/k10.jpg')
b10 = b10.convert('1')
K10 = list(b10.getdata())
b11 = Image.open('captchadata/k11.jpg')
b11 = b11.convert('1')
K11 = list(b11.getdata())
b12 = Image.open('captchadata/k12.jpg')
b12 = b12.convert('1')
K12 = list(b12.getdata())
b13 = Image.open('captchadata/k13.jpg')
b13 = b13.convert('1')
K13 = list(b13.getdata())
b14 = Image.open('captchadata/k14.jpg')
b14 = b14.convert('1')
K14 = list(b14.getdata())
b15 = Image.open('captchadata/k15.jpg')
b15 = b15.convert('1')
K15 = list(b15.getdata())
b16 = Image.open('captchadata/k16.jpg')
b16 = b16.convert('1')
K16 = list(b16.getdata())
result1 =  compare(b0, b1)
KR1 = list(result1.getdata())
result2 =  compare(b2, b3)
KR2 = list(result2.getdata())
result3 =  compare(b4, b5)
KR3 = list(result3.getdata())
result4 =  compare(b6, b7)
KR4 = list(result4.getdata())
result5 =  compare(b8, b9)
KR5 = list(result5.getdata())
result6 =  compare(b10, b11)
KR6 = list(result6.getdata())
result7 =  compare(b12, b13)
KR7 = list(result7.getdata())
result8 =  compare(b14, b15)
KR8 = list(result6.getdata())
result9 =  compare(b15, b16)
KR9 = list(result7.getdata())

b0 = Image.open('captchadata/l0.jpg')
b0 = b0.convert('1')
L0 = list(b0.getdata())
b1 = Image.open('captchadata/l1.jpg')
b1 = b1.convert('1')
L1 = list(b1.getdata())
b2 = Image.open('captchadata/l2.jpg')
b2 = b2.convert('1')
L2 = list(b2.getdata())
b3 = Image.open('captchadata/l3.jpg')
b3 = b3.convert('1')
L3 = list(b3.getdata())
b4 = Image.open('captchadata/l4.jpg')
b4 = b4.convert('1')
L4 = list(b4.getdata())
b5 = Image.open('captchadata/l5.jpg')
b5 = b5.convert('1')
L5 = list(b5.getdata())
b6 = Image.open('captchadata/l6.jpg')
b6 = b6.convert('1')
L6 = list(b6.getdata())
b7 = Image.open('captchadata/l7.jpg')
b7 = b7.convert('1')
L7 = list(b7.getdata())
b8 = Image.open('captchadata/l8.jpg')
b8 = b8.convert('1')
L8 = list(b8.getdata())
b9 = Image.open('captchadata/l9.jpg')
b9 = b9.convert('1')
L9 = list(b9.getdata())
b10 = Image.open('captchadata/l10.jpg')
b10 = b10.convert('1')
L10 = list(b10.getdata())
b11 = Image.open('captchadata/l11.jpg')
b11 = b11.convert('1')
L11 = list(b11.getdata())
b12 = Image.open('captchadata/l12.jpg')
b12 = b12.convert('1')
L12 = list(b12.getdata())
b13 = Image.open('captchadata/l13.jpg')
b13 = b13.convert('1')
L13 = list(b13.getdata())
result1 =  compare(b0, b1)
LR1 = list(result1.getdata())
result2 =  compare(b2, b3)
LR2 = list(result2.getdata())
result3 =  compare(b4, b5)
LR3 = list(result3.getdata())
result4 =  compare(b6, b7)
LR4 = list(result4.getdata())
result5 =  compare(b8, b9)
LR5 = list(result5.getdata())
result6 =  compare(b10, b11)
LR6 = list(result6.getdata())
result7 =  compare(b12, b13)
LR7 = list(result7.getdata())

b0 = Image.open('captchadata/m0.jpg')
b0 = b0.convert('1')
M0 = list(b0.getdata())
b1 = Image.open('captchadata/m1.jpg')
b1 = b1.convert('1')
M1 = list(b1.getdata())
b2 = Image.open('captchadata/m2.jpg')
b2 = b2.convert('1')
M2 = list(b2.getdata())
b3 = Image.open('captchadata/m3.jpg')
b3 = b3.convert('1')
M3 = list(b3.getdata())
b4 = Image.open('captchadata/m4.jpg')
b4 = b4.convert('1')
M4 = list(b4.getdata())
b5 = Image.open('captchadata/m5.jpg')
b5 = b5.convert('1')
M5 = list(b5.getdata())
b6 = Image.open('captchadata/m6.jpg')
b6 = b6.convert('1')
M6 = list(b6.getdata())
b7 = Image.open('captchadata/m7.jpg')
b7 = b7.convert('1')
M7 = list(b7.getdata())
b8 = Image.open('captchadata/m8.jpg')
b8 = b8.convert('1')
M8 = list(b8.getdata())
b9 = Image.open('captchadata/m9.jpg')
b9 = b9.convert('1')
M9 = list(b9.getdata())
b10 = Image.open('captchadata/m10.jpg')
b10 = b10.convert('1')
M10 = list(b10.getdata())
result1 =  compare(b0, b1)
MR1 = list(result1.getdata())
result2 =  compare(b2, b3)
MR2 = list(result2.getdata())
result3 =  compare(b4, b5)
MR3 = list(result3.getdata())
result4 =  compare(b6, b7)
MR4 = list(result4.getdata())
result5 =  compare(b8, b9)
MR5 = list(result5.getdata())
result6 =  compare(b9, b10)
MR6 = list(result6.getdata())

b0 = Image.open('captchadata/m0.jpg')
b0 = b0.convert('1')
N0 = list(b0.getdata())
b1 = Image.open('captchadata/m1.jpg')
b1 = b1.convert('1')
N1 = list(b1.getdata())
b2 = Image.open('captchadata/m2.jpg')
b2 = b2.convert('1')
N2 = list(b2.getdata())
b3 = Image.open('captchadata/m3.jpg')
b3 = b3.convert('1')
N3 = list(b3.getdata())
result1 =  compare(b0, b1)
NR1 = list(result1.getdata())
result2 =  compare(b2, b3)
NR2 = list(result2.getdata())

b0 = Image.open('captchadata/o0.jpg')
b0 = b0.convert('1')
O0 = list(b0.getdata())
b1 = Image.open('captchadata/o1.jpg')
b1 = b1.convert('1')
O1 = list(b1.getdata())
b2 = Image.open('captchadata/o2.jpg')
b2 = b2.convert('1')
O2 = list(b2.getdata())
b3 = Image.open('captchadata/o3.jpg')
b3 = b3.convert('1')
O3 = list(b3.getdata())
b4 = Image.open('captchadata/o4.jpg')
b4 = b4.convert('1')
O4 = list(b4.getdata())
b5 = Image.open('captchadata/o5.jpg')
b5 = b5.convert('1')
O5 = list(b5.getdata())
b6 = Image.open('captchadata/o6.jpg')
b6 = b6.convert('1')
O6 = list(b6.getdata())
b7 = Image.open('captchadata/o7.jpg')
b7 = b7.convert('1')
O7 = list(b7.getdata())
b8 = Image.open('captchadata/o8.jpg')
b8 = b8.convert('1')
O8 = list(b8.getdata())
b9 = Image.open('captchadata/o9.jpg')
b9 = b9.convert('1')
O9 = list(b9.getdata())
b10 = Image.open('captchadata/o10.jpg')
b10 = b10.convert('1')
O10 = list(b10.getdata())
b11 = Image.open('captchadata/o11.jpg')
b11 = b11.convert('1')
O11 = list(b11.getdata())
result1 =  compare(b0, b1)
OR1 = list(result1.getdata())
result2 =  compare(b2, b3)
OR2 = list(result2.getdata())
result3 =  compare(b4, b5)
OR3 = list(result3.getdata())
result4 =  compare(b6, b7)
OR4 = list(result4.getdata())
result5 =  compare(b8, b9)
OR5 = list(result5.getdata())
result6 =  compare(b10, b11)
OR6 = list(result6.getdata())


b0 = Image.open('captchadata/p0.jpg')
b0 = b0.convert('1')
P0 = list(b0.getdata())
b1 = Image.open('captchadata/p1.jpg')
b1 = b1.convert('1')
P1 = list(b1.getdata())
b2 = Image.open('captchadata/p2.jpg')
b2 = b2.convert('1')
P2 = list(b2.getdata())
b3 = Image.open('captchadata/p3.jpg')
b3 = b3.convert('1')
P3 = list(b3.getdata())
b4 = Image.open('captchadata/p4.jpg')
b4 = b4.convert('1')
P4 = list(b4.getdata())
b5 = Image.open('captchadata/p5.jpg')
b5 = b5.convert('1')
P5 = list(b5.getdata())
b6 = Image.open('captchadata/p6.jpg')
b6 = b6.convert('1')
P6 = list(b6.getdata())
b7 = Image.open('captchadata/p7.jpg')
b7 = b7.convert('1')
P7 = list(b7.getdata())
b8 = Image.open('captchadata/p8.jpg')
b8 = b8.convert('1')
P8 = list(b8.getdata())
result1 =  compare(b0, b1)
PR1 = list(result1.getdata())
result2 =  compare(b2, b3)
PR2 = list(result2.getdata())
result3 =  compare(b4, b5)
PR3 = list(result3.getdata())
result4 =  compare(b6, b7)
PR4 = list(result4.getdata())
result5 =  compare(b7, b8)
PR5 = list(result5.getdata())


b0 = Image.open('captchadata/q0.jpg')
b0 = b0.convert('1')
Q0 = list(b0.getdata())
b1 = Image.open('captchadata/q1.jpg')
b1 = b1.convert('1')
Q1 = list(b1.getdata())
b2 = Image.open('captchadata/q2.jpg')
b2 = b2.convert('1')
Q2 = list(b2.getdata())
b3 = Image.open('captchadata/q3.jpg')
b3 = b3.convert('1')
Q3 = list(b3.getdata())
b4 = Image.open('captchadata/q4.jpg')
b4 = b4.convert('1')
Q4 = list(b4.getdata())
b5 = Image.open('captchadata/q5.jpg')
b5 = b5.convert('1')
Q5 = list(b5.getdata())
b6 = Image.open('captchadata/q6.jpg')
b6 = b6.convert('1')
Q6 = list(b6.getdata())
b7 = Image.open('captchadata/q7.jpg')
b7 = b7.convert('1')
Q7 = list(b7.getdata())
b8 = Image.open('captchadata/q8.jpg')
b8 = b8.convert('1')
Q8 = list(b8.getdata())
b9 = Image.open('captchadata/q9.jpg')
b9 = b9.convert('1')
Q9 = list(b9.getdata())
result1 =  compare(b0, b1)
QR1 = list(result1.getdata())
result2 =  compare(b2, b3)
QR2 = list(result2.getdata())
result3 =  compare(b4, b5)
QR3 = list(result3.getdata())
result4 =  compare(b6, b7)
QR4 = list(result4.getdata())
result5 =  compare(b8, b9)
QR5 = list(result5.getdata())

b0 = Image.open('captchadata/r0.jpg')
b0 = b0.convert('1')
R0 = list(b0.getdata())
b1 = Image.open('captchadata/r1.jpg')
b1 = b1.convert('1')
R1 = list(b1.getdata())
b2 = Image.open('captchadata/r2.jpg')
b2 = b2.convert('1')
R2 = list(b2.getdata())
b3 = Image.open('captchadata/r3.jpg')
b3 = b3.convert('1')
R3 = list(b3.getdata())
b4 = Image.open('captchadata/r4.jpg')
b4 = b4.convert('1')
R4 = list(b4.getdata())
b5 = Image.open('captchadata/r5.jpg')
b5 = b5.convert('1')
R5 = list(b5.getdata())
b6 = Image.open('captchadata/r6.jpg')
b6 = b6.convert('1')
R6 = list(b6.getdata())
b7 = Image.open('captchadata/r7.jpg')
b7 = b7.convert('1')
R7 = list(b7.getdata())
b8 = Image.open('captchadata/r8.jpg')
b8 = b8.convert('1')
R8 = list(b8.getdata())
b9 = Image.open('captchadata/r9.jpg')
b9 = b9.convert('1')
R9 = list(b9.getdata())
b10 = Image.open('captchadata/r10.jpg')
b10 = b10.convert('1')
R10 = list(b10.getdata())
b11 = Image.open('captchadata/r11.jpg')
b11 = b11.convert('1')
R11 = list(b11.getdata())
b12 = Image.open('captchadata/r12.jpg')
b12 = b12.convert('1')
R12 = list(b12.getdata())
b13 = Image.open('captchadata/r13.jpg')
b13 = b13.convert('1')
R13 = list(b13.getdata())
result1 =  compare(b0, b1)
RR1 = list(result1.getdata())
result2 =  compare(b2, b3)
RR2 = list(result2.getdata())
result3 =  compare(b4, b5)
RR3 = list(result3.getdata())
result4 =  compare(b6, b7)
RR4 = list(result4.getdata())
result5 =  compare(b8, b9)
RR5 = list(result5.getdata())
result6 =  compare(b10, b11)
RR6 = list(result6.getdata())
result7 =  compare(b12, b13)
RR7 = list(result7.getdata())

b0 = Image.open('captchadata/s0.jpg')
b0 = b0.convert('1')
S0 = list(b0.getdata())
b1 = Image.open('captchadata/s1.jpg')
b1 = b1.convert('1')
S1 = list(b1.getdata())
b2 = Image.open('captchadata/s2.jpg')
b2 = b2.convert('1')
S2 = list(b2.getdata())
b3 = Image.open('captchadata/s3.jpg')
b3 = b3.convert('1')
S3 = list(b3.getdata())
b4 = Image.open('captchadata/s4.jpg')
b4 = b4.convert('1')
S4 = list(b4.getdata())
b5 = Image.open('captchadata/s5.jpg')
b5 = b5.convert('1')
S5 = list(b5.getdata())
b6 = Image.open('captchadata/s6.jpg')
b6 = b6.convert('1')
S6 = list(b6.getdata())
b7 = Image.open('captchadata/s7.jpg')
b7 = b7.convert('1')
S7 = list(b7.getdata())
b8 = Image.open('captchadata/s8.jpg')
b8 = b8.convert('1')
S8 = list(b8.getdata())
result1 =  compare(b0, b1)
SR1 = list(result1.getdata())
result2 =  compare(b2, b3)
SR2 = list(result2.getdata())
result3 =  compare(b4, b5)
SR3 = list(result3.getdata())
result4 =  compare(b6, b7)
SR4 = list(result4.getdata())
result5 =  compare(b8, b9)
SR5 = list(result5.getdata())

b0 = Image.open('captchadata/t0.jpg')
b0 = b0.convert('1')
T0 = list(b0.getdata())
b1 = Image.open('captchadata/t1.jpg')
b1 = b1.convert('1')
T1 = list(b1.getdata())
b2 = Image.open('captchadata/t2.jpg')
b2 = b2.convert('1')
T2 = list(b2.getdata())
b3 = Image.open('captchadata/t3.jpg')
b3 = b3.convert('1')
T3 = list(b3.getdata())
b4 = Image.open('captchadata/t4.jpg')
b4 = b4.convert('1')
T4 = list(b4.getdata())
result1 =  compare(b0, b1)
TR1 = list(result1.getdata())
result2 =  compare(b2, b3)
TR2 = list(result2.getdata())
result3 =  compare(b3, b4)
TR3 = list(result3.getdata())


b0 = Image.open('captchadata/u0.jpg')
b0 = b0.convert('1')
U0 = list(b0.getdata())
b1 = Image.open('captchadata/u1.jpg')
b1 = b1.convert('1')
U1 = list(b1.getdata())
b2 = Image.open('captchadata/u2.jpg')
b2 = b2.convert('1')
U2 = list(b2.getdata())
b3 = Image.open('captchadata/u3.jpg')
b3 = b3.convert('1')
U3 = list(b3.getdata())
b4 = Image.open('captchadata/u4.jpg')
b4 = b4.convert('1')
U4 = list(b4.getdata())
b5 = Image.open('captchadata/u5.jpg')
b5 = b5.convert('1')
U5 = list(b5.getdata())
b6 = Image.open('captchadata/u6.jpg')
b6 = b6.convert('1')
U6 = list(b6.getdata())
b7 = Image.open('captchadata/u7.jpg')
b7 = b7.convert('1')
U7 = list(b7.getdata())
b8 = Image.open('captchadata/u8.jpg')
b8 = b8.convert('1')
U8 = list(b8.getdata())
b9 = Image.open('captchadata/u9.jpg')
b9 = b9.convert('1')
U9 = list(b9.getdata())
b10 = Image.open('captchadata/u10.jpg')
b10 = b10.convert('1')
U10 = list(b10.getdata())
b11 = Image.open('captchadata/u11.jpg')
b11 = b11.convert('1')
U11 = list(b11.getdata())
b12 = Image.open('captchadata/u12.jpg')
b12 = b12.convert('1')
U12 = list(b12.getdata())
result1 =  compare(b0, b1)
UR1 = list(result1.getdata())
result2 =  compare(b2, b3)
UR2 = list(result2.getdata())
result3 =  compare(b4, b5)
UR3 = list(result3.getdata())
result4 =  compare(b6, b7)
UR4 = list(result4.getdata())
result5 =  compare(b8, b9)
UR5 = list(result5.getdata())
result6 =  compare(b10, b11)
UR6 = list(result6.getdata())
result7 =  compare(b11, b12)
UR7 = list(result7.getdata())


b0 = Image.open('captchadata/v0.jpg')
b0 = b0.convert('1')
V0 = list(b0.getdata())
b1 = Image.open('captchadata/v1.jpg')
b1 = b1.convert('1')
V1 = list(b1.getdata())
b2 = Image.open('captchadata/v2.jpg')
b2 = b2.convert('1')
V2 = list(b2.getdata())
b3 = Image.open('captchadata/v3.jpg')
b3 = b3.convert('1')
V3 = list(b3.getdata())
b4 = Image.open('captchadata/v4.jpg')
b4 = b4.convert('1')
V4 = list(b4.getdata())
b5 = Image.open('captchadata/v5.jpg')
b5 = b5.convert('1')
V5 = list(b5.getdata())
b6 = Image.open('captchadata/v6.jpg')
b6 = b6.convert('1')
V6 = list(b6.getdata())
b7 = Image.open('captchadata/v7.jpg')
b7 = b7.convert('1')
V7 = list(b7.getdata())
b8 = Image.open('captchadata/v8.jpg')
b8 = b8.convert('1')
V8 = list(b8.getdata())
b9 = Image.open('captchadata/v9.jpg')
b9 = b9.convert('1')
V9 = list(b9.getdata())
b10 = Image.open('captchadata/v10.jpg')
b10 = b10.convert('1')
V10 = list(b10.getdata())
b11 = Image.open('captchadata/v11.jpg')
b11 = b11.convert('1')
V11 = list(b11.getdata())
b12 = Image.open('captchadata/v12.jpg')
b12 = b12.convert('1')
V12 = list(b12.getdata())
b13 = Image.open('captchadata/v13.jpg')
b13 = b13.convert('1')
V13 = list(b13.getdata())
b14 = Image.open('captchadata/v14.jpg')
b14 = b14.convert('1')
V14 = list(b14.getdata())
b15 = Image.open('captchadata/v15.jpg')
b15 = b15.convert('1')
V15 = list(b15.getdata())
result1 =  compare(b0, b1)
VR1 = list(result1.getdata())
result2 =  compare(b2, b3)
VR2 = list(result2.getdata())
result3 =  compare(b4, b5)
VR3 = list(result3.getdata())
result4 =  compare(b6, b7)
VR4 = list(result4.getdata())
result5 =  compare(b8, b9)
VR5 = list(result5.getdata())
result6 =  compare(b10, b11)
VR6 = list(result6.getdata())
result7 =  compare(b12, b13)
VR7 = list(result7.getdata())
result8 =  compare(b14, b15)
VR8 = list(result6.getdata())


b0 = Image.open('captchadata/w0.jpg')
b0 = b0.convert('1')
W0 = list(b0.getdata())
b1 = Image.open('captchadata/w1.jpg')
b1 = b1.convert('1')
W1 = list(b1.getdata())
b2 = Image.open('captchadata/w2.jpg')
b2 = b2.convert('1')
W2 = list(b2.getdata())
b3 = Image.open('captchadata/w3.jpg')
b3 = b3.convert('1')
W3 = list(b3.getdata())
b4 = Image.open('captchadata/w4.jpg')
b4 = b4.convert('1')
W4 = list(b4.getdata())
b5 = Image.open('captchadata/w5.jpg')
b5 = b5.convert('1')
W5 = list(b5.getdata())
b6 = Image.open('captchadata/w6.jpg')
b6 = b6.convert('1')
W6 = list(b6.getdata())
b7 = Image.open('captchadata/w7.jpg')
b7 = b7.convert('1')
W7 = list(b7.getdata())
b8 = Image.open('captchadata/w8.jpg')
b8 = b8.convert('1')
W8 = list(b8.getdata())
result1 =  compare(b0, b1)
WR1 = list(result1.getdata())
result2 =  compare(b2, b3)
WR2 = list(result2.getdata())
result3 =  compare(b4, b5)
WR3 = list(result3.getdata())
result4 =  compare(b6, b7)
WR4 = list(result4.getdata())
result5 =  compare(b7, b8)

b0 = Image.open('captchadata/x0.jpg')
b0 = b0.convert('1')
X0 = list(b0.getdata())
b1 = Image.open('captchadata/x1.jpg')
b1 = b1.convert('1')
X1 = list(b1.getdata())
b2 = Image.open('captchadata/x2.jpg')
b2 = b2.convert('1')
X2 = list(b2.getdata())
b3 = Image.open('captchadata/x3.jpg')
b3 = b3.convert('1')
X3 = list(b3.getdata())
b4 = Image.open('captchadata/x4.jpg')
b4 = b4.convert('1')
X4 = list(b4.getdata())
b5 = Image.open('captchadata/x5.jpg')
b5 = b5.convert('1')
X5 = list(b5.getdata())
b6 = Image.open('captchadata/x6.jpg')
b6 = b6.convert('1')
X6 = list(b6.getdata())
result1 =  compare(b0, b1)
XR1 = list(result1.getdata())
result2 =  compare(b2, b3)
XR2 = list(result2.getdata())
result3 =  compare(b4, b5)
XR3 = list(result3.getdata())
result4 =  compare(b5, b6)


b0 = Image.open('captchadata/y0.jpg')
b0 = b0.convert('1')
Y0 = list(b0.getdata())
b1 = Image.open('captchadata/y1.jpg')
b1 = b1.convert('1')
Y1 = list(b1.getdata())
b2 = Image.open('captchadata/y2.jpg')
b2 = b2.convert('1')
Y2 = list(b2.getdata())
b3 = Image.open('captchadata/y3.jpg')
b3 = b3.convert('1')
Y3 = list(b3.getdata())
b4 = Image.open('captchadata/y4.jpg')
b4 = b4.convert('1')
Y4 = list(b4.getdata())
b5 = Image.open('captchadata/y5.jpg')
b5 = b5.convert('1')
Y5 = list(b5.getdata())
b6 = Image.open('captchadata/y6.jpg')
b6 = b6.convert('1')
Y6 = list(b6.getdata())
b7 = Image.open('captchadata/y7.jpg')
b7 = b7.convert('1')
Y7 = list(b7.getdata())
b8 = Image.open('captchadata/y8.jpg')
b8 = b8.convert('1')
Y8 = list(b8.getdata())
result1 =  compare(b0, b1)
YR1 = list(result1.getdata())
result2 =  compare(b2, b3)
YR2 = list(result2.getdata())
result3 =  compare(b4, b5)
YR3 = list(result3.getdata())
result4 =  compare(b6, b7)
YR4 = list(result4.getdata())
result5 =  compare(b7, b8)


b0 = Image.open('captchadata/z0.jpg')
b0 = b0.convert('1')
Z0 = list(b0.getdata())
b1 = Image.open('captchadata/z1.jpg')
b1 = b1.convert('1')
Z1 = list(b1.getdata())
b2 = Image.open('captchadata/z2.jpg')
b2 = b2.convert('1')
Z2 = list(b2.getdata())
b3 = Image.open('captchadata/z3.jpg')
b3 = b3.convert('1')
Z3 = list(b3.getdata())
b4 = Image.open('captchadata/z4.jpg')
b4 = b4.convert('1')
Z4 = list(b4.getdata())
b5 = Image.open('captchadata/z5.jpg')
b5 = b5.convert('1')
Z5 = list(b5.getdata())
b6 = Image.open('captchadata/z6.jpg')
b6 = b6.convert('1')
Z6 = list(b6.getdata())
b7 = Image.open('captchadata/z7.jpg')
b7 = b7.convert('1')
Z7 = list(b7.getdata())
b8 = Image.open('captchadata/z8.jpg')
b8 = b8.convert('1')
Z8 = list(b8.getdata())
b9 = Image.open('captchadata/z9.jpg')
b9 = b9.convert('1')
Z9 = list(b9.getdata())
b10 = Image.open('captchadata/z10.jpg')
b10 = b10.convert('1')
Z10 = list(b10.getdata())
b11 = Image.open('captchadata/z11.jpg')
b11 = b11.convert('1')
Z11 = list(b11.getdata())
b12 = Image.open('captchadata/z12.jpg')
b12 = b12.convert('1')
Z12 = list(b12.getdata())
b13 = Image.open('captchadata/z13.jpg')
b13 = b13.convert('1')
Z13 = list(b13.getdata())
result1 =  compare(b0, b1)
ZR1 = list(result1.getdata())
result2 =  compare(b2, b3)
ZR2 = list(result2.getdata())
result3 =  compare(b4, b5)
ZR3 = list(result3.getdata())
result4 =  compare(b6, b7)
ZR4 = list(result4.getdata())
result5 =  compare(b8, b9)
ZR5 = list(result5.getdata())
result6 =  compare(b10, b11)
ZR6 = list(result6.getdata())
result7 =  compare(b12, b13)
ZR7 = list(result7.getdata())



listdata = [A0, A1, A2, A3, A4, A5, A6, A7, AR1, AR2, AR3, AR4, 
            B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, BR1, BR2, BR3, BR4, BR5, BR6,
            C0, C1, C2, C3, C4, C5, C6, CR1, CR2, CR3, CR4,
            D0, D1, D2, D3, DR1, DR2,
            E0, E1, E2, E3, E4, E5, E6, E7, E8, E9, ER1, ER2, ER3, ER4,
            F0, F1, F2, F3, F4, FR1, FR2, FR3,
            G0, G1, G2, G3, G4, GR1, GR2, GR3,
            H0, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, HR1, HR2, HR3, HR4, HR5, HR6, HR7,
            I0, I1, I2, I3, I4, I5, IR1, IR2, IR3,
            J0, J1, J2, J3, J4, J5, J6, J7, J8, J9, J10, J11, J12, JR1, JR2, JR3, JR4, JR5, JR6, JR7,
            K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13, K14, K15, K16, KR1, KR2, KR3, KR4, KR5, KR6, KR7, KR8, KR9,
            L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, LR1, LR2, LR3, LR4, LR5, LR6, LR7,
            M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, MR1, MR2, MR3, MR4, MR5, MR6,
            N0, N1, N2, N3, NR1, NR2,
            O0, O1, O2, O3, O4, O5, O6, O7, O8, O9, O10, O11, OR1, OR2, OR3, OR4, OR5, OR6,
            P0, P1, P2, P3, P4, P5, P6, P7, P8, PR1, PR2, PR3, PR4, PR5,
            Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, QR1, QR2, QR3, QR4, QR5,
            R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RR1, RR2, RR3, RR4, RR5, RR6, RR7,
            S0, S1, S2, S3, S4, S5, S6, S7, S8, SR1, SR2, SR3, SR4, SR5,
            T0, T1, T2, T3, T4, TR1, TR2, TR3,
            U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, UR1, UR2, UR3, UR4, UR5, UR6, UR7,
            V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, VR1, VR2, VR3, VR4, VR5, VR6, VR7, VR8,
            W0, W1, W2, W3, W4, W5, W6, W7, W8, WR1, WR2, WR3, WR4,
            X0, X1, X2, X3, X4, X5, X6, XR1, XR2, XR3,
            Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, YR1, YR2, YR3, YR4,
            Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, ZR1, ZR2, ZR3, ZR4, ZR5, ZR6, ZR7
            ]


listdata1= [A0, A1, A2, A3, A4, A5, A6, A7, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11]
out = open('pixels_data.csv', 'w')
for row in listdata:
    for column in row:
        out.write('%s,' % column)
    out.write('\n')
out.close()   

listdata = [['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],['A', 1],
            ['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],['B', 2],
            ['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],['C', 3],
            ['D', 4],['D', 4],['D', 4],['D', 4],['D', 4],['D', 4],
            ['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],['E', 4],
            ['F', 5],['F', 5],['F', 5],['F', 5],['F', 5],['F', 5],['F', 5],['F', 5],
            ['G', 6],['G', 6],['G', 6],['G', 6],['G', 6],['G', 6],['G', 6],['G', 6],
            ['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],['H', 7],
            ['I', 8],['I', 8],['I', 8],['I', 8],['I', 8],['I', 8],['I', 8],['I', 8],['I', 8],
            ['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],['J', 9],
            ['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],['K',10],
            ['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],['L',11],
            ['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],['M',12],
            ['N',13],['N',13],['N',13],['N',13],['N',13],['N',13],
            ['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],['O',14],
            ['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],['P',15],
            ['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],['Q',16],
            ['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],['R',17],
            ['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],['S',18],
            ['T',19],['T',19],['T',19],['T',19],['T',19],['T',19],['T',19],['T',19],
            ['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],['U',20],
            ['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],['V',21],
            ['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],['W',23],
            ['X',24],['X',24],['X',24],['X',24],['X',24],['X',24],['X',24],['X',24],['X',24],['X',24],
            ['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],['Y',25],
            ['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26],['Z',26]
]
listdata2 = [['1'],['1'],['1'],['1'],['1'],['1'],['1'],['1'],['2'],['2'],['2'],['2'],['2'],['2'],['2'],['2'],['2'],['2'],['2'],['2']]
out = open('pixels_data_result.csv', 'w')
for row in listdata:
    for column in row:
        out.write('%s,' % column)
    out.write('\n')
out.close()   
    
listdata = [result_A, result_B]

out = open('img_pixels.csv', 'w')
for row in listdata:
    for column in row:
        out.write('%d,' % column)
    out.write(' ')
out.close()
#with open('pixels_data_result.csv','r') as userFile:
 #  useFileReader = csv.reader(userFile)
  # for row in useFileReader:
   #    print (row)
 
    
TRAIN_TO_TEST_RATIO = 0.8
start = time.time()

def shuffle_data(inp, tar):
    combined = list(zip(inp, tar))
    shuffle(combined)
    return zip(*combined)

def from_csv(filename, newline='', delimiter=','):
    x = []
    #y = []

    with open(filename, newline=newline) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        
        
        for row in csv_reader:
            x.append(list(map(str, row[0:499]))) #read all input attributes as floats row[:-1]
           # y.append(str(row[-1]))

    return x

def from_csv1(filename1, newline='', delimiter=','):
    #x = []
    y = []

    with open(filename1, newline=newline) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        
        
        for row in csv_reader:
            #x.append(list(map(str, row[0:499]))) #read all input attributes as floats row[:-1]
           y.append(str(row[0]))

    return y 
'''
def from_csv(filename, newline='', delimiter=','):
    x = []
    y = []

    with open(filename, newline=newline) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        
        
        for row in csv_reader:
            x.append(list(map(str, row[0:499]))) #read all input attributes as floats row[:-1]
            y.append(str(row[-1]))

    return x, y
'''
file_name = "pixels_data.csv"
file_name1 = "pixels_data_result.csv"
x = from_csv(file_name)
#x=listdata1
#print (x)
y = from_csv1(file_name1)
#y=listdata2
#x, y = shuffle_data(x, y) #shuffle data - important as dataset is sorted by class
#print (y)

#print(x)
#print(y)

size = len(x[0])

'''
for row in x:
    print(row)
    print('\n')
'''

#x.reshape(500, size)
                   
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = TRAIN_TO_TEST_RATIO) #split dataset into train/test sets
#Default C=0.01, gamma=0.001
C=0.01
gamma=0.001
clf = svm.SVC(C=C, gamma=gamma, kernel='linear')
print("C:", C, "gamma:", gamma)

#print(len(x_train))

#print(len(y_train))

clf.fit(x_train, y_train) #fit to training data

print(classification_report(y_test, clf.predict(x_test)))
end = time.time()
print(end - start, "Seconds")

#for x_i, y_i in zip(x, y):
 #   print("input:", x_i, "target:", y_i)

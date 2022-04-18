alpha = 1; b=0; w1=0; w2=0; w3=0; w4=0;

x1 = [-1,-1,-1,-1,-1,-1,-1,-1,1,1]
x2 = [-1,-1,-1,-1,1,1,1,1,-1,-1]
x3 = [-1,-1,1,1,-1,-1,1,1,-1,-1]
x4 = [-1,1,-1,1,-1,1,-1,1,-1,1]
t = [-1,1,-1,1,-1,1,-1,1,-1,1]

i = 0;

x = int(input("Enter the value: "));

yin = b+x1[0]*w1+x2[0]*w2+x3[0]*w3+x4[0]*w4;

if yin>0:
  yin = 1

elif yin == 0:
  win = 0
else:
  yin = 1

while (yin!=t[i]):
  b = b+alpha*t[i];
  w1 = w1+alpha*x1[i]*t[i];
  w2 = w2+alpha*x2[i]*t[i];
  w3 = w3+alpha*x3[i]*t[i];
  w4 = w4+alpha*x4[i]*t[i];

  i = i+1

  yin = b+x1[0]*w1+x2[0]*w2+x3[0]*w3+x4[0]*w4;
  
  if yin > 0:
    yin  =1
  elif yin == 0:
    yin = 0
  else:
    yin = -1

print("Value of yin and t is", yin, t[i]);

if yin!=t[i]:
  print("Perceptron can't learn")
else:
  y=x%10;
  k=0;

  if y==0:
    bina = [0,0,0,0];

  else:
      bina = [0,0,0,0];
      while (y!=0):
        bina[k] = y%2;
        y=int(y/2)
        k = k+1
  net = b+bina[3]*w1+bina[2]*w2+bina[1]*w3+bina[0]*w4;
  print("Net Value", net);
  if net>0:
    print("The number is ODD")
  else:
    print("The number is EVEN")

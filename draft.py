import numpy as np

s01=np.array([7,	-4	,	-8	,	-9	,	-15	,	3	,	-4	,	2	,	-11	,	11	])
s02=np.array([2,	0	,	-3	,	-4	,	-2	,	-3	,	-2	,	-8	,	-1	,	1	])
s03=np.array([5	,	2	,	0	,	5	,	-1	,	0	,	-1	,	-1	,	-2	,	2	])
s04=np.array([0,	0	,	1	,	2	,	0	,	3	,	2	,	8	,	1	,	-1	])
s05=np.array([2  ,	-1	,	-3	,	-4	,	-4	,	-1	,	-2	,	-4	,	-3	,	3	])


s11 = s05/2
s12=s01
s13=s02
s14=s03
s15=s04


s21=s11
s22=s11*(-7)+s12
s23=s11*(-2)+s13
s24=s11*(-5)+s14
s25=s15



s31=s21
s32=s23
s33=s23*0.5+s22
s34=s23*(-4.5)+s24
s35=s25

s41=s31
s42=s32
s43=s35
s44=s35*(-7.5)+s34
s45=s35*(-2.5)+s33

print(s41,
      s42,
      s43,
      s44,
      s45)

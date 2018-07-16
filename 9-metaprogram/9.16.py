# from  inspect import Signature,Parameter
#
#
# params = [
#     Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
#     Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
#     Parameter('z',Parameter.KEYWORD_ONLY,default=None)
# ]
# sig = Signature(params)
# def func(*args,**kwargs):
#     bound_values = sig.bind(*args,**kwargs)
#     for name,value in bound_values.arguments.items():
#         print(name,value)
#
# func(1,2,z=3)
# func(1)

x=2
print(eval('2 + 3*4 + x'))
exec('for i in range(10): print(i)')
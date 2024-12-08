input_text = ("""}}+{where()mul(873,602) mul(954,447)^where()~mul(548,799)-<what()mul(588,631)^who()'@( [mul(143,388)how(445,327))$ select()who()mul(746,719)mul(963,262)}'*+why()<?&/select()don't()[%]% ^^mul(933,492)don't() ^-who()(%how()]mul(583,700))""")


mulPositions = []
# commaPositons = []



pattern = pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

for i in range(len(input_text)):
    if input_text[i:i+4] == 'mul(':
        mulPositions.append(i+4)
    # if input_text[i] == ',':
    #     commaPositons.append(i)



# xNum = []
# xNumConnected = int(''.join(map(str,xNum)))

if len(str(int(input_text[mulPositions[0]]))) == 1:
    print(input_text[mulPositions[0]])
    
# print(xNumConnected)




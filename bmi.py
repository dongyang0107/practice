height = input('請輸入你的身高(cm): ')
height = float(height)
weight = input('請輸入你的體重(kg): ')
weight = float(weight)

bmi = weight / ((height/100)**2)
print('你的bmi是:', bmi)

if bmi < 18.5:
	print('體重過輕，需要多運動，均衡飲食，以增加體能，維持健康！')
elif bmi >= 18.5 and bmi < 24:
	print('恭喜!你是健康體重，要繼續保持！')
elif bmi >= 24 and bmi < 27:
	print('體重過重了，要小心囉，趕快力行「健康體重管理」！')
else:
	print('啊～你太胖了，需要立刻力行「健康體重管理」囉！')

# height = input('請輸入身高(cm)： ')
# weight = input('請輸入體重(kg)： ')
# height = int(height)
# weight = int(weight)
# height = height / 100 # 換成公尺
# bmi = weight / height / height     
# if bmi < 18.5:
#     print('你的bmi值為', bmi, '屬體重過輕')
# elif bmi >= 18.5 and bmi < 24:
#     print('你的bmi值為', bmi, '屬正常範圍')
# elif bmi >= 24 and bmi < 27:
#     print('你的bmi值為', bmi, '稍重')
# elif bmi >= 27 and bmi < 30:
#     print('你的bmi值為', bmi, '輕度肥胖')
# elif bmi >= 30 and bmi < 35:
#     print('你的bmi值為', bmi, '中度肥胖')
# elif bmi >= 35: # 寫else: 也可以
#     print('你的bmi值為', bmi, '重度肥胖')
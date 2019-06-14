# 讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])
print(products)
print(products[0][0])

# 印出所有購買紀錄
for product in products:
	print(product[0], '的價格是:', product[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:     # with 自動close
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' )

# practice
data = [1, 3, 5, 7, 9]
with open('numbers.csv', 'w') as f:
	for number in data:
		f.write(str(number) + '\n')

#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue        # continue/ break 只能用在迴圈裡
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)
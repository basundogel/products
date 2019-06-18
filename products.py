
import os  # check if the file is in the same directory as python file

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue        # continue/ break 只能用在迴圈裡
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price])
	print(products)   # print(products[0][0])
	return products

# 印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格是:', product[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:     # with 自動close
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n' )

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('file found')
		products = read_file(filename)
	else:
		print('file not found QQ')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()






# # practice
# data = [1, 3, 5, 7, 9]
# with open('numbers.csv', 'w') as f:
# 	for number in data:
# 		f.write(str(number) + '\n')


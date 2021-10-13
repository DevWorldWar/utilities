''' Math Repo Context '''

# Order by decreasing
class Order_By:
    def increasing(numbers: list):
        length = len(numbers)
        if length <= 1:
            return numbers
        else:
            x, y    = 0, 0
            res     = []
            for n in numbers:
                res.append(int(n))
            while x < length - 1:
                while y < length - 1:
                    y = y + 1
                    if res[y] < res[x]:
                        aux     = res[x] 
                        res[x]  = res[y]
                        res[y]  = aux
                x = x + 1
                y = x
        return res

    def decreasing(numbers: list):
        length = len(numbers)
        if length <= 1:
            return numbers
        else:
            x, y    = 0, 0
            res     = []
            for n in numbers:
                res.append(int(n))
            while x < length - 1:
                while y < length - 1:
                    y = y + 1
                    if res[y] > res[x]:
                        aux     = res[x] 
                        res[x]  = res[y]
                        res[y]  = aux
                x = x + 1
                y = x
        return res
        

# Find the next prime number from the input
def next_primo(n: int):
	if n < 2:
		return 2
	x = n
	y = 2
	while True:
		x = x + 1
		while y < x:
			res = x % y
			if res == 0:
				break
			else:
				y = y + 1
		if x == y:
			return x

# Find the MDC number of the entered numbers
def calc_mdc(numbers: list):
    length              = len(numbers)
    if length < 2:
        return 1
    numbers_list        = Order_By.increasing(numbers)
    res                 = []
    mdc, x, i, rest     = 1, 0, 2, 0
    while x < length:
        n   = numbers_list[x]
        if x == length - 1:
            if rest == x:
                if n % i == 0:
                    res.append(i)
            if rest == 0:
                i           = next_primo(i)
            rest            = 0
            x               = 0
        else:
            if n >= 2:
                if n % i == 0:
                    rest            = rest + 1
                    numbers_list[x] = n / i
                x               = x + 1
            else:
                break
    for n in res:
        mdc = mdc * n
    return mdc

def test_order_by(args: list):
    res = Order_By.increasing(args)
    print(f'\n Result: {res} ')

def test_mdc(args: list):
    try:
        res = calc_mdc(args)
        if res == 1:
            print(f'\n {args} não possuem um mdc. \n')
        else:
            print(f'\n MDC de {args} é {res} \n')
    except Exception as exc:
        raise exc
    else:
        print(' E acabou ...')

args = input('\n Escreva seus números separando-os somente por " " (espaço): \n')
args = args.split()

test_mdc(args)
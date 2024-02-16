mode = input('請選擇轉換器模式。攝氏轉華氏請輸入1，華氏轉攝氏請輸入2 : ')
if mode == '1':
	cs1 = input('請輸入攝氏溫度 : ')
	cs1 = float(cs1)
	fh1 = cs1 * 9 / 5 + 32
	fh1 = str(fh1)
	print('對應的華氏溫度為 : ' + fh1 + '度')
if mode == '2':
	fh2 = input('請輸入華氏溫度 : ')
	fh2 = float(fh2)
	cs2 = (fh2 - 32) * 5 / 9
	cs2 = str(cs2)
	print('對應的攝氏溫度為 : ' + cs2 + '度')
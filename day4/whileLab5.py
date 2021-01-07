#while문으로 무한루프처리
#길이가 0:  반복종료
#길이가 5이상 8이하 : 입력받는 기능부터 다시 수행
#길이가 5미만 : 문자열 앞뒤로 *
#길이가 8초과 : 문자열 앞뒤에 $

while True:
    word = input('문자열을 입력하세요')
    wordlength = len(word)

    if wordlength == 0:
        break
    elif 5<= wordlength <=8:
        continue
    elif wordlength <5 :
        result = '*%s*' %word
    elif wordlength > 8:
        result= '$%s$' %word
    print('유효한 입력 결과 : %s' % result)



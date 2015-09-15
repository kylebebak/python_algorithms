import sys
ZERO, HUNDRED = 'zero', 'hundred'

ONES = [
'', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

TENS = [
'', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]

THOUSANDS = [
'', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion'
]

def num_to_str(num):

    def _num_to_str(num):
        s_num = str(num)
        thousands, pre_len = divmod(len(s_num)-1, 3)
        if thousands >= len(THOUSANDS):
            raise OverflowError('Number is too large.')
        pre_len += 1
        pre, rest = int(s_num[:pre_len]), s_num[pre_len:]
        hundreds, tens, ones = pre//100, (pre%100)//10, (pre%10)

        str_rep = ''
        if hundreds:
            str_rep += ' {} hundred and'.format(ONES[hundreds]) if tens or ones \
            else ' {} hundred'.format(ONES[hundreds])
        if tens >= 2:
            str_rep += ' {}'.format(TENS[tens])
        if tens == 1:
            str_rep += ' {}'.format(ONES[10+ones])
        else:
            str_rep += ' {}'.format(ONES[ones])

        if not thousands:
            return str_rep
        else:
            return '{} {},'.format(str_rep, THOUSANDS[thousands]) + _num_to_str(int(rest))

    num, str_rep = int(num), ''
    if num == 0:
        return ZERO
    elif num < 0:
        str_rep += 'negative '
    str_rep += ' '.join(_num_to_str(abs(num)).split())
    return str_rep[:-1] if str_rep[-1] == ',' else str_rep



if __name__ == '__main__':
    print(num_to_str(sys.argv[1]))


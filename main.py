'prob 14'
def read():
    n=int(input('Numarul este: '))
    return n

def read_list():
    given = input("Dati numere separate prin virgula:")
    int_list = given.split(',')
    list = [ ]
    for int_lst in int_list:
        list.append(int(int_lst))
    return list



def get_cmmmmc(n, lst):
    '''
    Determinarea cmmmc a n numere.
    a-primul numar, b-al doilea numar
    :param n:
    :param lst:
    :return:
    '''
    a=lst[1]
    for i in range(2,n):
        b=lst[i]
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        a=(lst[i-1]*lst[i])//a
    return a




'prob 7'

def is_antipalindrome(n):
    '''
    Determina daca un numar este antipalindrom.
    :param:int n.
    :return:True daca e antipalindrom sau False daca nu e.
    '''
    cn=n
    inv =0
    while cn!=0:
        inv=inv*10+cn%10
        cn=cn//10
    if inv==n:
        return False
    else:
        return True




def test_is_antipalindrome():
    assert is_antipalindrome(121) == False
    assert is_antipalindrome(123) == True


test_is_antipalindrome()

'prob 11'

def get_leap_years(a,b):
    '''
    Afiseaza cati ani bisecti sunt intre 2 ani(inclusiv anii).
    :param a:
    :param b:
    :return:
    '''
    nr=0
    if a%4==0:
        nr=nr+1
    an=b-a+1
    nr=nr+an//4
    return nr

def test_get_leap_years():
    assert(2000,2005) == 2
    assert(2001,2003) == 0


def print_menu():
    print('1.(Prob. 7) Antipalindrom.')
    print('2.(Prob. 14) Cmmmc. ')
    print('3.(Prob. 11) Anii bisecti. ')

def main():
    while True:
        print_menu()
        op= input("Alegeti o optiune: ")
        if op=='1':
            n=read()
            print(is_antipalindrome(n))
        if op=='2':
            n = read()
            lst = read_list()
            print(get_cmmmmc(n,lst))
        if op=='3':
            a=read()
            b=read()
            print(get_leap_years(a,b))

main()







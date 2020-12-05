'''
Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
Sau đó, unpack các phần tử trong một tuple.
'''
def dulieu_tuple(your_tuple):
    a, b, c, d = your_tuple
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")
if __name__ == "__main__":
    your_tuple=(1,'long',3.16,'ooo')
    print(dulieu_tuple(your_tuple))
    print(type(your_tuple))


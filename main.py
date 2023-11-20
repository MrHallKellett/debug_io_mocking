
def example_test_passed():
    
    print(555)


def example_test_failed():
    
    print(666)


x = input("Which task, 1 or 2?" )

if x == "1":
    example_test_passed()
else:
    example_test_failed()
    

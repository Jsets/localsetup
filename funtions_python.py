def hello():
    print('Hello, user!')
    
def pack(paper, rock, scissors):
    return [paper, rock, scissors]


def eat_lunch(lunch):
    if len(lunch) == 0:
        print('My lunch box is empty!')
    else:
        for i in range(len(lunch)):
            if i == 0:
                print('First I eat', lunch[0])
            else:
                print('Next I eat', lunch[i])
                
hello()
print(pack('paper', 'rock', 'scissors'))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(['salad'])
eat_lunch(['salad', 'bread', 'cheese'])


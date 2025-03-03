for _ in range(20):  
    while True:
        try:
            n = int(input())
            if 1 <= n <= 20:
                for i in range(n):
                    print(f"{i * i}") 
                break  
            else:
                print()
        except ValueError:
            print("Invalid ")
    break  


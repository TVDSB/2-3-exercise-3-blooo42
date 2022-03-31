def main():
    #your code goes here
    number = int(input("enter a number here \n"))

    if number%15 == 0:
        print("fizzbuzz")

    elif number%3 == 0:
         print("fizz")

    elif number%5 == 0:
         print("buzz")

if __name__ =='__main__':
    main()

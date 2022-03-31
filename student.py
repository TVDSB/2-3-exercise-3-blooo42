def main():
    #your code goes here
    percentage = int(input("enter your mark percent here \n"))

  if percentage >= 80 and percentage <=100:
    print("you got an A!")

  elif percentage >= 70:
    print("you got a B")

  elif percentage >= 60:
    print("you got a C")

  elif percentage >= 50:
    print("you got a D")

  elif percentage >=0 and percentage <=49:
    print("you got an F")
if __name__ =='__main__':
    main()

Itmes = 2

if Itmes != 3:#raise Exception("condition failed")
  pass

assert(Itmes==2)

try:
    with open('mahehbabu.txt') as file:
        file.read()

except Exception as e:
    print("maheshbabu file not prseted in directory")
    print(e)

finally:
    print("maheshbabu")

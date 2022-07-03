
terminal_launch = True
      
def start():
   premiere_valeur = input("1st value : ")
   second_valeur = input("2nd value : ")

   def max2(a,b):
   
      if a > b:
         return a
      elif b > a:
         return b
      elif a == b:
         return "equality"

   try:  
      premiere_valeur = int(premiere_valeur)
      second_valeur = int(second_valeur)
      print(max2(premiere_valeur, second_valeur))
   except ValueError:
      print("digit or number only accepted")

while terminal_launch:
   exit = input("\
---------------------------------\n\
press 'a' to continue, 'z' to quit \n\
---------------------------------\n\
   ")
   if exit == "z":
      break
   else:
      start()
    
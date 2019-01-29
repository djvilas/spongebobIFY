def spongebob():
  #Inspired by Fiona Tuite, Third Year Computer Applications & Software Engineering student at Dublin City University, 2019.
  import random 
  text = input("Input the word/s that you'd like to alter: ")
  finish = 0
  while finish == 0:
    updatedText = text
    for x in range(0,10):
      newText = ""
      for x in updatedText:
        if random.randint(0,2) > 1:
          newText += x.upper()
        else:
          newText += x.lower()
      updatedText = newText    
    
    print("\nWe've generated:\n"+updatedText+"\nWould you like to generate a new version?\n")
    choice = input("Generate Again? Yes|No : ")
    if choice.lower() == "yes":
      choice = 0
    elif choice.lower() =="no":
      break
    else:
      print(choice.lower())
      print("\nWe didn't understand your command... Generating again.\n")    
     
spongebob()

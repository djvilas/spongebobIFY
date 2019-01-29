def spongebob():
  #Inspired by Fiona Tuite, Third Year Computer Applications & Software Engineering student at Dublin City University, 2019.
  import random 
  text = input()
  finish = 0
  while finish == 0:
    newText = ""
    for x in text:
      if random.randint(0,2) > 1:
        newText += x.capitalize()
      else:
        newText += x
    
    print("We've generated:\n"+newText+"\n Would you like to generate a new version?")
    choice = input("Generate Again? Yes|No : ")
    if choice.lower() == "yes":
      choice = 0
    elif choice.lower() =="no":
      break
    else:
      print(choice.lower())
      print("We didn't understand your command... Generating again.")    
     

spongebob()
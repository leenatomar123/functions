print("wELCOME......TO......KBC")
Question_list=("how many states are there in India?"
  "what is the capital of india?"
  "NG mai konsa course padhaya jata hai?")

options_list=[
          ["Twenty-four","Twenty-five","Twenty-eight","Twenty-nine"]
          ["Bhutan","Pakistan","Delhi","China"]
          ["Software engineering","Graphics","Animation","Architecture"]
          ]
Solution_list=[3,4,1]
Ans=["Twenty-eight","Twenty-four","Delhi","Bhutan","Graphics","Software engineering"]
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=question_list[i]
    print(i1)
    j=0
    k=i
    while j<len(option_list[i]):
        l=option_list[k][j]
        print(j+1,l)
        j=j+1

Lifeline1=(input("do u want 50-50 lifelline"))  
if lifeline1=="yes":
  print(50-50)
  if count==0:
    print(ans([y+i])
    print(ans([y+r])
    n=int(input("enter answer"))
    if n==solution[i]:
      print("Right Anwer")
    else:
      print("Wrong Anwer")
      break
    count+=1
else:
  print("Want 50-50 lifeline")
  m=int(input("enter your answer"))
  if m==solution[i]:
    print("you win this challenge")
  else:
    print("you lose this challenge")
    break
  r+=1
  y+=1

  i+=1




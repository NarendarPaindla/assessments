# codes

[Day-1](https://colab.research.google.com/drive/16hRa-RbgM4dpU1-oh9jNJ5-ydoOLhptm?usp=sharing)

[Day-8](https://colab.research.google.com/drive/16ge2K3cYqVTBHdNB-0X3vdy90ieKJqu-?usp=sharing)

[feedback](https://bytexl.app/feedback-requests/44q7rb8q7)

[assignment](https://forms.gle/hSUFoZEyEyFBNM569)

---`

---

# 📚 Notes Table of Contents

| Topic | Link |
|--------|--------|
| Functions | [functions.md](https://github.com/NarendarPaindla/assessments/blob/master-branch/notes/functions.md) |
| List | [list.md](https://github.com/NarendarPaindla/assessments/blob/master-branch/notes/list.md) |
| Tuple | [tuple.md](https://github.com/NarendarPaindla/assessments/blob/master-branch/notes/tuple.md) |
| Set | [set.md](https://github.com/NarendarPaindla/assessments/blob/master-branch/notes/set.md) |
| Dictionary | [dictionary.md](https://github.com/NarendarPaindla/assessments/blob/master-branch/notes/dictionary.md) |


```python
try:
    def calculator(num1,num2,operator):
      if operator=="+":
        return num1+num2
      elif operator=="-":
        return num1-num2
      elif operator=="*":
        return num1*num2
      elif operator=="/":
        try:
            return num1/num2
        except ZeroDivisionError:
            return "division by zero gives infinitely"
      else:
        return "Invalid operator"
    program_control={"y","Y"}
    while True:
        while True:
            try:
               num1=int(input("Enter number 1: "))
               break
            except ValueError:
               print("waring: enter only numbers --> try to enter again")
        while True:    
            try:
                num2=int(input("Enter number 2: "))
                break
            except ValueError:
                print("waring: enter only numbers --> try to enter again")
        op_set={"+","-","*","/"}
        while True:
            operator=input("Enter operator: ")
            if operator in op_set:
                break
            else:
                print("invalid operator please enter the  valid operator(+,-,*,/)")
        print(f"Result= {calculator(num1,num2,operator)}")
        pro=input("Do you want to continue (y/n or Y/N)")
        if pro in program_control:
            continue
        else:
            print("Thank you visit again")
            break
        
except KeyboardInterrupt:
    print("Thank you visit again")

```

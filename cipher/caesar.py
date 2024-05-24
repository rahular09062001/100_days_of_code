## Ceasar Single Function

from art import logo

print(logo)

loop_condition=True
while (loop_condition):
    def caesar(direction,text,shift):
        direction=direction.lower()
        text=text.lower()
        caesar_word=""
        letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in text:
            for j in range (0,26):
                if(i==letters[j]):
                    if(direction=="encode"):
                        if(j+shift>=26):
                            new_shift=((j+shift)%26)
                            caesar_word+=letters[new_shift]
                        else:
                            caesar_word+=letters[j+shift]                 
                    elif(direction=="decode"):
                        if(j-shift<0):
                            new_shift=((j-shift)%26)
                            caesar_word+=letters[new_shift]
                        else:
                            caesar_word+=letters[j-shift]
            if(i not in letters):
                caesar_word+=i
        if(direction=="encode"):
            print(f"The encrypted result is : {caesar_word}")
        elif(direction=="decode"):
            print(f"The decrypted result is : {caesar_word}")
    
    
    a=input("Enter decode or encode")

    if(a=="encode" or a=="decode"):
        b=input("Enter the text")
        c=int(input("Enter the shift"))
        caesar(direction=a,text=b,shift=c)
    else:
        print("You have input something else other than encode and decode")

    val=input("Do you want to continue the encoding and decoding ? [y/n]").lower()
    if(val=="y"):
        loop_condition=True
    else:
        loop_condition=False
        print("Good Bye....")

                    
                
            



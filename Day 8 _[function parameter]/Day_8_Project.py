#  casear  cipher

alphabates= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabates))


def  caesar(original_text,shift_number,encode_or_decode):
    coded_word = ''
    if encode_or_decode == 'decode':
        shift_number *= -1
    for letter  in original_text:

        if letter not in alphabates:
            coded_word += letter
        else:
            after_shifting = alphabates.index(letter) + shift_number
            after_shifting %= len(alphabates)
            coded_word += alphabates[after_shifting] 
    print(f'here is {encode_or_decode} result : {coded_word}')

should_continue = True
while should_continue:
    original_text = input("Enter  Text\n")
    shift_number = int(input("Enter  shift Number \n"))
    encode_or_decode = input("Do you Want  Encode or Decode\n").lower()

    caesar(original_text=original_text,shift_number=shift_number,encode_or_decode=encode_or_decode)
    
    restart = input("Type 'Yes'  if you want to  go again. Otherwise type 'No' \n" ).lower()
    if restart == "no":
        should_continue = False
        print("Bye Bye !")


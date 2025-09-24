#---------------------------------------------------------------------------#
#  Find the number of occurrences of +,-,* and / in the following string.   #
#                                                                           #
#  Hint:                                                                    #
# In python strings are considered as Lists and can be treated as such.     #
#---------------------------------------------------------------------------#

stringVar = "is simply dummy text of the printing and typesetting" \
" industry. Lorem Ipsum has been the industry's standard ++dummy text" \
" ever --since the 1500s,-- when an unknown printer took a galley of type" \
" and scrambled it to make a type specimen book. It has survived /not only" \
" five centuries, but also the leap into electronic typesetting, remaining" \
" essentially unchanged. It was popularised in the - 1960s with the rel/ease" \
" of Letraset sheets containing Lorem Ipsum passages, and more recently" \
" with desktop publishing software **like Aldus PageMaker including versions" \
" of Lorem Ipsum."


print(f"The sign \"+\" is {stringVar.count('+')} times in the given text.")
print(f"The sign \"-\" is {stringVar.count('-')} times in the given text.")
print(f"The sign \"*\" is {stringVar.count('*')} times in the given text.")

print(f"The signs \"+\", \"-\" and \"*\" are found {stringVar.count('+')+stringVar.count('-')+stringVar.count('*')} times in the given text.")

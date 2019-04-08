#Create function to convert list to string list separated by commas
def comma(list):
    list.insert(len(list)-1, 'and') #inserts "and" before last listed item
    statement=''
    for i in range(len(list)):
        statement+=list[i]
        if i<(len(list)-2):
            statement+=', ' #adds comma and space after each list item
        elif i<(len(list)-1):
            statement+=' ' #adds only a space after the inserted "and"
        elif  i>=(len(list)-1):
            statement+='.' #adds a period at the end of the list
    return statement
list=['apples','bananas','tofu', 'cats']
print(comma(list))

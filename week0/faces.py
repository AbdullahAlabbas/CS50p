# define a new function called "main"
def main():
    
    emoticon = input("")
    print(emoticon)
    
    emoticon = convert(emoticon)
    print(emoticon)
    
    
#define a new function called "convert"
def convert(emoticon):
    
    emoticon = emoticon.replace(":)","🙂")
    emoticon = emoticon.replace(":(","🙁")

    return emoticon
    
main()
    
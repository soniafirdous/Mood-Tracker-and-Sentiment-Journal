# 1.creating a user profile class



class UserProfile:
    def __init__(self,name):
        self.name=name
        self.entries={} # to keep date(mood,text)

    def add_entry(self,date,mood,text):
        self.entries[date]=(mood,text)

    def view_history(self):
        for date,(mood,text)in sorted (self.entries.items()):
            print(f" date:{date}------> {mood} : {text}")





#2. user input to add an entry 

def add_journal_entry(user):
    #  Ask how the user is feeling
    text=input("how are you feeling ? ")
    #  Analyze the mood from what they typed
    mood=analyze_mood(text)
    # Ask for the date 
    date=input("enter today's date: ")
    # Save the entry using the user object
    user.add_entry(date,mood,text)

#    Show message to say it worked
    print("Your entry is saved!")
    print("Date:", date)
    print("Mood:", mood)
    Suggest_activity(mood)

#3. creating function to analyze mood of user

def analyze_mood(text):
    text = text.lower()
    happy_keywords_list = ["happy", "great", "wonderful", "super", "glad", "excited"]
    sad_keywords_list = ["sad", "dull", "exhaust", "upset", "down"]
    
    if any(word in text for word in happy_keywords_list):
        return "Happy 😊"
    elif any(word in text for word in sad_keywords_list):
        return "Sad 😒"
    else:
        return "Tired 😫"


#4. view mood history

def mood_history(user):
    print(f"mood history of {user.name}")
    user.view_history()


#5. save and load jornal

import json

def save_journal(user,filename="journal.json"):
    with open(filename,"w") as f :
        data={"name":user.name,
              "entries":user.entries}
        json.dump(data,f)
    print("journal saved")

def load_journal(filename="journal.json"):

    try:
        with open(filename,"r") as f:
            data=json.load(f)
            user=UserProfile(data["name"])#This creates a new user profile using the name found in the file (data["name"]).
            user.entries=data["entries"]#It gives the user back all their old journal entries from the file.
            return user #It sends back the full user object with name and saved entries
        
    except FileNotFoundError:


        print("journal not found")
        name=input("enter your name : " )
        return UserProfile(name)
    

def Suggest_activity(mood):
    advices={"Happy 😊" : "That's wonderful ,Keep smiling",
              "Sad 😒" : " Listen to music ",
              "Tired 😫" : "Take rest"}
    print("advice :",advices.get(mood))


# weekly mood summary
def weekly_summary(user):
    weekly_mood=list(user.entries.items())[-7:]#get last week (7) entries 
    moods=[mood for _,(mood,_)in weekly_mood] #creating list of mood skipping date and text

    count={}#making an empty dictionary,if mood is in dic we add to its count
    for mood in moods:
      if mood in count:
        count[mood]+=1
      else:
        count[mood]=1
    print("weekly mood summary : ")
    for mood,count in count.items():
      print(f"{mood} : {count} times a week .")



#export to txt file


def export_to_txt(user,filename="mood_journal.txt"):
    with open(filename,"w",encoding="utf-8")as f:#UTF-8 encoding, which supports all characters (including emojis)
        f.write(f"Mood jounal for {user.name} \n:")
        for date,(mood,text)in sorted(user.entries.items()):
            f.write(f"{date} ------{mood}:{text} \n ")
    print(f"journal saved to mood_journal.txt")
               


def main():
    user=load_journal()


    while True:
        print( "Mood Journal & Sentiment TracKER 🙂📘")
        print("1 .Add a Journal entry")
        print("2 .Show mood history")
        print("3. Show weekly summary")
        print("4 .Export to txt File")
        print("5 .Save Journal")
        print("6. Exit")


        choice=input("enter your choice:")

        if choice=="1":
            add_journal_entry(user)
        elif choice=="2":
            mood_history(user)
        elif choice=="3":
            weekly_summary(user)
        elif choice=="4":
            export_to_txt(user)
        elif choice=="5":
            save_journal(user)
        elif choice=="6":
            print("Good bye,have a nice day")
            break
        else:
            print("invalid choice")
main()
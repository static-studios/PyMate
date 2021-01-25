######################## Chatbot v1.0 ########################
import random
#### Lists ####
chat_dict = {"happy": "I'm happy as well!",
             "sad": "Cheer up!",
             "raspberry": "Oh, yum! I love rasberries",
             "music": "What is your favourite instrument?",
             "art": "That reminds me, where did I put my paintbrush?",
             "python": "Yeah! I'm coded in Python!",
             "stupid": "Who's stupid?",
             "weather": "Weather can be very un predictable!",
             "certain": "How can you be so confident?",",
             "hello": "Why, hello to you to buddy!",
             "very": "Yes. Very."
             
}

random_replies = ["Oh, really?",
                  "I'm not so sure.",
                  "Hmmmmmmm.",
                  "I'm not so sure I agree with that...",
                  "Definitely!",
                  "Maybe...",
                  "So what are you saying exactly?",
                  "Meaning what?",
                  "Your're probably right.",
                  "Rubbish! Absolute nonsense!",
                  "Anyways, what are your plans for tomorrow?",
                  "I was just thinking the exact same!",
                  "Alot of people have been telling me that!",
                  "Do you really think so?",
                  "Wonderful!",
                  "Indeed...",
                  "My point exactly!"]
#### Functions ####
def dictionary_check(message):
  message = message.lower()
  user_words = message.split()
  smart_replies = []
  for each_word in user_words:
    if each_word in chat_dict:
      answer = chat_dict[each_word]
      smart_replies.append(answer)
  if smart_replies:
    reply_chosen = random.randint(1, len(smart_replies)) - 1
    return smart_replies[reply_chosen]
  else:
    return ""

#### Main #### 
print("What would you like to talk about today?")
user_says = ""
while user_says != "bye.":
  user_says = ""
  while user_says == "":
    user_says = input("You:")
    
    smart_response = dictionary_check(user_says)
    if smart_response:
      print(smart_response)
    else:
      reply_chosen = random.randint(1, len(random_replies)) - 1
      print(random_replies[reply_chosen])
      
print("Goodbye.")      

# AI-CHATBOT-WITH-NLP

Name : Chekuri Jayasri

Intern ID : CT06DA115

Domain Name : Python

Duration : 6 weeks

Mentor : Neela Santosh Kumar

Description : This Python script implements a simple memory-based chatbot using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to provide context-aware responses. It starts by initializing a conversation log to store user inputs. The preprocess function tokenizes and lowercases the input using regular expressions to ensure clean text for analysis. When a user enters a message, it is appended to the conversation history. If it’s one of the first messages, the chatbot responds with a generic prompt to encourage further conversation. Once enough history is available, the chatbot uses TfidfVectorizer from sklearn to convert all messages into vector form. It then calculates the similarity between the current message and past inputs using cosine similarity. If a past input is sufficiently similar (above a set threshold), the chatbot acknowledges it and prompts the user to elaborate on the earlier topic. Otherwise, it continues with general follow-up prompts. This structure allows the chatbot to appear attentive and context-aware without relying on complex natural language processing models. The design is lightweight and suitable for basic conversational applications or as a learning project to understand how TF-IDF and similarity metrics can be applied in dialogue systems.

Output :

![Image](https://github.com/user-attachments/assets/c4f5f165-1ae9-4e25-bd0a-c3af8311a06f)



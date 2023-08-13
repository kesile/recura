# Tear - Trainable, autonomous, efficient routing.
Tear is a simple tool that allows you to easily and cheaply control the flow of information through LLM chains via automated classification. It provides routing via two methods, LLMs and Embeddings. Furthermore, you can train an LLM on a set of question and use embeddings thereafter. Let's demonstrate this by creating a simple router for movie related questions.
```
API_KEY = "sk-xxx... ...xxx"
myRouter = Tear(API_KEY)
```
First, we will initialize a Tear instance.

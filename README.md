# Chatbot
Victor - A generative ChatBot based on Sequential Neural Network and Deep Learning which can be trained on any desired dataset for specific purposes. Instead of ordinary ChatBots which are based on hard-coded responses, it can understand context and respond accordingly.

##Description
The fame of Deep Learning is at its epitome today. This here is a simple demonstration of what elementary level Deep Learning can achieve.
Our project, Victor is a generative chatbot that works on a sequential neural network. 

"Victor" represents one of the several possibilities that are possible by training a sequential neural network. Going into the specifications, it is constructed of three layers of the sequential neural network each containing 128 neurons. The encoder and decoder have a vocabulary size of 20,000 each. The corpus used for training is a collection of dialogues from 617 movies containing about 220,000 conversations (Cornell Movie Dialogue Corpus).  

The real "catch" about Victor is that it can be trained on any data we like, it can learn however we want it to. It gives contextual answers instead of hard-coded responses. It draws information from previous conversational exchanges and is thus, closer to how humans interact. The ability to be trained on any data is not only limited to English, it can be trained in any language we want it to any that is the real beauty of it. 

The bot performs extremely well on casual conversations that are prevalent in movies given the fact that we had a relatively short time to train it and thus, several parameters had to be compromised (number of neurons in each layer etc.). Talking about future improvements, we can train it on even a bigger dataset and use more layers or more number of neurons in each layer. Also, we could add the feature of training it simultaneously while using it which would further increase its accuracy with experience.

##Tools and Libraries used

- Tensorflow
- Tkinter
- PyCharm
- SublimeText

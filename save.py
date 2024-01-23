import os ## IMPORT OS

class SAVE():
    def Save(self, text, hash): ## save get text data and make a txt file
        with open('texts/' + str(hash) + '.txt', 'w') as f: ## SAVE FILE
            f.write(text) 

    def SaveQuiz(self, text, hash): ## save get text data and make a txt file
        with open('json/' + str(hash) + '.json', 'w') as f: ## SAVE FILE
            f.write(str(text)) 

import helper
import gold
def check_word_in_dict(word,words):
    if(words.get(word,0) == 0):
        return False
    else:
        return True

def m_function(m_content):
    temp = list(m_content)
    print(m_content)
    return {}
def parse_content(content):
    m_content = content.split('\n')
    m_list = []
    for i in m_content:
        temp = i.split(' ')
        new_temp =[value for value in temp if value != '']
        m_list.append(new_temp)
    m_dict = dict(m_list)
    # print(m_dict)
    return m_dict
    
def make_trie(word,value):
    m_dict = dict()
    m_first_node = m_dict
    count = 0
    for char in word:
        if(count == len(word) -1):
            m_dict[char] = {'$'+word:value}
        else:
            m_dict[char] ={}
            m_dict = m_dict[char]
            count = count + 1

    return m_first_node
    


def make_tree(words):
    m_dict = {}
    for key,value in words.items():
        m_words = []
        for i in range(0,len(key)):
            if(check_word_in_dict(m_words)
        
    return {}

def predict(tree, numbers):
    return {}


if __name__ == '__main__': 
    content = helper.read_content(filename='ngrams-10k.txt')
    parse_content(content)
    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)
   
    # PART 2: Building a trie from a collection of words.
    # tree = gold.make_tree(words)
    make_tree('locally',words)
    # while True:
    #     # PART 3: Predict words that could follow
    #     numbers = helper.ask_for_numbers()
    #     predictions = gold.predict(tree, numbers)

    #     if not predictions:
    #         print('No words were found that match those numbers. :(')
    #     else:
    #         for prediction, frequency in predictions[:10]:
    #             print(prediction, frequency)

    #     response = input('Want to go again? [y/N] ')
    #     again = response and response[0] in ('y', 'Y')
    #     if not again:
    #         break

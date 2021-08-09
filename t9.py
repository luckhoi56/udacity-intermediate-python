import helper
import gold
secret_tree = ''
def check_word_in_dict(word,words):
    if(words.get(word,0) == 0):
        return False
    else:
        return True

def m_function(m_content):
    temp = list(m_content)
    
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


    
def merge_trie(word,value,m_dict):
    count = 0
    for char in word:
        if(count == len(word) -1):
            if(m_dict.get(char) is None):
                m_dict[char] = {'$'+word:value}
            else:
                 m_dict[char] = {**m_dict[char],**{'$'+word:value}}
           
        else:
            if(m_dict.get(char) is None):
                m_dict[char] ={}
            
            m_dict = m_dict[char]
            count = count + 1
    return m_dict
def make_tree(words):
    m_dict = {}
    for key,value in words.items():
       merge_trie(key,value,m_dict)
    return m_dict


def make_pre_process_tree(words):
    m_dict = {}
    for key,value in words.items():
       pre_process_tree(key,value,m_dict)
    return m_dict
def pre_process_tree(word,value,m_dict):
    count = 0
    for char in word:
        if(char in ['a','b','c'] ):
            char = '2'
        if(char in ['d','e','f'] ):
            char = '3'
        if(char in ['g','h','i'] ):
            char = '4'
        if(char in ['j','k','l'] ):
            char = '5'
        if(char in ['m','n','o'] ):
            char = '6'
        if(char in ['p','q','r','s'] ):
            char = '7'
        if(char in ['t','u','v'] ):
            char = '8'
        if(char in ['a','b','c'] ):
            char = '9'
        if(count == len(word) -1):
            if(m_dict.get(char) is None):
                m_dict[char] = {'$'+word:value}
            else:
                 m_dict[char] = {**m_dict[char],**{'$'+word:value}}
           
        else:
            if(m_dict.get(char) is None):
                m_dict[char] ={}
            
            m_dict = m_dict[char]
            count = count + 1
    return m_dict
def predict(tree, numbers):
    print(numbers)
    count = 0
    m_keys = []
    for number in numbers:
        tree = tree[number] #keep traversing until the last one
        if(count == len(numbers) -1):
            keys = tree.keys()
            for key in keys:
                if(key[0] =='$'):
                    m_keys.append(key)
        count = count + 1
    return m_keys
if __name__ == '__main__': 
    content = helper.read_content(filename='ngrams-10k.txt')
    parse_content(content)
    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)
    
    # PART 2: Building a trie from a collection of words.
    # tree = gold.make_tree(words)
    tree = make_tree(words)
    m_pre_process_tree = make_pre_process_tree(words)
    # print(m_pre_process_tree)
    print(predict(m_pre_process_tree,'583'))
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

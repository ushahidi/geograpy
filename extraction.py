from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree
from newspaper import Article
from .utils import remove_non_ascii


class Extractor(object):
    def __init__(self, text=None, url=None):
        if not text and not url:
            raise Exception('text or url is required')

        self.text = text
        self.url = url
        self.places = []
    
    def set_text(self):
        if not self.text and self.url:
            a = Article(self.url)
            a.download()
            a.parse()
            self.text = a.text

    def find_entities(self):
        """ 
        Below modified code can also extract the label of each Name Entity from the text for cities like "New York"
        """
        self.set_text()
        chunked = ne_chunk(pos_tag(word_tokenize(remove_non_ascii(self.text))))
        current_chunk = []
        
        for subtree in chunked:
            if type(subtree) == Tree and (subtree.label() == 'GPE' or subtree.label() == 'PERSON') and subtree[0][1] == 'NNP':
                current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in self.places:
                    self.places.append(named_entity)
                    current_chunk = []
            else:
                continue

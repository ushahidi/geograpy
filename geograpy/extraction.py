import nltk
from newspaper import Article


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
        self.set_text()

        text = nltk.word_tokenize(self.text)
        nes = nltk.ne_chunk(nltk.pos_tag(text))

        for ne in nes:
            if type(ne) is nltk.tree.Tree:
                if (ne.label() == 'GPE' or ne.label() == 'PERSON' or
                        ne.label() == 'ORGANIZATION'):
                    self.places.append(u' '.join([i[0] for i in ne.leaves()]))

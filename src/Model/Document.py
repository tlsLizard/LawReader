import os

def clean_text(raw_text) :
    return raw_text.strip("\n")


class Document:
    def __init__(self, file_path='declaration1789.txt', head_length=2):
        self.file_name = os.path.basename(file_path)
        self.content = []
        self.head_length = head_length
        with open(file_path, "r") as file:
            for line in file:
                self.content.append(clean_text(line))
        self.head = self.content[:self.head_length]
        self.articles = self.content[self.head_length:]


    def __str__(self):
        return self.file_name


    def set_head_length(self, new_head_length):
         self.head_length = new_head_length


    def get_article(self, article_id):
        return self.articles[article_id - 1]


if __name__ == '__main()__':
    print("tests of document Class...")
    doc = Document(file_path='declaration1789.txt', head_length=2)
    print("head:", doc.head)
    print("body:", doc.articles)

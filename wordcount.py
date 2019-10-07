# put your code here.
# test_txt = open("test.txt")
# twain_txt = open("twain.txt")

def count_words(the_file):

    file = open(the_file)

    word_count = {}
    for line in file:
        line = line.rstrip()
        line_list = line.split()
        
        for word in line_list:
            word_count[word] = word_count.get(word, 0) + 1

    for word_count_item, count in word_count.items():
        print("{} {}".format(word_count_item, count))

    file.close()


count_words("test.txt")
# count_words("twain.txt")
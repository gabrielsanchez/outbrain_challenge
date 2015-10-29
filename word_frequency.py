"""
word_frequency.py
Gabriel Sanchez

Challenge:
Consider a list of sets of words (each set of words is called a record) and a
single set of words (called the query). For each word that is not in the query,
how many times does the word appear in all records that the entire query is 
present in? Output a dictionary of words to counts, omitting words with counts
of zero. Given a list of records and a list of queries, determine the output 
for each query with respect to the entire list of records.
"""

from json import dumps

class WordFrequency:

    frequencies = {}

    def print_frequencies(self, records_file, queries_file):

        try:
            records = open(records_file, 'r')
            queries = open(queries_file, 'r')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        
        temp_frequencies = {}

        #save all records/freqs in a dictionary
        for record in records:
            record_words = record.strip().split(',')
            for word in record_words:
                if word not in self.frequencies:
                    self.frequencies[word] = 1
                else:
                    self.frequencies[word] = self.frequencies[word] + 1
        
        #save the word and frequency in a new dictionary if it's in query
        #we delete temporarily and then restore it.
        for query in queries:
            query_words = query.strip().split(',')
            for word in query_words:
                if word in self.frequencies:                    
                    temp_frequencies[word] = self.frequencies[word]
                    del self.frequencies[word]
            self.output(self.frequencies)
            self.frequencies.update(temp_frequencies)

        records.close()
        queries.close()

    def output(self, dictionary):    
        print(dumps(dictionary, sort_keys=True))

if __name__ == "__main__":
    frequencies = WordFrequency()
    #frequencies.print_frequencies("records_test.txt", "queries_test.txt")
    frequencies.print_frequencies("records.txt", "queries.txt")

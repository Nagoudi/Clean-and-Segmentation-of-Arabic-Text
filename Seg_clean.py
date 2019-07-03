#!/usr/bin/python
# -*- coding:utf-8 -*-
import script
import sys
import re
import io
def break_into_sentences(corpus_file):
    f = io.open(corpus_file, 'r', encoding='utf8')
    Sentence_Size = 0
    Max_Size = 40  # Max_Size od the sentences
    paragraph = f.read()
	#remove_diacritics fct
    regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
    paragraph = re.sub(regex, '', paragraph)
    #remove_urls fct
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    paragraph = re.sub(regex, '', paragraph)
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    paragraph = re.sub(regex, '', paragraph)
	#remove one_character words
    regex = re.compile(r'\s.\s')
    paragraph = re.sub(regex, ' ', paragraph)
    resultFile = io.open("SEG_Output.txt", 'w',encoding='utf8')
    sentences = list()
    temp_sentence = list()
    flag = False
    for ch in paragraph.strip():
        if ch in [u'؟', u'!', u'.', u':', u'؛',u'?']:
            Sentence_Size = 0
            flag = True
        elif flag:
            sentences.append(''.join(temp_sentence).strip())
            temp_sentence = []
            flag = False
        regex = re.compile(r'[إأٱآا]')
        ch = re.sub(regex, 'ا', ch)
        regex = re.compile(r'[ئ]')
        ch = re.sub(regex, 'ى', ch)
        #remove_non_arabic_symbols fct
        ch = re.sub(r'[^\u0600-\u06FF]', ' ', ch)		
        temp_sentence.append(ch)
        if ch.isspace():
           Sentence_Size = Sentence_Size + 1
           if Sentence_Size > Max_Size:
              Sentence_Size = 0
              flag = True
              
    else:
        sentences.append(''.join(temp_sentence).strip())
        for item in sentences:
            resultFile.write("%s\n" % re.sub(' +', ' ', item))

if __name__ == '__main__':
    break_into_sentences(sys.argv[1])
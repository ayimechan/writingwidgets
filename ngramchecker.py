# a simple Ngram finder
# only feasible for 3.x version
# original text file must be plain text 

n=1  # min N
howmany = 5  # max N
outlength = 200
white_pounc = ['，','。','“','”','—','？','！','…','"',"'",'：','?','!','.',',']
file_raw = open('put full path to youre text file here','r',encoding='utf-8')
file_out = open('output file with or without full path','w',encoding='utf-8')
full_text = ''

for line in file_raw:  #read and remove punctuation (ok pounc is a typo)
    _ = line[:-1].strip().replace(' ','')
    for ch in white_pounc:
        if ch in _:
            _ = _.replace(ch, '')
    full_text+=_
file_raw.close()


def search_ngram(n,fulltext):
    start = 0
    d = {}
    while start<=len(fulltext)-n:
        text = fulltext[start:start+n]
        if d.get(text):
            d[text][0]+=1
        else:
            d[text] = [1, text]
        start+=1
    return d


while n<=howmany:
    file_out.write('====='+str(n)+'=====\n')
    d = search_ngram(n, full_text)
    values = list(d.values())
    values.sort(key=lambda x:x[0], reverse=True)
    outcount = 0
    for element in values:
        if element[1] not in white_list:
            countp = 0
            for p in white_pounc:
                if p not in element[1]:
                    countp+=1
            if countp==len(white_pounc):
                file_out.write(element[1]+'\t'+str(element[0])+'\n')
                outcount+=1
        if outcount>outlength:
            break
    n+=1
    file_out.flush()


file_out.close()

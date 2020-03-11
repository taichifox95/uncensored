'''
This python code transposes paragraphs in .txt files.
Please use it in command line. Please read readme.md, and do not change the code unless you know what you are doing.

Usage:
In command line, run:

python transpose_words.py --fname [path/to/your/file.txt]  --nrow [n]  --interval [""]  --direction ["right"/"left"]

E.g.:

python transpose_words.py --fname test1.txt  --nrow 15  --interval "|"  --direction "left"

input file test1.txt:
2019年12月30日，艾芬曾拿到过一份不明肺炎病人的病毒检测报告，她用红色圈出「SARS冠状病毒」字样，当大学同学问起时，她将这份报告拍下来传给了这位同是医生的同学。当晚，这份报告传遍了武汉的医生圈，转发这份报告的人就包括那8位被警方训诫的医生。

output file test1_transposed.txt:

2|拿|测|冠|时|位|告|报|的
0|到|报|状|，|同|传|告|医
1|过|告|病|她|是|遍|的|生
9|一|，|毒|将|医|了|人|。
年|份|她|」|这|生|武|就|
1|不|用|字|份|的|汉|包|
2|明|红|样|报|同|的|括|
月|肺|色|，|告|学|医|那|
3|炎|圈|当|拍|。|生|8|
0|病|出|大|下|当|圈|位|
日|人|「|学|来|晚|，|被|
，|的|S|同|传|，|转|警|
艾|病|A|学|给|这|发|方|
芬|毒|R|问|了|份|这|训|
曾|检|S|起|这|报|份|诫|


Details:

--fname: path to your file. Must be a txt file.
--nrow: rows of each transposed paragraph. Default = 10.
--interval: whether insert chars into words. 
--direction: the direction of the resulting text. Either "left" or "right"
'''




import os.path as osp
from pathlib import Path
import argparse
import time

def split_text(fname):
    '''
    input: 
        fname:  a string, contains the input file name.
                must be a .txt file.
    
    '''
    assert isinstance(fname, str)
    assert osp.isfile(fname)
    assert fname[-4:] == '.txt'
    with open(fname, 'rt',encoding='UTF-8') as in_file:
        text = in_file.read()
    assert isinstance(text, str)
    assert len(text) <= 65535
    splited_text = text.split('\n')
    return splited_text

def get_paragraph(line, ncol, interval, nrow = 10, direction = "left"):
    '''
    function that actuall transposes a line into a paragraph.
    '''
    #create rows:
    assert isinstance(line,str)
    assert isinstance(ncol,int)
    assert isinstance(nrow,int)  
    assert isinstance(interval,str)
    ls_rows = []
    for i in range(nrow):
        #create each line in transposed text
        ls_words = []
        for j in range(ncol):
            try:
                ls_words.append(line[j*nrow+i])
                if j < ncol - 1:
                    ls_words.append(interval)               
            except:
                pass
            #whether reverse
        if "right" == direction:
            ls_words.reverse()
            
        line_str = ''.join(ls_words) + "\n"

        ls_rows.append(line_str)
    parag_str = ''.join(ls_rows)
    return parag_str

def transpose_text(splited_text, interval, nrow = 10, direction = "left", truncate = False):
    '''
    for each line, execute get_paragraph
    '''
    assert nrow >=2
    assert isinstance(nrow, int)
    assert isinstance(splited_text,list)
    for line in splited_text:
        assert isinstance(line,str)
    
    trans_texts = []
    n_para = len(splited_text)
    for p in range(n_para):
        line = splited_text[p]
        line_len = len(line)
        if 0 == line_len:
            pass
        else:
            #decide the number of columns:
            if 0 == line_len%nrow:
                ncol = line_len//nrow
            else:
                ncol = line_len//nrow+1
            # truncate lines:
            

            if ncol >= 15 :
                print("Number of Rows for Paragraph {} too big, may not display very well.".format(p))
                
            
            
            trans_texts.append(get_paragraph(line,ncol,interval,nrow,direction))
    return trans_texts

def write_file(trans_texts,fname):
    '''
    write files.
    '''
    n_par = len(trans_texts)
    outname = fname[0:-4] + '_transposed.txt'
    long_str = str()
    for i in range(n_par):
        long_str += str(trans_texts[i]) + '\n'

    f = open(outname, 'wt')
    f.write(long_str)
    f.close()

def main():
    parser = argparse.ArgumentParser(
        description='This script converts text to horizontal')
    parser.add_argument('--fname', type=str, default=None,
                        help='path to the file you want to convert')
    parser.add_argument('--nrow', type=int, default=None,
                        help='number of rows you want in each paragraph')
    parser.add_argument('--interval', type=str, default="|",
                        help='interval Char, default = "｜" ')                      
    parser.add_argument('--direction', type=str, default="left",
                        help='read from left  or right, default left')
    parser.add_argument('--truncate', type=bool, default=False,
                        help='truncate parag that is too long. Default false.')        
    args = parser.parse_args()
    splited_text = split_text(args.fname)
    transed_text = transpose_text(splited_text, args.interval, args.nrow, args.direction, args.truncate)
    write_file(transed_text,args.fname)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Execution time: --- {} seconds ---".format( (time.time() - start_time)))

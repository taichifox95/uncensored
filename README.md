# UNCENSORED
## A project to f**k censorship

### Branch 1: Transpose Words

This python code transposes paragraphs in .txt files.


Usage:
In command line, run:
```
git clone https://github.com/taichifox95/uncensored
cd uncensored
python transpose_words.py --fname [path/to/your/file.txt]  --nrow [n]  --interval [""]  --direction ["right"/"left"]
```

E.g.:

```
git clone https://github.com/taichifox95/uncensored
cd uncensored
python transpose_words.py --fname test1.txt  --nrow 15  --interval "|"  --direction "left"
```

Example input file test1.txt:
```
2019年12月30日，艾芬曾拿到过一份不明肺炎病人的病毒检测报告，她用红色圈出「SARS冠状病毒」字样，当大学同学问起时，她将这份报告拍下来传给了这位同是医生的同学。当晚，这份报告传遍了武汉的医生圈，转发这份报告的人就包括那8位被警方训诫的医生。
```

Output file test1_transposed.txt (in the same directory):

```
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
```

Details:

```
--fname: path to your file. Must be a txt file.
--nrow: rows of each transposed paragraph. Default = 10.
--interval: whether insert chars into words. 
--direction: the direction of the resulting text. Either "left" or "right"
```
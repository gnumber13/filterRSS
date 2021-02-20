#!/bin/sh

aria2c http://www.crunchyroll.com/rss/anime?lang=deDE -o rss.1.xml && rm rss.xml
python3 parse.py > items/crunchyroll/$(date +%Y_%m_%d-%H_%M).xml 

cat header.xml >  feed
cat $(ls -td items/crunchyroll/*) >> feed
cat footer.xml >> feed


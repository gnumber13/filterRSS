#!/bin/sh

startPath=$(pwd)

cd /root/fetchRSS

rm items/crunchyroll/*
python3 parse.py

cat header.xml > feed
cat items/crunchyroll/* >> feed
cat footer.xml >> feed

cp feed /var/www/html/feeds/anime && echo "feeds updated" >> /root/cron.log

cd $startPath

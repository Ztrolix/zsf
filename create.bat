@echo off
title Ztrolix Cloud
cls

git add .
git commit -m "Add Heroku deployment files"
git push origin master

heroku create ZtrolixCloud

git push heroku master

heroku open
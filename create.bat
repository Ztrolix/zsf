@echo off
title Ztrolix Cloud
cls

git add .
git commit -m "Add Heroku deployment files"
git branch -m main
git push -u origin main

heroku create ZtrolixCloud

git push heroku master

heroku open
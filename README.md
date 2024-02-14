# launch_intellij_idea
Simple automation script that launches IntelliJ IDEA through desktop app on Linux. Initially python script was written, but bash one is simpler, so I left both. 
My IntelliJ idea had to be launched through 

``` 
cd /home/[user]/IntelliJ/ideaIU-2023.3.3/idea-IU-233.14015.106/bin
./idea.sh
```

As a lazy programmer, I added this script that launches the app, it can also be added into Desktop and Quick bar

Steps to install
```
git clone https://github.com/ali-gaineshev/launch_intellij_idea.git

cd launch_intellij_idea

nano/vi IntelliJ_IDEA.desktop
```

Input path to the file. Choose either python file (add python3 ...) or bash script. If want to see terminal, set it to true Find path to idea.sh, copy. 

Now either:  
```
nano/vi launch_idea.py / sh
replace path to Intelli J idea in the file
```
or if python file
```
nano/vi IntelliJ_IDEA.desktop

Add [path] argument in Exec (python)
```
![alt text](<Screenshot from 2024-02-14 10-55-56.png>)
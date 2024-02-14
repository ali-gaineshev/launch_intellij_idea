#!/usr/bin/env python3

import subprocess
import sys
import os

def main():
    args = sys.argv

    if(len(args) <= 1):
        print("using \"~/IntelliJ/ideaIU-2023.3.3/idea-IU-233.14015.106/bin/idea.sh\"")
        path = '~/IntelliJ/ideaIU-2023.3.3/idea-IU-233.14015.106/bin/idea.sh'
    else:
        path = args[1]

    idea_path = os.path.expanduser(path)
    try:
        subprocess.run(idea_path, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()

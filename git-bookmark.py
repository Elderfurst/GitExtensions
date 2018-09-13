import sys
import os

if 'read' in sys.argv:
    if not os.path.exists('.git'):
        print('fatal: Not a git repository: no .git directory')
        sys.exit(0)
    with open('.git/bookmark', 'r') as file:
        print(file.read())
elif len(sys.argv) != 2:
    print('Usage: git bookmark read || git bookmark \"Message to note your current progress\"')
else:
    if not os.path.exists('.git'):
        print('fatal: Not a git repository: no .git directory')
        sys.exit(0)
    message = sys.argv[1]
    with open('.git/bookmark', 'w+') as file:
        file.write(message)
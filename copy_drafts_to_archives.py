

import sys
import getopt
import os.path,time
import shutil

def __init__(self):
    self.drafts_path = ''
    self.posts_path = ''

def printHelp():
    print '''This software help you to copy file from _drafts to _posts.
-s --source /path/to/your/jekyll/dir'''

args = sys.argv[1:]
#print args

try:
    opts,args = getopt.getopt(args,'s:',['source='])
except getopt.GetoptError:
    printHelp()
    sys.exit(2)

for o,a in opts :
    if o in ('-s','--source'):
        if not os.path.exists(a) :
            print 'the path is not a dir'
            sys.exit(2)
        elif not os.path.exists(a+'/_drafts'):
            print 'the _drafts not exists'
            sys.exit(2)
        elif not os.path.exists(a+'/_posts'):
            print 'the _posts not exists'
            sys.exit(2)

    filelst = os.listdir(a + '/_drafts')

    for f in filelst:
        draft_name = a + '/_drafts/' + f
        splitext_file = os.path.splitext(draft_name)
        if splitext_file[-1] == '.done':
            ctime = time.gmtime(os.path.getctime(draft_name))
            print ctime
            ## move file to _posts
            new_file = '%s/_posts/%s-%s-%s-%s' % (a,ctime[0],ctime[1],ctime[2], splitext_file[0].split('/')[-1])
            #shutil.move(draft_name,new_file)

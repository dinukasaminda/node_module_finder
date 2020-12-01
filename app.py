import glob,os.path


root_dir  = "../"
pattern = "build"
# pattern = "node_modules"

founds = []

# flog= open("path.log", "w")
# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob(root_dir + '/*/*/*/*', recursive=True):
# for filename in glob.iglob(root_dir + '/*/'+pattern+'/*', recursive=True):
    # flog.write(filename)
    # print(filename)
   
    if  filename.endswith(".git") == True or filename.endswith(".gitignore")  == True or filename.endswith(".vscode")  == True:
        continue
    
    fileMatch =pattern in str(filename)
    filteredFilename= filename[:len(pattern)+filename.find(pattern)]

    # print(filteredFilename)

    if fileMatch == True:

        isSub=False
        for pv in founds:

            if filteredFilename in pv:
                isSub=True
                break
        if isSub== False:
            founds.append(filteredFilename)

f = open("path_"+pattern+"_.log", "w")
f.write("\n".join(founds))
f.close()
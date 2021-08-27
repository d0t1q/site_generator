import os
import shutil
from PIL import Image
import PIL
import glob

minpath="G:\\Minis\\"
web="G:\\Minis\\Web\\"
images=[]
webimages=[]
extensions=["jpg","png","jpeg"]

#Build Creator list from top level directories
for dirs in os.walk(minpath):
    creators=next(os.walk(minpath))[1]  


#Gather Top level Images
for root, dirs, files in os.walk(minpath):
    for file in files:
        for i in creators:
            if file.startswith("{}-".format(i)):
                if file.endswith(tuple(extensions)):
                    images.append(os.path.join(root, file))

#Check if Web Directory Exists
if not os.path.exists(web):
    os.makedirs(web)
#Copy Files to Web folder
for x in images:
    try:
        shutil.copy(x, web)
    except Exception:
        pass

#Compile web dir
i=0
for root, dirs, files in os.walk(web):
    for file in files:
        for i in creators:
            if file.startswith("{}-".format(i)):
                webimages.append(file)
#compress
images = [file for file in os.listdir(web) if file.endswith(tuple(extensions))]
for image in images:
    img = Image.open(web+image)
    img.save(web+image, optimize=True, quality=40)


#Build the website
#build index
f=open(web+"index.html","w")
f.truncate()
f.write("""<link rel="stylesheet" href="style.css">
<div class="container">
  <main>
<div class="image-mosaic"> """)
f.close()

f=open(web+"index.html","a")
for i in webimages:
    f.write("<div class=\"card card-tall card-wide\" style=\"background-image: url(\'{}\')\" onclick=\"window.location.href=\'{}\';\"></div>\n".format(i,i))
f.close()
f=open(web+"index.html","a")
f.write("""  </main>
  <aside> Creators:\n""")
for i in creators:
    f.write("<br>{}\r\n".format(i))
f.write(""" </aside>
</div> """)
f.close()


#generate css
f=open(web+"style.css","w")
f.truncate()
f.write(""".image-mosaic {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  grid-auto-rows: 240px;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #353535;
  font-size: 3rem;
  color: #fff;
  box-shadow: rgba(3, 8, 20, 0.1) 0px 0.15rem 0.5rem, rgba(2, 8, 20, 0.1) 0px 0.075rem 0.175rem;
  height: 100%;
  width: 100%;
  border-radius: 4px;
  transition: all 500ms;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 0;
  margin: 0;
}

@media screen and (min-width: 600px) {
  .card-tall {
    grid-row: span 2 / auto;
  }

  .card-wide {
    grid-column: span 2 / auto;
  }
}

.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 7%);
  height: 100px;
}

main, aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #FFFFFF;
}
aside {
  background: #81cfd9;
}""")
f.close()

import os
import shutil
from PIL import Image
import PIL
from tqdm import tqdm

minpath="Z:\\Minis\\"
web="Z:\\Minis\\Web\\"
images=[]
webimages=[]
extensions=["jpg","png","jpeg"]
ignore=["Notes", "Random", "Web"]


#Check if Web Directory Exists
print("Checking if Web Dir Exists")
if not os.path.exists(web):
    os.makedirs(web)
    print("Created Web Directory {}".format(web))
else:
  print("Web Director already exists")
  print("Removing old directory")
  shutil.rmtree(web)
  os.makedirs(web)
  print("Created Web Directory {}".format(web))

print("Gathering Creators")
#Build Creator list from top level directories
for dirs in tqdm(os.walk(minpath)):
    creators0=next(os.walk(minpath))[1]  
creators = [x for x in creators0 if x not in ignore]
print("Gathered {} different Creators".format(len(creators)))

#Gather Top level Images
print("Gathering Images from each creator")
for root, dirs, files in tqdm(os.walk(minpath)):
    for file in files:
        for i in creators:
            if file.startswith("{}-".format(i)):
                if file.endswith(tuple(extensions)):
                    images.append(os.path.join(root, file))
print("Gathered {} total images for Website".format(len(images)))                

#Copy Files to Web folder
print("Copying {} images to web directory".format(len(images)))
for x in tqdm(images):
    try:
        shutil.copy(x, web)
    except Exception:
        pass

#Compile web dir
i=0
print("Gathering Web directory paths")
for root, dirs, files in os.walk(web):
    for file in files:
        for i in creators:
            if file.startswith("{}-".format(i)):
                webimages.append(file)

#gather size of directory
sizeod = sum(d.stat().st_size for d in os.scandir(web) if d.is_file())
sizeod = sizeod/1024/1024
#compress+thumbnail 
images = [file for file in os.listdir(web) if file.endswith(tuple(extensions))]
print("Comrpessing and converting Images")
print("Size of web directory before comrpession: {:0.2f} MB".format(sizeod))
for image in tqdm(images):
    img = Image.MAX_IMAGE_PIXELS = None
    img = Image.open(web+image)
    img.thumbnail([1920, 1920],PIL.Image.ANTIALIAS)
    img = img.convert('RGB').save(web+image,"JPEG", optimize=True, quality=80)
    #img.save(web+image, optimize=True, quality=80)
sizeod = sum(d.stat().st_size for d in os.scandir(web) if d.is_file())
sizeod = sizeod/1024/1024
print("Size of web directory after comrpession: {:0.2f} MB".format(sizeod))

#Build the website
#build index
print("Writing Index file")
f=open(web+"index.html","w")
f.truncate()
f.write("""<link rel="stylesheet" href="style.css">
<div class="image-mosaic"> """)
f.close()

f=open(web+"index.html","a")
for i in webimages:
  f.write("<div class=\"card card-tall card-wide\" style=\"background-image: url(\'{}\')\" onclick=\"window.location.href=\'{}\';\"></div>\n".format(i,i))
f.close()

#generate css
print("Generating CSS")
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
print("COMPLETED")

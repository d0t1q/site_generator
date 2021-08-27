# site_generator
**Windows OS**

Generates a website based subfolders and release images for my miniature collection 

requires pillow
```
pip3 isntall -r requirements.txt
```

usage: ./imageBuilder.py

be sure to set your relative paths in code

minpath="G:\\\Minis\\\\"

web="G:\\\Minis\\\Web\\\\"

Collection directory must be structured as follows: 

```
Drive:.
├───ArchVillain - (creator name)
│   ├───Agama_Rising - (release folder, this isn't important)
│   └───ArchVillain-Agama_Rising.png (Release image, MUST start with "creator-" and is case sensitive based on the parent folder name)
```

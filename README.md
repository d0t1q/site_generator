# site_generator
**Windows OS**

Generates a website based on subfolders and release images from miniature collections
requires pillow
```
pip3 install -r requirements.txt
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

**Result**
![example](https://github.com/d0t1q/site_generator/blob/main/example.jpg?raw=truee)


**Too Doo**

Add the ability to auto-rename image files to match parent folders 

# site_generator
**Windows OS**

Generates a website based on subfolders and release images from miniature collections
requires pillow
```
pip3 install -r requirements.txt
```

usage: 
```
./imageBuilder.py
```
be sure to set your relative paths in code
```
minpath="Z:\\\Minis\\"

web="Z:\\Minis\\Web\\"
```
Update the ignore list incase you have any directories that should be ignored 
```
ignore=["Notes", "Random", "Web"]
```
Collection directory must be structured as follows: 

```
Drive:.
├───ArchVillain - (creator name)
│   ├───Agama_Rising - (release folder, this isn't important)
│   └───ArchVillain-Agama_Rising.png (Release image, MUST start with "creator-" and is case sensitive based on the parent folder name)
```

**Result**

Output of script 

![image](https://user-images.githubusercontent.com/8010159/142051541-c7482ba1-637f-41ab-bc66-72d8b9796b99.png)


Example Website generated

![example](https://github.com/d0t1q/site_generator/blob/main/example.jpg?raw=truee)


**Too Doo**

Add the ability to auto-rename image files to match parent folders 

***Updates***

20211003:
* Added in compression and thumbnail pictures rather than linking directly to possibile 4K/8K images, this resulted in a 75% reduction in content size
* Added in an ignore list so that certain folder names don't get included in the creator generation section 

20211018:
* Added output to state what script is currently doing 
* Added pil method to convert image to 'RGB' - will hopefuly remove any unneeded alpha data. 
* Added TQDM progress bar output
* Removed glob library as its not in use
* Fixed the Ignore method as it wasn't properly implimented

20211116:
* Modified Compression settings, pil method now converts to JPEG - This resulted in a 90% decrease in overal directory size
* Updated logic to first remove any pre-existing Wed directory before executing
* Removed side banner

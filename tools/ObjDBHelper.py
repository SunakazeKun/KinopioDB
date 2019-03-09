from time import gmtime, strftime
import os
import json


#----------------------------------------------------------------------------------
#
# This sets up the basic JSON file for an object.
#
#----------------------------------------------------------------------------------
def init_object(internalName, className):
    data = {}
    data["InternalName"] = internalName
    data["ClassName"] = className
    data["Name"] = internalName
    data["List"] = "ObjectList"
    data["Category"] = "unknown"
    data["Notes"] = ""

    outf = open(internalName + ".json", "w")
    outf.write(json.dumps(data, indent=4))
    outf.flush()
    outf.close()


#----------------------------------------------------------------------------------
#
# This sets up the basic JSON file for each element in the given file of object
# names. The strings in the input file should be structured like this:
#  "UnitConfigName" "ParameterConfigName"
#
#----------------------------------------------------------------------------------
def init_objects(filepath):
    with open(filepath) as f:
        objs = f.readlines()
    objs = [x.strip() for x in objs]
    
    for obj in objs:
        splitName = obj.split(" ")
        
        unitConfigName = splitName[0]
        parameterConfigName = splitName[1]
        
        init_object(unitConfigName, parameterConfigName)


#----------------------------------------------------------------------------------
#
# This will compile all single object files in the given directory into a huge list
# of objects.
#
#----------------------------------------------------------------------------------
def build_objects(dirpath, destpath):
    data = {
        "Statistics": {},                # some statistics on the object database
        "Classes": {},                   # each available object class
        "Objects": {},                   # contains every object structure
        "Categories": {}                 # categorizes every object alphabetically
    }

    statistics = data["Statistics"]
    classes = data["Classes"]
    objects = data["Objects"]
    categories = data["Categories"]

    objpath = dirpath + "/Objects"
    classpath = dirpath + "/Classes"
    
    # Populate and initialize categories
    cats = json.load(open(dirpath + "/Categories.json", "r"))
    
    for catname, catdict in cats.items():
        print("-- Processing category " + catname + " ...")
        
        categories[catname] = catdict
        
        if "Objects" not in catdict:
            catdict["Objects"] = []

    # Process classes
    for classdir in os.listdir(classpath):
        classfile = classpath + "/" + classdir
        if not os.path.isfile(classfile):
            continue

        clazz = json.load(open(classfile, "r"))

        if not "ClassName" in clazz:  # make sure we load classes
            continue

        classname = clazz["ClassName"]
        print("-- Processing class " + classname + " ...")
        classes[classname] = clazz

    # Now, add each object
    for objdir in os.listdir(objpath):
        objfile = objpath + "/" + objdir
        if not os.path.isfile(objfile):
            continue

        obj = json.load(open(objfile, "r"))
        
        if not "InternalName" in obj:  # make sure we load objects
            continue
        
        internalName = obj["InternalName"]
        category = obj["Category"]

        objects[internalName] = obj
        print("-- Processing object " + internalName + " ...")
        
        if category in categories:
            categories[category]["Objects"].append(internalName)
    
    # Sort category objects, just to be safe
    for catname, catdict in categories.items():
        catdict["Objects"].sort()
    
    statistics["BuildDate"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    statistics["NumClasses"] = len(classes)
    statistics["NumObjects"] = len(objects)
    statistics["NumCategories"] = len(categories)
    
    # Finally, store all the data
    outf = open(destpath, "w")
    outf.write(json.dumps(data, indent=4))
    outf.flush()
    outf.close()
    
    print("-- Done")

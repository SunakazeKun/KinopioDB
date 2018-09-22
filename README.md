# KinopioDB
A public modding database for **Captain Toad Treasure Tracker** (Switch and 3DS ports). Here, we collect information regarding every object or stage in the game. The tools require **Python3.X**.

# Objects
Each object has a corresponding JSON file storing its properties in a structured style. These files are rather simple to set up and edit. Here's an example of *Moamoa*:
```
{
    "InternalName": "Moamoa",
    "ClassName": "MoamoaHolder",
    "Name": "Blurker",
    "List": "ObjectList",
    "Category": "enemy",
    "Description": "A rare pink block-like enemy. It will temporarily disappear when pointed at. While exclusive to the Wii U version, it works just as fine in the ports.",
    "Properties": {
        "DepthNum": "Int32",
        "HeightNum": "Int32",
        "IsHideShadow": "Boolean",
        "UsingDepthShadow": "Boolean",
        "WeakWaitStep": "Int32",
        "WidthNum": "Int32"
    },
    "Models": [],
    "Links": []
}
```

## Fields
| Field | Description |
| ----- | ----------- |
| InternalName | Internal object name (*UnitConfigName*) |
| ClassName | Internal class name (*ParameterConfigName*) |
| Name | Descriptive name |
| List | Preferred object list (*ObjectList*, *AreaList*, ...) |
| Category | Category the object belongs in (for browsing purposes) |
| Description | Description of the object's functionality and use |
| Properties | Dictionary of additional object properties |
| Models | List of usable models |
| Links | List of compatible links |

### List
The game utilizes the following types of object lists:

| List | Description |
| ---- | ----------- |
| ObjectList | Any kind of object. |
| SkyList | Level backdrops. |
| AreaList | Area controllers. |
| PlayerList | Player spawn points, etc. |
| CheckPointList | Player respawn controllers. |
| GoalList | Power stars and related objects. |
| DemoObjList | Cutscene objects. |
| ZoneList | Locations of level chunks. |
| Objs | Unknown. Always empty. |
| Rails | Paths. Always empty. |

### Categories
Object categories are defined in **objects/_Categories.json**. The key is usually referenced in the object's *Category* field. When compiled, it is assigned the list *Objects* which stores the name of every object it categorizes. The format is rather simple and self-explanatory; here are some examples:
```
...
	"enemy": {
		"Name": "Enemies"
	},
	"boss": {
		"Name": "Bosses"
	},
	"item": {
		"Name": "Items"
	},
...
```

### Properties
Properties can be of the following supported value types:
* **Boolean**
* **Int32**
* **UInt32**
* **Single**
* **In64**
* **UInt64**
* **Double**
* **String**
* **List**
* **Dictionary**

## Common Properties & Links
A couple of properties and link types are shared by every object and may not be included as part of object definitions.

### Properties
| Property | Type |
| -------- | ---- |
| Comment | String |
| Id | String |
| IsLinkDest | Boolean |
| LayerConfigName | String |
| Links | Dictionary |
| ModelName | String |
| Rotate | Dictionary |
| Scale | Dictionary |
| Translate | Dictionary |
| UnitConfig | Dictionary |
| UnitConfigName | String |

### Links
* **GroupClipping**
* **Rail**
* **ViewGroup**

# KinopioDB
A public modding database for **Captain Toad Treasure Tracker** (Switch and 3DS ports). Here, we collect information regarding every object, stage and more in the game. The tools require **Python 3**.

# Objects
Each object has an associated JSON file storing information about its properties. These files are rather simple to set-up and edit. Here's an example of *Moamoa*:
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
The game uses lists to order objects. The following lists are supported:

| List | Description |
| ---- | ----------- |
| ObjectList | Any kind of object |
| SkyList | Level backdrops |
| AreaList | Area controllers |
| PlayerList | Player spawn points, etc. |
| CheckPointList | Player respawn controllers |
| GoalList | Power stars and related objects |
| DemoObjList | Cutscene objects |
| ZoneList | Locations of level chunks |
| Objs | Unknown; always empty |
| Rails | Paths; always empty |

### Categories
Object categories are defined in **objects/_Categories.json**. The key is usually referenced in the object's *Category* field. When building the object database it is assigned the list *Objects* which stores the name of every object it categorizes. As usual, the format is self-explanatory; here are some examples:
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
* **Int64**
* **UInt64**
* **Double**
* **String**
* **List**
* **Dictionary**

## Common Properties & Links
A handful of properties and link types are shared by every object and may not be included as part of object definitions.

### Properties
| Property | Type | Used |
| -------- | ---- | ---- |
| Comment | String | no |
| Id | String | yes |
| IsLinkDest | Boolean | no |
| LayerConfigName | String | no |
| Links | Dictionary | yes |
| ModelName | String | yes |
| Rotate | Dictionary | yes |
| Scale | Dictionary | yes |
| Translate | Dictionary | yes |
| UnitConfig | Dictionary | yes |
| UnitConfig:DisplayName | String | yes |
| UnitConfig:DisplayRotate | Dictionary | ? |
| UnitConfig:DisplayScale | Dictionary | ? |
| UnitConfig:DisplayTranslate | Dictionary | yes |
| UnitConfig:GenerateCategory | String | no |
| UnitConfig:ParameterConfigName | String | yes |
| UnitConfig:PlacementTargetFile | String | no |
| UnitConfigName | String | yes |

### Links
* **GroupClipping**
* **Rail**
* **ViewGroup**

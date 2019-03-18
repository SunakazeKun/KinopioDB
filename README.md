# KinopioDB
**KinopioDB** is a public modding database for **Captain Toad Treasure Tracker** (Switch and 3DS ports). Here you can find any information regarding every object, stage and more in the game. You may contribute to this database by sharing your findings.
The tools require **Python 3**.

# Objects
Each object's information is stored in a corresponding JSON file which consists of these properties:

| Field | Description |
| ----- | ----------- |
| InternalName | Internal object name (*UnitConfigName*) |
| ClassName | Class name (*ParameterConfigName*) |
| Name | Descriptive name |
| List | Preferred object list (*ObjectList*, *AreaList*, ...) |
| Category | Category the object belongs in (for browsing purposes) |
| Notes | Notes on the object's functionality and usage |

Here's an example of *Moamoa*:
```
{
    "InternalName": "Moamoa",
    "ClassName": "MoamoaHolder",
    "Name": "Blurker",
    "List": "ObjectList",
    "Category": "enemy",
    "Notes": ""
}
```

### List
*Treasure Tracker* uses different lists to sort objects. The following lists are supported by the game:

| List | Description |
| ---- | ----------- |
| ObjectList | Any kind of object |
| SkyList | Level backdrops |
| AreaList | Area controllers |
| PlayerList | Player spawn points, etc. |
| PlayerPlacementList | Player 2 placement |
| PlayerMPPlacementList | Player 1 placement(?) |
| CheckPointList | Player respawn controllers |
| GoalList | Power stars and related objects |
| DemoObjList | Cutscene objects |
| ZoneList | Locations of level chunks |
| Objs | Generic objects; always empty |
| Rails | Paths; always empty |

### Categories
Object categories are defined in **Categories.json**. The key is referenced in an object's *Category* field. When creating the object database it is also assigned the list *Objects* which stores the name of every object it categorizes. As usual, the format is self-explanatory; here are some examples:
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

# Classes
| Field | Description |
| ----- | ----------- |
| ClassName | Internal class name (*ParameterConfigName*) |
| Properties | Dictionary of additional object properties |
| Models | List of usable models |
| Links | List of compatible links |

Here's an example of GoalItem:
```
{
    "ClassName": "GoalItem",
    "Links": [
        "SwitchAppear",
        "SwitchGotOn",
        "ViewGroup"
    ],
    "Models": [
        "GoalItem",
        "GoalItemCrown",
        "GoalItemCrownDLC",
        "GoalItemSuperCrown",
        "GreenStarGoalItem",
        "ShineGoalItem"
    ],
    "Properties": {
        "AppearAnimName": "String",
        "ColorType": "Int32",
        "DisableGetCount": "Int32",
        "IsConnectToCollision": "Boolean",
        "IsDisableGetAtMove": "Boolean",
        "IsExpandClippingShadowLength": "Boolean",
        "IsInvalidClipping": "Boolean",
        "IsNoDepthShadow": "Boolean",
        "ShadowLength": "Single",
        "UsingOccludedEffect": "Boolean"
    }
}
```

## Properties
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

## Common properties
A handful of properties are shared by all objects and should not be included as part of class definitions. Some properties don't appear to be used anyway and may be useless.

| Property | Type | Used |
| -------- | ---- | ---- |
| Comment | String | ? |
| CubeMapUnitName | String | yes |
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
| UnitConfig:DisplayRotate | Dictionary | no |
| UnitConfig:DisplayScale | Dictionary | yes |
| UnitConfig:DisplayTranslate | Dictionary | yes |
| UnitConfig:GenerateCategory | String | no |
| UnitConfig:ParameterConfigName | String | yes |
| UnitConfig:PlacementTargetFile | String | yes |
| UnitConfigName | String | yes |


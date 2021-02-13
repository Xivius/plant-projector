# Plant Projector

#### TreeHacks 2021 Project by Noah and Jack

An app that uses AR to show a plant's projected future based on multiple factors. Not all factors can be accounted for in the prototype, but as many as possible will be included. Here are some factors to consider:

* Weather (tough to factor due to unpredictability)
  * Precipitation
  * Temperature
  * Cloudiness (blocks out the sun)
* Location and Date
  * Season and time of year
  * Regional climate generalization
* Plant type & characteristics
  * Appearance over the stages of life
  * Lifespan
  * Species (e.g. what kind of tomato?)
  * Current age (The time lapse between the last recorded session will help)
  * Pollination required (are there bees in the area for instance)?
* Current circumstances
  * Going on a trip?
  * Watering it this much? (may have to ask the user for this info)
  * In the shade or out in the sunlight? (have to use latitude and time for this one. sun rises in the east and sets in the west can be used to determine how much light the plant is actually getting)
  * Appearance of pests and wild animals

To see the plant overtime, a time meter will be placed that the user can drag to see the plant's future if things kept going the way they are. The more recently and frequently the predictions are taken, the more accurate the current projection will be. Initially, the plant data will be sourced from online farmer's guides. Overtime, data collected will be aggregated and stored in a large database.

For the level of future accuracy to improve, many different scenarios will need to be mapped with variables and circumstances being recorded. This current repo will feature a demo using a cherry tomato. It may be discovered that for certain plant species, specific factors determine success more than others. This whole app is just one large data collecting experiment.
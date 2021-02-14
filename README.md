# Plant Projector

#### TreeHacks 2021 Project by Avdhesh, Jack, and Noah

### General Concept

Plant Projector is an app for inexperienced gardeners that predicts a plant's future based on the weather forecast. It uses image classification (photo taken from phone) to identify the plant and determine its ideal temperature range. Afterwards, based on the current weather and forecasted weather, the app gives a prediction on the quality of the plant's health and/or yield in the given days. The initial plant-specific information is provided by farmer's guides online, who have much more knowledge and wisdom in this matter. Obviously, there are many other factors that contribute to a plant's health. Due to time constraints, this prototype only accounts for weather. See the future plans for details on how the app can improve.

This current repo will feature a demo using tomatoes.

### Future Plans

We plan to include a feature that allows one to see the plant's projection over time period. A time meter that the user can drag would indicate the plant's predicted state at a specific moment assuming things remain as is.

For the level of future accuracy to improve, predictions must be taken more frequently or recently. As mentioned before, the initial plant data is sourced from online farmer's guides. Overtime, data will be collected, aggregated, and stored in a large database for further processing. Many different scenarios will need to be explored and more variables mapped to gain a more accurate idea of what specific factors determine success of a plant more than others. Here are more factors to consider tracking in the future:

* Weather
  * Precipitation
  * Temperature
  * Cloudiness (blocks out the sun)
* Location and Date
  * Season and time of year
  * Regional climate generalization
* Plant type & characteristics
  * Appearance over the stages of life
  * Ideal temperature
  * Lifespan
  * Species (e.g. what kind of tomato?)
  * Pollination requirements (e.g. bees?)
* Current circumstances
  * Plant's current age
  * Gardener going on a trip?
  * Amount being watered (may have to ask the user for this info)
  * Time in the shade vs sunlight (have to use latitude and time for this one. sun rises in the east and sets in the west can be used to determine how much light the plant is actually getting)
  * Appearance of pests and wild animals

### Usage

1. Run  `pip install -r requirements.txt` to install necessary dependencies
2. Run `python server.py` to start the server

### Sources

1. https://www.kaggle.com/andrewmvd/tomato-detection (data set)
2. https://www.kaggle.com/gverzea/edible-wild-plants (data set)
3. http://www.omafra.gov.on.ca/english/crops/facts/info_tomtemp.htm (general info)
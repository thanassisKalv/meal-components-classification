# meal-components-classification
menu components classification to *ontology concepts*

This is meant to take raw input (textual - i.e. tags or annotation) in e.g. a menu, a supermarket product, or even a system recipe and through the NUTRIUM DBs classify the components to ontology concepts (food's category and style of cooking)


## to do
```diff
#E.g. if the meal includes "tomato" and tomato is in the ontology, then it's fine, a simple direct classification will be performed. But if the meal includes "spinach" and spinach does not exist in the ontology per se, but it can be tracked to the group "dark leafy green vegetables", which is a category in the Nutrium DBs *and* an ontology concept, then the meal classification will contain dark leafy greens.

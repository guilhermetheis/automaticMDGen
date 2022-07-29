# automaticMDGen for Jekyll posts

This script intents to automatize the flow for a new Jekyll post. Currently I'm figuring out this for my own [Github Pages Website](https://github.com/guilhermetheis/guilhermetheis.github.io). The idea is pretty simple, there should be three different applications.

1) Create a simple Front Matter ready .md by simply requiring the Title.
2) Create a simple post that should include Front Matter and some kind of body, ideally something like an image with caption. Where the image and caption would also be automatic
3) Finally the last step of the project is to add the capability of safely pushing this .md to the github pages repo (and posting)

## Current codes to base of

I've done a quick run down in google and found [Kris van der Mast](https://www.krisvandermast.com/post/2022/03/08/python-script-to-generate-a-new-jekyll-post-with-front-matter.html) post on something similar. I also thought that [mdutils](https://github.com/didix21/mdutils) would be an option, but it might be too strict to "normal" markdown usage, making the creation of the **Front Matter** hard. 
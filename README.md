# automaticMDGen for Jekyll posts

This script intents to automatize the flow for a new Jekyll post. Currently I'm figuring out this for my own [Github Pages Website](https://github.com/guilhermetheis/guilhermetheis.github.io). The idea is pretty simple, there should be three different applications.

* ~~Create a simple Front Matter ready .md by simply requiring the Title.~~
  
    1. Verify if first letter is upper cased
* Create a simple post that should include Front Matter and some kind of body, ideally something like an image with caption. Where the image and caption would also be automatic
* Finally the last step of the project is to add the capability of safely pushing this .md to the github pages repo (and posting)

## Current codes to base of

I've done a quick run down in google and found [Kris van der Mast](https://www.krisvandermast.com/post/2022/03/08/python-script-to-generate-a-new-jekyll-post-with-front-matter.html) post on something similar. I also thought that [mdutils](https://github.com/didix21/mdutils) would be an option, but it might be too strict to "normal" markdown usage, making the creation of the **Front Matter** hard. 

**Kris van der Mast** outputs the following Front Matter

```
---
layout: post
title: Python script to generate a new Jekyll post with front matter
date: 2022-07-29 07:59:46 +0200
comments: true
published: true
categories: ["post"]
tags: ["jekyll","python","front matter"]
author: Kris van der Mast
---
```

But it requires a big input to run such as the following

```
py .\createMarkdown.py 2022-07-29 “Python script to generate a new Jekyll post with front matter” “jekyll python front_matter”
```

We'd like to take the date automatically as we use the script and keep only the title. As we have the `layout: post` as a default we can also remove, as well for `published` and `comments`. The attributes `categories` and `tags` should be custom, so it should not be set within this, only created in order to allow us to modify it (i.e: `categories: [""]`.

# Create a simple Front Matter ready .md by simply requiring the Title

To first run this I simply took the code from **Kris van der Mast** and updated it to automatically get the current date and also accept `categories` as my website allows for multiple categories. I need to update the function `format_cat` to check if the first letter of each word is upper cased or not. The code is extremely similar from Kris, but the end goal should differ/improve uppon it. 

This was firstly in the commint from 29/07/2022
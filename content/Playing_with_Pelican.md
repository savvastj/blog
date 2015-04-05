Title: Playing around with Pelican, Plugins, and Markdown
Date: 2015-04-06 07:00
Category: Blog
Author: Savvas Tjortjoglou
Tags: Python, Pelican, Plugins

<center>{% img [Pelican] http://t0.gstatic.com/images?q=tbn:ANd9GcQ7FPifj2hTdhQaRZ1FDuCkpK-jOR04ns7W4f71Kbo8ebNLC1rS [40 [22]] [] %}</center> 

I'm just testing out the variety of plugins I've installed for this blog as well as playing around with Markdown syntax.

I've added the summary and liquid tags plugins. 

I could also use footnotes using markdown syntax.[^1]  However the navbar blocks the sentence when I jump back from the footnote.  Not sure how I will fix that or if I will.

<!-- PELICAN_END_SUMMARY -->

[^1]: Like this


# Embedding Youtube and Vimeo Videos Using Liquid Tag Plugin

## Youtube

I'll embed a youtube video with the following:

	{% literal youtube vwC1rhjzmRg [width] [height] %}

And here it is:

{% youtube vwC1rhjzmRg [width] [height] %}


## Vimeo

Now let's try it with vimeo and centered: 

	<center>{% literal vimeo 14912890 [width] [height] %}</center>

<center>{% vimeo 14912890 [width] [height] %}</center>

### Favorite GIF of the playoffs

{% img [Lance] https://espngrantland.files.wordpress.com/2014/05/lance-blowin-cutoff-on-the-eye-contact.gif [width [height]] [] %}


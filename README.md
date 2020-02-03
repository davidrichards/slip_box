# Slip Box
> Summary description here.


Here is the idea:

* read with a pen (pencil is fine)
* take temporary notes
* curate permanent notes
* keep citations

Why? It's easier to focus. I'm more productive. I'm more creative. I'm more collaborative. Hard problems have well-known and tractable research approaches that break things down and give me a reusable mindspace. It's kind of cool. The practice comes from Niklas Luhmann's prolific academic career and is well-explained in Sönke Ahrens' book, [How to Take Smart Notes](https://takesmartnotes.com/).

Why not use one of the million existing and really good note systems? I've used many of them, and they're very good at getting the information collected, but not as good at using it again when curating my notes or preparing an early draft of an article. For the last year or two I've written scripts to make it easier to store plain-text notes from the command line. This project is an upgrade to those scripts.

Why not use Jupyter Notebooks or blog articles? I find that a humble note is more likely to be useful than a finished product. I tend to protect something that took a lot of effort to build, like a data demonstration. The notes in there feel precious. I'm not likely to dig through them and reuse parts, or change them when I'm working on an article. If the notes are simple, they don't get in my way.

What I do to make things useful is:

* index my notes with a filename, e.g. 1.a.tell_it_like_it_is.md
* keep plain-text notes in a backed up volume (like a Dropbox or Google Drive volume)
* ensure I can search my notes
* create an outline that I can export as an early draft for an article

## Install

`pip install slip_box`

## How to use

Fill me in please! Don't forget code examples:

```
1+1
```




    2



## TODO

* Indexes
* Config
* Paths
* Store Files
* Search
* CLI
* Deploy

### Indexes

Mostly done, but need to fix a few bugs and move it to nbs. There are notes in that notebook.

### Config

I'll want to write a default configuration, make it available in the imports, and create utilities to read and write these files generally.

ConfigParser is part so this. So is the nbdev stuff. I can see a copy in the data_lab of what was done in nbdev.

Because this is going to imports, develop it in experiments instead of nbs.

### Paths

Deal with Paths:

* pathlib
* os
* s3fs
* minio

I don't need to handle all of these, but since the data_lab will, I might as well solve it and then figure out where things go.

I'd also like to find a way to split the index from the filename by either changing naming conventions, or doing something else that's smart.

It's possible my indexes code, filename generation needs to be target sensitive, meaning I don't write files to S3 that are illegal, I use subdirectories in smart ways, if I go there, and generally push the details down.

### Store Files

Storing files includes taking the title, index, body, and citation, applying a template, and writing a note.

Templating is generally important for writing and reading data. I'll pull outlines in a tree structure with a template as well.

### Search

I'll likely just store a search index and wrap something for now.

For notes, it's mostly just a full-text index. For some things, I may want the parent/child relationships to come into it. Also, it would be good to get a synonym driver, if not a full deep index implemented.

Mostly for what I'm doing, it's just a shell and something simple.

The cloud hosting for notes would change what's available/best. Article drafts change this as well. Rebuilding is critical, for a stable index.

I may want sqlite in this project, so I can get some of the tabular summarization going. If so, those values could be added as well.

It's possible that a queue would be smart for processing the indexing. Or, simply a processing scheme that I like.

### CLI

The CLI should include at least:

* list/ls
* add/put
* remove/rm
* search

I'd like to keep state and some history here, so it's easier to call things. That means I could just add a file, and it would be the next index, or specify child, and it just works.

Because I was using a shared volume and file system modified timestamps to work with recency and state, I could get some hinky results. This is another argument for using sqlite instead of a filestysem--to manage state more cleanly.

Version 2 also had:

* recent
* get
* append
* append-list
* export

### Deploy

I'd like to get something into PyPi today, then maintain this a little each week until I've created something I can't get anywhere else. My current (private) version is much better than anythign I can get from Zettelkasten or many of the other slip tools. I like iaWriter for some things, and others use notes, but nothing is a full package.

I'm purposefully avoiding the outlining for a bit, just get notes, I'll curate and export them later.

Also, this should use a GUI at some point, or a web app, or something.

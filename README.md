# BOOKMARK's Management in CLI

This is an app that lets you keep bookmarks of your books located in different files from the CLI.

[BOOKMARK's Management in CLI](#bookmarks-management-in-cli)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setup](#setup)
  - [Demo](#demo)
  - [Commands](#commands)
    - [bm](#bm)
    - [initbm](#bm)
    - [delbm](#delbm)
    - [addbm](#addbm)
    - [gotobm](#gotobm)

## Prerequisites

Only works on **Linux** or by using **WSL 2**.

## Installation

`git clone https://github.com/georgevanuta/Bookmarks-CLI-app`

## Setup

*Firstly*, modify the path to the **BOOKS_FILE** and **BOOKMARKS_FILE**.

*Then*, add the following lines at the bottom of your **~/.bashrc** file:
`PATH_SCRIPTS_BM='/mnt/e/Programming/BOOKMARK-CLI/Scripts'`\
`alias bm="$PATH_SCRIPTS_BM/print_bookmarks.py"`\
`alias initbm="$PATH_SCRIPTS_BM/init_bookmarks.py"`\
`alias delbm="$PATH_SCRIPTS_BM/remove_bookmark.py"`\
`alias addbm="$PATH_SCRIPTS_BM/add_bookmark.py"`\
`alias gotobm="$PATH_SCRIPTS_BM/goto_bookmark.sh"`

*Finally:*
`source ~/.bashrc`

## Demo

-Move to a directory where you have a book.
-`initbm "some great book by some great author"` *starts a bookmarks file in the current directory*
-`bm --all` *to see that it was added corectly*
-`addbm 13 "cool part"` *adds a bookmark to page 13 with description "cool part" at the current date*
-`bm` *shows all bookmarks from the current directory*
-`delbm` *deletes the bookmark file*

## Commands

### bm

Shows the bookmarks from the current directory.

| Example: `bm` |
|---|

### initbm

Starts a bookmarks file in the current directory.

| Example: `initbm "book example"` |
|---|

### addbm

Adds a bookmark to the current bookmarks file.

| Example: `addbm 13 "cool stuff here"` |
|---|

### delbm

Deletes the bookmarks file from the current directory.

| Example: `delbm` |
|---|

### gotobm

Changes directory to the one containing the title given as argument.

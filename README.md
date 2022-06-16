# TODO's Management in CLI

This is a lightweight app that lets you easily keep your tasks in check right from the CLI.

[TODO's Management in CLI](#todos-management-in-cli)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setup](#setup)
  - [Demo](#demo)
  - [Commands](#commands)
    - [*todo*](#todo)
    - [*createtodo*](#createtodo)
    - [*addtodo*](#addtodo)
    - [*marktodo*](#marktodo)
    - [*deltodo*](#deltodo)
    - [*helptodo*](#helptodo)
    - [*replacetodo*](#replacetodo)
    - [*searchtodo*](#searchtodo)
    - [*hltodo*](#hltodo)
    - [*savetodo*](#savetodo)
    - [*cleartodo*](#cleartodo)
    - [*loadtodo*](#loadtodo)

## Prerequisites

Only works on **Linux** or by using **WSL 2**.

## Installation

`git clone https://github.com/georgevanuta/TODO-CLI`

## Setup

*First of all*, modify the path to the main todo's file and to the saves directory in --misc.py--\
(modify the **TODO_FILE**, **SAVES**, **SCRIPTS** variables).

*Then*, add the following lines at the bottom of your **~/.bashrc** file:\
`PATH_TODO=same as TODO_FILE`\
`PATH_SCRIPTS='/path/to/Scripts'`\
*instead of **cat** you could use something like **mdless** since this app is *.md* friendly.*\
`alias todo="cat \$PATH_TODO"`\
`alias addtodo="\$PATH_SCRIPTS/add_todo.py"`\
`alias deltodo="\$PATH_SCRIPTS/delete_todo.py"`\
`alias marktodo="\$PATH_SCRIPTS/mark_todo.py"`\
`alias createtodo="\$PATH_SCRIPTS/init_todo.py"`\
`alias replacetodo="$PATH_SCRIPTS/replace_todo.py"`\
`alias helptodo="$PATH_SCRIPTS/help_todo.py"`\
`alias searchtodo="$PATH_SCRIPTS/search_todo.py`\
`alias hltodo="$PATH_SCRIPTS/hl_todo.py`\
`alias savetodo=$PATH_SCRIPTS/save_todo.py`\
`alias cleartodo=$PATH_SCRIPTS/clear_todo.py`\
`alias loadotod=$PATH_SCRIPTS/load_todo.py`

*Finally:*
source ~/.bashrc

## Demo

-Create the TODO's file:\
`createtodo`\
-Then, check that we created it:\
`todo`\
-Let's add some todo's:\
`addtodo "Listen to Death Grips."`\
`addtodo "Make a TODO management app."`\
`addtodo "Learn for exams."`\
`todo`\
-Mark what we've done:\
`marktodo 1`\
`marktodo 2`\
`todo`\
-Delete what we won't do today:\
`deltodo 3`

## Commands

### *todo*

Displays the contents of your TODO's.

| Example: `todo` |
|---|

### *createtodo*

Initalizes an empty TODO's file in the specified path (*TODO_FILE*).

| Example: `createtodo`|
|---|

### *addtodo*

Adds a new TODO at the end of your TODO's.

| Example: `addtodo "Learn Haskell."`|
|---|

### *marktodo*

Marks a **TODO** by the *line number*.

| Example: `marktodo 1` |
|---|

**Note:** If a **TODO** is already *marked*, **marktodo** will *unmark* it.

### *deltodo*

Deletes a **TODO** by the *line number*.

| Example: `deltodo 1`|
|---|

### *helptodo*

Shows useful information about the TODO commands or lists them.

| Example: `helptodo replacetodo` |
|---|

**Note:** If it receives zero arguments it lists all possible commands.

### *replacetodo*

Replaces an existing todo with a new one.

| Example: `replacetodo 3 "Buy Three Bedrooms in a Good Neighborhood"` |
|---|

### *searchtodo*

Searches for a **highlighted** keyword and returns all TODO's containing it.

| Example: `searchtodo Scala` |
|---|

### *hltodo*

Highlights a word given a line number.

| Example: `hltodo 13 Monads` |
|---|

### *savetodo*

Saves a snapshot of the current TODO's file in the $SAVES directory.

| Example: `savetodo` |
|---|

### *cleartodo*

Deletes all marked TODO's.

| Example: `cleartodo` |
|---|

### *loadtodo*

Loads a previous save in the current TODO's file.

| Example: `loadtodo 4` |
|---|

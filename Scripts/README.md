# TODO's Management in CLI

This is a lightweight app that lets you easily keep your tasks in check right from the CLI.

[TOC]

## Prerequisites

Only works on **Linux** or by using **WSL 2**.

## Installation

`git clone ...`

## Setup

*First of all*, modify the path to the main todo's file path in --misc.py--
(modify the **TODO_FILE** variable).

*Then*, add the following lines at the bottom of your **~/.bashrc** file:
`PATH_TODO=same as TODO_FILE`
`PATH_SCRIPTS='/path/to/Scripts'`
*instead of **cat** you could use something like **mdless** since this app is *.md* friendly.*
`alias todo="cat \$PATH_TODO"`
`alias addtodo="\$PATH_SCRIPTS/add_todo.py"`
`alias deltodo="\$PATH_SCRIPTS/delete_todo.py"`
`alias marktodo="\$PATH_SCRIPTS/mark_todo.py"`
`alias createtodo="\$PATH_SCRIPTS/init_todo.py"`

*Finally:*
source ~/.bashrc

## Demo

-First of all, we need to create the TODO's file:
`createtodo`
-Then, check that we created it:
`todo`
-Let's add some todo's:
`addtodo "Listen to Death Grips."`
`addtodo "Make a TODO management app."`
`addtodo "Learn for exams."`
`todo`
-Mark what we've done:
`marktodo 1`
`marktodo 2`
`todo`
-Delete what we won't do today:
`deltodo 3`

## Commands

### *todo*

Displays the contents of your TODO's.

| Example: `todo` |
-

### *createtodo*

Initalizes an empty TODO's file in the specified path (*TODO_FILE*).

| Example: `createtodo`|
-

### *addtodo*

Adds a new TODO at the end of your TODO's.

| Example: `addtodo "Learn Haskell."`|
-

### *marktodo*

Marks a **TODO** by the *line number*.

| Example: `marktodo 1` |
-

**Note:** If a **TODO** is already *marked*, **marktodo** will *unmark* it.

### *deltodo*

Deletes a **TODO** by the *line number*.

| Example: `deltodo 1`|
-

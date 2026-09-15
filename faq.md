---
title: FAQ
---

# Frequently Asked Questions

::::{tab-set}

:::{tab-item} General

## General FAQ

| Problem | Try This |
| --- | --- |
| Java tests do not appear, or the main class does not load or run. | Run **Clean Java Server Workspace**:<br><br>1. Press <code>CTRL+SHIFT+P</code>.<br>2. Enter <code>clean java server workspace</code>.<br>3. Select **Reload &amp; Delete**.<br>4. Repeat the process if necessary.<br>5. If you are using Codespaces, remove the temporary files by running <code>sudo rm -rf /tmp/\*</code>. |
| Java FX codespaces loading in recovery mode? | See how to disable the sound drivers from loading here. |
| Java FX won't run on codespaces: `Error: JavaFX runtime components are missing, and are required to run this application` | Open up and look at the file: *`.vscode/launch.json`* It's likely you have changed or created a different app that is missing the "linux" section that is needed to find the java fx libraries. Copy that section over to your current configuration so it can find the libraries again. You can usually tell if you see a "projectname" section that is not set to an empty string project name. You can safely delete this launch configuration and use the original one I set up for you instead. **"linux": { "vmArgs": "--module-path ...** |
| Codespaces shows error running the UI port window (x -Failed To Connect To Server) | Try "SHIFT-REFRESH" in your browser window for the VNC UI port. This will delete all cached data in the browser window and seems to fix this problem. |
| I don't know how to use Git/GitHub | There are video tutorials [here](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV) and we also have a set of tutorials hosted at the NCHS website [here](https://nchs-cs.github.io/idp/static/gitbranching/learnGitBranching/) |
| I am confused about codespaces | GitHub codespaces directions are [here](https://docs.github.com/en/codespaces/developing-in-a-codespace/developing-in-a-codespace). NCHS specific directions and help are in this doc below [here](https://docs.google.com/document/d/1_pbLhVmvnMzIhO-ja_HQkc8UjtaZ4OkBJi2YwU3Vpf0/edit?pli=1&tab=t.0). |
| Running Java UI from VS Code results in X11 display issue | This results from clicking to open the project directly to VS code with the "Open in VS code" from the classroom. (It's trying to run codespaces remotely but this doesn't work for Swing). Instead clone the repository from VS Code (create a new window and select to clone a repository and use the link for your github repository from GitHub to clone it). This will then run as expected in your local VS code. Alternatively run remotely and follow directions below for running in CodeSpaces. |
| GitHub complains you don't have user.name or user.email | `git config --global user.name "Your name"` <br> `git config --global user.email <id>@apps.nsd.org` |
| If you have an ssl issue in vscode saving your work | `git config --global http.sslVerify false` |
| When trying to clone a repository to a local machine: "SSL certificate problem: self-signed certificate in certificate chain" | If you are on Windows: enter this on the terminal to configure ssl correctly <br> `git config --global http.sslbackend schannel` <br> On linux/codespaces: <br> `git config --global http.sslbackend openssl` |
| "Sync" fails / conflict (when trying to submit) | Enter this into the terminal and sync again: <br> `git config set pull.rebase true` |
| "Commit" looks it's taking forever | Make sure you don't have the "COMMIT_MSG" file up and waiting for you to edit and close. Just close it and put your commit message in above the commit button. |
| Other random codespace error or message of something weird (aka rebuild codespace) | **Warning this will lose any changes you haven't pushed to your github repo** <br> Enter Ctrl-Shift-P for the command palette, type "Reb…" to get "Codespaces: Rebuild Container", select "Full Rebuild". |
| Trying to run java main isn't working (e.g. main is not found or perhaps the java run/play button is missing) | Check you have enabled the Microsoft java extension pack and not the oracle one. <br> This is correct: (insert photo here) <br> This doesn't fully support VS code use: (insert photo here) |

:::

:::{tab-item} Markdown

## Markdown

Markdown syntax allows rich formatting in documents using any plain text editor.

### Basic Markdown Guide

Here is a basic markdown guide: [markdownguide.org](https://www.markdownguide.org/basic-syntax/)

### Integrating with Google Docs

You may upload and download markdown documents to Google Docs. To edit a markdown document in Google Docs, upload the document and then edit in Google Docs.

Note you must use the Google Drive "upload" feature or from Google Docs you can select **File → Open** to directly open the markdown document (this is the easiest way).

Whenever you want to save the current version of the document choose **File → Download → Markdown**.

**Warning**: If you include images in your Google documents these will be encoded in the markdown content. It's often better to just edit the markdown document directly instead of using Google Docs if you make heavy use of images that you may modify and replace so you can reference these with markdown links to image files.

:::

:::{tab-item} GitHub

## GitHub

### Signing up for GitHub

It's recommended that you create a "school" github account. To do this you can use your google SSO (single sign on) and you should create your account username with the following credentials using "firstname-lastname" for your username. **Do not enable 2 factor authentication** as this will cause you to need to use your phone or other device when you sign in.

### GitHub Education Accounts

If you run out of time in GitHub codespaces apply for a free GitHub education account. Here's how to do that:

You can request an education account [here](https://github.com/settings/education/benefits) which will take you to your settings for your github account to start the application process.

Do not put in any billing information. Make sure to select that you are a student. You may need to turn on two factor authentication and verify your email address. Make sure to set two factor to use your email address so you can still reset and access your account in school without your phone. **Do not set two-factor** to your phone number as it disrupts class to have to use your phone for two factor authentication.

You need proof that you are a student so you'll need to edit and print the following document for you to use during the signup process (I'll need to sign it for you too): [Google Doc Link](https://docs.google.com/document/d/1vyFcQCQlhnSlcZG_f_q3uXCPplXpojHtnhs67t94Pok/edit?usp=sharing).

### Committing and Pushing Changes

1. **Stage changes**: In the Source Control view (left sidebar), you'll see a list of changed files. Click the '+' icon next to each file you want to commit.
2. **Commit changes**: Type a commit message describing your changes, then click the checkmark icon to commit.
3. **Push changes**: Click the "Sync Changes" button to push your commits back to GitHub.

### Following Classwork in GitHub

In order for students to follow along with code-alongs on larger projects we are going to adopt the following workflow.

Students can do work in their workspace using their "main" branch of their code saved to their computer or codespace.

The easiest way for students to track these separately is to clone their GitHub repository for the "Classwork" repository to a different folder on their local computer. They can cut/copy the code from here into their ongoing project if they miss work or want to compare their work with the classwork.

**NOTE**: It's very easy to confuse work between the two. If you are getting an error that you can't write/sync your work, check first to make sure you are actually doing the work in your own repository vs trying to send updates to our class project (which you can't).

:::

:::{tab-item} Classroom50

## Classroom50

You join classroom50 after you have created your github account at the following link:

[Access Link from the Document here for NCHS](https://docs.google.com/document/d/1_pbLhVmvnMzIhO-ja_HQkc8UjtaZ4OkBJi2YwU3Vpf0/edit?pli=1&tab=t.un9fr0b19qkw)

Or the teacher provided schoology link for your specific assignment.

### IDP Assignments

For IDP you can use the following assignment for your classwork and assignments:

[Access Link from the Document here for NCHS](https://docs.google.com/document/d/1_pbLhVmvnMzIhO-ja_HQkc8UjtaZ4OkBJi2YwU3Vpf0/edit?pli=1&tab=t.un9fr0b19qkw)

Once you accept this assignment you can clone the repository to your computer.

You can now work on the jupyter notebooks locally using VS Code (and read the lesson content). See notes on running VS code from Anaconda [here](https://docs.google.com/document/d/1_pbLhVmvnMzIhO-ja_HQkc8UjtaZ4OkBJi2YwU3Vpf0/edit?pli=1&tab=t.un9fr0b19qkw)

### Updating your Assignment

At times I will make updates to the website and you will want to incorporate these into your repository. To do this you'll need to follow a few more steps.

First - you need to add the original IDP website as an upstream repository. Note - you only need to do this once.

```bash
git remote add upstream https://github.com/NCHS-CS/cse163-nchs
```

You can now fetch and merge upstream changes.

```bash
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

**Tip**: Subscribe to notifications and changes to the main website so you can decide when to update your local repository.

**Tip**: Go to the upstream repository and select to watch all notifications in the UI.

:::

:::{tab-item} Anaconda

## Anaconda

### Anaconda/VS Code Setup

Computers in class have Anaconda installed. There are a few more steps needed to set it up on your personal account correctly.

Firstly you need to make sure you are able to install from the correct channels. Press the windows key on your keyboard and search "anaconda prompt". Enter the following commands:

```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```

1. Start Anaconda (icon is on your desktop)
2. Import the env_26_27.yml file to a new environment and name it "idp". This will take some time.
3. Go to main and click to start VS Code (make sure it's not running already), making sure you've selected your idp environment first.

In visual studio, the first time you should clone your repository you will be working with. Here's an example cloning my idp personal repository:

After this your environment in VS code will show that you are running in the selected environment.

**Tip**: You can make "idp" your default environment in anaconda.

**Tip**: VS-Code: You can select defaults in VS code so you can start VS code directly without going through anaconda.

Make sure setting `python.terminal.activateEnvironment` is checked.

### Selecting the Correct Python Interpreter in VS Code

Tell VS Code exactly which Conda environment to use for your workspace:

1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Search for and select **Python: Select Interpreter.**
3. Choose the environment labeled with **'conda'** (e.g., `Python 3.x.x ('idp': conda)`)

:::

::::

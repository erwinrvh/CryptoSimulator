# CryptoSimulator
Have the urge to mine for crypto, but don't want to get into the legalities of it? Here, you can scratch that itch by simulating mining a crypto coin! You won't get any money out of it, but it'll look cool (kinda)

When using pip install, please activate the virtual environment (venv) (preferably via the terminal on your IDE).

For linux:
- Be in the root folder
- Use command "source .venv/bin/actiavate"
- Proceed to install anything via pip once activated
- When done, use command "deactivate"

For Windows:
- Be in the root folder
- Use command ".venv\Scripts\activate" or ".\venv\Scripts\activate"
- Proceed to install anything via pip once activated
- When done, use command "deactivate"

Some useful git commands:

When wanted to pull from main, follow these commands as it is a safe way to pull from main.
- git fetch
- get pull

When wanting to work on something, you should make a branch. This makes a local version of the main you just pulled,
and won't affect anyone else
- git checkout -b <branchname> 
(If possible, please have the branchname related to what you are doing)

When your branch has been merged, make sure to move from your local branch into main, do the fetch and pull, and delete your local branch
- `git branch` is used to see what branches there are, and there will be a * on the branch you are on
- `git checkout main` should be how you move from your local branch to main
- `git fetch` then `git pull`
- Upon success, delete your local branch via `git branch -d <branchname>`

If your branch name doesn't relate/changes definition as you go, just make sure to summarize what you did in the commit message.

Before commiting, double check files. Depending on OS, it will make a file that shouldn't be pushed. Utilize AI to doublecheck on how to add it to the .gitignore file. Also make sure to save the file before commiting and pushing.


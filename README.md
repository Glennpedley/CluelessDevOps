# CluelessDevOps
CluelessDevOpsstuff
This is how I am doing the DevOps class homework. Starting from totally Dunno Clueless mode, yet again.
First off, to get hands on familiarity with GitHub. Then only go and do the clone lah, commit lah, deploy lah, trigger lah, Actions lah dunno wat shit.
So I started off by learning how to branch off the main.
  I created a branch (clone the main), named it (whatever lah) and made changes to it (commit, is like... save my changes)
I then made a Pull request, which is say hey main, there are some changes I made in this file that I want the main file to now update itself with.
  (I got to do this, cos you know, I dont just DO IT ONE TIME at the main file, but dua kerja, DO TWO TIMES, do at branch then add in Pull request action)
  In the Pull request, I ask to compare my branch with the main branch.
Then I, myself, who made the changes, and requested a pull request to myself, then went to accept the changes that I myself made to my own file to be updated in the main.
  I did this using the Merge process.

So, basically, from my own file, I have a main and from the main, branches can be made where changes made to branches are not updated to main or destroying the main. Branches drop off and die also nevermind, main one still okay. Once the branches, test, deploy all okay, then can make pull request to merge with main. AND WHO APPROVES the pull requests? ME! Siapa raja? ME! Siapa lembu? Kita juga orangnya.

Now the SHow and Tell itself

Project 2: CI/CD
Your Task
Create a GitHub repository that contains your application code, 
along with workflows that execute steps to 
test, 
package, or 
deploy it.


In a previous course you may have produced applications (frontend, backend, API) which is now disconnected to the MySQL server rendering them quite useless to use here,
alternatively you could use this project as a basis. (Had a look, not gonna work for me)

So we basically clone one repository that have all the above. Why not just say CLONE a GitHub repository instead of CREATE? No?




Pushing new commits to the repository should trigger a workflow that 
does something with your code.  
It could be 
a notification on a chat app, 
executing tests, 
packaging it up, or 
deploying it to the cloud. 

Bonus points if you do several of these, but that is not the expectation.



SO MY CODE is the one I cloned, and I have to trigger a workflow that does something with my code?




Tips & Guidelines
Your GitHub repository should contain
Application Source Code
Workflow(s)
README.md (or any other document) that explains the outcome, your steps, and your thought process
Start with an empty (or initialized) GitHub repository. 

Okay, initialized GitHUb means, all the changes from the point I started to make the changes.

As you implement and make changes, do a commit + push each time


So how the heck do I initialize from here???


CREATE An EXAMPLE WORKFLOW
How? See here https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions

So I went to my repository called CluelessDevOps and created the .github/workflows/ directory to store my workflow files. 

I then went to the .github/workflows/ directory, created a new file called learn-github-actions.yml (yeah I copied the name, so sue me) and added the following code.

name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v1
      - run: npm install -g bats
      - run: bats -v


Then performed the "Commit these changes" and "push"(what the hell lah weii,,, just now PULL now PUSH fucking cibai... ) them to my GitHub repository.

CHANGE THE WORKFLOW to WHATSAPP Notification.
Okayyy so i got the workflow files in the directory. Now I want to change them, I would like to a workflow that will send a whatsapp message to a group (guess who I am going to BOMB). What I need to do is to find a Whatsapp workflow to use and replace mine with that..(oh found out i need to sign up for Twilio)

Then from my twilio dashboard fetch Account Sid and Auth Token.

To encrypt them, create new secrets in your repository named account_sid, auth_token, to_whatsapp_no and give it's value. Well, I did that, took the values from Twilio.

Then I change my workflow directory to  .github/workflows/whatsapp-push-notify-action.yml.
And I edited it to the following properties to newly edited  whatsapp-push-notify-action.yml file
name: When a push occurs in the master branch, a private message is sent on the Whatsapp.
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: whatsapp-notify
        id: whatsapp-notify
        env:
          account_sid: ${{ secrets.ACCOUNT_SID }}
          auth_token: ${{ secrets.AUTH_TOKEN }}
          to_whatsapp_no: ${{ secrets.TO_WHATSAPP_NO }}


          uses: ishween/whatsapp-push-notify-action@master
      
      - name : Run
        run: |
          echo 'Start!'

Then I test by creating a branch and try to do a push..whatever that is... I only know commit..what the hell is a push?

This sends me a whatsapp message saying

Yay! Push event triggered in master branch
WHere the hell did these text come from and how can I edit them?

I think they came from iishween/whatsapp-push-notify-action@master cos when i change to 
glennpedley/whatsapp-push-notify-action@master

nothing jalan.

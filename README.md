# CluelessDevOps
<h1 align="center">Clueless DevOps stuff from NUS class</h1>

<p>This is how I am doing the DevOps class homework. Starting from totally Dunno Clueless mode, yet again.</p><br>
First off, to get hands on familiarity with GitHub. <br>Then only go and do the clone lah, commit lah, deploy lah, trigger lah, Actions lah dunno wat shit. <br>
So I started off by learning how to branch off the main. <br>
  <p>I created a branch (clone the main), named it (whatever lah) and made changes to it (commit, is like... save my changes) <br>
I then made a Pull request, which is say hey main, there are some changes I made in this file that I want the main file to now update itself with. <br>
  (I got to do this, cos you know, I dont just DO IT ONE TIME at the main file, but dua kerja, DO TWO TIMES, do at branch then add in Pull request action) <br>
  In the Pull request, I ask to compare my branch with the main branch. <br>
<h3>Then I, myself, who made the changes, and requested a pull request to myself, then went to accept the changes that I myself made to my own file to be updated in the main.
  I did this using the Merge process.</h3></p>
 <br>
<p>So, basically, from my own file, I have a main and from the main, branches can be made where changes made to branches are not updated to main or destroying the main. Branches drop off and die also nevermind, main one still okay. Once the branches, test, deploy all okay, then can make pull request to merge with main..... AAAAAAND WHO APPROVES the pull requests? ME! Siapa raja? ME! Siapa lembu? Kita juga orangnya.</p> <br> <br>

<h2 align="center">Now the SHow and Tell itself</h2>
(Intructions)
Project 2: CI/CD <br>
Your Task <br>
Create a GitHub repository that contains your application code,  <br>
along with workflows that execute steps to  <br>
test,  <br>
package, or  <br>
deploy it. <br>
 <br>

In a previous course you may have produced applications (frontend, backend, API) which is now disconnected to the MySQL server rendering them quite useless to use here,
alternatively you could use this project as a basis. (Had a look, not gonna work for me) <br>

So we basically clone one repository that have all the above. Why not just say CLONE a GitHub repository instead of CREATE? No? (Post, note, so in then end, tell you alll horr, I cloned one repository and then, guess what, I copied all the files from that repository in to the repository I "created" earlier, so, can say I created it, right? right? <br>

 <br>
 <br>
(Instrcutions) 
Pushing new commits to the repository should trigger a workflow that  <br>
does something with your code.   <br>
It could be  <br>
a notification on a chat app,  <br>
executing tests,  <br>
packaging it up, or  <br>
deploying it to the cloud.  <br>

Bonus points if you do several of these, but that is not the expectation. <br>
(Bonus points get to do what ah? Buy burger ah?) <br> <br>

SoOooOOooo MY CODE is the one that I cloned and copied into a new repository that I "created" and made adjustments to, <br>
and I have to trigger a workflow that does something with my code?  <br>
<h3>Decision - I AM going to do a whatsapp notification message then.</h3>

(Tips from instructions) <br>
Tips & Guidelines <br>
Your GitHub repository should contain <br>
Application Source Code ( OKAY ini ada) <br>
Workflow(s) (Ok, Ini ada) <br>
README.md (or any other document) that explains the outcome, your steps, and your thought process (oooOooOo Ini MESTI ADA!) <br>
Start with an empty (or initialized) GitHub repository. (am going to START with empty one) <br>

Okay, initialized GitHUb means, all the changes from the point I started to make the changes. Goodness totally forgot about this. All changes made in GitHub and not on local computer.  <br>

As you implement and make changes, do a commit + push each time (YES, AKU BERJAYA!) <br>
So how the heck do I initialize from here??? Dont have, did the local computer and committed the push ONCE, then just did the changes in GitHub instead. Where is the "push" button in GitHub by the way? Only thing I can find is commit, and to push to main is to do some pull-request, where the "push"? <br> <br>



<h2>1. CREATE An EXAMPLE WORKFLOW (STEPS to CREATE)</h2>
How? See here https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions <br>

So I went to my repository called CluelessDevOps and created the .github/workflows/ directory to store my workflow files.  <br>

I then went to the .github/workflows/ directory, created a new file called learn-github-actions.yml (yeah I copied the name, so sue me) and added the following code. <br>

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

 <br>
Then performed the "Commit these changes" and "push"(what the hell lah weii,,, just now PULL now PUSH fucking cibai... ) them to my GitHub repository. WHere got PUSH button? DUn have also. <br>


<h2>2. CHANGE THE WORKFLOW to WHATSAPP Notification. (Adjust the workflow to what I want)</h2> <br>
Okayyy so I got the workflow files in the directory. Now I want to change them, I would like to a workflow that will send a whatsapp message to a group (guess who I am going to BOMB-cheh). What I need to do is to find a Whatsapp workflow to use and replace mine with that..(oh found out I need to sign up for Twilio from the readme of the other guy's repository) <br>
 <br>
SO I did signed up at Twilio (at first didnt get anumber but got some US number ater cos nothing was working so might as well get it in case it affects the workflow)
Then from my Twilio dashboard fetch Account Sid and Auth Token and put them in secrets page of github, which means... go to the repository I wan to put secrets in, then look for the "gear" icon which means settings, there are TWO gear icons that I saw... use the one in a line of many tabs. <br>
 <br>
To encrypt them, create new secrets in your repository named account_sid, auth_token, to_whatsapp_no and give it's value. Well, I did that, took the values from Twilio. <br>
 <br>
Then I change my workflow directory to  .github/workflows/whatsapp-push-notify-action.yml. <br>
NOTICE - this is the file name, not the actual path or action, later will show you no need use this name IF your repository is another name, a great example would be CluelessDevOps (oh wow, what a great repository name!) <br>
And I edited it to the following properties to newly edited  "whatsapp-push-notify-action.yml" file;
 <br>
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
 <br>
Then I test by creating a branch and try to do a push...whatever that is... I only know commit..what the hell is a push again? <br>

This sends me a whatsapp message saying <br>

Yay! Push event triggered in master branch
WHere the hell did these text come from and how can I edit them?

I think they came from iishween/whatsapp-push-notify-action@master  <br>
cos when i change to  <br>
glennpedley/whatsapp-push-notify-action@master <br>
nothing jalan.
 <br>
  <br>
So knowing a bit more about what can work and what cannot, after this, I am going to start to edit the codes to learn which code is needed and if possible what code does what in the process, to "test" I did some changes to test to find out for myself what works and what does not, ONE by bloody ONE. <br>
SO after this, I am going to start to edit the codes to learn which code is needed and if possible what code does what in the process.
<h1>This ReadMe is bascially to see that there are different versions and which codes we can use and works and which ones does not, more or less</h1>.
 <br>
SO after this, I am going to start to edit the codes to learn which code is needed and if possible what code does what in the process. <br>

I changed;  <br>
1) line 100:- <br>
the "on" to include a pull request (yupe, it works, so if only one like push, can type push without the [] or with also can. But when more than one, just put [ then the event type separated by comma(s), and close with] (how the hell did that underline come in here?) <br>
WORKS. Can put many types <br> <br> 

2) line 105:-  <br> 
2.1) the "uses" from "actions/checkout@main" to  "actions/checkout@v2 (just cos having the "main" and "master" is a bit confusing as to which is the main master.. so kill them both, just use the mighty v.  <br>
IT WORKS. Both can be used. <br> 

2.2) the "uses" from "actions/checkout@main" to ./.github/actions/whatsapp-push-notify-action" <br>
Does NOT seem to work, and after changing to "Glennpedley/CluelessDevOps/github/actions/whatsapp-push-notify-action" (also does NOT seem to work) so changed back to  "actions/checkout@v2" <br> <br>

3) line 107:- <br>
I removed the "id" cos I dont know what file path that means at all. All I read was that this was input path to use. <br>
STILL WORKS. <br> <br>

4) lines 109-111:- <br>
I edited the "secrets" path to use CAPITAL letter, will test if camel works just as well....testing...testing....testing....testing... <br>
OKAY! BOTH WORKS, so capital or camel letters both also can use for secrets path. <br> <br>

5) line 113:- <br>
5.1) I removed "ishween/whatsapp-push-notify-action@master" <br>
DID NOT WORK - so means, I have to reference this repository for "something" and I am thinking that is why or where the "text" in the whatsapp message is living? <br>
5.2) I changed this uses to "Glennpedley/whatsapp-push-notify-action@master" <br>
DID NOT WORK - so, I cannot make my own yet, still have to reference some fella's repository for this? <br>
5.3) I changed it to "Glennpedley/whatsapp-push-notify-action@main"  <br>
DID NOT WORK <br>
5.4) I changed it to "Glennpedley/CluelessDevOps/whatsapp-push-notify-action@master" <br>
DID NOT WORK <br>
5.5) I changed it to "Glennpedley/CluelessDevOps/whatsapp-push-notify-action@main" <br>
DID NOT WORK <br>
5.6) I changed it to "Glennpedley/CluelessDevOps/github/actions/whatsapp-push-notify-action" <br>
So, why is this? Logic is telling me it is because in the fella's bloody repository there are other files there that also runs!!! Bloody hell. Just went to see his repository, so many files, and found the file where the text "Yay!Push event triggered in master branch"!!! <br>
So I cloned her repository by forking the hell out of it. Then, I am going to copy and adjust one file at a time  to see which ones are needed, instead of adjusting from my clone. <br>

<h2>COPY FILES OVER TO REPOSITORY / Other normal people say...clone/fork lah..apa copy copy? </h2>

So I cloned that fella's one over. <br>
Changed the "text" message to be sent to the whatsapp which was in the "main.py" file; and made a commit to see if I could get MY own message. <br>
YAYYY It Works!  <br>
Now I wanna see if it works with the link to the fella's repository or can I delete that from the workflow main.yml file <br>
7) line 113:- <br>
Deleted "uses: ishween/whatsapp-push-notify-action@master" <br>
DOES NOT SEEM TO WORK>>> SEEMS LIKE STILL NEED TO HAVE THAT LINK????? U know why? Cos need to link to somewhere to run the "other" files and so far, I have not created a link to run from MY OWN repository. <br>
 <br>
8) line 113:- <br> <br>
Added "uses: Glennpedley/CluelessDevOps@main"
WORKS! But why cannot work without THIS line??? Is this not in my own repository oledi? <br>
Will figure this out in next few changes to codes along with what the "run: | echo Start!" is all about is possible.
Deleted the cloned repositoy. Then not working? WTH has this got to do with the cloned repository? 
Thinking maybe cos I did not copy the "License" file over and somehow, it affected this? Coped the License file over.
Let's see if this works.Something is wrong with Twilio. The action ran fine.
This is the working code so far to be checked further. Using ONE Twilio account, it ran fine but when changed Twilio secrets, it did not work. So, now going to the one that did NOT work to reconnect with the Sandbox in Twilio and try again. The last few said was outside the window and needed to use a template (under logged messages in Twilio)
  
name: When one of the following events occur in the master branch, a message is sent to the Whatsapp.
on: [push, pull_request, issues, fork, watch]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: whatsapp-notify
   
        env:
          account_sid: ${{ secrets.ACCOUNT_SID }}
          auth_token: ${{ secrets.AUTH_TOKEN }}
          to_whatsapp_no: ${{ secrets.TO_WHATSAPP_NO }}
        uses: Glennpedley/CluelessDevOps@main
      - name : Run
        run: echo 'Start!'

From here on out will check others if have time.

## World Improv Guide

## Important URLs

* [Production Site](http://improv.guide)
* Trello Board
* [WhatsApp Group](https://chat.whatsapp.com/La3ctCUSo6SFzStqH3dSht)
* Slack Workspace
* [GitHub Project](https://github.com/salimfadhley/uk_improv_guide)

## Developer Guide

These instructions will get you started as a developer.

### Developer Requirements

* Docker CE
* Git
* An IDE of your choice (I use IntelliJ Ultimate)

### How to install

Create a file at `~/.secret/uk_improv_guide.sh`. It should contain the following content, but change the paaswords as appropriate for you:

```
#! /bin/bash
export POSTGRES_PASSWORD=abc1aa
export SLACK_WEB_HOOK=http://example.com
export PRODUCTION_SECRET="dsfdsdffsdfsf"
```

Run the script:

```
./up_dev.sh
```

This will install all of the components and start the containers. Next you can load some content:

```
./restore.sh
```

This installs a snapshot of production data into the locally running app.

### Special Windows instructions

Just do all of the above in a Git Bash session. 

## Improv Guide

## Important URLs

* [Production Site](http://improv.guide)
* [Dev site](http://localhost:8080)
* [Dev adminer](http://localhost:8080)
* [Trello Board](https://trello.com/b/aZ48umXI/general)
* [WhatsApp Group](https://chat.whatsapp.com/La3ctCUSo6SFzStqH3dSht)
* [GitHub Project](https://github.com/improv-guide/uk_improv_guide)
* [Slack Workspace](https://improvguide.slack.com/messages/CKVGVGBL2)
* [Travis CI](https://travis-ci.org/improv-guide/uk_improv_guide)

## Developer Guide

These instructions will get you started as a developer.

### Developer Requirements

* [Docker CE or Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Git](https://git-scm.com/)
* An IDE of your choice (I use [IntelliJ Ultimate](https://www.jetbrains.com/idea/), but Visual Studio Code, Sublime Text is all good!)

### How to install

Create a file at `~/.secret/uk_improv_guide.sh`. It should contain the following content, but change the paaswords as appropriate for you:

```
#! /bin/bash
export POSTGRES_PASSWORD=abc1aa
export SLACK_WEB_HOOK=http://example.com
export PRODUCTION_SECRET="dsfdsdffsdfsf" 
```
The password and production secrets can be any random text.

Run the development "up" script:

```
./up_dev.sh
```

This will install all of the components and start the containers. Next you can load some content:

```
./restore.sh
```

This installs a snapshot of production data into the locally running app.

### Special Windows instructions

When you install Git, make sure you set it to "Check out as is, Commit UNIX-style"

Just do all of the above in a Git Bash session. 

## Common problems

### The port Docker wants to use (8000 or 8080) is in use!

Get rid of your firewall. Most Windows firewalls are incompatible with Docker.

### You want to look at the database?

Login to [adminer](http://localhost:8080). Use these login credentials:
* System: PostgreSQL
* Server: db
* Username: improv
* Password: <use whatever password you defined in your `~/.secret/uk_improv_guide.sh` file.
* Database: improv

### You want to drop all the data but Postgress Foreign-key constraints won't let you?

Execute this SQL inside Adminer:
```sql
DO $$ DECLARE
    tabname RECORD;
BEGIN
    FOR tabname IN (SELECT tablename
                    FROM pg_tables
                    WHERE schemaname = current_schema())
LOOP
    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(tabname.tablename) || ' CASCADE';
END LOOP;
END $$;
```

After you drop the tables you will have to do one of the following before you can run the `./restore.sh` script:

* Restart the dev environment with `./up_dev.sh`, or
* Run the migrate script, `./migrate.sh`

### You want to completely reset Postgres

Dropping tables is not extreme enough for you? This is the nuclear option:

* Kill the currently running dev-environment, just press `CTRL-C` if you have a your docker-compose console live.
* Run `./kill_and_remove.sh` to ensure that all the containers have stopped.
* Run `docker volume ls` to list all the docker volumes
* Delete the database volume: `docker volume rm uk_improv_guide_postgres_data`
* Restart the dev environment: `./up_dev.sh`

### You want to create a super-user account

If you are starting from a brand-new database, run the `./up_dev.sh` script to create the tables and authentication data.

Next, start a docker shell in another window:

```bash
./shell.sh
```
From within the shell enter the following command:
```bash
python manage.py createsuperuser
```


If you see an error like this: `django.db.utils.ProgrammingError: relation "auth_user" does not exist` the chances are that your superuser account was created. Just try to login.

### The data does not restore

it's possible that the database is in a state incompatible with the restore data. The simplest way to fix this is to wipe the database
and then re-populate it.

* Kill all the running containers.
```bash
sal@gruntyman:~/workspace/uk_improv_guide$ ./kill_and_remove.sh 
a0401d6747b9
b23f274401fa
db107b245e11
0d43601de0b8
a52a73aee288
```
* Restart the dev environment.
```bash
sal@gruntyman:~/workspace/uk_improv_guide$ ./up_dev.sh 
Removing network uk_improv_guide_internal
Creating network "uk_improv_guide_internal" with the default driver
Creating postgres ... done
Creating uk_improv_guide_dev_1    ... done
Creating dev_adminer              ... done
Creating uk_improv_guide_python_1 ... done
```
* In another shell, load the data:

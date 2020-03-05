## Improv Guide

[![Updates](https://pyup.io/repos/github/improv-guide/uk_improv_guide/shield.svg)](https://pyup.io/repos/github/improv-guide/uk_improv_guide/)

## Important URLs

* [Production Site](https://improv.guide)
* [Dev site](http://localhost:8080), when you run it locally
* [Trello Board](https://trello.com/b/aZ48umXI/general), for project management
* [GitHub Project](https://github.com/improv-guide/uk_improv_guide), for source code
* [Slack Workspace](https://improvguide.slack.com/messages/CKVGVGBL2), for technical discussions of this system,
* [Travis CI](https://travis-ci.org/improv-guide/uk_improv_guide), production builds & tests.

## Developer Guide

These instructions will get you started as a developer.

### Developer Requirements

* [Docker CE or Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Git](https://git-scm.com/)
* An IDE of your choice (I use [IntelliJ Ultimate](https://www.jetbrains.com/idea/), but Visual Studio Code, Sublime Text is all good!)

You will also need:
* A GitHub account
* An RSA public/private key pair on your workstation
* Your public key must be installed on GitHub.

### Pull the code for the first time.

First, clone the whole repository:

```$bash
git clone git@github.com:improv-guide/uk_improv_guide.git
```

Don't use the HTTPS URL that github provides. It will only work if you pull it via the SSH URL given above.

Database snapshots and media files (photos, logos, etc) are stored in two
separate repos to the source code. They have been included into the source
repo as Git Submodules. These need to be pulled separately:

If you have only just cloned the repository, do:
```bash
git submodule update --init --recursive
```

Next, do:

```bash
git pull && git submodule update --recursive
```

This 2nd step can be repeated any time you want to update the backed-up content.

### How to install

Create a file at `~/.secret/uk_improv_guide.sh`. It should contain the following content, but change the paaswords as appropriate for you:

```
#! /bin/bash
export POSTGRES_PASSWORD=abc1234
export POSTGRES_SSLMODE=allow
export POSTGRES_HOST=db
export POSTGRES_DB=improv
export POSTGRES_PORT=5432
export PRODUCTION_SECRET=dfsdsjdsjdsjkds
export FACEBOOK_APP_KEY=xxx
export FACEBOOK_SECRET=xxx
```
`PRODUCTION_SECRET` should be a random string. `POSTGRES_PASSWORD` should be a memorable password. It will be used to set the defaullt password on the postgres datgabase when it is first set up.

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

By default, a newly created Postgres database does not include an admin account. You will not be able to login until you execute the next step:

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

### When running the restore script you get an error: "CommandError: No fixture named 'uk_improv_guide' found."

This means the backup submodule was not pulled. Did you check out the original repo using the SSH Git URL? If not the submodules will not update.

Solution: Trash your local repo, and re-clone it using the SSH URL.

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

### The production certificate has expired

  * Login to the certbot container (it doesn't havd Bash, only Sh)

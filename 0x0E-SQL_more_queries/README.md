<p align="center"><img src='https://media.giphy.com/media/vISmwpBJUNYzukTnVx/giphy.gif' alt='Banner' width=10%></p>

# 0x0E. SQL - More queries

<p>

###### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION
<p>

In this repo, you will find the following topics:

Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 5.7 on Ubuntu 14.04 LTS
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
Don’t forget your root password

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:

$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart
If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common

Use “container-on-demand” to run MySQL
Ask for container Ubuntu 14.04 - Python 3.4
Connect via SSH
Or via the WebTerminal
In the container, you should start MySQL before playing with it:
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
In the container, credentials are root/root

How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller



### Authors :black_nib:
* __Maria Fernanda Lopez__

#### Software Academy 👨‍💻

<p aling="center">
<a>

<img src="https://i.pinimg.com/originals/ba/46/c8/ba46c8090ccc536ef26c005f9f2fc404.gif" alt="Twitter" width=10% /></a>
*:sparkles: Follow me *[Twitter](https://twitter.com/ferchislopez910)*
*<p aling="center">

<p>resource:
https://docs.python.org/3.4/tutorial/classes.html#inheritance
<p>

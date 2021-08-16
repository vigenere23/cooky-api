cp ./init/privileges.sql /docker-entrypoint-initdb.d

filename=/docker-entrypoint-initdb.d/0_users.sql
echo "" > $filename
echo "CREATE USER 'api'@'%' IDENTIFIED BY '$MYSQL_API_PASSWORD';" >> $filename

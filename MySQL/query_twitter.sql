USE twitter;
SELECT users.first_name as followed, users2.first_name as following FROM users
JOIN follows
ON users.id = follows.followed_id
JOIN users as users2
ON users2.id = follows.follower_id;

USE lead_gen_business;
SELECT * FROM billing;




# Specify DB
USE natl;

# Insert Users
INSERT INTO user (id, username, password, access_id) VALUES (1, 'test1', 'test1', "test1_access_id");
INSERT INTO user (id, username, password, access_id) VALUES (2, 'test2', 'test2', "test2_access_id");


# Insert List
INSERT INTO list (id, user_id, name, description, is_done) VALUES (1, 1, 'test_list', 'test_desc', 0);

# Insert Task
INSERT INTO task (id, list_id, name, description, is_done) VALUES (1, 1, 'test_task', 'test_desc', 0);
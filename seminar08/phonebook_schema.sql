create table if not exists phonebook (
  id             integer primary key autoincrement,
  full_name      varchar(255) not null,
  phone_number   varchar(20)  not null,
  comment        varchar(255) not null default "No comments",
  creation_date  datetime default current_timestamp);

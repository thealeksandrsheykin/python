create table if not exists phonebook (
  full_name      varchar(255) not null,
  phone_number   varchar(20)  not null primary key,
  comment        varchar(255) not null default 'No comments',
  creation_date  datetime default current_timestamp);

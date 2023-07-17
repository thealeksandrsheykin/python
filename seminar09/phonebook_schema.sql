create table if not exists phonebook (
  name      varchar(255) not null,
  phone     varchar(20)  not null primary key,
  creation_date  datetime default current_timestamp);
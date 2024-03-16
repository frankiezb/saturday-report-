


CREATE TABLES IF NOT EXISTtask(
    id INTEGER PRIMMARY KEY AUTOINCREMENT,
    name Varchar(128),
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFUALT 0
);

insert into task(
    name, 
    summary,
    description
) values
(
    "wash dishes",
    "use dish soap to wash dishes",
    "lorem ipsum(discription)",
),
("walk dog",
"take fido to the park for a walk",
"Make sure sure fido get their execrises",
),
(
    "buy grocergies",
    "drive to the store to buy groceries",
    "we need eggs,milk and ham"
);
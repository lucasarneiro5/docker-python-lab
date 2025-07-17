CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE
);

-- Insere uma tarefa de exemplo
INSERT INTO tasks (title, description, completed) 
VALUES ('Estudar Docker', 'Revisar todos os comandos do Docker', FALSE);
